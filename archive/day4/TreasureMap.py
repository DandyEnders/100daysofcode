treasure_map = [[" "]*3, [" "]*3, [" "]*3]
any(map(lambda x: print(x), treasure_map))

position = input("Where do you want to put the treasure? ")
h, v = int(position[0]), int(position[1])

treasure_map[h-1][v-1]= "x"
any(map(lambda x: print(x), treasure_map))