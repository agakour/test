print("please insert salary")

salary = int(input())

hundred_count = salary // 100

print("hundreds: ", hundred_count)

salary = salary - hundred_count * 100

print("new salary minus hundreds: ", salary)

fifty_count = salary // 50

print("fifties:", fifty_count)

salary = salary - fifty_count * 50

print("new salary minus fifties", salary)

twenties_count = salary // 20

print("twenties:", twenties_count)

salary = salary - twenties_count * 20

print("new salary minus twenties", salary)

fives_count = salary // 5

print("fives:", fives_count)

salary = salary - fives_count * 5

print("new salary minus fives:", salary)

print("100,50,20,5:", hundred_count, fifty_count, twenties_count, fives_count)
