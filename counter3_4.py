for count in range(1, 10001):

    if (count % 3) == 0 and (count % 4) == 0:
        print("teilbar durch 3 und 4: " + str(count))

    elif (count % 3) == 0:
        print("teilbar durch 3: " + str(count))

    elif (count % 4) == 0:
        print("teilbar durch 4: " + str(count))

    else:
        print(count)


