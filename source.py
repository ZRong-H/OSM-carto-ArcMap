import arcpy

# At this part, you have to define your files' path.
polygon_input_path = r"INPUT YOUR PATH HERE!"
polygon_output_path = r"INPUT YOUR PATH HERE!"
line_input_path = r"INPUT YOUR PATH HERE!"
line_output_path = r"INPUT YOUR PATH HERE!"
point_input_path = r"INPUT YOUR PATH HERE!"
point_output_point = r"INPUT YOUR PATH HERE!"
output_png = r"INPUT YOUR PATH HERE!"

# Here is your project coordinate.
project_coordinate = arcpy.SpatialReference("WGS84 ARC System Zone 01")

# To project the polygon shapefile so we can calculate there area.
arcpy.management.Project(polygon_input_path, polygon_output_path, project_coordinate)

#Calculate every element's area.
with arcpy.da.UpdateCursor(polygon_output_path, ["SHAPE@", "Shape_Area"]) as cursor:
    for row in cursor:
        area = row[0].area
        row[1] = area
        cursor.updateRow(row)

#Devide the polygon shapefile according to fileds.
fields = ["barrier", "historic", "leisure",  "man_made", "military", 
              "natural", "power", "shop", "tourism", "Shape_Area"]

#Here is the fields' dictionary, the number means area and the string means SQL to select elements.
fields_dict = {"barrier" : [0.0, "barrier <> ''"], "historic" : [0.0, "historic <> ''"], "leisure" : [0.0, "leisure <> ''"],
               "man_made" : [0.0, "man_made <> ''"], "military" : [0.0, "military <> ''"], "natural" :  [0.0, "natural <> ''"],                    
               "power" : [0.0, "power <> ''"], "shop" : [0.0, "shop <> ''"], "tourism" : [0.0, "tourism <> ''"],}

#Calculate every field's area.
with arcpy.da.SearchCursor(polygon_output_path, fields) as cursor:
     for attrib in cursor:
         barrier = attrib[0]         
         historic = attrib[1]
         leisure = attrib[2]
         man_made = attrib[3]
         military = attrib[4]
         natural = attrib[5]
         power = attrib[6]
         shop = attrib[7]
         tourism = attrib[8]
         shape_area = attrib[9]

         if barrier != " ":
             fields_dict["barrier"][0] += shape_area            
         if historic != " ":
             fields_dict["historic"][0] += shape_area
         if natural != " ":
             fields_dict["natural"][0] += shape_area
         if leisure != " ":
             fields_dict["leisure"][0] += shape_area
         if man_made != " ":
             fields_dict["man_made"][0] += shape_area
         if military != " ":
             fields_dict["military"][0] += shape_area
         if natural != " ":
             fields_dict["natural"][0] += shape_area
         if power != " ":
             fields_dict["power"][0] += shape_area
         if shop != " ":
             fields_dict["shop"][0] += shape_area
         if tourism != " ":
             fields_dict["tourism"][0] += shape_area

#Make every field become a layer, ordered by the field's area's size.
arcpy.MakeFeatureLayer_management(polygon_output_path, "boundary_polygon", "boundary <> ''")
arcpy.MakeFeatureLayer_management(polygon_output_path, "place_polygon", "place <> ''")
arcpy.MakeFeatureLayer_management(polygon_output_path, "landuse_polygon", "landuse <> ''")
arcpy.MakeFeatureLayer_management(polygon_output_path, "amenity_polygon", "amenity <> ''")

for key, value in sorted(fields_dict.items(), key=lambda x: x[1][0], reverse=True):
    area, sql = value
    arcpy.MakeFeatureLayer_management(polygon_output_path, key + "_polygon", sql)

arcpy.MakeFeatureLayer_management(polygon_output_path, "building_polygon", "building <> ''")

way = ["aerialway", "aeroway", "highway", "railway", "waterway", "Shape_Area"]
way_dict = {"aerialway" : [0.0, "aerialway <> ''"], "aeroway" : [0.0, "aeroway <> ''"], "highway" : [0.0, "highway <> ''"],
            "railway" : [0.0, "railway <> ''"], "waterway" : [0.0, "waterway <> ''"]}

with arcpy.da.SearchCursor(polygon_output_path, way) as cursor:
     for attrib in cursor:
         aerialway = attrib[0]
         aeroway = attrib[1]
         highway = attrib[2]
         railway = attrib[3]
         waterway = attrib[4]
         shape_area = attrib[5]

         if aerialway != " ":
             way_dict["aerialway"][0] += shape_area
         if aeroway != " ":
             way_dict["aeroway"][0] += shape_area
         if highway != " ":
             way_dict["highway"][0] += shape_area 
         if railway != " ":
             way_dict["railway"][0] += shape_area
         if waterway != " ":
             way_dict["waterway"][0] += shape_area

for key, value in sorted(way_dict.items(), key=lambda x: x[1][0], reverse=True):
    area, sql = value
    arcpy.MakeFeatureLayer_management(polygon_output_path, key + "_polygon", sql)

'''Import style files according to the layer's name'''
# This is the map document we have opened.
mxd = arcpy.mapping.MapDocument("CURRENT")

#Get the dataframe's list.
data_frames = arcpy.mapping.ListDataFrames(mxd)

