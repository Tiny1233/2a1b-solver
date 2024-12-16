
import random 

def check_unique_digits(num):
    num_str = str(num)
    return len(set(num_str)) == len(num_str)

def compare_numbers(guess, target):
    guess_str = str(guess)
    target_str = str(target)
    a_count = 0
    b_count = 0
    for i in range(len(guess_str)):
        if guess_str[i] in target_str:
            if guess_str[i] == target_str[i]:
                b_count += 1
            else:
                a_count += 1
    return f"{a_count}a{b_count}b"


def mod(x):
    xm = str(x)
    return ('0'*(4-len(xm))+xm)

candidates = [mod(i) for i in range(0,10000) if check_unique_digits(mod(i))]

print("Press enter to continue...")
input()

remaining_guesses = 10
while remaining_guesses > 0 and candidates:
    current_guess = candidates[random.randint(0,len(candidates))]
    print(f"enter result of：{current_guess}(1 in the {str(len(candidates))})")
    feedback = input("the feedback：")
    
    new_candidates = []
    for candidate in candidates:
        if compare_numbers(candidate, current_guess) == feedback:
            new_candidates.append(candidate)
    candidates = new_candidates
    remaining_guesses -= 1
