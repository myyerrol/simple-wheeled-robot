# raspberry_pi_simple_car

![raspberry_pi_simple_car_c](.images/raspberry_pi_simple_car_3.jpg)

## Description

This project is what I did in the freshman year in the university, using arduino and raspberry pi boards to implement a simple mobile car. It can achieve the functions are: remote control, obstacle avoidance and ranging.

## Principle

![raspberry_pi_simple_car_fritzing](.images/raspberry_pi_simple_car_fritzing.png)

## Video

The following video show the basic function of the [raspberry_pi_simple_car(raspberry pi + arduino)](http://v.youku.com/v_show/id_XNzMzMzcxNjU2.html?from=y1.7-2).

## Configure

1. Please connect lines correctly.
2. Download **raspberry_pi_simple_car.ino** program to the arduino.
3. Start the raspberry pi, switch directory to Desktop, and use follow command to get codes.

  ```bash
  $> cd Desktop
  $> git clone https://github.com/myyerrol/raspberry_pi_simple_car.git
  ```

4. Set autostart and reboot raspberry pi to enjoy!

  ```bash
  $> mkdir /home/pi/.config/autostart
  $> cd ../.config/autostart
  $> cp ../Desktop/raspberry_pi_simple_car/config/raspberry_pi_simple_car.desktop ./
  $> sudo reboot
  ```

## Summary

By finishing this project, I learned simple python programming, sensors programming, and using of arduino and raspberry pi boards, ect. Although this car's function is very limited, I still enjoyed that happiness when I made the car run! I believe I can do better on the road of maker in the future!
