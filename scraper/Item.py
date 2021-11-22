import random

class Item:
  def __init__(self,id, name,image, price,price_with_tax, description, technical_properties, category):
    self.id = id
    self.name = name
    self.image = image
    self.price = price
    self.price_with_tax = price_with_tax
    self.description = description
    self.technical_properties = technical_properties
    self.category = category

  def generate_csv(self):    
    #         ID| Aktywny (0 lub 1)| Nazwa  | Kategorie (x,y,z...)
    raw = str(self.id) + ";1;" + self.name + ";" + self.category + ";" 
    #Cena bez podatku. (netto)||ID reguły podatku
    raw += str(self.price) + ";1;"
    # Koszt własny|W sprzedaży (0 lub 1)|Wartość rabatu|Procent rabatu
    raw += ";0;;;"
    # Rabat od dnia (rrrr-mm-dd)|Rabat do dnia (rrrr-mm-dd)|Indeks #|Kod dostawcy
    raw += ";;;;"
    # Dostawca|Marka|kod EAN13|Kod kreskowy UPC|MPN|Podatek ekologiczny|Szerokość
    raw += ";;;;;;;"
    # Wysokość|Głębokość|Waga|Czas dostawy produktów dostępnych w magazynie:
    raw += ";;;;"
    # Czas dostawy wyprzedanych produktów z możliwością rezerwacji:|Ilość|Minimalna ilość
    raw += ";"+ str(random.randint(0,100)) + ";1;"
    # Niski poziom produktów w magazynie|Wyślij do mnie e-mail, gdy ilość jest poniżej tego poziomu
    raw += "1;1;"
    # Widoczność|Dodatkowe koszty przesyłki|Jednostka dla ceny za jednostkę|Cena za jednostkę
    raw += "both;;;;"
    # Podsumowanie|Opis|Tagi (x,y,z...)|Meta-tytuł|Słowa kluczowe meta|Opis meta|Przepisany URL
    raw += self.technical_properties + ";" + self.description + ";;Meta title-" + str(self.id) + ";Meta keywords-" + str(self.id) + ";Meta description-" + str(self.id) + ";;"
    # Etykieta, gdy w magazynie|Etykieta kiedy dozwolone ponowne zamówienie
    raw += "Dostępny;Niedostępny;"
    # Dostępne do zamówienia (0 = Nie, 1 = Tak)|Data dostępności produktu|Data wytworzenia produktu
    raw += "1;;2021-01-01 10:10:10;"
    # Pokaż cenę (0 = Nie, 1 = Tak)|Adresy URL zdjęcia (x,y,z...)|Tekst alternatywny dla zdjęć (x,y,z...)
    raw += "1;" + self.image + ";;"
    # Usuń istniejące zdjęcia (0 = Nie, 1 = Tak)|Cecha(Nazwa:Wartość:Pozycja:Indywidualne)
    raw += "0;;"
    # Dostępne tylko online (0 = Nie, 1 = Tak)|Stan:|Konfigurowalny (0 = Nie, 1 = Tak)
    raw += "0;new;0;"
    # Można wgrywać pliki (0 = Nie, 1 = Tak)|Pola tekstowe (0 = Nie, 1 = Tak)|Akcja kiedy brak na stanie
    raw += "0;0;0;"
    # Wirtualny produkt (0 = No, 1 = Yes)|Adres URL pliku|Ilość dozwolonych pobrań|Data wygaśnięcia (rrrr-mm-dd)
    raw += "0;;;;"
    # Liczba dni;ID / Nazwa sklepu|Zaawansowane zarządzanie magazynem|Zależny od stanu magazynowego|Magazyn
    raw += ";0;0;0;0;"
    # Akcesoria (x,y,z...)
    raw += ""
    ###---------------------------------------------------------------------------------------------------
    return raw
  
  def generate_simple_csv(self):
              #id     aktywny   nazwa             #kategoria              #cena brutto         
    raw = str(self.id) + ";1;" + self.name + ";" + self.category + ";" + str(self.price) + ";";
                                     #na sell
    raw += str(self.price_with_tax) + ";1;"
          #url zdjecia          #opis                 #opis techniczny
    raw += self.image + ";" + self.description + ";" + self.technical_properties + ";"
          #dostepnosc
    raw += "1;"
    #raw += ";"
    return raw