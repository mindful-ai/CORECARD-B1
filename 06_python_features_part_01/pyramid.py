# Program to generate charecter triangle/pyramid

'''
N = 3
C = $

    $
   $$$
  $$$$$

'''

# input

N = int(input("Enter number of lines: "))
C = input("Enter the charecter: ")
print('-' * 60)

# process
# output

nc = 1  # increase by 2
ns = N  # Spaces reducing by 1
for i in range(N):
    s = ' ' * ns + C * nc
    print(s)
    ns -= 1
    nc += 2

    
