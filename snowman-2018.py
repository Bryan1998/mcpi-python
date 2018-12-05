from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
from datetime import date, datetime

# start StackOverflow code from https://stackoverflow.com/a/28688724
Y = 2000 # dummy leap year to allow input X-02-29 (leap day)
seasons = [('winter', (date(Y,  1,  1),  date(Y,  3, 20))),
           ('spring', (date(Y,  3, 21),  date(Y,  6, 20))),
           ('summer', (date(Y,  6, 21),  date(Y,  9, 22))),
           ('autumn', (date(Y,  9, 23),  date(Y, 12, 20))),
           ('winter', (date(Y, 12, 21),  date(Y, 12, 31)))]

def get_season(now):
	if isinstance(now, datetime):
		now = now.date()
	now = now.replace(year=Y)
	return next(season for season, (start, end) in seasons
			if start <= now <= end)
# end StackOverflow code

def init(): 
	# change 192.168.1.13 to 127.0.0.1 or your ip
	mc = Minecraft.create('10.183.13.13', 4711)
	x, y, z = mc.player.getPos()  
	return mc

def snowman(mc,x,y,z):
	yl = [0,0,0,0,1,1,2,2,2,3,3,3,3,3,3,3,4,4,4,5,5,5,6,6,6]
	zl = [1,2,4,5,2,4,2,3,4,0,1,2,3,4,5,6,2,3,4,2,3,4,2,3,4]

	for a in range(0,len(zl)):
		m = 80
		if a is 19 or a is 21:
			m = 46,1
		mc.setBlock(x, y+yl[a], z+zl[a], m)
		print(a, zl[a], yl[a], m)
		m = 80
		mc.setBlock(x+1, y+yl[a], z+zl[a], m)
#main  
def main():
	mc = init()
	x, y, z = mc.player.getPos()
	if get_season(date.today()) == 'winter':
		mc.postToChat("It's winter!  Here's a snowman for you...")
	else:
		mc.postToChat("It's summer!  No snowman for you!  Ok, fine here's your snowman...")
	snowman(mc, x, y, z)
  
main()
  
# multiple line comment
"""
AIR                   0
STONE                 1
GRASS                 2
DIRT                  3
COBBLESTONE           4
WOOD_PLANKS           5
SAPLING               6
BEDROCK               7
WATER_FLOWING         8
WATER                 8
WATER_STATIONARY      9
LAVA_FLOWING         10
LAVA                 10
LAVA_STATIONARY      11
SAND                 12
GRAVEL               13
GOLD_ORE             14
IRON_ORE             15
COAL_ORE             16
WOOD                 17
LEAVES               18
GLASS                20
LAPIS_LAZULI_ORE     21
LAPIS_LAZULI_BLOCK   22
SANDSTONE            24
BED                  26
COBWEB               30
GRASS_TALL           31
WOOL                 35
FLOWER_YELLOW        37
FLOWER_CYAN          38
MUSHROOM_BROWN       39
MUSHROOM_RED         40
GOLD_BLOCK           41
IRON_BLOCK           42
STONE_SLAB_DOUBLE    43
STONE_SLAB           44
BRICK_BLOCK          45
TNT                  46
BOOKSHELF            47
MOSS_STONE           48
OBSIDIAN             49
TORCH                50
FIRE                 51
STAIRS_WOOD          53
CHEST                54
DIAMOND_ORE          56
DIAMOND_BLOCK        57
CRAFTING_TABLE       58
FARMLAND             60
FURNACE_INACTIVE     61
FURNACE_ACTIVE       62
DOOR_WOOD            64
LADDER               65
STAIRS_COBBLESTONE   67
DOOR_IRON            71
REDSTONE_ORE         73
SNOW                 78
ICE                  79
SNOW_BLOCK           80
CACTUS               81
CLAY                 82
SUGAR_CANE           83
FENCE                85
GLOWSTONE_BLOCK      89
BEDROCK_INVISIBLE    95
STONE_BRICK          98
GLASS_PANE          102
MELON               103
FENCE_GATE          107
GLOWING_OBSIDIAN    246
NETHER_REACTOR_CORE 247
"""
