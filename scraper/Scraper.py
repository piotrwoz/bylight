from bs4 import BeautifulSoup
import requests
from Category import Category
from Combination import Combination
from Item import Item

def generate_categories():
  categories = []
  categories.append(Category("19-lampy-wiszace","Lampy wiszace"))
  categories.append(Category("21-kinkiety","Kinkiety"))
  categories.append(Category("12-zarowki-dekoracyjne","Zarowki dekoracyjne"))
  categories.append(Category("63-plafony","Plafony"))
  #categories.append(Category("46-kolorowe-kable","Kolorowe kable"))
  #categories.append(Category("20-lampy-biurkowe","Lampy biurkowe"))
  #categories.append(Category("22-akcesoria","Akcesoria"))
  #categories.append(Category("23-lampy-podlogowe","Lampy podlogowe"))
  #categories.append(Category("97-lampy-marynistyczne","Lampy marynistyczne"))
  #categories.append(Category("98-lampy-podtynkowe","Lampy podtynkowe"))
  #categories.append(Category("24-oswietlenie-ogrodowe","Oswietlenie ogrodowe"))
  #categories.append(Category("94-oswietlenie-szynowe","Osiwetlenie szynowe"))
  #categories.append(Category("108-akcesoria-thpg","Akcesoria THPG"))
  #categories.append(Category("54-gadzety","Gadzety"))
  #categories.append(Category("99-nanlite","NANLITE"))
  #categories.append(Category("116-meble","Meble"))
  return categories

def get_page_code(path):
  page = requests.get(path).text
  return page

def get_title(main):
  title = main.find('h1', itemprop='name')
  return title.text

def get_image(main):
  proper_block = main.find('div', class_='primary_block row')
  photo_path = ""
  images = proper_block.find_all('img')
  
  first_photo = images[0]
  photo_path = first_photo['src']
  return photo_path

def get_description(main):
  try:
    tmp = main.find('div', itemprop='description')
    descriptions = tmp.find_all("p")
    description = ""
    for i in range(len(descriptions)):
      description += "<p>" + descriptions[i].text + "</p>"
    return description
  except:
    return ''

def get_technical_properties(main):
  try:
    technical_properties = ""
    definitions = main.find_all("dt")
    values = main.find_all("dd")
    for i in range(len(definitions)):
      technical_properties += definitions[i].text + ":" + values[i].text + '\n'
    return technical_properties
  except:
    return ''
  
def get_technical_properties_table(main):
  table = "<dl>"
  try:
    technical_properties = ""
    definitions = main.find_all("dt",class_="feat-name")
    values = main.find_all("dd",class_="feat-value")
    for i in range(len(definitions)):
      table += "<dt>" + definitions[i].text + "</dt><dd>" + values[i].text.strip() + "</dd>"
    table += "</dl>"
    return table
  except:
    return ''

def print_desc(desc):
  for it in desc:
    print(it.text)
  return

def get_price(main):
  price = main.find('p', class_='our_price_display')
  price_number = price.text.split('z??')[0].replace(" ","").replace(",",".")
  return round(float(price_number),2)

def calculate_netto(price_with_tax):
  price_without_tax = (100 * price_with_tax)/(123)
  return round(price_without_tax,2)
  

###--------------------REAL SCRIPT---------------------------###
file = open('./allProductsCSV.csv','w', encoding='utf-8')
headerText = "ID;Aktywny (0 lub 1);Nazwa;Kategorie (x,y,z...);Cena zawiera podatek. (brutto);"
headerText += "ID regu??y podatku;Koszt w??asny;"
headerText += "W sprzeda??y (0 lub 1);Warto???? rabatu;Procent rabatu;Rabat od dnia (rrrr-mm-dd);"
headerText += "Rabat do dnia (rrrr-mm-dd);Indeks #;Kod dostawcy;Dostawca;Marka;kod EAN13;"
headerText += "Kod kreskowy UPC;MPN;Podatek ekologiczny;Szeroko????;Wysoko????;G????boko????;Waga;"
headerText += "Czas dostawy produkt??w dost??pnych w magazynie:;Czas dostawy wyprzedanych produkt??w z mo??liwo??ci?? rezerwacji:;"
headerText += "Ilo????;Minimalna ilo????;Niski poziom produkt??w w magazynie;Wy??lij do mnie e-mail, gdy ilo???? jest poni??ej tego poziomu;"
headerText += "Widoczno????;Dodatkowe koszty przesy??ki;Jednostka dla ceny za jednostk??;Cena za jednostk??;Podsumowanie;Opis;"
headerText += "Tagi (x,y,z...);Meta-tytu??;S??owa kluczowe meta;Opis meta;Przepisany URL;Etykieta, gdy w magazynie;"
headerText += "Etykieta kiedy dozwolone ponowne zam??wienie;Dost??pne do zam??wienia (0 = Nie, 1 = Tak);Data dost??pno??ci produktu;"
headerText += "Data wytworzenia produktu;Poka?? cen?? (0 = Nie, 1 = Tak);Adresy URL zdj??cia (x,y,z...);"
headerText += "Tekst alternatywny dla zdj???? (x,y,z...);Usu?? istniej??ce zdj??cia (0 = Nie, 1 = Tak);Cecha(Nazwa:Warto????:Pozycja:Indywidualne);"
headerText += "Dost??pne tylko online (0 = Nie, 1 = Tak);Stan:;Konfigurowalny (0 = Nie, 1 = Tak);Mo??na wgrywa?? pliki (0 = Nie, 1 = Tak);"
headerText += "Pola tekstowe (0 = Nie, 1 = Tak);Akcja kiedy brak na stanie;Wirtualny produkt (0 = No, 1 = Yes);"
headerText += "Adres URL pliku;Ilo???? dozwolonych pobra??;Data wyga??ni??cia (rrrr-mm-dd);Liczba dni;ID / Nazwa sklepu;"
headerText += "Zaawansowane zarz??dzanie magazynem;Zale??ny od stanu magazynowego;Magazyn;Akcesoria (x,y,z...)"

