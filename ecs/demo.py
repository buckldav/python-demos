with open('phrases.txt','r') as f:
    content = f.readlines()

content = [x.strip("\n") for x in content] 
for phrase in content:
    print(phrase)
    print("  How many characters? " + str(len(phrase)))
    print("  What is the phrase reversed? " + phrase[::-1])
    vowels = {i:0 for i in 'aeiouAEIOU'}
    vowelsInPhrase = 0
    for char in phrase:
        if char in vowels:
            vowelsInPhrase += 1
    print("  What is the number of vowels? " + str(vowelsInPhrase))
