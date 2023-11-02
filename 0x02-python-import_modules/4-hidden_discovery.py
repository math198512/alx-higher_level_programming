#!/usr/bin/python3
if __name__ == "__main__":
    """Print all names from hidden_4"""
    import hidden_4

    contents = dir(hidden_4)
    for name in contents:
        if name[:2] != "__":
            print(name)
