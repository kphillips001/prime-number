def prime_checker(number):
  is_prime = True
  for i in range(2, number):
    if number % i == 0:
    # Not a prime
      is_prime = False
  # Is a prime number
  if is_prime:
    print("It is a prime number")
  else:
    print("It is not a prime number")




n = int(input("Check this number: "))
prime_checker(number=n)