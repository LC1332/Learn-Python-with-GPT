import numpy as np
import os
import pickle

# 假设CLIPExtractor类和cosine_similarity函数已经定义
from src.CLIPExtractor import CLIPExtractor

def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

class ImageDatabase:
    def __init__(self, folder_name="record_images"):
        self.folder_name = folder_name
        self.feature_dict = self._load_features()
        # 如果你有cache_dir的话，在这里指定，没有的话直接用 self.clip_extractor = CLIPExtractor() 初始化就可以。
        cache_dir = "D:\\aistudio\\LubaoGithub\\models"
        self.clip_extractor = CLIPExtractor(model_name = "openai/clip-vit-large-patch14", cache_dir = cache_dir)
        self._update_features()

    def _load_features(self):
        feature_file = os.path.join(self.folder_name, "feature.pkl")
        if os.path.exists(feature_file):
            with open(feature_file, 'rb') as f:
                return pickle.load(f)
        else:
            return {}

    def _update_features(self):
        for filename in os.listdir(self.folder_name):
            if filename.endswith(".jpg"):
                img_path = os.path.join(self.folder_name, filename)
                if filename not in self.feature_dict:
                    feature = self.clip_extractor.extract_image_from_file(img_path)
                    self.feature_dict[filename] = feature
        self._save_features()

    def _save_features(self):
        feature_file = os.path.join(self.folder_name, "feature.pkl")
        with open(feature_file, 'wb') as f:
            pickle.dump(self.feature_dict, f)

    def search_with_feature(self, query_feature):
        max_similarity = -1
        most_similar_image = None

        for filename, feature in self.feature_dict.items():
            similarity = cosine_similarity(query_feature, feature)
            if similarity > max_similarity:
                max_similarity = similarity
                most_similar_image = filename

        return most_similar_image, max_similarity
    