import cv2
import mediapipe as mp
import numpy as np
import pandas as pd
import os
import time
from classify_hand import classify_hand

# 初始化MediaPipe手势模型
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False,
                        max_num_hands=2,
                        min_detection_confidence=0.5,
                        min_tracking_confidence=0.5)

# 用于绘制关键点的函数
def draw_landmarks(image, hand_landmarks):
    # 绘制关键点
    for landmark in hand_landmarks.landmark:
        x, y = int(landmark.x * image.shape[1]), int(landmark.y * image.shape[0])
        cv2.circle(image, (x, y), 5, (0, 255, 0), -1)

# 归一化坐标
def normalize_landmarks(landmarks):
    x = np.array([landmark.x for landmark in landmarks])
    y = np.array([landmark.y for landmark in landmarks])
    z = np.array([landmark.z for landmark in landmarks])
    
    # 减去均值
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    z_mean = np.mean(z)
    
    x = x - x_mean
    y = y - y_mean
    z = z - z_mean
    
    # 合并成一个列表
    normalized_coordinates = np.concatenate([x, y, z]).tolist()
    return normalized_coordinates

# 主程序
def main():
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            continue

        # 左右镜像翻转
        image = cv2.flip(image, 1)

        original_image = image.copy()

        # 处理图像
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        max_hand = None
        # 如果检测到手势
        if results.multi_hand_landmarks:
            # 找到最大的手
            max_hand = max(results.multi_hand_landmarks, key=lambda h: h.landmark[0].x)

            # 绘制关键点
            draw_landmarks(image, max_hand)

            # 归一化坐标
            normalized_coordinates = normalize_landmarks(max_hand.landmark)

            # 调用classify_hand函数
            result = classify_hand(normalized_coordinates)

            # 显示结果
            if result == 0:
                cv2.putText(image, "Rock", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            elif result == 1:
                cv2.putText(image, "Scissors", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            elif result == 2:
                cv2.putText(image, "Paper", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        # 显示图像
        cv2.imshow('MediaPipe Hands', image)

        # 按键处理
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
