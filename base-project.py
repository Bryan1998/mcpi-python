from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

def init():
    mc = Minecraft.create("127.0.0.1", 4711)
    x, y, z = mc.player.getPos()		
    return mc

def clear_with_air(mc,x,y,z,h,k,l):
	air = 0;
	mc.setBlocks(x-h,y,z,x+h,y+k,z+l,air)	
	
def core(mc,x,y,z,m):
	mc.setBlock(x,y,z,m)

def engine(mc,x,y,z,m):
	pass

def posta(mc,x,y,z,m):
	pass

def postb(mc,x,y,z,m):
	pass

def disc(mc,x,y,z,m):
  pass
  
def main():
	mc = init()
	x,y,z = mc.player.getPos()
  h = 50; k = 50; l = 50;
  clear_with_air(mc,x,y,z,h,k,l)
  disc(mc,x,y-1,z,20,4,42)
  posta(mc,x,y-7,z,11)
  core(mc,x,y-7,z+15,42)
  postb(mc,x,y-4,z+15,42)
  engine(mc,x-5,y,z+15,42)
