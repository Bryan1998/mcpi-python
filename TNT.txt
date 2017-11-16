Install the mcpi library
$cd ~/Desktop/mcpi/api/python/
$sudo python3 setup.py install

Open the python console
$python3

Import the Minecraft library
>>>from mcpi.minecraft import Minecraft

Create the connection
>>>mc = Minecraft.create('127.0.0.1', 4711)

Get player position
>>>x, y, z = mc.player.getPos()

Create the TNT blocks and set data to 1
>>>mc.setBlocks(x, y, z, x+10, y+10, z+10, 46, 1)

Hit the one of the TNT blocks until it flashes...
...AND RUN TO THE HILLS!!!
