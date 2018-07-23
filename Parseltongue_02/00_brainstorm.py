import random
import shutil
import time

columns = shutil.get_terminal_size().columns
random_int = random.randint(0,10)
user_input = []
category_name = ["Action", "Party", "Tabletop", "Video", "Technology", " Role-playing", "MMO","Simulation", "Strategy", "Sports"]

def _one_frame(text):                 # text is supposed to be a list of lines
    lt = len(text[0])
    horz = '*' + ' '*lt + '*'         # Make the horizontal line +-------+
    result = [horz]                   # Top of the frame
    for line in text:
        result.append( '*'+line+'*' ) # Add the borders for each line
    #result.append(horz)               # Bottom of the frame
    return result

def frame(text, repeat, thickness):
    text = [" %s "%text]*repeat       # add spaces and repeat as a list
    for i in range(thickness):
        text = _one_frame(text)       # draw one frame per iteration
    return '\n'.join(text)            # join lines

print(category_name[random_int])
num = len(category_name)
t0 = time.time()

for i in range (10):
    name = input("what you wanna play?\n")
    user_input.append(name)
t1 = time.time() - t0

k = len(user_input[0].center(columns))
print('*' + '*'*k + '***')
for i in range(len(user_input)):
    print(frame((user_input[i].center(columns)),1,1))
print('*' +'*'*k + '***')
print("elapsed time: ",t1)
