import sdl2
import sdl2.ext
from Joystick import Joystick

def main():

    sdl2.SDL_Init(sdl2.SDL_INIT_JOYSTICK)

    joy = Joystick()

    joy.list_joysticks()
    joy.open_joystick(0)

    WIDTH = 640
    HEIGHT = 480

    window = sdl2.ext.Window("Joystick Tester", size=(640, 480))
    window.show()

    surface = window.get_surface()

    myColor = sdl2.ext.Color(234, 100, 120)
    myColor2 = sdl2.ext.Color(0,255,0)

    running = True

    while running:

        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break 

        sdl2.ext.fill(surface, sdl2.ext.Color(0,0,0))
        x = joy.read_axis(0, 300)
        y = joy.read_axis(1, 300)
        x2 = joy.read_axis(4, 300)
        y2 = joy.read_axis(5, 300)
        if joy.get_button_state(2):
            sdl2.ext.fill(surface, myColor, (x + WIDTH/2, y + HEIGHT/2, 25, 25))
            sdl2.ext.fill(surface, myColor2, (x2 + WIDTH/2, y2 + HEIGHT/2, 25, 25))
        else:
            sdl2.ext.fill(surface, myColor2, (x + WIDTH/2, y + HEIGHT/2, 25, 25))
            sdl2.ext.fill(surface, myColor2, (x2 + WIDTH/2, y2 + HEIGHT/2, 25, 25))
        window.refresh()




if __name__ == '__main__':
    main()
