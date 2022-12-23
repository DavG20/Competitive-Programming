if __name__ == '__main__':
    n = int(input())
    input_list_int = map(int, input().split())
    tuple_=tuple(input_list_int)
    print(hash(tuple_))