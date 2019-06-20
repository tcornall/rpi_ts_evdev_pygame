#on a 270 rotated  touch LCD,
#x iincreases vertically
#and y increases L->R
import evdev

def device(devname):
    dev = evdev.InputDevice(devname)
    return dev

def get_touch_coords(dev):
    #print(dev)

    #print('Capabilities')
    #capabilities=dev.capabilities(verbose=True)
    #print(capabilities)
    x=0
    y=0
    for  event in dev.read_loop():   #This BLOCKS. need a version that doesn't
        if event.type == evdev.ecodes.EV_ABS:
            absevent=evdev.categorize(event) 
            if event.code == evdev.ecodes.ABS_X:
                x=absevent.event.value
            if event.code == evdev.ecodes.ABS_Y:
                y=absevent.event.value
                return(x,y)
if __name__ == '__main__':
    for n in range(10):
        x,y=get_touch_coords('/dev/input/touchscreen')
        if x<300 or x >4000 or y<300 or y>4000:
            pass
        else:
            print(x,y)
