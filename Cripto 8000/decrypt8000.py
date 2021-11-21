cipher = u'籐籢籎籌籝籏粄籬簼粃簽类籨簹籿簼类籨簹粁籁簹簹簹籨籱籾籱籪籱籪籱籪粆'
offset = 0x8000
x = 0x0
while x < offset:
    flag = ''
    for char in cipher:
        value = int(hex(ord(char)),16) - x
        try:
            flag += chr(value)
        except ValueError:
            pass
    if flag.startswith('G'):
        print(x)
        print(flag)
    x += 1
