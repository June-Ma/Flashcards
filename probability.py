import random

def simulate_monty_hall(trials=10000):
    switch_wins = 0
    stay_wins = 0

    for _ in range(trials):
        # Randomly place the prizes behind the doors
        doors = ['car', 'sheep', 'nothing']
        random.shuffle(doors)

        # Contestant picks a door
        contestant_choice = random.randint(0, 2)

        # Host opens a door that is not the contestant's choice and does not have the car
        possible_doors = [i for i in range(3) if i != contestant_choice and doors[i] != 'car']
        host_opens = random.choice(possible_doors)

        # Remaining unopened door
        remaining_door = [i for i in range(3) if i != contestant_choice and i != host_opens][0]

        # Check result if contestant switches
        if doors[remaining_door] == 'car':
            switch_wins += 1

        # Check result if contestant stays
        if doors[contestant_choice] == 'car':
            stay_wins += 1

    print(f"Out of {trials} trials:")
    print(f" - Switching won the car {switch_wins} times ({(switch_wins/trials)*100:.2f}%)")
    print(f" - Staying won the car {stay_wins} times ({(stay_wins/trials)*100:.2f}%)")

simulate_monty_hall()
