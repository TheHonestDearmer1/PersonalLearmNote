## 使用OpenCv进行角度测量

- 使用OpenCV进行角度测量可以通过以下步骤实现：图像读取与显示、鼠标点击事件处理、点和连线绘制、斜率和角度计算、角度显示和循环执行与退出。
- 通过`cv2.imshow()`函数显示图像，`cv2.setMouseCallback()`函数设置鼠标点击事件处理函数。
- 在鼠标点击事件处理函数中，将点击坐标存储在列表中。
- 使用`cv2.circle()`绘制选定的点，使用`cv2.line()`在相邻的点之间绘制连线。
- 通过计算两点之间斜率的函数和公式计算角度的弧度值，并转换为角度值。
- 使用`cv2.putText()`函数在图像上显示角度。
- 通过无限循环实现连续角度测量，按下 'q' 键退出并重置点列表和图像。

希望对你有帮助！如有其他问题，请随时提问。

```python
import cv2
import math
 
# 读取图像
path = 'test.jpg'
img = cv2.imread(path)
pointsList = []

# 鼠标点击事件处理函数
def mousePoints(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        size = len(pointsList)
        # 如果已经选择了一部分点，并且当前点不是每组 3 个点中的最后一个点
        if size != 0 and size % 3 != 0:
            # 在前一个点和当前点之间画线
            cv2.line(img, tuple(pointsList[round((size-1)/3)*3]), (x,y), (0,0,255), 2)
        # 在当前点位置画圆
        cv2.circle(img, (x,y), 5, (0,0,255), cv2.FILLED)
        # 将当前点坐标添加到列表中
        pointsList.append([x, y])
 
# 计算两点间的斜率
def gradient(pt1, pt2):
    return (pt2[1] - pt1[1]) / (pt2[0] - pt1[0])
 
# 计算三个点构成的角度
def getAngle(pointsList):
    pt1, pt2, pt3 = pointsList[-3:]  # 获取最后三个点
    m1 = gradient(pt1, pt2)  # 计算第一条线的斜率
    m2 = gradient(pt1, pt3)  # 计算第二条线的斜率
    angR = math.atan((m2 - m1) / (1 + (m2 * m1)))  # 计算角度的弧度值
    angD = round(math.degrees(angR))  # 将角度转换为度数并四舍五入
 
    # 在图像中显示角度值
    cv2.putText(img, str(angD), (pt1[0]-40, pt1[1]-20), cv2.FONT_HERSHEY_COMPLEX,
                1.5, (0,0,255), 2)
 
while True:
    # 检查是否已经选择了一组完整的三个点
    if len(pointsList) % 3 == 0 and len(pointsList) != 0:
        getAngle(pointsList)  # 计算角度
 
    cv2.imshow('Image', img)
    cv2.setMouseCallback('Image', mousePoints)  # 设置鼠标点击事件回调函数
    if cv2.waitKey(1) & 0xFF == ord('q'):  # 按下 'q' 键退出程序
        pointsList = []  # 重置点列表
        img = cv2.imread(path)  # 重新加载图像
```

