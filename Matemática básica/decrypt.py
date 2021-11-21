flag = [86, -85, 105, 249, -199, 40, -123, 107, 20, 179, 123, 57, 111, 238, 139, 184, -75, -93, -27, 110, 137, -63, 53, 233, 53, 233, -108]


flag[0] = flag[0]-15
flag[0] = flag[0]^flag[0]^flag[0]^flag[0]^flag[0]
flag[1] = -flag[1]^(12)
flag[2] = flag[2]^44
flag[3] = ord('C')
flag[4] = ord('T')
flag[5] = ord('F') 
flag[6] = ord('{')
flag[7] = flag[7]^24
flag[8] = (flag[8]^(105))-77
flag[9] = (((flag[9]^(-199))^40)^107)^(-85)
flag[10] = (flag[10]^flag[1]^flag[0]^flag[1]^flag[0])-9
flag[11] = -flag[11]^(-12)
flag[12] = flag[12]^4
flag[13] = (flag[13]^111)-77
flag[14] = flag[14]^86^57^111^249
flag[15] = (flag[15]-81)
flag[15] = flag[15]^86^86^1^1
flag[16] = ord('a')
flag[17] = flag[17]^(-4)
flag[18] = flag[18]^(77-199)
flag[19] = flag[19]^(-27)^(111)^238^(-199)
flag[20] = flag[20]-23
flag[20] = (flag[20]^flag[20]^flag[20]^flag[20]^flag[20])
flag[21] = -flag[21]^12
flag[22] = flag[22]^87
flag[23] = (flag[23]^86)-77
flag[24] = flag[24]^1
flag[26] = flag[26]+flag[25]
flag[25] = flag[25]-flag[26]
print(flag[25])
print(chr(flag[25]))
final_flag = ''
for char in flag:
    final_flag += chr(char)
print(final_flag)