file.write(headerText)

file.close()

###------------------------------DO KOMBINACJI--------------------------------------------
file = open('./allCombinationsCSV.csv','w', encoding='utf-8')
combinationsHeader = "Identyfikator Produktu (ID);Indeks produktu;Atrybut (Nazwa:Typ:Pozycja)*;";
combinationsHeader += "Warto???? (Warto????:Pozycja)*;Identyfikator dostawcy;Indeks;kod EAN13;Kod kreskowy UPC;"
combinationsHeader += "MPN;Koszt w??asny;Wp??yw na cen??;Podatek ekologiczny;Ilo????;Minimalna ilo????;"
combinationsHeader += "Niski poziom produkt??w w magazynie;Wy??lij do mnie e-mail, gdy ilo???? jest poni??ej tego poziomu;"
combinationsHeader += "Wp??yw na wag??;Domy??lny (0 = Nie, 1 = Tak);Data dost??pno??ci kombinacji;"
combinationsHeader += "Wybierz z po??r??d zdj??ci produkt??w wg pozycji (1,2,3...);Adresy URL zdj??cia (x,y,z...);"
combinationsHeader += "Tekst alternatywny dla zdj???? (x,y,z...); ID / Nazwa sklepu;Zaawansowane zarz??dzanie magazynem;"
combinationsHeader += "Zale??ny od stanu magazynowego;Magazyn"
file.write(combinationsHeader)
file.close()


###--------------------------------------------------------------------------------------
main_path = "https://bylight.pl/"
categories = generate_categories()
items = []
hanging_lamps_indexes = []
index = 0
low_index = 14
high_index = 15

for category in categories:
  
  category_path = category.path
  category_title = category.name
  page_code = get_page_code(main_path + category_path)
  
  soup = BeautifulSoup(page_code, 'lxml')
  list_elements = soup.find_all('li', class_= 'ajax_block_product')
  
  for element in list_elements:
    index += 1
    if category.name == "Lampy wiszace":
      hanging_lamps_indexes.append(index)
    
    product_path = element.find('a', class_='product_img_link').attrs['href']
    print(f'Item number: {index} with path: {product_path}')
    product_page_data = get_page_code(product_path)
    soup2 = BeautifulSoup(product_page_data,'lxml')
    main_content = soup2.find('div', id='center_column')
    title = get_title(main_content)
    description = get_description(main_content)
    technical_properties = get_technical_properties_table(main_content)
    full_price = get_price(main_content)
    price_without_tax = calculate_netto(full_price)
    image_path = get_image(main_content)

    product = Item(index,title,image_path,price_without_tax,full_price,description,technical_properties, category.name)
    items.append(product)
    product_csv_raw = "\n" + product.generate_csv()

  
    with open('allProductsCSV.csv', 'a', encoding='utf-8') as file:
          file.write(product_csv_raw)
    
file.close()

for i in range (1,len(hanging_lamps_indexes) + 1):
  for j in range(0,4):
    combo = Combination(i, j)
    combination_csv_raw = "\n" + combo.generate_csv()
    with open('allCombinationsCSV.csv', 'a', encoding='utf-8') as file:
      file.write(combination_csv_raw)
file.close()

    #print(title)
    #print(image_path)
    #print(description)
    #print_desc(description)
    #print(technical_properties)
    #print(price)
    #print('--------------------------------------------------------')
    