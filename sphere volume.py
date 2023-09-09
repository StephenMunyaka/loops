def main():
    r = int(input("what is r"))
    print("volume is ", sphere_volume(r))
def sphere_volume(radius):
    volume = (4/3) * math.pi * (radius ** 3)
    return volume
main()