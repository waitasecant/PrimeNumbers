from math import sqrt

def isPrime(n):
	if (n <= 1):
		return None
	for i in range(2, int(sqrt(n))+1):
		if (n % i == 0):
			return None
	return str(n)

def PrimesUptoM(m):
    for j in range(m+1):
        x = isPrime(j)
        if x != None:
            data.append(x + " ")
        else:
            pass
    return data

def PrimesBetweenMandN(a ,b):
    for k in range(a, b+1):
        x = isPrime(k)
        if x != None:
            data.append(x + " ")
        else:
            pass
    return data

def LogDataUptoM(m):
    with open("test.txt", "a+") as fm:
        fm.writelines(PrimesUptoM(m))

def LogDataBetweenMandN(m , n):
    with open("test.txt", "a+") as fmn:
        fmn.writelines(PrimesBetweenMandN(m, n))

# driver code
data = []
def main():


    a = open("test.txt", "a+")
    a.close()

    r = open("test.txt", "r+")
    t = r.readlines()
    if t == []:
        inp1 = int(input("Enter the value"))
        LogDataUptoM(inp1)
    elif t != []:
        init = t[0]
        init = init.strip()
        init= init.split(" ")
        init1 = init[len(init)-1]
        print(init1)
        inp2 = int(input("Enter the value"))
        LogDataBetweenMandN(eval(init1), inp2)

    r.close()
if __name__ == "__main__":
    main()