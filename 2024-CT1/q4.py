def main():
    area: int = get_area()
    buckets: int = get_buckets(area)
    price: int = get_price(buckets)
    print(f"you need to purchase {buckets} buckets of paint at a price of ${price}.00")

def get_area() -> int:
    height: int = get_int("What is the height of the wall? ")
    width: int = get_int("What is the width of the wall? ")
    return height * width

def get_buckets(area):
    #resene needs 1 litre for 11 Sqm of wall area, but you need two coats:
    if area % 11 > 0:
        litres: int = ((area // 11) + 1) * 2
    else:
        litres: int = ((area // 11)) * 2
    # buckets contain 4 litres
    if litres % 4 > 0:
        return (litres // 4) + 1
    else:
        return litres // 4    
    
def get_price(buckets: int) -> int:
    if buckets <= 3:
        return buckets * 180
    else:
        return int((buckets * 180) * 0.8)

def get_int(prompt:int) -> int:
    while True:
        try:
            value: int = int(input(prompt))
        except:
            pass
        if value > 0:
            return value


main()