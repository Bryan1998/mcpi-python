#!/usr/bin/python

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
	# you can change this to a remote ip
	mc = Minecraft.create('127.0.0.1', 4711)
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

def main():
	mc = init()
	x, y, z = mc.player.getPos()
	
	if get_season(date.today()) == 'winter':
		mc.postToChat("It's winter!  Here's a snowman for you...")
	else:
		mc.postToChat("It's summer!  No snowman for you!  Ok, fine here's your snowman...")
		
	snowman(mc, x, y, z)
  
main()
