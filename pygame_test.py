import pygame



if __name__ == "__main__":
	
	pygame.init()

	#initialise the joystick module
	pygame.joystick.init()
	
	joystick = None
	count = 0
	
	print("hello world")
	while True:
		for event in pygame.event.get():
			if event.type == pygame.JOYDEVICEADDED:
				joystick = pygame.joystick.Joystick(event.device_index)
				print("joystick connected!")
		if joystick.get_button(0):
			count+=1
			print(f"button presseed {count} times")
		  
		
