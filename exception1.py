



try:
    #1st logic
    filename = input("Enter any filename :")
    with open(filename,'r') as fobj:
        for line in fobj:
            print(line)
    #2nd logic
    val = 3 + "hello"
    
except Exception as error:
    print(error)

print('regular code')
