# Orange Pi PC + Blinka SETUP


## Enable UART, I2C and SPI
### Edit /boot/armbianEnv.txt
```
overlay_prefix=sun8i-h3
overlays=uart3 i2c0 spi-spidev
param_spidev_spi_bus=0
```
   > reboot

```console
sudo apt-get install -y python3 git python3-pip python3-smbus python-dev-is-python3 i2c-tools
```


reboot then:
```console
sudo adduser jody i2c # group i2c does not exist -> require i2c-tools
```


```console
sudo apt-get install -y python-smbus python-dev-is-python3 i2c-tools
```

## Install Kernel headers to compile libgpiod
```console
armbian-config
```
    > Software Install > Headers_install


## Install libgpiod
```console
cd ~
wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/libgpiod.sh
chmod +x libgpiod.sh
./libgpiod.sh --legacy # legacy option to prevent error "linux headers version >= v5.5.0"
```


### libgpiod needs linux headers version >= v5.5.0

cf: https://github.com/adafruit/Raspberry-Pi-Installer-Scripts/issues/95


```console
sudo apt-get install libgpiod2 python3-libgpiod gpiod
```

## Set your Python install to Python 3 Default
```console
sudo apt-get install -y python3 git python3-pip
```

```console
sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.8 2
sudo update-alternatives --config python
```

## Enable UART, I2C and SPI

```console
sudo apt-get install -y python-smbus python-dev i2c-tools
sudo adduser pi i2c
```

Correction:
```console
sudo apt-get install -y python3-smbus python-dev-is-python3 i2c-tools
sudo adduser jody i2c
```




### Install Python libraries
```console
sudo pip3 install adafruit-blinka # /!\ only sudo works
sudo pip3 install adafruit-circuitpython-servokit # /!\ only sudo works
```

### other packages ?
ModuleNotFoundError: No module named 'board'

```console
sudo apt-get install libgpiod2 python3-libgpiod gpiod
```




```python
#servotest.py
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
```



```console
sudo python3 servotest.py
```







```console
    1  armbian-config
    2  sudo armbian-config
    3  sudo apt-get install bash-completion
    4  apt --fix-broken install
    5  sudo apt --fix-broken install
    6  sudo apt-get install -y python3 git python3-pip python-smbus python-dev i2c-tools
    7  apt-cache search python-dev
    8  apt-cache search python-smbus
    9  apt-cache search python3-smbus
   10  sudo apt-get install -y python3 git python3-pip python3-smbus python-dev-is-python3 i2c-tools
   11  sudo adduser jody i2c
   12  sudo vim /boot/armbianEnv.txt
   13  wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/libgpiod.sh
   14  vim libgpiod.sh
   15  chmod +x libgpiod.sh
   16  ./libgpiod.sh --legacy
   17  sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.8 2
   18  sudo update-alternatives --config python
   19  sudo reboot
   20  ls /dev/i2c-0
   21  ls /dev
   22  pip3 install adafruit-blinka
   23  vim servotest.py
   24  python3 servotest.py
   25  sudo python3 servotest.py
   26  vim blinkatest.py
   27  python3 blinkatest.py
   28  sudo python3 blinkatest.py
   29  pip install pygpiod
   30  pip3 install pygpiod
   31  sudo python3 blinkatest.py
   32  dpkg -l | grep python3-libgpiod
   33  dpkg -l | grep libgpiod2
   34  dpkg -l | grep gpiod
   35  sudo apt-get install libgpiod2 python3-libgpiod gpiod
   36  sudo python3 blinkatest.py
   37  sudo pip3 install adafruit-blinka
   38  sudo python3 blinkatest.py
   39  sudo python3 servotest.py
   40  pip3 install adafruit-circuitpython-servokit
   41  sudo python3 servotest.py
   42  pip3 install -g adafruit-circuitpython-servokit
   43  sudo pip3 install adafruit-circuitpython-servokit
   44  sudo python3 servotest.py
   45  history
   46  sudo python3 servotest.py
   47  cat servotest.py
   48  ls
   49  vim libgpiod.sh
   50  history
   51  sudo su
   52  history
```