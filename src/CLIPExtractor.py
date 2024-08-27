import os
import torch
from transformers import CLIPProcessor, CLIPModel
import cv2
from PIL import Image
import numpy as np


class CLIPExtractor:
    def __init__(self, model_name="openai/clip-vit-large-patch14", cache_dir=None):
        # 设置环境变量
        os.environ["HF_ENDPOINT"] = "https://hf-api.gitee.com"
        os.environ["HF_HOME"] = os.path.expanduser("models/")

        # Initialize the model and processor with specified values
        if cache_dir is not None:
            self.model = CLIPModel.from_pretrained(model_name, cache_dir=cache_dir)
            self.processor = CLIPProcessor.from_pretrained(model_name, cache_dir=cache_dir)
        else:
            self.model = CLIPModel.from_pretrained(model_name)
            self.processor = CLIPProcessor.from_pretrained(model_name)

        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model.to(self.device)

    def extract_image(self, frame):
        # Convert frame (from OpenCV) to PIL Image
        image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        images = [image]
        
        # Process the image and extract features
        inputs = self.processor(images=images, return_tensors="pt").to(self.device)
        with torch.no_grad():
            outputs = self.model.get_image_features(**inputs)
        
        ans = outputs.cpu().numpy()
        return ans[0]

    def extract_image_from_file(self, file_name):
        if not os.path.exists(file_name):
            raise FileNotFoundError(f"File {file_name} not found.")
        
        images = [Image.open(file_name).convert("RGB")]
        
        # Process the image and extract features
        inputs = self.processor(images=images, return_tensors="pt").to(self.device)
        with torch.no_grad():
            outputs = self.model.get_image_features(**inputs)
        
        ans = outputs.cpu().numpy()
        return ans[0]
    
    def extract_text(self, text):
        if not isinstance(text, str) or not text:
            raise ValueError("Input text should be a non-empty string.")
        
         # Tokenize the text
        inputs = self.processor.tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=77).to(self.device)
        

        # Process the text and extract features
        # inputs = self.processor(text=[text], return_tensors="pt", padding=True).to(self.device)
        
        with torch.no_grad():
            outputs = self.model.get_text_features(**inputs)
        
        ans = outputs.cpu().numpy()
        return ans[0]


if __name__ == "__main__":

    clip_extractor = CLIPExtractor()

    sample_image = "images/狐狸.jpg"
    # 提取图像特征
    image_feature = clip_extractor.extract_image_from_file(sample_image)


    # 提取文本特征
    sample_text = "A photo of fox"
    text_feature = clip_extractor.extract_text(sample_text)

    # consine similarity
    cosine_similarity = np.dot(image_feature, text_feature) / (np.linalg.norm(image_feature) * np.linalg.norm(text_feature))
    print(cosine_similarity)