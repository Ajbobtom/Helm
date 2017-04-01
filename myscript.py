print("hello world")

from picamera import PiCamera
from time import sleep
camera = PiCamera()

def main():    
    camera.start_preview()
    sleep(10)
    camera.stop_preview()


main()

print "goodbye world"


    
