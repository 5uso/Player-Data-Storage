scoreboard players add $i suso.pldata.var 1
data modify storage suso:pldata constructed_arr append from storage suso:pldata working_arr[0]
data remove storage suso:pldata working_arr[0]
function suso.player_data:put/search_player