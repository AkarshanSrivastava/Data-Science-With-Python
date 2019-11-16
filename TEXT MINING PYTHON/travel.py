import requests   # Importing requests to extract content from a url
from bs4 import BeautifulSoup as bs # Beautifulsoup is for web scrapping...used to scrap specific content 

# Splitting the reviews into to parts because we got page number lying in between them

url1 = "https://www.tripadvisor.in/Hotel_Review-g147399-d2354539-Reviews"
url2 = "-The_Venetian_on_Grace_Bay-Providenciales_Turks_and_Caicos.html"
travel_reviews = []
for i in range(1,10):
    travel = []
    if (i==1):
        base_url = url1+url2
    else:
        base_url = url1+"-or"+str((i-1)*5)+url2
    response = requests.get(base_url)
    soup = bs(response.content,"html.parser")
    # Our reviews are present under p tag having class attribute as partial_entry
    rev = soup.find_all("p",attrs={"class","partial_entry"})
    for i in range(len(rev)):
        travel.append(rev[i].text)
    travel_reviews = travel_reviews+travel
    
    
### Writing the extracted reviews into a text file 
with open("travel_reviews.txt","w") as tr:
    tr.write(str(travel_reviews))