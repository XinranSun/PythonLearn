def hello(name, language):
    greet = {
        "chinese": "nihao",
        "english": "hello"
    }
    msg = f"{greet[language]} {name}"
    print(msg)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='hen duo jieshi')
    parser.add_argument('-n', '--name', metavar="name", required=True, help='Name of the person')
    parser.add_argument('-l', '--lang', metavar="langu", required=True, help='Language of the person')
    arg = parser.parse_args()

hello(arg.name, arg.lang)
