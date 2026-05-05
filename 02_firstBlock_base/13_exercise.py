str = "start"
match str:
        case "start":
            print("start")
        case "stop":
            print("stop")
        case "exit":
            print("exit")
        case _:
            print("Unknown command")