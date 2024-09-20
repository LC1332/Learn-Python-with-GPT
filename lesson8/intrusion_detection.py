import cv2
import mediapipe as mp
import numpy as np

# 初始化MediaPipe的Holistic模型
mp_holistic = mp.solutions.holistic
holistic = mp_holistic.Holistic()

# flip函数，用于左右镜像翻转图像
def flip(image):
    return cv2.flip(image, 1)

# 判断点是否在多边形内的函数
def point_in_polygon(point, polygon):
    x, y = point
    n = len(polygon)
    inside = False
    p1x, p1y = polygon[0]
    for i in range(n+1):
        p2x, p2y = polygon[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside

# 绘制入侵区域的边缘
def draw_intrusion_area(image, points):
    cv2.polylines(image, [np.array(points, dtype=np.int32)], True, (0, 0, 255), 2)

# 判断人体底部中心点是否进入入侵区域
def is_body_center_in_area(center, area):
    return point_in_polygon(center, area)

# 渲染对应的区域为红色透明
def render_area_red_transparent(image, points):
    overlay = image.copy()
    cv2.fillPoly(overlay, [np.array(points, dtype=np.int32)], (0, 0, 255, 50))
    cv2.addWeighted(overlay, 0.5, image, 0.5, 0, image)

# 入侵检测区域坐标
intrusion_area = [(200, 240), (440, 240), (620, 470), (20, 470)]

# 打开摄像头
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        continue

    # 左右镜像翻转图像
    image = flip(image)
    # 转换为RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # 处理图像
    results = holistic.process(image)
    # 转换回BGR
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # 绘制入侵区域边缘
    draw_intrusion_area(image, intrusion_area)

    # 检测人体并在人体周围画绿色框
    if results.pose_landmarks:
        h, w, c = image.shape
        # 获取人体底部中心点
        hip_left = results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_HIP]
        hip_right = results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_HIP]
        center_x = int((hip_left.x + hip_right.x) * w / 2)
        center_y = int((hip_left.y + hip_right.y) * h / 2)
        body_center = (center_x, center_y)
        cv2.rectangle(image, (int(hip_left.x * w), int(hip_left.y * h)),
                      (int(hip_right.x * w), int(hip_right.y * h)),
                      (0, 255, 0), 2)

        # 检查人体底部中心点是否在入侵区域内
        if is_body_center_in_area(body_center, intrusion_area):
            render_area_red_transparent(image, intrusion_area)

    cv2.imshow('MediaPipe Holistic', image)

    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
