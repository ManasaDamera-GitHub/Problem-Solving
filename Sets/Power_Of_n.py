base=5
power=4
initial_val=1
def sample(intial_val,base):
    global initial_val
    temp=0
    for i in range(base):
        temp+=intial_val
    initial_val=temp
for i in range(power):
    sample(initial_val,base)
print(initial_val)