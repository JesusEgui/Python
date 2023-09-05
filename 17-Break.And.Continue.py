while True:
    name = input('Enter your name or type "EXIT" to close the program: ')
    if name.lower() == 'exit':
        break
    print('Hello', name)

------------------------------------------------------------------------------------

Requesting names and exiting with a custom exit condition:

while True:
    name = input('Enter your name or type "EXIT" to close the program: ')
    if name.lower() == 'exit':
        break
    print('Hello', name)

Printing numbers from 1 to 20 excluding multiples of 5:
for i in range(1, 21):
    if i % 5 == 0:
        continue
    print(i)
