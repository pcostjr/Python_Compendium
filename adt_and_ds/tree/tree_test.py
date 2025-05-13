from tree import SimpleDict

if __name__ == '__main__':
    sd = SimpleDict()
    sd['key'] = 'a value'
    print(sd.depth())
    print('key' in sd)
    for key in sd:
        print(key)