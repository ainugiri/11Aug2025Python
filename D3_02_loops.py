# for - > iteration 

for i in range(10,21,2):
    print(i)

l1 = ['a', 'b', 'c', 'd', 'e']
for items in l1:
    print(items)




# while loop

x = 100
while x >=10:
    if x == 10:
        break
    print(x)
    x -= 10  # increment x by 1dddd


op = int(input("Enter a number: 1-7 1. Monday 2. Tuesday 3. Wednesday 4. Thursday 5. Friday 6. Saturday 7. Sunday: "))
op = op % 7
if op == 1:
    print("Monday")
elif op == 2:
    print("Tuesday")
elif op == 3:
    print("Wednesday")
elif op == 4:
    print("Thursday")
elif op == 5:
    print("Friday")
elif op == 6:
    print("Saturday")
elif op == 7:
    print("Sunday")


match op:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid option")


# hi | hello -> Hi,  welcome, 
# how are you? -> How are you doing?
# purchase -> iPhone, Macbook, iPad, Samsung, OnePlus, Vivo, Oppo, Realme
# service -> mobile, laptop, desktop, tablet, smartwatch
# bye -> Thank you for visiting, have a great day!


while True:
    prompt = input("YOU: ").lower().split()
    match True:
        case _ if 'hi' in prompt or 'hello' in prompt:
            print("BOT: Hi, welcome!")
        case _ if 'purchase' in prompt:
            print("BOT: We have iPhone, Macbook, iPad, Samsung, OnePlus, Vivo, Oppo, Realme.")
        case _ if 'service' in prompt:
            print("BOT: We provide service for mobile, laptop, desktop, tablet, smartwatch.")
        case _ if 'bye' in prompt or 'exit' in prompt or 'quit' in prompt:
            print("BOT: Thank you for visiting, have a great day!")
            break

prompt = input("YOU: ").lower().split()
if 'hi' in prompt or 'hello' in prompt:
    print("BOT: Hi, welcome!")
elif 'purchase' in prompt:
    print("BOT: We have iPhone, Macbook, iPad, Samsung, OnePlus, Vivo, Oppo, Realme.")
elif 'service' in prompt:
    print("BOT: We provide service for mobile, laptop, desktop, tablet, smartwatch.")
elif 'bye' in prompt or 'exit' in prompt or 'quit' in prompt:
    print("BOT: Thank you for visiting, have a great day!")