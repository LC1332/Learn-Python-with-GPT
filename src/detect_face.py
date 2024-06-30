# 我希望实现一个detect_one_face( frame )函数

# 利用opencv对frame中的人脸进行检测，对于最大的人脸，返回人脸的中心坐标x, y

# 如果没有人脸，返回-1, -1

import cv2

def detect_one_face(frame):
    # 加载预训练的人脸检测分类器模型
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # 转换为灰度图像
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 检测人脸
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

    if len(faces) == 0:
        return -1, -1

    # 找到最大的脸
    largest_face = max(faces, key=lambda rect: rect[2] * rect[3])

    # 计算人脸中心点坐标
    x, y, w, h = largest_face
    center_x = x + w // 2
    center_y = y + h // 2

    return center_x, center_y

if __name__ == '__main__':
    try:
        from src.capture_frame import capture_frame
    except:
        from capture_frame import capture_frame

    frame = capture_frame(5)
    center_x, center_y = detect_one_face(frame)
    print(center_x, center_y)