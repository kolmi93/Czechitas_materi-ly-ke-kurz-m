# ÚKOL Č. 3 - BALÍK PODRUHÉ

class Package:
    def __init__(self, adress, weight, state):
        self.adress = adress
        self.weight = weight
        self.state = state

        
    def __str__(self):   
        return f'Balik na adresu{self.adress} má váhu {self.weight} a je ve stavu: {self.state}.'
    
    def delivery_price(self):
        if self.weight < 10:
            price = 129
        elif self.weight < 20:
            price = 159
        else:
            price = 359
        return price
    
    def deliver(self):
        if self.state == 'nedoručen':
            self.state = 'doručen'
            return 'Doručení uloženo'
        else:
            return 'Balík již byl doručen.'


package_01 = Package('Václavské Náměstí 12, Praha', 0.25, 'nedoručen')
package_02 = Package('Horni Dolní 44, Tramtárie', 27.5, 'doručen')

print(package_01)
print(package_02)

print(package_01.deliver())
print(package_02.deliver())







# ÚKOL Č. 4 - KNIHY PODRUHÉ:+

class Book:
    def __init__(self, title, pages, price, sold, costs):
        self.title = title
        self.pages = pages
        self.price = price
        self.sold = sold
        self.costs = costs
    
    def get_info(self):
        return f'Kniha {self.title} má {self.pages} stran a stojí {self.price},- Kč.'

    def get_time_to_read(self, minutes_per_pages = 4):
        time_to_read = (minutes_per_pages * self.pages) / 60
        return f'Knihu {self.title} trvá přečíst {round(time_to_read)} hodin.'
    
    def profit(self):
        return self.sold * (self.price - self.costs)
    
    def rating(self):
        if self.profit() < 50000:
            return f'Kniha {self.title} je propadák.'
        elif self.profit() >= 50000 and self.profit() < 500000:
            return f'Kniha {self.title} je průměr.'
        else:
            return f'Kniha {self.title} je bestseller.'

book_01 = Book('Saturnin', 365, 400, 4500, 250)
book_02 = Book('Harry Potter a kámen mudrců', 275, 300, 2000000, 50)

print(book_01.profit())
print(book_01.rating())

print(book_02.profit())
print(book_02.rating())