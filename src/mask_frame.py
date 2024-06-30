import numpy as np
import cv2

def mask(frame, color_name, left=0, right=1):
    # 获取图像的高度和宽度
    height, width, _ = frame.shape

    # 计算要保留的区域的起始和结束位置
    left_idx = int(left * width)
    right_idx = int(right * width)

    # copy from frame
    masked_frame = frame.copy()

    # 选择保留的颜色通道
    if color_name == 'r':
        channel_idx = 2  # 红色通道
    elif color_name == 'g':
        channel_idx = 1  # 绿色通道
    elif color_name == 'b':
        channel_idx = 0  # 蓝色通道
    else:
        raise ValueError("color_name must be one of 'r', 'g', or 'b'")

    # 复制指定区域的指定通道值到新图像
    for channel in range(3):
        if channel == channel_idx:
            # masked_frame[:, left_idx:right_idx, channel_idx] = frame[:, left_idx:right_idx, channel_idx]
            pass
        else:
            masked_frame[:, left_idx:right_idx, channel] = 0

    return masked_frame

# 示例使用
if __name__ == "__main__":
    # 读取图像
    try:
        from src.capture_frame import capture_frame
    except:
        from capture_frame import capture_frame

    frame = capture_frame(5)

    # 应用mask函数，保留红色通道，区域为左边50%
    masked_frame = mask(frame, 'r', left=0, right=0.5)

    # 显示原图和处理后的图像
    cv2.imshow('Original', frame)
    cv2.imshow('Masked', masked_frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
