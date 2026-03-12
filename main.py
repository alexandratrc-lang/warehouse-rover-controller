from rover import Rover
from logger import save_log

def run_mission():
    bot = Rover("Warehouse-Bot-01")
    # A list of commands including one error ("JUMP") to test logic
    commands = ["NORTH", "EAST", "NORTH", "JUMP", "SOUTH"]

    save_log("--- STARTING MISSION ---")
    for cmd in commands:
        result = bot.move(cmd)
        save_log(result)
    save_log("--- MISSION COMPLETE ---")

if __name__ == "__main__":
    run_mission()
