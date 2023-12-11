x="serga"

def gen(res, t, p, used: list):
    if p==len(x):
        res.append(t)
        return
    z = list(range(10))
    if p==0: z.remove(0)
    if x[p].isdigit():
        z = [int(x[p])]
    if x[p].isalpha():
        for c in used:
            z.remove(c)
    for c in z:
        if x[p].isalpha():
            used.append(c)
        gen(res, t*10+c,p+1,used)
        if x[p].isalpha():
            used.remove(c)

#freecodecamp pacekot
#lai apstadinatu programmu ir jaspiez - ctrl c

res = []
gen(res,0,0,[])
print(len(res))

def ok(serga_w, covid19_w):
    if len(covid19_w)<10:
        return False
    if covid19_w[6] !='1':
        return False
    if covid19_w[7] !='9':
        return False
    c_s = set(covid19_w[1:6])
    if len(c_s)<5:
        return False
    for c in serga_w:
        if c in c_s:
            return False
    return True
for y in res:
    for z_245 in range(10):
        m = str(y*z_245)
        if "2021" not in m:
            continue
        for z_3 in range(10):
            for z_1 in range(1,10):
                z=int(f"{z_1}{z_245}{z_3}{z_245}{z_245}")
           
                if ok(str(y), str(z*y)):
                    print(z,y,z*y)

#wolframalpha - a^(1/3)+b^(1/3)=c^(1/3) ievadit
            