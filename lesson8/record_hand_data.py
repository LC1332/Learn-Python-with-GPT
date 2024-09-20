import cv2
import mediapipe as mp
import numpy as np
import pandas as pd
import os
import time

# 初始化MediaPipe手势模型
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False,
                        max_num_hands=2,
                        min_detection_confidence=0.5,
                        min_tracking_confidence=0.5)

# 用于绘制关键点的函数
def draw_landmarks(image, hand_landmarks, handedness):
    # 绘制关键点
    for landmark in hand_landmarks.landmark:
        x, y = int(landmark.x * image.shape[1]), int(landmark.y * image.shape[0])
        cv2.circle(image, (x, y), 5, (0, 255, 0), -1)

# 主程序
def main():
    cap = cv2.VideoCapture(0)
    csv_file = 'lesson8/hand_record_data/hand_data.csv'
    img_dir = 'lesson8/hand_record_data/imgs'
    os.makedirs(img_dir, exist_ok=True)

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            continue

        # 左右镜像翻转
        image = cv2.flip(image, 1)

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
            handedness = results.multi_handedness[results.multi_hand_landmarks.index(max_hand)].classification[0].label

            # 绘制关键点
            draw_landmarks(image, max_hand, handedness)

        # 显示图像
        cv2.imshow('MediaPipe Hands', image)

        # 按键处理
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        elif key != -1 and max_hand is not None:
            # 记录数据
            landmarks = [landmark.x for landmark in max_hand.landmark] + [landmark.y for landmark in max_hand.landmark] + [landmark.z for landmark in max_hand.landmark]
            data = [chr(key)] + landmarks
            df = pd.DataFrame([data])
            df.to_csv(csv_file, mode='a', header=not os.path.exists(csv_file), index=False)

            # 保存图片
            timestamp = int(time.time())
            img_name = f"{chr(key)}_{timestamp}.jpg"
            img_path = os.path.join(img_dir, img_name)
            cv2.imwrite(img_path, image)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
