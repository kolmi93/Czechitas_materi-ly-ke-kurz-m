ODDELOVAC = (1*'\n' + 30* '_' + 1*'\n')
print(ODDELOVAC)

# ÚKOL Č.1 - ZVÍŘATA:

class Zvire:
    def __init__(self, jmeno: str, druh: str, vaha: int):
        self.jmeno = jmeno
        self.druh = druh
        self.vaha = vaha

    def __str__(self):
        return f'{self.jmeno} patří mezi druh {self.druh} a váží {self.vaha}.'
    
    def export_to_dict(self):
        jmeno = self.jmeno
        druh = self.druh
        vaha = self.vaha
        dict_zvirata = {
            'jmeno':jmeno,
            'druh': druh,
            'vaha': vaha,
        }
        return dict_zvirata

panda = Zvire('Růženka', 'Panda Velká', 150)
vydra = Zvire('Vilda', 'Vydra Mořská', 20)
tygr = Zvire('Matýsek', 'Tygr Sumatera', 300)
medved = Zvire('Karlík', 'Lední Medvěd', 700)

zvirata = [panda, vydra, medved, tygr]

zvirata_dict = []

for zvire in zvirata:
    zvirata_dict.append(zvire.export_to_dict())
    print(zvire)

# vypíše slovník zvířat
print(zvirata_dict)

assert hasattr(zvire, 'jmeno')
assert hasattr(zvire, 'druh')
assert hasattr(zvire, 'vaha')
assert isinstance(zvire.jmeno, str)
assert isinstance(zvire.druh, str)
assert isinstance(zvire.vaha, int)

print(ODDELOVAC)

# ÚKOL Č.2 - ZAMĚSTNANEC:

class Zamestnanec:
    def __init__(self, jmeno: str, rocni_plat: int, pozice: str):
        self.jmeno = jmeno
        self.rocni_plat = rocni_plat
        self.pozice = pozice

    def __str__(self):
        return f'{self.jmeno} je na pozici {self.pozice} a roční plat má {self.rocni_plat},- Kč.'

    def ziskej_inicialy(self):
        jmeno = self.jmeno.split()
        return f'{jmeno[0][0].upper()}.{jmeno[1][0].upper()}.'
    
    def dictionary(self):
        jmeno = self.jmeno
        plat = self.rocni_plat
        pozice = self.pozice
        dict_zamestnanci  = {
            'jmeno': jmeno,
            'plat': plat,
            'pozice': pozice,
        }
        return dict_zamestnanci
    
tereza = Zamestnanec('Tereza Vysoká', 700000, 'Cvičitelka tygrů')
aneta = Zamestnanec('Anet Krasna', 600000, 'Cvičitelka vyder')
martin = Zamestnanec('Martin Veliký', 650000, 'Cvičitel ledních medvědů')

zamestnanci = [tereza, aneta, martin]

zamestnanci_list = []
for zamestnanec in zamestnanci:
    zamestnanci_list.append(zamestnanec.dictionary())
    print(zamestnanec.ziskej_inicialy())

print(zamestnanci_list)

assert hasattr(zamestnanec, 'jmeno')
assert hasattr(zamestnanec, 'rocni_plat')
assert hasattr(zamestnanec, 'pozice')
assert isinstance(zamestnanec.jmeno, str)
assert isinstance(zamestnanec.rocni_plat, int)
assert isinstance(zamestnanec.pozice, str)
    
print(ODDELOVAC)

# ÚKOL Č. 3 - ŘEDITEL:

class Reditel(Zamestnanec):
    def __init__(self, jmeno, rocni_plat, pozice = 'Ředitel', oblibene_zvire = Zvire):
        super().__init__(jmeno, rocni_plat, pozice)
        self.oblibene_zvire = oblibene_zvire

    def __str__(self):
        return f'{self.jmeno} je na pozici {self.pozice} a roční plat má {self.rocni_plat},- Kč. Jeho oblíbené zvíře je {self.oblibene_zvire.druh} {self.oblibene_zvire.jmeno}.'
      
reditel = Reditel('Karel', 800000, oblibene_zvire = zvire)

print(reditel)

assert reditel.pozice == 'Ředitel'
assert isinstance(reditel.oblibene_zvire, Zvire)

'''print(ODDELOVAC)

# ÚKOL Č. 4 - ZOO:
class Zoo:
    def __init__(self, jmeno: str, adresa: str, reditel: Reditel, zamestnanci: list[Zamestnanec], zvirata: list[Zvire]):
        self.jmeno = jmeno
        self.adresa = adresa
        self.reditel = reditel
        self.zamestnanci = zamestnanci
        self.zvirata = zvirata

    def __str__(self):
        return f'Zoo {self.jmeno} se nachází na adrese {self.adresa}. V této ZOO pracuje {self.zamestnanci} zaměstnanců a chová se zde {self.zvirata} zvířat.'

    def vaha_vsech_zvirat_v_zoo(self):
        celkova_vaha = 0
        for zvire in self.zvirata:
            celkova_vaha += zvire.vaha
        return celkova_vaha

    def mesicni_naklady_na_zamestnance(self):
        vsichni_zamestnanci = [self.reditel] + self.zamestnanci[:]
        celkove_naklady = 0
        for zamestnanec in vsichni_zamestnanci:
            celkove_naklady += zamestnanec.rocni_plat
        return celkove_naklady / 12
    
    def mesicni_naklady_na_zamestnance_2(self):
        vsichni_zamestnanci = [tereza, aneta, martin, reditel]
        celkove_naklady = 0
        for zamestnanec in vsichni_zamestnanci:
            celkove_naklady += zamestnanec.rocni_plat
        return celkove_naklady / 12

zoo = Zoo('ZOO Praha', 'U Trojského zámku 3/120', reditel, zamestnanci, zvirata)


print(zoo.reditel)
print('Celková váha zvířat v ZOO:', zoo.vaha_vsech_zvirat_v_zoo())
print('Měsíční náklady na zaměstnance:', zoo.mesicni_naklady_na_zamestnance())
print('Měsíční náklady na zaměstnance:', zoo.mesicni_naklady_na_zamestnance_2())'''