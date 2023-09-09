def main():
    x = int(input("what is x"))
    print("volume is ", cube_volume(x))
def cube_volume(side_length):
    volume = side_length ** 3
    return volume

main()