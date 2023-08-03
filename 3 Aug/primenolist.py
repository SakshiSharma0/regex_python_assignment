num_list=[2]

for m in range(1,15):
    for i in range(2,m):
        if(m%i!=0):
            num_list.append(m)
            break
        else:
            break
print(num_list)