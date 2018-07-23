import sys

num_one = (int)(sys.argv[1])
num_two = (int)(sys.argv[2])
dividend = num_one / num_two
remainder = num_one % num_two

a = 5
b = 56.99
c = 9.322e-36j

def data_type(x):
    if type(x) == int:
        return "Integer"
    elif type(x) == float:
        return "Float"
    elif type(x) == complex:
        return "Complex"

print("%i divided by %i equals %i remainder %i" % (num_one, num_two, dividend, remainder))
print("Variable a contains : %i  which is of type: %s" % (a, data_type(a))) 
print("Variable b contains :", b, "which is of type:", data_type(b)) 
print("Variable c contains :", complex(c), "which is of type:", data_type(c)) 
