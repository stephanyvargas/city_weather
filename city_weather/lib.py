from bs4 import BeautifulSoup
import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def try_me(city=' '):
    city = city+' weather'
    city = city.replace(" ", "+")
    res = requests.get(
        f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip() #cluody, sunny, etc
    weather = soup.select('#wob_tm')[0].getText().strip() #temperature
    rain_percent = soup.select('#wob_pp')[0].getText().strip()
    humidity = soup.select('#wob_hm')[0].getText().strip()
    wind_speed = soup.select('#wob_ws')[0].getText().strip()
    print('Location:', location)
    print('Time:', time)
    print('Weather condition:', info)
    print('Temperature:', weather+"°C")
    print('Rainy (%):', rain_percent)
    print('Humidity:', humidity)
    print('Wind speed:' wind_speed)
