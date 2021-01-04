#Ids start at 1
scoreboard players add #current suso.pldata.id 1
scoreboard players operation @s suso.pldata.id = #current suso.pldata.id

#Data starts off as a blank nbt object
data modify storage suso:pldata player_arr append value {}

#Name change handling
data modify storage suso:pldata new_id.UUID set from entity @s UUID
execute store result storage suso:pldata new_id.id int 1 run scoreboard players get @s suso.pldata.id
data modify storage suso:pldata id_data append from storage suso:pldata new_id

tag @s add suso.pldata.id