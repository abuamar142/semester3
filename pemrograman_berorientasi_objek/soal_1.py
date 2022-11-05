import locale
from prettytable import PrettyTable

locale.setlocale(locale.LC_ALL, 'id_ID')

class Category:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name
    @name.setter   
    def name(self, name):
        self.__name = name

class Product:
    def __init__(self, name, category, price, stock):
        self.__name = name
        self.__category = category
        self.__price = price
        self.__stock = stock

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def category(self):
        return self.__category
    @category.setter
    def category(self, category):
        self.__category = category
    
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price):
        self.__price = price
    
    @property
    def stock(self):
        return self.__stock
    @stock.setter
    def stock(self, stock):
        self.__stock = stock
    
class CartItem:
    def __init__(self, product, amount):
        self.__product = product
        self.__amount = amount
        self.__subtotal()

    def __subtotal(self):
        self.__product.price * self.__amount
    
    @property
    def subtotal(self):
        return self.__product.price * self.__amount

    @property
    def product(self):
        return self.__product
    @product.setter
    def product(self, product):
        self.__product = product
        self.__subtotal()
    
    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount):
        self.__amount = amount
        self.__subtotal()

class Cart:
    def __init__(self, items):
        self.__items = items
        self.__total()

    def __total(self):
        return sum([
            item.subtotal
            for item in self.__items
        ])
    
    @property
    def items(self):
        return self.__items
    @items.setter
    def items(self, items):
        self.__items = items
        self.__total()       

    @property
    def total(self):
        return sum([
            item.subtotal
            for item in self.__items
        ])
    @property
    def printout(self):
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
            for i, item in enumerate(self.__items)
        ])
        tb.add_row(['', '', '', '', '', f'{self.__total():n}'])
        
        return tb.get_string(title='Keranjang Belanja')
    

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
    print(cart.printout)