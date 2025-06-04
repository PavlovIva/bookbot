

def read_the_book(file_name):
    with open(file_name) as f:
        try:
            print(f.read())
        except UnicodeDecodeError:
            print(UnicodeDecodeError)

