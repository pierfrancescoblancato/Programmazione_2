comando = "Monday"

match comando:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print(f"{comando} is a weekday")
        
    case "Saturday" | "Sunday":
        print(f"{comando} is the weekend!")