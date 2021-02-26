import numpy

def parlay_calculator(wager, underdogs_ml_odds, favorites_ml_odds):

    underdogs_decimal_odds = [ml_odd / 100 + 1 for ml_odd in underdogs_ml_odds]

    favorites_decimal_odds = [100 / -(ml_odd) + 1 for ml_odd in favorites_ml_odds]

    return numpy.round(wager * numpy.prod(underdogs_decimal_odds) * numpy.prod(favorites_decimal_odds), 2)

def main():

    print("Welcome to parlay_calculator!")

    wager_input = input("Enter wager amount in USD: ")
    try:
        wager_input = float(wager_input)
    except TypeError:
        print("You must enter a valid amount in USD. Program exiting.")
        return -1

    num_legs_input = input("Enter number of legs in the parlay: ")
    try:
        num_legs_input = int(num_legs_input)
    except TypeError:
        print("You must enter a positive whole number. Program exiting.")
        return -2

    if num_legs_input <= 0:
        print("You must enter a positive whole number. Program exiting.")
        return -3

    underdogs_ml_odds_input = []
    favorites_ml_odds_input = []

    for i in range( num_legs_input ):
        temp_ml_odd = input(f"Enter leg {i+1} odds: ")
        try:
            temp_ml_odd = int(temp_ml_odd)
        except TypeError:
            print("You must enter a valid odds value. Program exiting.")
            return -4

        if temp_ml_odd < 0:
            favorites_ml_odds_input.append(temp_ml_odd)
        else:
            underdogs_ml_odds_input.append(temp_ml_odd)

    payout = parlay_calculator(wager_input, underdogs_ml_odds_input, favorites_ml_odds_input)

    print(f"Your total payout is ${payout}")

    return 0


if __name__ == "__main__":
    main()
