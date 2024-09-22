import cv2
import mediapipe as mp
import numpy as np

# 初始化MediaPipe手势模型
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False,
                        max_num_hands=2,
                        min_detection_confidence=0.5,
                        min_tracking_confidence=0.5)

# 用于绘制关键点的函数
def draw_landmarks(image, hand_landmarks, handedness, classification):
    # 绘制关键点
    for landmark in hand_landmarks.landmark:
        x, y = int(landmark.x * image.shape[1]), int(landmark.y * image.shape[0])
        cv2.circle(image, (x, y), 5, (0, 255, 0), -1)

    # 显示分类结果
    cv2.putText(image, f"Hand: {classification}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

# 分类函数
def classify_hand(coordinates):
    threshold1 = (-0.2352 + -0.1755) / 2
    threshold2 = (0.0013 + -0.1595) / 2
    
    if coordinates[32] < threshold1:
        return "Scissors"
    elif coordinates[32] < threshold2:
        return "Paper"
    else:
        return "Rock"

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

            # 提取关键点数据并归一化
            landmarks = np.array([[landmark.x, landmark.y, landmark.z] for landmark in max_hand.landmark])
            mean = np.mean(landmarks, axis=0)
            normalized_landmarks = landmarks - mean

            xs = normalized_landmarks[:, 0].tolist()
            ys = normalized_landmarks[:, 1].tolist()
            zs = normalized_landmarks[:, 2].tolist()

            # 将归一化后的坐标转换为list of float，格式为21个x, 21个y, 21个z
            # coordinates = normalized_landmarks.flatten().tolist()
            coordinates = xs + ys + zs

            # 分类
            classification = classify_hand(coordinates)

            # 绘制关键点和分类结果
            draw_landmarks(image, max_hand, None, classification)

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
