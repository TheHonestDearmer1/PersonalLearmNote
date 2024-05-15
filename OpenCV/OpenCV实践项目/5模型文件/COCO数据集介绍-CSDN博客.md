 

#### [COCO数据集](https://so.csdn.net/so/search?q=COCO%E6%95%B0%E6%8D%AE%E9%9B%86&spm=1001.2101.3001.7020)详细介绍

*   [前言](#_3)
*   [一、什么是COCO数据集？](#COCO_7)
*   *   [COCO数据集可以应用到的Task：](#COCOTask_10)
    *   [一个简单的数据集实例展示：](#_24)
    *   [附录](#_28)
    *   *   [80个类别](#80_29)
*   [二、COCO数据集的格式介绍](#COCO_56)
*   *   [基础的数据格式介绍](#_59)
    *   [不同Task下的annotation](#Taskannotation_80)
    *   *   [Object Detection annotation](#Object_Detection_annotation_82)
        *   [other task：](#other_task_100)
    *   [Result format 输出格式](#Result_format___103)
*   [三、COCO数据集的下载](#COCO_107)

前言
--

以下内容均来自[COCO官方](https://cocodataset.org/#home)  
以及[Microsoft COCO: Common Objects in Context](https://arxiv.org/pdf/1405.0312.pdf)

一、什么是COCO数据集？
-------------

COCO数据集是一个可用于图像检测（image detection），[语义分割](https://so.csdn.net/so/search?q=%E8%AF%AD%E4%B9%89%E5%88%86%E5%89%B2&spm=1001.2101.3001.7020)（semantic segmentation）和图像标题生成（image captioning）的大规模数据集。它有超过330K张图像（其中220K张是有标注的图像），包含150万个目标，80个目标类别（object categories：行人、汽车、大象等），91种材料类别（stuff categoris：草、墙、天空等），每张图像包含五句图像的语句描述，且有250,000个带关键点标注的行人。

### COCO数据集可以应用到的Task：

1.  目标检测（object detection），使用 bounding box 或者 object segmentation (也称为instance segmentation)将不同的目标进行标定。  
    ![在这里插入图片描述](https://img-blog.csdnimg.cn/5dc9dcdbf85a4d3e8373020202a78da3.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA562J5b6F5oiI5aSa44CC,size_20,color_FFFFFF,t_70,g_se,x_16)  
    COCO数据集用于image segmentation的教程：[Master the COCO Dataset for Semantic Image Segmentation](https://towardsdatascience.com/master-the-coco-dataset-for-semantic-image-segmentation-part-1-of-2-732712631047)
2.  Densepose（密集姿势估计），DensePose任务涉及同时检测人、分割他们的身体并将属于人体的所有图像像素映射到身体的3D表面。用于不可控条件下的密集人体姿态估计。![1](https://img-blog.csdnimg.cn/2fefb41ac395401d918e4df432132554.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA562J5b6F5oiI5aSa44CC,size_20,color_FFFFFF,t_70,g_se,x_16)
3.  Key-points detection（关键点检测），在任意姿态下对人物的关键点进行定位，该任务包含检测行人及定位到行人的关键点。  
    ![0](https://img-blog.csdnimg.cn/5582fb173a0542eda65cb2512a1a4630.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA562J5b6F5oiI5aSa44CC,size_20,color_FFFFFF,t_70,g_se,x_16)
4.  Stuff Segmentation，语义分割中针对stuff class类的分割。（草，墙壁，天空等）  
    ![在这里插入图片描述](https://img-blog.csdnimg.cn/00df72b46c2e43fdb3e8c1f0c53b3c7d.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA562J5b6F5oiI5aSa44CC,size_20,color_FFFFFF,t_70,g_se,x_16)
5.  Panoptic Segmentation（全景分割）。其目的是生成丰富且完整的连贯场景分割，这是实现自主驾驶或增强现实等真实世界视觉系统的重要一步。  
    ![在这里插入图片描述](https://img-blog.csdnimg.cn/82d96c0e10f84cfcbb68f4cd79f0f4e6.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA562J5b6F5oiI5aSa44CC,size_20,color_FFFFFF,t_70,g_se,x_16)
6.  image captioning（图像标题生成），根据图像生成一段文字。  
    ![在这里插入图片描述](https://img-blog.csdnimg.cn/43f591aff7ee45ab97c2c378c6d6cb56.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA562J5b6F5oiI5aSa44CC,size_20,color_FFFFFF,t_70,g_se,x_16)

### 一个简单的数据集实例展示：

一张包含汽车，行人，画板的图片：  
![1](https://img-blog.csdnimg.cn/c513032663a54fe59341e3ab7e4910d5.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA562J5b6F5oiI5aSa44CC,size_20,color_FFFFFF,t_70,g_se,x_16)  
![1](https://img-blog.csdnimg.cn/97545fcba86641ed8a85e39b9f4822e1.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA562J5b6F5oiI5aSa44CC,size_20,color_FFFFFF,t_70,g_se,x_16)

### 附录

#### 80个类别

![0](https://img-blog.csdnimg.cn/daf866bae93c45f8ae0795b36c5dbae2.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA562J5b6F5oiI5aSa44CC,size_20,color_FFFFFF,t_70,g_se,x_16)

person(人)

交通工具：bicycle(自行车) car(汽车) motorbike(摩托车) aeroplane(飞机) bus(公共汽车) train(火车) truck(卡车) boat(船)

公共设施：traffic light(信号灯) fire hydrant(消防栓) stop sign(停车标志) parking meter(停车计费器) bench(长凳)

动物：bird(鸟) cat(猫) dog(狗) horse(马) sheep(羊) cow(牛) elephant(大象) bear(熊) zebra(斑马) giraffe(长颈鹿)

生活用品：backpack(背包) umbrella(雨伞) handbag(手提包) tie(领带) suitcase(手提箱)

运动装备：frisbee(飞盘) skis(滑雪板双脚) snowboard(滑雪板) sports ball(运动球) kite(风筝) baseball bat(棒球棒) baseball glove(棒球手套) skateboard(滑板) surfboard(冲浪板) tennis racket(网球拍)

餐具：bottle(瓶子) wine glass(高脚杯) cup(茶杯) fork(叉子) knife(刀)  
spoon(勺子) bowl(碗)

水果：banana(香蕉) apple(苹果) sandwich(三明治) orange(橘子) broccoli(西兰花) carrot(胡萝卜) hot dog(热狗) pizza(披萨) donut(甜甜圈) cake(蛋糕)

家居：chair(椅子) sofa(沙发) pottedplant(盆栽植物) bed(床) diningtable(餐桌) toilet(厕所) tvmonitor(电视机)

电子产品：laptop(笔记本) mouse(鼠标) remote(遥控器) keyboard(键盘) cell phone(电话)  
家用电器：microwave(微波炉) oven(烤箱) toaster(烤面包器) sink(水槽) refrigerator(冰箱)  
家用产品：book(书) clock(闹钟) vase(花瓶) scissors(剪刀) teddy bear(泰迪熊) hair drier(吹风机) toothbrush(牙刷)

二、COCO数据集的格式介绍
--------------

针对上述提到不同的TASK（object detection, keypoint detection, stuff segmentation, panoptic segmentation, densepose, and image captioning），COCO数据集有不同的标注类型。这些标注类型都用“JSON”格式进行存储。接下来将针对性的对其JSON内的标注格式进行详细介绍。

### 基础的数据格式介绍

针对所有的TASK，所有的annotation都有如下的相同的数据结构/格式：

```c
{
"info": info, "images": [image], "annotations": [annotation], "licenses": [license],
}

info{
"year": int, "version": str, "description": str, "contributor": str, "url": str, "date_created": datetime,
}

image{
"id": int, "width": int, "height": int, "file_name": str, "license": int, "flickr_url": str, "coco_url": str, "date_captured": datetime,
}

license{
"id": int, "name": str, "url": str,
}
```

提示：info内的信息不需要怎么管，是数据来源和贡献者等信息。license也不需要管。annotation是指不同的TASK的annotation，（那六种task）。image内是图片的size，id，file\_name等等。

### 不同Task下的annotation

针对不同task的annotation，我们分别进行描述：

#### Object Detection annotation

```c
annotation{
"id": int, "image_id": int, "category_id": int, "segmentation": RLE or [polygon], "area": float, "bbox": [x,y,width,height], "iscrowd": 0 or 1,
}

categories[{
"id": int, "name": str, "supercategory": str,
}]
```

iscrowd:0 对应polygon （多边形） 注意：单个对象也可能需要多个多边形，例如我们上面例子中的汽车的多边形的分割，就是两个多边形。（蓝色代表为汽车）![0](https://img-blog.csdnimg.cn/8c8f5a362fbc4b0eb31aabaa34d87428.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA562J5b6F5oiI5aSa44CC,size_10,color_FFFFFF,t_70,g_se,x_16)

iscrowd:1 对应segmentation:RLE编码 。 一般用于标注大量的密集对象。

除此之外，还为每个对象提供了一个封闭的bounding box（框坐标从图像左上角开始测量，并为0索引）。最后，注释结构的categories字段用于存储类别id到类别和超类别名称的映射。 （例如 id:0 对应映射 为people）

#### other task：

其它annotation的介绍略过，可以参考 [https://cocodataset.org/#format-data](https://cocodataset.org/#format-data)

### Result format 输出格式

为了便于比较，COCO采用统一的输出格式。具体格式形式可以参考：[https://cocodataset.org/#format-results](https://cocodataset.org/#format-results)。  
便于后续可以通过官方的测试集来和公共榜单上的结果比较。

三、COCO数据集的下载
------------

下载网址：[官网下载链接](https://cocodataset.org/#download)  
![1](https://img-blog.csdnimg.cn/aa21f658133941958de00d294a37507c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA562J5b6F5oiI5aSa44CC,size_20,color_FFFFFF,t_70,g_se,x_16)  
不用全部下载，只需要下载2017 Train images\\2017 Val images\\和对应的所需的Task的annotation即可。

 

文章知识点与官方知识档案匹配，可进一步学习相关知识

[OpenCV技能树](https://edu.csdn.net/skill/opencv/opencv-a181ede3b8c7487fbcc212796c27ce77?utm_source=csdn_ai_skill_tree_blog)[OpenCV中的深度学习](https://edu.csdn.net/skill/opencv/opencv-a181ede3b8c7487fbcc212796c27ce77?utm_source=csdn_ai_skill_tree_blog)[图像分类](https://edu.csdn.net/skill/opencv/opencv-a181ede3b8c7487fbcc212796c27ce77?utm_source=csdn_ai_skill_tree_blog)24310 人正在系统学习中

本文转自 <https://blog.csdn.net/qq_44554428/article/details/122597358?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-0-122597358-blog-82939959.235^v43^pc_blog_bottom_relevance_base5&spm=1001.2101.3001.4242.1&utm_relevant_index=3>，如有侵权，请联系删除。