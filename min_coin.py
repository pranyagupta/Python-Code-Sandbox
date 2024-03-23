#ask for change due
change_due=int(input("enter the change in cents: "))
# Intiaise coins = 0
coins=0
#calculate coins for "25" cents
coins = change_due // 25
#calculate change remaining
change_due = change_due % 25
#repeat it for all "10" "5" and "1" coins
coins += change_due // 10
change_due = change_due % 10
coins += change_due // 5
change_due = change_due % 5
coins += change_due // 1
change_due = change_due % 1

print(coins)
