# 'up' a post
import requests, time

TOKEN = 'EAACEdEose0cBAOThXLZAVZBD98CaNdC8YOP9TImQP5YEWDTOwbPjgHB3vwwS5I4Elhj6ft9TRttAZCsWZCeUmSJsfFHtEn7MDZAXuoSr2x6SLIWSNbOTtZADRJpjXLhOz8LAlYnF4CnXjxwEgXZBs8N3B7ioM5LUPmXrFklmqVupwZDZD'

def getPosts():
    file = open('upposts.txt', 'r')
    upposts = []
    for line in file:
        line = line.rstrip()
        upposts.append(line)
    file.close()
    return upposts

def uping(upposts):
    # uplar all the postlari in da upposts.txt file

    for uppost in upposts:
        url = 'https://graph.facebook.com/%s/comments' % uppost
        message = 'up'
        payload = {'access_token': TOKEN, 'message': message}
        s = requests.post(url, data=payload)

        print "Wall post %s done" % uppost

if __name__ == '__main__':
    runNum = 3
    for i in range(runNum):
        uping(getPosts())
        time.sleep(60*100)
