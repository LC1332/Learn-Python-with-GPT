import cv2

cap = cv2.VideoCapture(0)  # 初始化摄像头
if not cap.isOpened():  # 检查摄像头是否打开
    print("无法打开摄像头")
    exit()

while True:
    ret, frame = cap.read()  # 从摄像头读取一帧
    if ret:  # 如果读取帧成功
        mirrored_frame = cv2.flip(frame, 1)  # 实现左右镜像
        cv2.imshow('Mirrored Camera', mirrored_frame)  # 显示镜像后的图像
        if cv2.waitKey(1) == ord('q'):  # 按 'q' 键退出循环
            break
    else:
        print("无法从摄像头读取帧")
        break

cap.release()  # 释放摄像头资源
cv2.destroyAllWindows()  # 关闭所有OpenCV窗口
