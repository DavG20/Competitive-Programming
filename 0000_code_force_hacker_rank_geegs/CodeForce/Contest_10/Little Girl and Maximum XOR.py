left , right = list(map(int, (input().split())))

bit_len = (left ^ right).bit_length()

# print((2**bit_len )^ (2**(bit_len) - 1))
print(2 **(bit_len )- 1)


