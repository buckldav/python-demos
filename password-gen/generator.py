from random import randrange

f = open("words.txt", "r")
words = f.readline().split(", ")
new_list = ""
for word in words:
  if len(word) == 3:
    new_list += word + ", "
f.close()

f = open("output.txt", "w")
f.writelines(new_list)
f.close()

def passwords():
  try:
    num_of_passwords = int(input("How many passwords do you want? "))
    for i in range(num_of_passwords):
      rand_digit = randrange(0,100)
      rand_digit = "0" + str(rand_digit) if rand_digit < 10 else str(rand_digit)
      print(f"{words[randrange(0,len(words))]}{words[randrange(0,len(words))]}{rand_digit}")
  except:
    print("Please type a number")
    passwords()
passwords()