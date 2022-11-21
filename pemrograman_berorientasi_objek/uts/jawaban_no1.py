import locale
from prettytable import PrettyTable

locale.setlocale(locale.LC_ALL, 'id_ID')

class Category:
    def __init__(self, name):
        self.name = name

class Product:
    def __init__(self, name, category, price, stock):
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

class CartItem:
    def __recalc(self):
        self.__subtotal = self.__product.price * self.__amount
    
    def __init__(self, product, amount):
        self.__product = product
        self.__amount = amount
        self.__recalc()

    @property
    def product(self):
        return self.__product
    @property
    def amount(self):
        return self.__amount
    @property
    def subtotal(self):
        return self.__subtotal
    @amount.setter
    def amount(self, value):
        self.__amount = value
        self.__recalc()

class Cart:
    def __recalc(self):
        '''
        self.__total = 0
        for item in self.__items:
            self.__total += item.subtotal
        '''
        self.__total = sum([
            item.subtotal
            for item in self.__items
        ])
        tb = PrettyTable()
        tb.field_names = [
            'No',
            'Barang',
            'Kategori',
            'Harga',
            'Jumlah',
            'Total',
        ]
        tb.align.update(dict(zip(
            tb.field_names,
            ['r', 'l', 'l', 'r', 'r', 'r']
        )))
        tb.add_rows([
            [
                i + 1,
                item.product.name,
                item.product.category.name,
                f'{item.product.price:n}',
                f'{item.amount:n}',
                f'{item.subtotal:n}',
            ]
            for i, item in enumerate(self.items)
        ])
        tb.add_row(['', '', '', '', '', f'{self.__total:n}'])
        self.__printout = tb.get_string(title='Keranjang Belanja')

    def __init__(self, items):
        self.__items = items
        self.__recalc()
    
    @property
    def items(self):
        return self.__items
    @property
    def total(self):
        return self.__total
    @property
    def printout(self):
        return self.__printout

if __name__ == '__main__':
    categories = [
        Category('Sabun Mandi'),
        Category('Pasta Gigi'),
    ]
    products = [
        Product('Lux', categories[0], 10000, 100),
        Product('Lifebuoy', categories[0], 5000, 200),
        Product('Pepsodent', categories[1], 8000, 120),
    ]
    cart = Cart([
        CartItem(products[0], 20),
        CartItem(products[1], 30),
        CartItem(products[2], 10),
    ])
    cart.items[0].product.name = 'Nuvo'
    print(cart.items[0].product.name)
    print(cart.printout)