def main():
    with open('assets/naming_list.txt', 'r', encoding='utf8') as source:
        contents = [content.strip().split('|') for content in source.readlines()]
        contents = [list(filter(lambda x : x.strip() != '', content)) for content in contents]
        print(contents)

if __name__ == '__main__':
    main()
