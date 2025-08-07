import random

compliments = [
    "Your debugging aura is immaculate.",
    "Your code compiles and your vibes are crisp.",
    "You have main-character energy and unit tests.",
    "You’re the human equivalent of a well-named variable.",
    "You handle chaos with O(1) elegance.",
    "If excellence were a module, you’d be default export.",
    "Your presence raises everyone’s FPS.",
    "Even your TODOs are inspirational.",
    "Your indentation style cured my headache.",
    "You ship features and serotonin.",
    "Your Google-fu is legendary.",
    "You are the plot twist and the fan favourite.",
]

favourites = []
last_index = -1

def new_compliment():
    global last_index
    if len(compliments) <= 1:
        choice = compliments[0]
    else:
        choice = random.choice([c for i, c in enumerate(compliments) if i != last_index])
        last_index = compliments.index(choice)
    print(f"\n✨ {choice}")
    return choice

def main():
    print("=== Random Compliment Generator ===")
    print("n = new compliment | f = favourite | v = view favourites | q = quit")

    current = new_compliment()

    while True:
        cmd = input("\nCommand: ").strip().lower()
        if cmd == "n":
            current = new_compliment()
        elif cmd == "f":
            if current not in favourites:
                favourites.append(current)
                print("★ Saved to favourites.")
            else:
                print("Already in favourites.")
        elif cmd == "v":
            if favourites:
                print("\n=== Your Favourites ===")
                for i, c in enumerate(favourites, start=1):
                    print(f"{i}. {c}")
            else:
                print("\nNo favourites yet.")
        elif cmd == "q":
            print("Bye! Stay fabulous ✨")
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
