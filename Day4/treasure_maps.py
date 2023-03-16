row1 = [" 🏞"," 🏞"," 🏞"]
row2 = [" 🏞"," 🏞"," 🏞"]
row3 = [" 🏞"," 🏞"," 🏞"]

maps = [row1,row2,row3]

print(f"{row1}\n{row2}\n{row3}")


location_y = int(input("Where is the colum do you put?"))
location_x = int(input("Where is the line do you put?"))

maps[location_y][location_x] = "X"

print(f"{row1}\n{row2}\n{row3}")

