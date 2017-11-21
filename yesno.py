from time import sleep
from mcpi.minecraft import Minecraft
mc = Minecraft.create('10.183.13.13',4711)
try:
	while True:
		mc.postToChat('NO')
		sleep(.5)
		mc.postToChat('YES')
		sleep(.5)
except KeyboardInterrupt:
	mc.postToChat('CAN WE STOP ARGUING?!?')
