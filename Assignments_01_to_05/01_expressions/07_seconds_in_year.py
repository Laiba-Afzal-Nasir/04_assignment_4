DAYS_PER_HOUR : int = 365
HOURS_PER_DAY : int = 24
MINUTES_PER_HOUR : int = 60
SECONDS_PER_MINUTE : int = 60

def main():
    calculation : int = DAYS_PER_HOUR * HOURS_PER_DAY * MINUTES_PER_HOUR * SECONDS_PER_MINUTE
    print(f"\nThere are {calculation} seconds in a year!\n")

if __name__ == "__main__":
    main()