row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure?")
#eg 23
horizontal = int(position[0]) 
vertical = int(position[1])
#Longer way:
# selected_raw = map[vertical -1]
# selected_raw[horizontal -1 ] = "X"
#print(selected_raw)

#Shorter way:
map[vertical -1][horizontal -1 ] = "X"
print(f"{row1}\n{row2}\n{row3}")