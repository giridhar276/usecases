


try:
    #1st logic
    filename = input("Enter any filename :")
    with open(filename,'r') as fobj:
        for line in fobj:
            print(line)
    #2nd logic
    val = str(3) + "hello"

except FileNotFoundError as error:
    print("File doen't exist.. pl check")
    print(error)
except TypeError as error:
    print("Invalid operation")
    print(error)
except ValueError as error:
    print("Invalid conversion")
    print(error)
except (IndexError, KeyError ) as err:
    print("key or index is not existing.. pl check")
except Exception as err:
    print("System error :" , err)
else:
    print("few lines of code")


