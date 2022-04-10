import time
start = time.monotonic_ns()
print(start)
x=1
while(x<=100):
    print(x)
    x +=1
finish=time.monotonic_ns()    
duration = finish -  start
print(f"That took {duration}ns")

print ("Privet")