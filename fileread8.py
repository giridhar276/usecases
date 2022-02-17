with open('data.txt','r') as fobj:
    for line in fobj:
        print(line)

#  fobj can be called as file object or file handler or pointer
with open('data.txt','r') as fobj:
    print(fobj.readlines())

#  fobj can be called as file object or file handler or pointer
with open('data.txt','r') as fobj:
    print(fobj.readlines())

# using loop
with open('data.txt','r') as fobj:
    for line in fobj.readlines():
        print(line)

## using fobj.read()
with open('data.txt','r') as fobj:
    print(fobj.read())
    
print("------------")
# display first 20 characters
with open('data.txt','r') as fobj:
    print(fobj.read(20))

print("------------")
# display 2nd char to 9th char
with open('data.txt','r') as fobj:
    print(fobj.read()[2:10])
