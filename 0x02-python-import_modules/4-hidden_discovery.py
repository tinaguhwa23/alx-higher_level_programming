#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    # Print the sorted name from directory
    for name in sorted(dir(hidden_4)):
        # print only the names that do not start with __
        if name[:2] != '':
            print("{}".format(name))
