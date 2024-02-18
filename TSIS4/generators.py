def square_generator(N):
    for i in range(1, N + 1):
        yield i ** 2

squares = square_generator(5)

print(squares)
for square in squares:
    print(square)
    
    

def even_numbers_generator(N):
    for i in range(N + 1):
        if i % 2 == 0:
            yield i
            
even_numbers = even_numbers_generator(5)
result = ', '.join(map(str, even_numbers))
print(result)


def divisible_by_3_and_4_generator(N):
    for i in range(N + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
divisible_numbers = divisible_by_3_and_4_generator(0)
for num in divisible_numbers:
        print(num)
        
        
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2
for square in squares(0, 2):
    print(square)