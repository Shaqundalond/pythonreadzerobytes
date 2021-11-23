def read_bytes(file_to_check):
    with open(file_to_check, 'rb') as f:
        while byte := f.read(1):
            if b'\x00' != byte:
                return False

        print(file_to_check)
        return True

files = ['testfile1','testfile2','testfile3','testfile4']

for lel in files:
    read_bytes(lel)
