
sentence = "This is the most common Interview Question for beginners"

repeat_letter = {}

print(type(repeat_letter))

for i in sentence.lower():
    # print(i)
    # repeat_leatter = {}


    if i in repeat_letter:
        # print(True)
        if i != ' ':
            fetch_value = repeat_letter[i]
            repeat_letter[i] = fetch_value + 1

    else:
        # print(False)
        repeat_letter[i] = 1
 
print(sentence)
print(repeat_letter)

char_frequency = sorted(
    repeat_letter.items(), 
    key = lambda kv: kv[1], 
    reverse=True)

print('char = ',char_frequency)


print('Most Repetative Letter = ',char_frequency[0])
