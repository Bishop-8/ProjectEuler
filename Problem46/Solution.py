#This one was rough. I started out on lack of sleep, which led to some elevated frustration when I couldn't get the problem solved quickly
#I eventually got it figured out, but I have a lot of storage complexity to trim down. I went a little overboard with the brute force because
#I was ready to just be done with it. Still, It was a helpful problem in getting used to some python list methods

#Things I learned: It's more complicated than one thinks to validate a perfect square, the way python iterates through lists is weird, but still really nice, and
#it will always pay off to write some lines of code to help you diagnose your program. Visibility is important!

#As always, I am frustrated by the sieve of erastothenes, but life goes on. Also, it seems I am a c++ programmer at heart. When I finished the logic of everything
#I could not help but organize the code into declared functions, even though everything really runs once.

#In-line comments and time/storage complexity optimization to come later!

max = 6000
Primes =[True for i in range(max)]
Composites = []
PrimesValue = []
Squares = []
Solutions = []

#Creating Primes, OddComposites, and PrimeValues
def Sieve():
    x = 2
    y = a = 1
    while(a < (max/2)):
        y = x * a
        a += 1
        if Primes[y] == True:
            Primes[y] = False
    for i in range(3,max):
        y = a = 2
        while(a < (max/i)):
            y = i * a
            a+=1
            if Primes[y] == True:
                Primes[y] = False
    for index,n in enumerate(Primes):
        if Primes[index] == True:
            PrimesValue.append(index)
        elif(index % 2 != 0):
            Composites.append(index)
    print("Sieve Completed")
Sieve()

#CreatingSquares
def FindSquares():
    S = iterator = 1
    while(S < max):
        S = int((iterator*iterator)*2)
        if S < max:
            Squares.append(S)
        iterator += 1
    print("Squares Found")
FindSquares()

#Diagnostic Tool
def CheckThings(int):
    if int == 3:
        print(Primes)
    if int == 4:
        print(Composites)
    if int == 5:
        print(PrimesValue)
    if int == 6:
        print(Squares)
    if int == 7:
        print(Solutions)

#Logical Portion
def Main():
    for idx,k in enumerate(Composites):
        for x in Squares:
            if x < k:
                value = k-x
                if(Primes[value]==True):
                    Solutions.append(k)
                    break
        if Solutions[-1] != Composites[idx]:
            print(k," is a counterexample")
Main()
