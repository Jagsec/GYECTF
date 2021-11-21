cipher = u'籐籢籎籌籝籏粄籬簼粃簽类籨簹籿簼类籨簹粁籁簹簹簹籨籱籾籱籪籱籪籱籪粆'
decimal_values = []
offset = 0x1F40
x = 23800
while x > 23000:
    flag = ''
    for char in cipher:
        value = int(hex(ord(char)),16) - offset - x
        flag += chr(value)
    if flag.startswith('G'):
        print(x)
        print(flag)
    x -= 1