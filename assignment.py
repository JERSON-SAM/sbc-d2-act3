from random import randint

print ("E Enter Ang Una na Number:")
una = int(input())
print ("E Enter Ang Ikaduha na Number:")
duha = int(input())
print ("E Enter Ang Ikatulo na Number:") 
tulo = int(input())

bet = [una,duha,tulo]
print ("Your Bet: ", una, duha, tulo)


result = [randint(1,3) for _ in range(3)]

if bet == result:
    game_result = ("Daug Ka!")
elif set(bet) == set(result):
    game_result = ("Hapit Ka na Daug")
else:
    game_result = ("pilde ka! haha")

    print(f"result: {result}")
    print(game_result)

