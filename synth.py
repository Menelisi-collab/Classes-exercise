"""
Synth
- props
-- buttons
-- sliders
-- knobs
-- pads
-- wheels
-- keys (count)
-- slots
-- info screen


- methods
-- depend on buttons, sliders, etc




buttons | sliders | knobs | wheels | pads
- props
-- type (transport, channel, template, bank selection, transpose, clip launch, page)
-- range
-- sensitivity (pads only)
-- location

- methods
-- depend on type (how many types? don't know)


slots
- props
-- type (USB or MIDI)
-- size (jack size)

- methods
-- depend on type


keys
- props
-- colour
-- velocity
-- MIDI channel number
-- on or off

- methods
-- on/off state() => if key pressed or not
-- MidiSignal(on/off state) => send midi channel number, send velocity level,


infoScreen
- props
-- colour
-- information

- methods
--on/off state() =>
-- informs status if on, blank screen if off

"""

class Synth:
    def __init__(self, Buttons, Sliders, Knobs, Pads, Wheels, Keys, Slots, InfoScreen):
        self.Buttons = Buttons
        self.Sliders = Sliders
        self.Knobs = Knobs
        self.Pads = Pads
        self.Wheels = Wheels
        self.Keys = Keys
        self.Slots = Slots
        self.InfoScreen = InfoScreen

    play_on = True
    stop_play = True

    class Properties:
        def __init__(self, type, range, sensitivity, location):
            self.type = type
            self.range = range
            self.sensitivity = sensitivity
            self.location = location

            def __set_name__(self, name):
                if play_on == True
                    print(f"The {self} is active")
                else:
                    print(f"The {self}" is off)

                if stop_play == True
                    print(f"The {self} has stopped")


class Buttons:
    pass


class Sliders:
    pass


class Knobs:
    pass


class Pads:
    pass


class Wheels:
    pass


class Keys:
    pass


class Slots:
    pass


class InfoScreen:
    pass












