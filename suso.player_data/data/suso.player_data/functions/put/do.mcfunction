data modify storage suso:pldata working_arr set from storage suso:pldata player_arr
scoreboard players set $i suso.pldata.var 1
function suso.player_data:put/search_player
data modify storage suso:pldata player_arr set from storage suso:pldata constructed_arr
data remove storage suso:pldata constructed_arr