# Gen Ed Generator

print("Hello. Welcome to Gen Ed Generator.")
print("This application generates the number of current Gen Ed requirements a student must meet before graduation.")

art_gened = input("GA: Enter the number of Gen Ed Art courses completed: ")
print("Your answer: ", art_gened)

def main():

    if art_gened == "0":
        print("To satisfy this Gen Ed requirement you must complete 1 additional 3 or 4 credit hour course.")

    elif art_gened == "1":
        print("All Gen Ed Art credit requirements are met.")

main()


psych_gened = input("GB: Enter the number of Gen Ed Human Behavior courses completed: ")
print("Your answer: ", psych_gened)

def main():

        if psych_gened == "0":
            print("To satisfy this Gen Ed requirement you must complete 1 additional 3 credit hour course.")

        elif psych_gened == "1":
            print("All Gen Ed Human Behavior credit requirements are met.")

main()


race_gened = input("GD: Enter the number of Gen Ed Race and Diversity courses completed: ")
print("Your answer: ", race_gened)

def main():

        if race_gened == "0":
            print("To satisfy this Gen Ed requirement you must complete 1 additional 3 credit hour course.")

        elif race_gened == "1":
            print("All Gen Ed Race and Diversity credit requirements are met.")

main()


world_gened = input("GG: Enter the number of Gen Ed World Society courses completed: ")
print("Your answer: ", world_gened)

def main():

        if world_gened == "0":
            print("To satisfy this Gen Ed requirement you must complete 1 additional 3 credit hour course.")

        elif world_gened == "1":
            print("All Gen Ed World Society credit requirements are met.")

main()


science_gened = input("GS: Enter the number of Gen Ed Science and Technology courses completed: ")
print("Your answer: ", science_gened)

def main():

        if science_gened == "0":
            print("To satisfy this Gen Ed requirement you must complete 2 additional 3 credit hour courses.")

        elif science_gened == "1":
            print("To satisfy this Gen Ed requirement you must complete 1 additional 3 credit hour course.")

        elif science_gened == "2":
            print("All Gen Ed Science and Technology credit requirements are met.")

main()


society_gened = input("GS: Enter the number of Gen Ed U.S. Society courses completed: ")
print("Your answer: ", society_gened)

def main():

        if society_gened == "0":
            print("To satisfy this Gen Ed requirement you must complete 1 additional 3 credit hour course.")

        elif society_gened == "1":
            print("All Gen Ed U.S. Society credit requirements are met.")

main()


