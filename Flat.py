class Flat:
    def __init__(self, number, price, floor, block, available=True):
        self.number = number
        self.price = price
        self.floor = floor
        self.block = block
        self.available = available

    def __repr__(self):
        return "{position : {number}, price : {price}, floor : {floor}, available : {available}\}".format(number=self.number,price=self.price,floor=self.floor,available=self.available)
