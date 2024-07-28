import random
import string

command = int(input("Press 1 for code it and press 0 for decode it: "))
message = input("Enter your message: ")
words = message.split(" ")
answer = []

if command == 1:
    for word in words:
        if len(word) >= 3:
            new_word = "".join(random.choice(string.ascii_lowercase) for _ in range(3))
            new_word += word.lower()[1::] + word.lower()[0] + "".join(random.choice(string.ascii_lowercase) for _ in range(3))
            answer.append(new_word)
        elif len(word) == 2:
            new_word = word.lower()[1] + word.lower()[0]
            answer.append(new_word)
        else:
            new_word = word.lower()
            answer.append(new_word)
    print(" ".join(answer))

elif command == 0:
    for word in words:
        if len(word) >= 3:
            new_word = word.lower()[-4] + word.lower()[3:-4]
            answer.append(new_word)
        elif len(word) == 2:
            new_word = word.lower()[1] + word.lower()[0]
            answer.append(new_word)
        else:
            new_word = word.lower()
            answer.append(new_word)
    print(" ".join(answer))

else:
    print("Press given number please")
    raise ValueError





