import board
import digitalio
import time

BLINK_DELAY = 0.25
DONT_WALK_BLINK_SECS = 8
DONT_WALK_SOLID_SECS = 8
WALK_SECS = 8

walk_relay = digitalio.DigitalInOut(board.GP6)
walk_relay.direction = digitalio.Direction.OUTPUT
dont_walk_relay = digitalio.DigitalInOut(board.GP7)
dont_walk_relay.direction = digitalio.Direction.OUTPUT

while True:
    # Start in safe mode: don't walk is on and walk is off
    dont_walk_relay.value = True
    walk_relay.value = False

    # Run the Don't Walk blink cycle
    start_time = time.time()
    while (time.time() - start_time) < DONT_WALK_BLINK_SECS:
        print("Blinking don't walk")
        dont_walk_relay.value = True
        time.sleep(BLINK_DELAY)
        dont_walk_relay.value = False
        time.sleep(BLINK_DELAY)

    # Don't Walk solid cycle
    print("Solid don't walk")
    dont_walk_relay.value = True
    time.sleep(DONT_WALK_SOLID_SECS)

    # Time to walk!
    print("Walk Signal")
    dont_walk_relay.value = False
    walk_relay.value = True
    time.sleep(WALK_SECS)
