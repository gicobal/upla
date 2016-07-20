# 'up' a post
import requests

TOKEN = 'insert token'

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
    uping(getPosts())