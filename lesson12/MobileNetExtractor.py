import os
import time
from transformers import AutoImageProcessor, AutoModelForImageClassification
from PIL import Image
import torch
import numpy as np
from scipy.spatial.distance import cosine

class MobileNetExtractor:
    def __init__(self):
        """初始化MobileNet并加载模型和预处理器"""
        self.model_name = "google/mobilenet_v2_1.0_224"
        self.preprocessor = AutoImageProcessor.from_pretrained(self.model_name)
        self.model = AutoModelForImageClassification.from_pretrained(self.model_name, output_hidden_states=True)

    def extract_feature(self, image):
        """
        输入图像路径或图像对象，返回抽取的特征。
        :param image: str 或 PIL.Image 对象
        :return: 抽取的特征 (list of float)
        """
        if isinstance(image, str):  # 如果是路径，加载图片
            image = Image.open(image)

        inputs = self.preprocessor(images=image, return_tensors="pt")
        outputs = self.model(**inputs)
        hidden_states = outputs.hidden_states

        # 提取最后一层的特征并进行平均化
        features = hidden_states[-1]
        reduced_feature = torch.mean(features, dim=(2, 3))

        return reduced_feature.squeeze().tolist()  # 返回list of float

    def extract_feature_and_label(self, image):
        """
        输入图像路径或图像对象，返回特征和预测的标签。
        :param image: str 或 PIL.Image 对象
        :return: (list of float, label)
        """
        if isinstance(image, str):
            image = Image.open(image)

        inputs = self.preprocessor(images=image, return_tensors="pt")
        outputs = self.model(**inputs)
        logits = outputs.logits
        hidden_states = outputs.hidden_states

        # 获取预测类别
        predicted_class_idx = logits.argmax(-1).item()
        predicted_label = self.model.config.id2label[predicted_class_idx]

        # 提取最后一层的特征并进行平均化
        features = hidden_states[-1]
        reduced_feature = torch.mean(features, dim=(2, 3))

        return reduced_feature.squeeze().tolist(), predicted_label

# 测试类功能
if __name__ == "__main__":
    extractor = MobileNetExtractor()
    image_files = ["images/狐狸.jpg", "images/狗.jpg", "images/老虎.jpg", "images/骆驼.jpg"]

    features_list = []
    labels_list = []

    for image_file in image_files:
        start_time = time.time()
        features, label = extractor.extract_feature_and_label(image_file)
        end_time = time.time()

        features_list.append(features)
        labels_list.append(label)

        print(f"Time to extract features from {image_file}: {end_time - start_time} seconds")
        print(f"Predicted label: {label}")

    # 计算两两之间的余弦距离
    for i in range(len(features_list)):
        for j in range(i + 1, len(features_list)):
            distance = cosine(features_list[i], features_list[j])
            print(f"Cosine distance between {image_files[i]} and {image_files[j]}: {distance}")
