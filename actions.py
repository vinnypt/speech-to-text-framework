def turn_lights_on():
    print("Turning the lights ON.")

def turn_lights_off():
    print("Turning the lights OFF.")

def check_weather():
    print("Checking weather... (future: connect to API)")

def play_music():
    print("Playing your favorite playlist.")

intent_actions = {
    "lights_on": turn_lights_on,
    "lights_off": turn_lights_off,
    "weather": check_weather,
    "music": play_music,
}