import random
WORDS_POOL = ["АРБУЗ", "БАНАН", "ВЕТКА", "ГОРОД", "ДВЕРЬ", 
            "ЗЕБРА", "ИГРОК", "КАШКА", "ЛАМПА", "МАСКА", 
            "НИТКА", "ОКЕАН", "ПАРУС",
            "РЫБАК", "САПОГ", 
            "ТУЧКА", "АКУЛА", 
            "ФИНИК", "ШКОЛА", "БЛЮДО"]  

MARK_GREEN = "[√]"
MARK_YELLOW = "[*]"
MARK_GRAY = "[×]"

def secret_word(words_list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            secret_word_value = random.choice(words_list)
            return func(secret_word_value, *args, **kwargs)
        return wrapper
    return decorator

@secret_word(WORDS_POOL)
def play(secret):
    used_letters = {}
    print("== ИГРА WORDE ===")
    print(f"Правила: {MARK_GREEN} - верно, {MARK_YELLOW} - не на месте, {MARK_GRAY} - нет в слове\n")

    for attempt in range(1, 7):
        while True:
            guess = input(f"Попытка {attempt} / 6. Введите 5 букв: ").strip().upper()
            if len(guess) == 5 and guess.isalpha():
                break
            print("Ошибка! Введите ровно 5 БУКВ.")

        result_marks = []
        for i in range(5):
            letter = guess[i]
            if letter == secret[i]:
                result_marks.append(f"{letter}{MARK_GREEN}")
                used_letters[letter] = MARK_GREEN
            elif letter in secret:
                result_marks.append(f"{letter}{MARK_YELLOW}")
                if used_letters.get(letter) != MARK_GREEN:
                    used_letters[letter] = MARK_YELLOW
            else:
                result_marks.append(f"{letter}{MARK_GRAY}")
                used_letters[letter] = MARK_GRAY

        print("Результат:", " ".join(result_marks))
        print("Использованные буквы:", end=" ")
        for let, status in sorted(used_letters.items()):
            print(f"{let}:{status}", end=" ")
        print("\n")

        if guess == secret:
            print("Поздравляем! Вы выиграли!")
            return

    print(f"Попытки кончились. Загаданное слово: {secret}")

if __name__ == "__main__":
    play()
