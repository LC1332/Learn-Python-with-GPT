import cv2
import mediapipe as mp
import numpy as np

# 初始化MediaPipe的人体检测模型
mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

# 打开默认摄像头
cap = cv2.VideoCapture(0)

# MediaPipe模型
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:

    while cap.isOpened():
        # 读取摄像头帧
        success, image = cap.read()
        if not success:
            continue

        # 图像左右镜像
        image = cv2.flip(image, 1)

        # 转换颜色从BGR到RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # 处理图像
        results = holistic.process(image)

        # 转换颜色从RGB到BGR
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # 检测到人体时，用绿色框框住
        if results.pose_landmarks:
            # 获取人体中心点
            x_center = results.pose_landmarks.landmark[mp_holistic.PoseLandmark.NOSE].x * image.shape[1]
            # 检测人体中心是否在画面左半边
            if x_center < image.shape[1] / 2:
                # 创建红色半透明的遮罩层
                overlay = image.copy()
                cv2.rectangle(overlay, (0, 0), (int(image.shape[1] / 2), image.shape[0]), (0, 0, 255), -1)
                alpha = 0.5
                image = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)

            # 在原图上绘制人体关键点
            mp_drawing.draw_landmarks(
                image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
                mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2)
            )

            # 绘制绿色边框
            x_min, y_min = int(results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_SHOULDER].x * image.shape[1]), int(results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_SHOULDER].y * image.shape[0])
            x_max, y_max = int(results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_SHOULDER].x * image.shape[1]), int(results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_SHOULDER].y * image.shape[0])
            cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

        # 显示结果
        cv2.imshow('MediaPipe Holistic', image)

        # 按'q'键退出
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

# 释放摄像头
cap.release()
