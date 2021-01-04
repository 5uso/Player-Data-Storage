#Assign ids to players
execute as @a[tag=!suso.pldata.id] run function suso.player_data:ids/get_id

#Recover id on name change
execute as @a[tag=suso.pldata.id] unless score @s suso.pldata.id matches 1.. run function suso.player_data:ids/recover_id