from bluedot import BlueDot
from picamera2 import Picamera2
from pathlib import Path

#PHOTO_PATH = Path('/photos')
#PHOTO_PATH.mkdir(parents=True, exist_ok=True)


def main():
    print("Hello from blue-dot-test!")
    bd = BlueDot()
    
    picam2 = Picamera2()
    count = 0
    
    while True:
        bd.wait_for_press()
        print("You pressed the blue dot!")
        count += 1
        picam2.start_and_capture_file(f"test_{count}.jpg")
        #picam2.start_and_capture_file(PHOTO_PATH / f"test_{count}.jpg")


if __name__ == "__main__":
    main()
