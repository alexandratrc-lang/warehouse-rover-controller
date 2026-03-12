def save_log(entry):
    with open("mission_log.txt", "a") as f:
        f.write(entry + "\n")
    print(f"Logged: {entry}")