for data_frame in data_frames:
    # Get the layer list
    layer_list = arcpy.mapping.ListLayers(mxd, "", data_frame)
    for layer in layer_list:
        #Get the layer's name
        layer_name = layer.name
        # Here is the style files' path.
        style_path = r"INPUT YOUR FOLDER PATH HERE!\{}.lyr".format(layer_name) # polygon layer's style folder
        # To check if the file's path exists.
        if arcpy.Exists(style_path):
            #Import layer's style file.
            layer_source = arcpy.mapping.Layer(style_path)
            # Refresh this layer.
            arcpy.mapping.UpdateLayer(data_frame, layer, layer_source)

#The same operations to line shapefile as described above.
fields = ["aeroway", "aerialway", "waterway", "railway", "barrier", "boundary","natural", 
              "amenity", "place", "power", "leisure", "man_made", "tourism", "route"]

fields_dict = {"aeroway" : "aeroway <> ''",
               "aerialway" : "aerialway <> ''",
               "waterway" : "waterway <> ''",
               "railway" : "railway <> ''",
               "barrier" : "barrier <> ''",
               "boundary" : "boundary <> ''",
               "natural" : "natural <> ''",
               "amenity" : "amenity <> ''",
               "place" : "place <> ''",
               "power" : "power <> ''",
               "leisure" : "leisure <> ''",
               "man_made" : "man_made <> ''",
               "tourism" : "tourism <> ''",
               "route" : "route <> ''"}

for key, value in fields_dict.items():
    sql = value
    arcpy.MakeFeatureLayer_management(line_input_path, key + "_line", sql)

highway = ["construction", "cycleway", "elevator", "footway", "motorway",  "path", "pedestrain", "raceway", 
                   "road", "steps", "trunk", "track"]

highway_dict = {"construction" : "highway = 'construction'", "cycleway" : "highway = 'cycleway'", "elevator" : "highway = 'elevator'",
                "footway" : "highway = 'footway'", "motorway" : "highway = 'motorway' OR highway = 'motorway_link'", 
                "path" : "highway = 'path'", "pedestrain" : "highway = 'pedestrain'", "raceway" : "highway = 'raceway'",
                "road" : "highway = 'road'", "steps" : "highway = 'steps'", "trunk" : "highway = 'trunk' OR highway = 'trunk_link'"}

for key, value in highway_dict.items():
    sql = value
    arcpy.MakeFeatureLayer_management(line_input_path, key + "_line", sql)

arcpy.MakeFeatureLayer_management(line_input_path, "track_line", "highway = 'track'")
arcpy.MakeFeatureLayer_management(line_input_path, "service_line", "highway = 'service'")
arcpy.MakeFeatureLayer_management(line_input_path, "living_street_line", "highway = 'living_street'")
arcpy.MakeFeatureLayer_management(line_input_path, "residential_line", "highway = 'residential'")
arcpy.MakeFeatureLayer_management(line_input_path, "unclassified_line", "highway = 'unclassified'")
arcpy.MakeFeatureLayer_management(line_input_path, "tertiary_line", "highway = 'tertiary' OR highway = 'tertiary_link'")
arcpy.MakeFeatureLayer_management(line_input_path, "secondary_line", "highway = 'secondary' OR highway = 'secondary_link'")
arcpy.MakeFeatureLayer_management(line_input_path, "primary_line", "highway = 'primary' OR highway = 'primary_link'")


#Here is how to renders line layer's style
mxd = arcpy.mapping.MapDocument("CURRENT")
data_frames = arcpy.mapping.ListDataFrames(mxd)
for data_frame in data_frames:
    layer_list = arcpy.mapping.ListLayers(mxd, "", data_frame)
    for layer in layer_list:
        layer_name = layer.name
        style_path = r"INPUT YOUR FOLDER PATH HERE!\{}.lyr".format(layer_name) # line layer's style folder
        if arcpy.Exists(style_path):
            layer_source = arcpy.mapping.Layer(style_path)
            arcpy.mapping.UpdateLayer(data_frame, layer, layer_source) 


#The same operations to point shapefile as described above.
point = ["amenity", "leisure", "highway", "power", "historic", "railway", "shop", "tourism", "waterway"]
point_dict = {"amenity" : "amenity <> ''", "leisure" : "leisure <> ''", "highway" : "highway <> ''",
              "power" : "power <> ''", "historic" : "historic <> ''", "railway" : "railway <> ''",
              "shop" : "shop <> ''", "tourism" : "tourism <> ''", "waterway" : "waterway <> ''"}
for key,value in point_dict.items():
    sql = value
    arcpy.MakeFeatureLayer_management(point_input_path, key + "_point", sql)

mxd = arcpy.mapping.MapDocument("CURRENT")

data_frames = arcpy.mapping.ListDataFrames(mxd)

for data_frame in data_frames:
    layer_list = arcpy.mapping.ListLayers(mxd, "", data_frame)
    for layer in layer_list:
        layer_name = layer.name
        style_path = r"NPUT YOUR FOLDER PATH HERE!\{}.lyr".format(layer_name) # point layer's style folder
        if arcpy.Exists(style_path):
            layer_source = arcpy.mapping.Layer(style_path)
            arcpy.mapping.UpdateLayer(data_frame, layer, layer_source) 

#Set the scale
data_frame.scale = 10000

#Refresh the map view
arcpy.RefreshActiveView()

#Export the map
arcpy.mapping.ExportToPNG(mxd, output_png, data_frame, resolution = 300)
