
hwanyul = int(input())
money = int(input())


euro = money / hwanyul
if euro < 100:
    euro = euro - 1
hundred = int(euro/100)
fifty = int(euro%100/50)
ten = int(euro%100%50/10)
unit = int(euro%100%50%10/1)

print(hundred, fifty, ten, unit)