# rpi_ts_evdev_pygame
One way to get a touch LCD working on a raspberry pi using evdev for touchscreen and pygame for display
I bought a rpi 3+ and an xc9022 2.8" resistive touch lcd from Jaycar, thinking that of course it would be easy to put the two together, after all,  the touchscreen was designed for that, wasn't it? It was certainly being advertised that way. This was my first foray into the world of rpi and I was expecting things to be as easy as 'pi'. Nope...

There's lots of great stuff out there, from Adafruit and various forums, discussing how to use the lcd and touchscreen. The lcd proved to be fairly straightforward and it wasn't long, after running the ??? script from Adafruit, before I a tiny little desktop running on the lcd, rotated by 270 to give me the landscape orientation that I wanted. Too small to be useful, but so cute! Mouse worked, but touch didn't.

For my particular application (a security door timer... yeah, I know, there are simpler ways to do this, why use a pi? Learning....) I needed a little pygame program running with buttons that the touchscreen could activate. Unfortunately, out of the box, pygame and the touchscreen wouldn't play nice. It kinda worked, but x and y were flipped because I chose to rotate teh screen, and I could have dealt with that using userspace code transforms, but I found that the position that the pygame event handler reported for touches was badly inconsistant. I believe that part of the reason this didn't all work was because the various workarounds discussed on the 'net were mainly aimed at older versions of raspbarian and TSLIB. I needed something for raspbarian Stretch (which was the latest version at the time I tried to do this)

A posting on ??? showed some interesting application of python-evdev to read touchscreens and so I tried that and it worked much better. X and Y were still rotated and scale was badly wrong plus there was an offset in the reported coordinates, but as mentioned, I was happy to deal with that as long as the reported coords were consistant, and they were!

So, here is the python code that I wrote to investigate this, plus slightly edited version of the ???? script.
