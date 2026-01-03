import time
import sys

# Width of the “box”
width = 20

# Starting position
x = 0
dx = 1  # direction

try:
    while True:
        # Clear the screen (works in most terminals)
        sys.stdout.write("\033[2J\033[H")

        # Print the “O” at the current position
        print(" " * x + "O")

        # Move the position
        x += dx

        # Bounce back if it reaches the edges
        if x <= 0 or x >= width:
            dx = -dx

        # Control the speed
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nAnimation stopped!")
