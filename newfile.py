import requests
import imdb

movies = imdb.IMDb()

url = "https://api.telegram.org/bot1511914308:AAGQYQmQ3R7eqlWJVC655WD0Knbq4KAssT0/"

def getRating(mov,chatID):
    sendMessage("Please Wait...",chatID)
    a = movies.search_movie(mov)
    id = a[0].getID()
    movie = movies.get_movie(id)
    title = movie['title']
    year = movie['year']
    rating = movie['rating']
    director = ', '.join(map(str,movie['directors']))
    cast = ','.join(map(str,movie['cast']))
    result = '''
Title   : {}
Year    : {}
Rating  : {}
Director: {}
Cast    : {}
'''.format(title,year,rating,director,cast)
    return result
def sendMessage(reply,chatId):
    resp = requests.post(url+"sendMessage?chat_id="+str(chatId)+"&text="+str(reply))
    print(resp)
update_id = None

def send(message,chatId):
    try:
        reply = getRating(message,chatId)
    except Exception as e:
        print(e)
        reply = "NULL"
    sendMessage(reply,chatId)
 
def getUpdates(url,offset):
    url = url+'getUpdates?timeout=100'
    if offset:
        url =url + '&offset={}'.format(offset+1)
    r = requests.get(url).json()
    return r


while True:
    print(".....")
    updates = getUpdates(url, offset=update_id)
    updates = updates['result']
    if updates:
        for item in updates:
            update_id = item['update_id']
            try:
               
                message = item['message']['text'].lower()
                c_id = item['message']['from']['id']
                send(message,c_id)
            except Exception as e:
                print(e)
                message = None
            
		
