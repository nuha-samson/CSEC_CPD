registered = {}
for i in range(int(input())):
    name = input()
    if name not in registered:
        registered[name] = 1
        print('OK')
    else:
        print(name+str(registered[name]))
        registered[name] += 1
        
