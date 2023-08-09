def main():
    n = int(input("Enter the number: "))
    '''for sheeps in sheep(n):
        print(sheeps)'''
    for sheeps in sheep_gen(n):
        print(sheeps)


#using normal method
def sheep(X):
    flock = []
    for i in range(X):
        flock.append("SHEEP" *1)
    return flock

#using generator
def sheep_gen(X):
    for i in range(X):
        yield "SHEEP" *1

if __name__ == "__main__":
    main()
