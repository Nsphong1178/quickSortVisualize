import cv2
import numpy as np


def draw_bars(arr, selected_index, width, height):
    bar_width = width // len(arr)
    bar_height_scale = (height - 100) / max(arr)

    # Tạo hình ảnh trắng
    image = 255 * np.ones((height, width, 3), dtype=np.uint8)

    # Vẽ các thanh cột
    for i, num in enumerate(arr):
        bar_height = int(num * bar_height_scale)
        bar_x = i * bar_width
        bar_y = height - 100 - bar_height
        bar_color = (0, 0, 250) if i == selected_index else (0, 0, 0)
        cv2.rectangle(image, (bar_x, bar_y), (bar_x + bar_width, height - 100), bar_color, -1)

    # Hiển thị hình ảnh
    cv2.imshow("Sorting Visualization", image)
    cv2.waitKey(500)


def selection_sort(arr, width, height):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        draw_bars(arr, i, width, height)  # Hiển thị mỗi bước sắp xếp


# Nhập số lượng phần tử từ bàn phím
num = int(input("Nhập số lượng phần tử: "))

# Nhập các phần tử từ bàn phím
numList = []
for i in range(num):
    numList.append(int(input()))

# Tính toán kích thước hình ảnh dựa trên số lượng phần tử
width = 2000
bar_width = width // num
height = max(numList) * bar_width + 200

# Tạo cửa sổ hiển thị
cv2.namedWindow("Sorting Visualization", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("Sorting Visualization", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
# Hiển thị mảng ban đầu
draw_bars(numList, -1, width, height)
cv2.waitKey(3000)

# Sắp xếp mảng và hiển thị từng bước
selection_sort(numList, width, height)

cv2.waitKey(0)
cv2.destroyAllWindows()
