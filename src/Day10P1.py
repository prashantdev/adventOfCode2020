joltages=[35, 111, 135, 32, 150, 5, 106, 154, 41, 7, 27, 117, 109, 63, 64, 21, 138, 98, 40, 71, 144, 13, 66, 48, 12, 55, 119, 103, 54, 78, 65, 112, 39, 128, 53, 140, 77, 34, 28, 81, 151, 125, 85, 124, 2, 99, 131, 59, 60, 6, 94, 33, 42, 93, 14, 141, 92, 38, 104, 9, 29, 100, 52, 19, 147, 49, 74, 70, 84, 113, 120, 91, 97, 17, 45, 139, 90, 116, 149, 129, 87, 69, 20, 24, 148, 18, 58, 123, 76, 118, 130, 132, 75, 110, 105, 1, 8, 86]

#joltages=[28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]
joltages.insert(0,0)
joltages.append(max(joltages)+3)

joltages.sort()
oneJolts=0
threeJolts=0
for jolt1 in joltages:
    for jolt2 in joltages:
        if jolt1>=jolt2:
            continue
        if jolt2-jolt1==1:
            oneJolts=oneJolts+1
            break
        if jolt2-jolt1==3:
            threeJolts=threeJolts+1
            break
print(oneJolts)
print(threeJolts)

print(oneJolts*threeJolts)

                
