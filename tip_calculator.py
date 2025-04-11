def main():
meal = float(input(f"How much was the meal? $:"))
tip = str(input(f"what percentage would you like to tip?"))
tip =  float(tip.replace("%", ""))
percentage = (tip / 100) * meal
print (f"leave ${percentage:.2f}")

main()
