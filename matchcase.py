def week_days(day):
    match day:
        case 1:
            return "monday"
        case 2:
            return "tuesday"
        case 3:
            return "wednesday"
        case 4:
            return "thursday"
        case 5:
            return "friday"
        case 6:
            return "saturday"
        case 7:
            return "Sunday"
        case _:
            return "not valid..."
print(week_days(10))