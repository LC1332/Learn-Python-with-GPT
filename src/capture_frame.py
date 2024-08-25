# 我希望实现一个capture_frame() 函数


# 这个函数会打开一个摄像头，在摄像头上显示左右镜像过的画面

# 同时，在frame上回渲染一个进度条，进度条随着时间会从左到右运行，总共10秒

# 10秒后会记录frame，release掉camera对象，并且return记录下来的frame

import cv2
import time

def capture_frame( duration = 5 ):
    # 打开摄像头
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return None

    start_time = time.time()
    # duration = 10  # 10秒
    frame = None

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # 左右镜像翻转
        frame = cv2.flip(frame, 1)

        # 计算进度条位置
        elapsed_time = time.time() - start_time
        progress = min(elapsed_time / duration, 1.0)

        # 渲染进度条
        height, width, _ = frame.shape
        bar_width = int(progress * width)
        cv2.rectangle(frame, (0, height - 50), (bar_width, height - 30), (0, 255, 0), -1)

        # 显示图像
        cv2.imshow('Mirrored Frame with Progress Bar', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # 10秒后记录frame并退出循环
        if elapsed_time >= duration:
            break

    # 记录下当前帧
    captured_frame = frame

    # 释放摄像头并关闭窗口
    cap.release()
    cv2.destroyAllWindows()

    return captured_frame

def display_frame_in_notebook(frame):
    from IPython.display import display, Image
    import PIL.Image
    # 将OpenCV的BGR格式转换为RGB格式
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # 将NumPy数组转换为PIL图像
    img = PIL.Image.fromarray(frame_rgb)
    # 使用IPython显示图像
    display(img)

if __name__ == '__main__':

    # 调用函数并显示捕获的帧
    captured_frame = capture_frame()
    if captured_frame is not None:
        cv2.imshow('Captured Frame', captured_frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
