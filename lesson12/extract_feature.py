import os
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com' # 设置环境变量

from transformers import AutoImageProcessor, AutoModelForImageClassification
from PIL import Image
import torch

# 加载本地图像
image_path = "images/狗.jpg"
image = Image.open(image_path)

# 加载预处理器和模型
preprocessor = AutoImageProcessor.from_pretrained("google/mobilenet_v2_1.0_224")
model = AutoModelForImageClassification.from_pretrained("google/mobilenet_v2_1.0_224", output_hidden_states=True)

# 预处理图像
inputs = preprocessor(images=image, return_tensors="pt")

# 获取模型输出
outputs = model(**inputs)
logits = outputs.logits
hidden_states = outputs.hidden_states  # 提取特征

# 获取预测类别
predicted_class_idx = logits.argmax(-1).item()
print("Predicted class:", model.config.id2label[predicted_class_idx])

# 打印logits
print("Logits:", logits)

# 提取最后一个隐藏层的特征（通常是最有代表性的）
features = hidden_states[-1]  # hidden_states[-1] 是最后一个隐藏层的输出
print("Extracted features:", features.shape)  # 例如，你可以查看特征维度

#将1 320 7 7的特征平均化为1 320
reduced_feature = torch.mean(features, dim=(2, 3))
print("Reduced features:", reduced_feature.shape)

# 如果你想将这些特征进一步处理或保存为numpy数组：
features_np = features.detach().numpy()
