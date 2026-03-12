class Rover:
    def __init__(self, name="Rover01"):
        self.name = name
        self.x = 0
        self.y = 0
        self.battery = 100

    def move(self, direction):
        if self.battery < 5:
            return f"LOW BATTERY: {self.battery}% - Movement halted."

        direction = direction.upper()
        if direction == "NORTH" and self.y < 10:
            self.y += 1
        elif direction == "SOUTH" and self.y > 0:
            self.y -= 1
        elif direction == "EAST" and self.x < 10:
            self.x += 1
        elif direction == "WEST" and self.x > 0:
            self.x -= 1
        else:
            return f"INVALID: {direction} (Boundary or Error)"

        self.battery -= 1
        return f"SUCCESS: {self.name} at ({self.x}, {self.y}) | Bat: {self.battery}%"
