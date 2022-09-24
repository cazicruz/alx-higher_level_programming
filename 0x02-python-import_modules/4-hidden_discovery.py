#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4.pyc

    dicovers_1 = dir(hidden_4.pyc)

    for i in dicovers_1[1:]:
	print(dicovers_1 + "\n")
