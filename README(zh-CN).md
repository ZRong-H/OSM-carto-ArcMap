# OSM-carto/ArcMap
这是一份在ArcMap软件中还原OpenStreetMap的代码

我们可以在OpenStreetMap中下载数据，并将其导入ArcMap中。然后，我们可以通过在ArcMap中的python工作台中执行这个脚本，从而将地图还原成OpenStreetMap的样式
为了使脚本能正常运行，你需要在执行脚本之前导入正确的路径. 对于需要导入的路径，包括了以下10个路径: <br>
| 需要输入的路径 | 意思 |
|:--------------:|:--------:|
| input polygon path | 输入的面图层的路径 |
| input line path | 输入的线图层的路径 |
| input point path | 输入的点图层的路径 |
| output polygon path | 输出的面图层的路径 |
| output line path | 输出的线图层的路径 |
| output point path | 输出的点图层的路径 |
| polygon's style path | 面图层的样式文件|
| line's style path | 线图层的样式文件 |
| point's style path | 点图层的样式文件 |
| output png's path | 最后输出的图片的位置 |


你需要按照以下图片所展示的位置输入相应的路径：
![image](https://github.com/ZRong-H/OSM-carto-ArcMap/assets/105121100/3211c355-b12a-48f2-b150-a33373fec781)
![image](https://github.com/ZRong-H/OSM-carto-ArcMap/assets/105121100/b38aab0b-a87a-4edf-ad56-ffb1b2572c7b)
![image](https://github.com/ZRong-H/OSM-carto-ArcMap/assets/105121100/40397fed-6c95-4dfa-aa3c-8c50a361827b)
![image](https://github.com/ZRong-H/OSM-carto-ArcMap/assets/105121100/10113294-3e3f-4cee-bd25-e7a3a66b40da)

你可以在我的仓库中找到各个图层对应的样式文件。 在你输入路径并开始执行代码之后，我们只需要等待一小会，就能在ArcMap中得到一张类似于OpenStreetMap的地图了。 
然而，这份代码生成的地图中，并不能完全还原成OpenStreetMap，部分面图层之间可能还需要手动去调整其叠置的顺序。

我们可以比较一下OpenStreetMap原图与利用代码在ArcMap中生成的地图进行比较：

## OpenStreetMap:<br>
![image](https://github.com/ZRong-H/OSM-carto-ArcMap/assets/105121100/68f5909d-db50-4b34-9253-2db6ec2a8669)

## 利用代码绘制的地图:<br>
![2](https://github.com/ZRong-H/OSM-carto-ArcMap/assets/105121100/cbe91d74-827e-471f-a980-a27612c0d94b)

## OpenStreetMap:<br>

![image](https://github.com/ZRong-H/OSM-carto-ArcMap/assets/105121100/bf9560d8-e9bf-4de7-9402-3dd55e71aa15)

## 利用代码绘制的地图:<br>

![1](https://github.com/ZRong-H/OSM-carto-ArcMap/assets/105121100/1f94f9d3-1d17-4e52-aea2-5e71d4e29941)

## OpenStreetMap:<br>

![image](https://github.com/ZRong-H/OSM-carto-ArcMap/assets/105121100/f4fe3432-82af-46bb-a386-dea500a7c489)

## 利用代码绘制的地图:<br>
![3](https://github.com/ZRong-H/OSM-carto-ArcMap/assets/105121100/898ba126-928b-43f2-b7e3-dc2572544d60)

让我们一起尝试并在ArcMap中使用这份代码吧！

代码的原理：主要是计算面图层中各个字段所对应的总面积，然后根据面积的大小进行排序以确定叠置的顺序。但是可能最后会有一些差错，因此在最后可能还需要手动去调整一下面图层之间的叠置顺序。
