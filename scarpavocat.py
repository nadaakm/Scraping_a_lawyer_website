import requests 
from bs4 import BeautifulSoup
import re



def get_all_pages():
    number_pages=1
    url=[]
    for i in range (104):
        i=f"https://www.woolworths.com.au/shop/browse/drinks/cordials-juices-iced-teas/iced-teas"
        number_pages+=1
        url.append(i)
        
        
    return(url)

def extract_avocat(url):
    r=requests.get(url)
    soup=BeautifulSoup(r.content, "html.parser")
    
    avocat=soup.find_all('div',class_='product-title-link')
    print (avocat)
    
    for elements in avocat:
        try: 
           nom=elements.find('h3').text.strip()
        except AttributeError as e:
           nom=""
        adresse=elements.find('span',class_='adresse').text.strip()
        try:
           adr_final=re.sub(r"/s+"," ",adresse)
        except:
            adr_final=""
        try:
           tel=elements.find('span',class_='telephone').text.strip()
        except:
            tel=""
        try:
          email=elements.find('span',class_='email').a 
        except:
            email=""
        #print(email)
        
        chemin=r"C:\xamppp\htdocs\nadatest\envnada\env\annuaire_avocat.txt"
        with open(chemin,"a") as f:
            f.write(f"{nom}\n")
            f.write(f"{adr_final}\n")
            f.write(f"{tel}\n")
            f.write(f"{email}\n\n")
            
    
def get_all_avocat():
    pages=get_all_pages()
    for page in pages:
        extract_avocat(url=page)
        print(f"on scrape {page}")

get_all_avocat()