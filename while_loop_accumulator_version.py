def get_starting_number():
    while True:
        num = input("How many bottles of beer on the wall? ")
        if num.isdigit() and int(num) >= 1:
            return int(num)


def sing(num_bottles):
    n = num_bottles
    while n > 0:
        if n > 1:
            print(f"{n} bottles of beer on the wall, {n} bottles of beer.")
            if n - 1 == 1:
                print(f"Take one down, pass it around, 1 bottle of beer on the wall.\n")
            else:
                print(f"Take one down, pass it around, {n-1} bottles of beer on the wall.\n")
        else:
            print(f"1 bottle of beer on the wall, 1 bottle of beer.")
            print(f"Take it down, pass it around, no more bottles of beer on the wall!")
        n -= 1
