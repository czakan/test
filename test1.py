import random

print("------------------------------------------------------")
print("    Witaj w zgadywance! Ile mmsów jest w słoiku?")
print("------------------------------------------------------")

print(" Zgadnij ile MMsów jest w słoiku a otrzymasz nagrodę!")
print()

mm_count =  random.randint(1, 100)
attempt_limit = 5
attempts = 0


while attempts < attempt_limit:
    guess_text = input("Jak wiele MMsów jest w słoiku?")
    guess = int(guess_text)
    print(guess)
    attempts += 1

    if mm_count == guess:
        print(f"Gratulacje! Jest ich właśnie {guess}! Wygrałeś talon na kurwe i balon")
        print(f"Udało Ci się zgadnąć za {attempts} razem!")
        break
    elif guess < mm_count:
        print("O nie to o wiele za mało!")
    else:
        print("O nie, nie, nie! To za dużo!")


if attempts == attempt_limit:
    print(f'Niestety,przekroczyłeś liczbę {attempt_limit}. Nie udało się :( Żegnaj!')