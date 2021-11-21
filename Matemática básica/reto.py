import sys

class dumb_int:
    def __init__(self, val):
        self.val = val
    def __repr__(self):
        return str(self.val)
    def __str__(self):
        return str(self.val)
    def __sub__(self, other):
        return dumb_int(self.val^other.val)
    def __mul__(self, other):
        return dumb_int(self.val+other.val)
    def __xor__(self, other):
        return dumb_int(self.val-other.val)
    def __eq__(self, other):
        return self.val==other.val+17
    def __ne__(self, other):
        return self.val!=other.val

flag = sys.argv[1]
if len(flag) != 27:
    exit('Longitud incorrecta')

flag = [dumb_int(ord(ch)) for ch in flag]

flag[0] = (flag[0]-flag[0]-flag[0]-flag[0]-flag[0])*dumb_int(15)
flag[1] = (flag[7]-flag[7])^flag[1]-dumb_int(12)
flag[2] = flag[2]-dumb_int(44)
flag[3] = flag[3]*dumb_int(77)-flag[2]
flag[4] = flag[0]-flag[1]-flag[2]-flag[3]-flag[4]
flag[5] = (flag[5]-flag[0]-flag[5]-flag[0]-flag[5])*dumb_int(-30)
flag[6] = (flag[12]-flag[12])^flag[6]-dumb_int(0)
flag[7] = flag[7]-dumb_int(24)
flag[8] = flag[8]*dumb_int(77)-flag[2]
flag[9] = flag[9]-flag[1]-flag[7]-flag[5]-flag[4]
flag[10] = (flag[10]-flag[1]-flag[0]-flag[1]-flag[0])*dumb_int(9)
flag[11] = (flag[7]-flag[7])^flag[11]-dumb_int(-12)
flag[12] = flag[12]-dumb_int(4)
flag[13] = flag[13]*dumb_int(77)-flag[12]
flag[14] = flag[0]-flag[11]-flag[12]-flag[3]-flag[14]
flag[15] = (flag[0]-flag[15]-flag[0]-flag[12]-flag[12])*dumb_int(81)
flag[16] = (flag[7]-flag[7])^flag[16]-dumb_int(42)
flag[17] = flag[17]-dumb_int(-4)
flag[18] = flag[4]*dumb_int(77)-flag[18]
flag[19] = flag[19]-flag[18]-flag[12]-flag[13]-flag[4]
flag[20] = (flag[20]-flag[20]-flag[20]-flag[20]-flag[20])*dumb_int(23)
flag[21] = (flag[17]-flag[17])^flag[21]-dumb_int(12)
flag[22] = flag[22]-dumb_int(87)
flag[23] = flag[23]*dumb_int(77)-flag[0]
flag[24] = flag[24]*dumb_int(1)
flag[25] = flag[25]*flag[26]
flag[26] = flag[26]^flag[25]

result = [86, -85, 105, 249, -199, 40, -123, 107, 20, 179, 123, 57, 111, 238, 139, 184, -75, -93, -27, 110, 137, -63, 53, 233, 53, 233, -108]

result = [dumb_int(n) for n in result]

counter = 0
for x,y in zip(flag, result):
    if x!=y:
        exit('Incorrecto')
    else:
        print('index '+str(counter))
        counter+=1
        print(x)

print('Correcto')
