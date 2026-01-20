def main():
    pounds = pounds_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to charge? "))
    charge = pounds * percent
    print(f"Charge £{charge:.2f}")

def pounds_to_float(pounds):
    pounds=float(pounds.replace("£",""))
    return pounds
def percent_to_float(percent):
    percent=int(percent.replace("%",""))
    percent=float(percent/100)
    return percent

main()
