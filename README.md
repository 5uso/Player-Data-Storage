# Player-Data-Storage
A Minecraft datapack aimed at handling player data easily.

Designed for use in multiplayer maps/datapacks.

Automatically handles player name changes.

Handles up to 32 players.


## How to use
Execute `function suso.player_data:get/do` as the player whose data you want to get. This will result in that player's data being copied to path `storage suso:pldata working_data`.

After editing the data, the result contained in this path can be saved by running `function suso.player_data:put/do`, again, as the player in question. If the data wasn't edited (read only operations), there's no need to run this function.

Every player's data starts off as a blank nbt object (`{}`).

If used on a world that's going to be distributed, run `function suso.player_data:package` to reset the pack. This will pause it until the next reload.

Accessing the same player's data multiple times in a row is faster than when switching between players. When possible, this should be taken into account to optimize usage.


## Example
`test:example.mcfunction`:
```mcfunction
#Get player data
function suso.player_data:get/do

#Add one to a counter
execute store result score $temp objective run data get storage suso:pldata working_data.counter
scoreboard players add $temp objective 1
execute store result storage suso:pldata working_data.counter int 1 run scoreboard players get $temp objective

#Store the players currently held item
data modify storage suso:pldata working_data.held set value {}
data modify storage suso:pldata working_data.held set from entity @s SelectedItem

#Save player data
function suso.player_data:put/do
```
In this case, running `execute as @p run function test:example` would increase a counter inside the nearest player's data, as well as storing their held item.
