def sit(a, b):
    correct = 0
    found = 0
    ar = []
    br = []
    for i in range(3):
        if a[i] == b[i]:
            correct += 1
        else:
            ar.append(a[i])
            br.append(b[i])

    for i in ar:
        if i in br:
            found += 1
            br.remove(i)

    return (correct, found)


def test_sit():
    assert sit("123", "111") == (1, 0)


for i in range(1000):
    i = str(i).zfill(3)
    if sit(i, "682") == (1, 0) and \
       sit(i, "614") == (0, 1) and \
       sit(i, "206") == (0, 2) and \
       sit(i, "780") == (0, 1):
        print(i)
