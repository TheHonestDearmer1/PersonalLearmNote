 

> 省流：
> 
> 1.  内含 Python Opencv 双目相机拍照代码（手动 or 自动），可自取；
> 2.  如果你的 cv2.VideoCapture() 函数卡住但不报错，打开 Windows “相机”应用可以正常看到摄像头画面，且能够正常用 cv2.imshow() 打开图像，请继续阅读。

这个学期选修了方璐老师的媒体与认知课程，期末的 Final Project 涉及到[双目相机](https://so.csdn.net/so/search?q=%E5%8F%8C%E7%9B%AE%E7%9B%B8%E6%9C%BA&spm=1001.2101.3001.7020)的标定问题（也许期末做完 Project 我会发一些感想和体会？）

助教提供了一段基于 Python [Opencv](https://so.csdn.net/so/search?q=Opencv&spm=1001.2101.3001.7020) 的双目相机自动拍摄和保存的代码给我们直接用，但是在运行的时候我遇到了奇怪的现象，程序卡在 cv2.VideoCapture(0) 这里就不能运行，不报错，就是单纯的卡在这里。先放代码：

```python
import time
 
import cv2
import numpy as np
 
AUTO = False  # 自动拍照，或手动按s键拍照
INTERVAL = 2  # 自动拍照间隔
 
camera_0 = cv2.VideoCapture(0) # 代码运行的时候卡在这里！！
camera_1 = cv2.VideoCapture(1)
 
cv2.namedWindow("left")
cv2.namedWindow("right")
 
counter = 0
utc = time.time()
folder = "./SaveImage/"  # 拍照文件目录， 先新建再运行，否则无法保存
 
 
def shot(pos, frame):
    global counter
    path = folder + pos + "_" + str(counter) + ".jpg"
    cv2.imwrite(path, frame)
    print("snapshot saved into: " + path)
 
 
while True:
    ret_0, frame_0 = camera_0.read()
    ret_1, frame_1 = camera_1.read()
    left_frame = frame_0
    right_frame = frame_1
    cv2.imshow("left", left_frame)
    cv2.imshow("right", right_frame)
    now = time.time()
 
    if AUTO and now - utc >= INTERVAL:
        shot("left", left_frame)
        shot("right", right_frame)
        counter += 1
        utc = now
 
    key = cv2.waitKey(1)
 
    # press 's' in keyboard for capturing, 'q' for exit.
    if key == ord("q"):
        break
    elif key == ord("s"):
        shot("left", left_frame)
        shot("right", right_frame)
        counter += 1
 
camera_0.release()
camera_1.release()
cv2.destroyWindow("left")
cv2.destroyWindow("right")
```

这就比较违反常理，我和助教进行了一番讨论，无果。

最后解决的办法也比较奇怪，把卡住的代码修改为：

```python
camera_0 = cv2.VideoCapture(0, cv2.CAP_DSHOW)
```

就可以了。（当然每一个 cv2.VideoCapture 都要改一下的）

这里我并不知道是怎么回事，我找到的一些资料说这个参数的作用是“不指定无法使用高分辨率摄像头”，那是不是有可能是因为课程提供的摄像头非常高清导致不设置不能使用（瞎猜，如有了解万望赐教）？因为我对 opencv 这个库基本上不了解，感觉这个大作业里面涉及到 opencv 的也就是拍个照，就不会深究了。

希望能帮助到一些和我一样在这里 stuck 的同学们~

（希望我的大作业能继续推进啊啊啊啊啊啊）

### 2022.12.14 补充

最近准备用新装的 Fedora 37 做开发平台了，于是把之前的代码 copy 到 Linux 上试了一下，发现 Linux 好像并不需要加这个参数……就还挺无语的 orz

文章知识点与官方知识档案匹配，可进一步学习相关知识

[OpenCV技能树](https://edu.csdn.net/skill/opencv/?utm_source=csdn_ai_skill_tree_blog)[首页](https://edu.csdn.net/skill/opencv/?utm_source=csdn_ai_skill_tree_blog)[概览](https://edu.csdn.net/skill/opencv/?utm_source=csdn_ai_skill_tree_blog)24285 人正在系统学习中

本文转自 <https://blog.csdn.net/qq_53937391/article/details/128046952>，如有侵权，请联系删除。