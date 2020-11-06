import time # system
from board import SCL, SDA # blinka
from busio import I2C
from adafruit_pca9685 import PCA9685 # PCA Module
from adafruit_motor import servo # servo library

i2c_bus = I2C(SCL, SDA)
pca = PCA9685(i2c_bus)
pca.frequency = 50

my_servo = servo.Servo(pca.channels[0])
pan = servo.Servo(pca.channels[1])

my_servo.angle = int(0)
pan.angle = int(0)
time.sleep(0.5)
my_servo.angle = int(90)
pan.angle = int(90)
time.sleep(0.5)
my_servo.angle = int(180)
time.sleep(0.5)
my_servo.angle = int(45)
pan.angle = int(0)

time.sleep(0.5)