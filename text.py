def greetng ():
    numberss= [1,2,1,5,3,5]
    firstnumber = numberss[0]
    lastenumber = numberss[-1]
    return firstnumber, lastenumber

f, l = greetng ()
print(f, l)

def greet(name, last_name):
    print(f"Hello, {name} {last_name}!")


greet("Alice", "Smith")
greet("Bob")
