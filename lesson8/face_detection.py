import cv2
import mediapipe as mp

# 初始化Mediapipe人脸检测
mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5)

def process_frame(frame):
    # 图像左右镜像
    frame = cv2.flip(frame, 1)

    # 将图像从BGR转换为RGB，因为Mediapipe需要RGB图像
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # 使用Mediapipe处理帧进行人脸检测
    results = face_detection.process(rgb_frame)

    # 检查是否检测到人脸
    if results.detections:
        for detection in results.detections:
            # 提取边界框坐标
            bbox = detection.location_data.relative_bounding_box
            x, y, w, h = int(bbox.xmin * frame.shape[1]), int(bbox.ymin * frame.shape[0]), \
                         int(bbox.width * frame.shape[1]), int(bbox.height * frame.shape[0])

            # 在检测到的人脸周围画一个绿色的矩形框
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return frame

def main():
    # 访问默认摄像头
    cap = cv2.VideoCapture(0)

    while True:
        # 从摄像头读取一帧
        ret, frame = cap.read()

        if not ret:
            print("无法捕获帧")
            break

        # 处理帧
        processed_frame = process_frame(frame)

        # 显示处理后的帧
        cv2.imshow('Face_Detection', processed_frame)

        # 如果按下'q'键，则退出循环
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 释放摄像头并关闭所有窗口
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
