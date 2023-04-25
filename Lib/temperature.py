import os
import glob
import time

os.system('modprobe w1-gpio')
os.system('mopdprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file,'r')
    lines = f.readlines()
    f.close()
    return lines


def read_temp():
    maxc=maxf=0
    # loop over the temperature reading for 6sec
    t_end = time.time() + 6
    while time.time() < t_end:
        lines = read_temp_raw()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = read_temp_raw()
        equal_pos = lines[1].find('t=')
        if equal_pos != -1:
            temp_string = float(lines[1][equal_pos+2:])
            temp_string += (temp_string/10)
            temp_c = temp_string / 1000.0
            temp_c = round(temp_c,3)
            temp_f = temp_c * 9.0 / 5.0 + 32
            temp_f = round(temp_f,3)
            maxc=temp_c if maxc<temp_c else maxc
            maxf=temp_f if maxc<temp_c else maxf
        time.sleep(0.8)
    return maxc, maxf
#try:
    #while True:
        #print(read_temp())
        #time.sleep(1)       
#except KeyboardInterrupt:
    #os.system('exit()')


def main():
    pass

if __name__ == "__main__":
    main()