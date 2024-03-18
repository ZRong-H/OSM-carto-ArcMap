# OSM-carto/ArcMap
An OpenStreetMap tool for ArcMap

We can utilize this Python script with arcpy library to redrawing OpenStreetMap in ArcMap with data download from OpenStreetMap offical.
  To use this tool, simply input the related paths within the script, import it into ArcMap, and execute it. This process will generate a map resembling OpenStreetMap. As the related paths, we need to input ten paths, that include:
-------------------------------------------------------------------------------------------------------
|  input polygon path, input line path,  input point path, output polygon path, output line path,     |
|  output point path, polygon's style path, line's style path, point's style path, output png's path  |
-------------------------------------------------------------------------------------------------------
You need to input the corresponding path at the location indicated in the image below：
![image](https://github.com/ZRong-H/OSM-carto-ArcMap/assets/105121100/3211c355-b12a-48f2-b150-a33373fec781)
![image](https://github.com/ZRong-H/OSM-carto-ArcMap/assets/105121100/b38aab0b-a87a-4edf-ad56-ffb1b2572c7b)
![image](https://github.com/ZRong-H/OSM-carto-ArcMap/assets/105121100/40397fed-6c95-4dfa-aa3c-8c50a361827b)
![image](https://github.com/ZRong-H/OSM-carto-ArcMap/assets/105121100/10113294-3e3f-4cee-bd25-e7a3a66b40da)

You can find the corresponding layer style's documents(.lyr) in this repository. After you input all of the paths, you can execute it, an wait just a few seconds, you will get a map resembling OpenStreetMap in ArcMap. 
However, this code may not completely restore the map to its original OpenStreetMap; sometimes, you may need to adjust the positions of the layers accordingly.

We can compare the results between OpenStreetMap and the redraw maps as follow:

**OpenStreetMap:**

![image](https://github.com/ZRong-H/OSM-carto-ArcMap/assets/105121100/68f5909d-db50-4b34-9253-2db6ec2a8669)

**redraw map:**

![output882](https://github.com/ZRong-H/OSM-carto-ArcMap/assets/105121100/69f880f1-5eec-4749-8f83-e7a2b87e49b9)

**OpenStreetMap:**

![image](https://github.com/ZRong-H/OSM-carto-ArcMap/assets/105121100/bf9560d8-e9bf-4de7-9402-3dd55e71aa15)


**redraw map:**

![output617](https://github.com/ZRong-H/OSM-carto-ArcMap/assets/105121100/0db17ef8-b4ee-4372-b746-f1a310f5753d)


**OpenStreetMap:**

![image](https://github.com/ZRong-H/OSM-carto-ArcMap/assets/105121100/f4fe3432-82af-46bb-a386-dea500a7c489)

**redraw map:**

![output478](https://github.com/ZRong-H/OSM-carto-ArcMap/assets/105121100/ec39da53-83cc-41e8-a244-b4aaf252c904)

Just try it and use it in ArcMap!
