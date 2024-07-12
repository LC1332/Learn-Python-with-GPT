import cv2
import numpy as np

def dilate_image(image_path, output_path, dilation_size):
    # 读取带有alpha通道的图像
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    
    # 分离通道
    b_channel, g_channel, r_channel, a_channel = cv2.split(image)
    
    # 创建膨胀核
    kernel = np.ones((dilation_size, dilation_size), np.uint8)
    
    # 对每个通道进行膨胀
    b_dilated = cv2.dilate(b_channel, kernel, iterations=1)
    g_dilated = cv2.dilate(g_channel, kernel, iterations=1)
    r_dilated = cv2.dilate(r_channel, kernel, iterations=1)
    a_dilated = cv2.dilate(a_channel, kernel, iterations=1)
    
    # 合并通道
    dilated_image = cv2.merge((b_dilated, g_dilated, r_dilated, a_dilated))
    
    # 保存膨胀后的图像
    cv2.imwrite(output_path, dilated_image)
    print(f"Dilated image saved to {output_path}")

# 图像路径和输出路径
image_path = 'images/car2.png'
output_path = 'images/car2_dilated.png'

# 膨胀大小
dilation_size = 11  # 11x11的核将膨胀5个像素

# 执行膨胀操作
dilate_image(image_path, output_path, dilation_size)
