#       QUESTION 1

f = open("TestText.txt", "r")
n = int(input('Enter the number of last lines to read: '))
print(f.readlines()[-n:])
f.close()


#       QUESTION 2

count = 0
word = input('Enter the word to count: ')

with open("TestText.txt", "r") as f:
    text = f.read()

for ch in '-.,\n"':
    text = text.replace(ch, ' ')

for w in text.split():
    if word == w:
        count += 1
print(count)


#       QUESTION 3

with open("file1.txt", "r") as f1, open("file2.txt", "w") as f2:
    for line in f1:
        f2.write(line)


#       QUESTION 4

f1 = open("file1.txt", "r")
f2 = open("file2.txt", "r")

for line1, line2 in zip(f1, f2):
    print(line1+line2)

f1.close()
f2.close()


#       QUESTION 5

f = open("file.txt", "r+")
arr = input('Enter 10 random numbers: ')
f.write(arr)
Arr = f.read()
Arr = [int(x) for x in Arr]
Arr.sort()
f.write(str(Arr))
