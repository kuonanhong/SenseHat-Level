#!/usr/bin/env python3
# Northcliff Level - Version 1.0
from sense_hat import SenseHat
from datetime import datetime

class NorthcliffLevel(object):

    def print_update(self, print_message): # Prints with a date and time stamp
        today = datetime.now()
        print(print_message + today.strftime('%A %d %B %Y @ %H:%M:%S'))

    def run(self, tilt_range):
        try:
            self.print_update("Northcliff Level started on ")
            max_tilt=tilt_range/2
            min_tilt=360-tilt_range/2
            tilt_step=tilt_range/7
            led_step=255/tilt_step
            red=(255,0,0)
            blue=(0,0,255)
            green=(0,255,0)
            yellow=(255,255,0)
            off=(0,0,0)
            last_high_roll_led=0
            last_low_roll_led=0
            last_high_pitch_led=0
            last_low_pitch_led=0
            while True:
                o = sense.get_orientation()
                pitch = round(o["pitch"],1)
                roll = round(o["roll"],1)
                yaw = int(round(o["yaw"],1))
                if pitch<0.5 or pitch>359.5:
                    pitch_level=True
                else:
                    pitch_level=False
                if roll<0.5 or roll>359.5:
                    roll_level=True
                else:
                    roll_level=False
                valid_roll=True
                if roll<=max_tilt:
                    if roll>=max_tilt-tilt_step:
                        low_roll_lev=(max_tilt-roll)*led_step
                        high_roll_lev=255-low_roll_lev
                        high_roll_led=0
                        low_roll_led=1
                    elif roll<max_tilt-tilt_step and roll>=max_tilt-2*tilt_step:
                        low_roll_lev=(max_tilt-tilt_step-roll)*led_step
                        high_roll_lev=255-low_roll_lev
                        high_roll_led=1
                        low_roll_led=2
                    elif roll<max_tilt-2*tilt_step and roll>=max_tilt-3*tilt_step:
                        low_roll_lev=(max_tilt-2*tilt_step-roll)*led_step
                        high_roll_lev=255-low_roll_lev
                        high_roll_led=2
                        low_roll_led=3
                    else:
                        low_roll_lev=(max_tilt-3*tilt_step-roll)*led_step
                        high_roll_lev=255-low_roll_lev
                        high_roll_led=3
                        low_roll_led=4
                elif roll>=360-tilt_range/2:
                    if roll<=min_tilt+tilt_step:
                        low_roll_lev=(min_tilt+tilt_step-roll)*led_step
                        high_roll_lev=255-low_roll_lev
                        high_roll_led=6
                        low_roll_led=7
                    elif roll>min_tilt+tilt_step and roll<=min_tilt+2*tilt_step:
                        low_roll_lev=(min_tilt+2*tilt_step-roll)*led_step
                        high_roll_lev=255-low_roll_lev
                        high_roll_led=5
                        low_roll_led=6
                    elif roll>min_tilt+2*tilt_step and roll<=min_tilt+3*tilt_step:
                        low_roll_lev=(min_tilt+3*tilt_step-roll)*led_step
                        high_roll_lev=255-low_roll_lev
                        high_roll_led=4
                        low_roll_led=5
                    else:
                        low_roll_lev=(min_tilt+4*tilt_step-roll)*led_step
                        high_roll_lev=255-low_roll_lev
                        high_roll_led=3
                        low_roll_led=4
                else:
                    valid_roll=False
                valid_pitch=True
                if pitch<=max_tilt:
                    if pitch>=max_tilt-tilt_step:
                        low_pitch_lev=(max_tilt-pitch)*led_step
                        high_pitch_lev=255-low_pitch_lev
                        high_pitch_led=7
                        low_pitch_led=6
                    elif pitch<max_tilt-tilt_step and pitch>=max_tilt-2*tilt_step:
                        low_pitch_lev=(max_tilt-tilt_step-pitch)*led_step
                        high_pitch_lev=255-low_pitch_lev
                        high_pitch_led=6
                        low_pitch_led=5
                    elif pitch<max_tilt-2*tilt_step and pitch>=max_tilt-3*tilt_step:
                        low_pitch_lev=(max_tilt-2*tilt_step-pitch)*led_step
                        high_pitch_lev=255-low_pitch_lev
                        high_pitch_led=5
                        low_pitch_led=4
                    else:
                        low_pitch_lev=(max_tilt-3*tilt_step-pitch)*led_step
                        high_pitch_lev=255-low_pitch_lev
                        high_pitch_led=4
                        low_pitch_led=3
                elif pitch>=360-tilt_range/2:
                    if pitch<=min_tilt+tilt_step:
                        low_pitch_lev=(min_tilt+tilt_step-pitch)*led_step
                        high_pitch_lev=255-low_pitch_lev
                        high_pitch_led=1
                        low_pitch_led=0
                    elif pitch>min_tilt+tilt_step and pitch<=min_tilt+2*tilt_step:
                        low_pitch_lev=(min_tilt+2*tilt_step-pitch)*led_step
                        high_pitch_lev=255-low_pitch_lev
                        high_pitch_led=2
                        low_pitch_led=1
                    elif pitch>min_tilt+2*tilt_step and pitch<=min_tilt+3*tilt_step:
                        low_pitch_lev=(min_tilt+3*tilt_step-pitch)*led_step
                        high_pitch_lev=255-low_pitch_lev
                        high_pitch_led=3
                        low_pitch_led=2
                    else:
                        low_pitch_lev=(min_tilt+4*tilt_step-pitch)*led_step
                        high_pitch_lev=255-low_pitch_lev
                        high_pitch_led=4
                        low_pitch_led=3
                else:
                    valid_pitch=False
                if valid_roll==True and valid_pitch==True:    
                    sense.set_pixel(last_high_pitch_led,last_high_roll_led,off)
                    sense.set_pixel(last_low_pitch_led,last_low_roll_led,off)
                    sense.set_pixel(last_low_pitch_led,last_high_roll_led,off)
                    sense.set_pixel(last_high_pitch_led,last_low_roll_led,off)
                    low_roll_lev=abs(int(low_roll_lev))
                    high_roll_lev=abs(int(high_roll_lev))
                    if low_roll_lev>255:
                        low_roll_lev=255
                    if high_roll_lev>255:
                        high_roll_lev=255
                    low_pitch_lev=abs(int(low_pitch_lev))
                    high_pitch_lev=abs(int(high_pitch_lev))
                    if low_pitch_lev>255:
                        low_pitch_lev=255
                    if high_pitch_lev>255:
                        high_pitch_lev=255
                    l_l_level= int((low_pitch_lev+low_roll_lev)/2)
                    h_h_level= int((high_pitch_lev+high_roll_lev)/2)
                    #print("Roll", roll, "High", high_roll_lev, "Low", low_roll_lev)
                    #print("Pitch", pitch, "High", high_pitch_lev, "Low", low_pitch_lev)
                    #print("LL", l_l_level, "HH", h_h_level, "Low Pitch High Roll", high_roll_lev, "High Pitch Low Roll", high_pitch_lev)
                    if roll_level==True and pitch_level==True:
                        sense.set_pixel(0,0,red)
                        sense.set_pixel(0,7,red)
                        sense.set_pixel(7,0,red)
                        sense.set_pixel(7,7,red)
                    elif roll_level==True and pitch_level==False:
                        sense.set_pixel(0,0,red)
                        sense.set_pixel(0,7,red)
                        sense.set_pixel(7,0,off)
                        sense.set_pixel(7,7,off)
                    elif roll_level==False and pitch_level==True:
                        sense.set_pixel(0,0,off)
                        sense.set_pixel(0,7,off)
                        sense.set_pixel(0,0,red)
                        sense.set_pixel(7,0,red)
                    else:
                        sense.set_pixel(0,0,off)
                        sense.set_pixel(0,7,off)
                        sense.set_pixel(7,0,off)
                        sense.set_pixel(7,7,off)
                    sense.set_pixel(low_pitch_led,low_roll_led,(l_l_level,l_l_level,l_l_level))
                    sense.set_pixel(high_pitch_led,high_roll_led,(h_h_level,h_h_level,h_h_level))
                    sense.set_pixel(low_pitch_led,high_roll_led,(high_roll_lev,high_roll_lev,high_roll_lev))
                    sense.set_pixel(high_pitch_led,low_roll_led,(high_pitch_lev,high_pitch_lev,high_pitch_lev))
                    last_high_roll_led=high_roll_led
                    last_low_roll_led=low_roll_led
                    last_high_pitch_led=high_pitch_led
                    last_low_pitch_led=low_pitch_led
                    #print("pitch {0} roll {1} yaw {2}". format(pitch, roll, yaw))
        except KeyboardInterrupt:
            sense.clear()
            self.print_update("Northcliff Level stopped on ")

if __name__ == '__main__': # This is where to overall code kicks off
    sense = SenseHat()
    sense.set_rotation(180)
    sense.clear()
    # Create a level instance
    level = NorthcliffLevel() 
    level.run(tilt_range=90)#Vary the tilt range to adjust sensitivity
