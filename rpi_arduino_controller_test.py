#!/usr/bin/env python3
import serial
import time
import pygame

def main():
    # serial channel
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()

    # init pygame controller
    pygame.init()
    pygame.joystick.init()

    joystick = None
    is_button_held = False

    # look for controller already plugged in (quicker than polling connection)
    if pygame.joystick.get_count() > 0:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        print(f"Joystick found: {joystick.get_name()}")

    while True:
        # process pygame events for hot plugging
        for event in pygame.event.get():
            if event.type == pygame.JOYDEVICEADDED:
                joystick = pygame.joystick.Joystick(event.device_index)
                joystick.init()
                print("Joystick connected")

            elif event.type == pygame.JOYDEVICEREMOVED:
                print("Joystick disconnected")
                joystick = None

        # listen for button press
        if joystick is not None:
            button_state = joystick.get_button(0)
            if button_state and not is_button_held:
                is_button_held = True
                print("Button held, turning on")
                ser.write(b"ON\n")

            elif not button_state and is_button_held:
                is_button_held = False
                print("Button released, turning off")
                ser.write(b"OFF\n")

        time.sleep(0.005)

if __name__ == '__main__':
    main()
