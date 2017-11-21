from time import sleep
from mcpi.minecraft import Minecraft
mc = Minecraft.create('10.183.13.13',4711)
try:
	while True:
		mc.postToChat('Life sucks...')
		sleep(2)
except KeyboardInterrupt:
	mc.postToChat('Goodbye cruel world!')
