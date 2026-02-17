import random


def generate_variations(base_pass):
    # Common character substitutions
    substitutions = {"A": "4", "D": "0", "I": "1", "E": "3", "S": "5"}

    variations = {base_pass}  # Using a set to ensure uniqueness

    while len(variations) < 10:
        char_list = list(base_pass)

        # Strategy 1: Random substitution
        if random.random() > 0.5:
            for i, char in enumerate(char_list):
                if char.upper() in substitutions and random.random() > 0.7:
                    char_list[i] = substitutions[char.upper()]

        # Strategy 2: Case swapping
        if random.random() > 0.5:
            idx = random.randint(0, len(char_list) - 1)
            char_list[idx] = char_list[idx].swapcase()

        # Strategy 3: Append a common symbol
        new_pass = "".join(char_list)
        if len(variations) % 3 == 0:
            new_pass += "!"

        variations.add(new_pass)

    return list(variations)


original = "KD21D1620"
password_list = generate_variations(original)

for i, pw in enumerate(password_list, 1):
    print(f"{i}. {pw}")
