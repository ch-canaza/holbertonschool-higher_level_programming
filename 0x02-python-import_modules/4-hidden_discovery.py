#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4 as str_modules
    modules = dir(str_modules)
    for i in range(0, len(modules)):
        if (modules[i][0] != '_'):
            print(modules[i])
