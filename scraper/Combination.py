class Combination:
  def __init__(self,productId,colorIndex):
    self.productId = productId
    self.attribute = 'Kolor kabla:select:1'
    self.value = ("Miedziany:1", "Srebrzysty:1", "Czarny:1", "Biały:1")[colorIndex]
    self.additionalPrice = 0
    self.default = 1 if colorIndex == 1 else 0
    
  def generate_csv(self):
    #Identyfikator Produktu (ID)|Indeks produktu|Atrybut (Nazwa:Typ:Pozycja)*|
    raw = str(self.productId) + ";;" + self.attribute + ";"
    #Wartość (Wartość:Pozycja)*|Identyfikator dostawcy|Indeks|kod EAN13|Kod kreskowy UPC|
    raw += self.value + ";;;;;"
    #MPN|Koszt własny|Wpływ na cenę|Podatek ekologiczny|Ilość|Minimalna ilość|
    raw += ";0;0;0;10;1;"
    #Niski poziom produktów w magazynie|Wyślij do mnie e-mail, gdy ilość jest poniżej tego poziomu|
    raw += "0;;"
    #Wpływ na wagę|Domyślny (0 = Nie, 1 = Tak)|Data dostępności kombinacji|
    raw += "0;" + str(self.default) + ";;"
    #Wybierz z pośród zdjęci produktów wg pozycji (1,2,3...)|Adresy URL zdjęcia (x,y,z...)|
    raw += ";;"
    #Tekst alternatywny dla zdjęć (x,y,z...)| ID / Nazwa sklepu|Zaawansowane zarządzanie magazynem|
    raw += ";0;0;"
    #Zależny od stanu magazynowego|Magazyn
    raw += "0;" 
    return raw