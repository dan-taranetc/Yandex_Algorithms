end_code = int(input())
interactor = int(input())
cheker = int(input())

if interactor == 0:
    if end_code != 0:
        print(3)
    else:
        print(cheker)
elif interactor == 1:
    print(cheker)
elif interactor == 4:
    if end_code != 0:
        print(3)
    else:
        print(4)
elif interactor == 6:
    print(0)
elif interactor == 7:
    print(1)
else:
    print(interactor)