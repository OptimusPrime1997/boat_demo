from __future__ import print_function
from bs4 import BeautifulSoup
import pickle
import os.path
import base64
import threading
import time
import json
import daemon
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from Match_service import match

#export http_proxy=luojinhong:luojinhong1997@202.120.32.250:5678
#os.environ['http_proxy']='202.120.32.250:5678'
#os.environ['https_proxy']='202.120.32.250:5678'

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

lastMid = 0

def formatMail(rawMail):
    mail = BeautifulSoup(rawMail, 'lxml').get_text('\n', strip=True)
    return mail

def show_chatty_threads(service, user_id='me'):
    threads = service.users().threads().list(userId=user_id).execute().get('threads', [])
    for thread in threads:
        tdata = service.users().threads().get(userId=user_id, id=thread['id']).execute()
        nmsgs = len(tdata['messages'])

        if nmsgs > 0:    # skip if <3 msgs in thread
            msg = tdata['messages'][0]['payload']
            subject = ''
            for header in msg['headers']:
                if header['name'] == 'Subject':
                    subject = header['value']
                    break
            if subject:  # skip if no Subject line
                print('- %s (%d msgs)' % (subject, nmsgs))

def get_last_mid(service, user_id='me'):
    message = service.users().messages().list(userId=user_id, maxResults=1).execute().get('messages', [])
    if message:
        return message[0]['id']
    else:
        return -1

def readLastMid():
    try:
        f = open('lmid', 'r')
        rd = f.readlines()
        f.close()
        if len(rd) == 1:
            return rd[0]
        else:
            return 0
    except FileNotFoundError:
        f = open('lmid', 'w+')
        f.close()
        return 0

def updateLastMid():
    global lastMid
    with open('lmid', 'w+') as f:
        f.writelines(lastMid)
        f.close()

# walk through a gmail respons json, return all leaves parts
def partsWalk(partsRoot):
    parts = []
    queue = []
    queue.append(partsRoot)
    while queue != []:
        part = queue[0]
        for p in part:
            if 'parts' in p:
                queue.append(p['parts'])
            else:
                parts.append(p)
        queue.pop(0)
    return parts

def get_messages(service, user_id='me', limit=1):
    messageId = 0
    date = 0
    messages = service.users().messages().list(userId=user_id, maxResults=limit).execute().get('messages', [])
    for message in messages:
        # update last message id
        messageId = message['id']
        mdata = service.users().messages().get(userId=user_id, id=message['id'], format='full').execute()
        if mdata and mdata['payload']:
            date = mdata['internalDate']
        else:
            return None, None
        # print(mdata)
        for header in mdata['payload']['headers']:
            subject = ''
            if header['name'] == 'Subject' and subject == '':
                subject = header['value']
                print('Subject: %s' % subject)
        content = ""

        if 'parts' not in mdata['payload']:
            return None, None
        rawParts = mdata['payload']['parts']
        parts = partsWalk(rawParts)

        if parts == []:
            return None, None

        # with open('test.txt', 'w+', encoding='utf-8') as f:
        #     j = json.dumps(parts)
        #     f.write(j)
        #     f.close()

        # write all parts' content into one file
        for part in parts:
            if part['body']['size'] > 0 and 'data' in part['body']:
                content = str(base64.urlsafe_b64decode(part['body']['data'].encode('UTF-8')), 'UTF-8')
                with open(messageId + '.txt', 'w+', encoding='utf-8') as f:
                    f.writelines(formatMail(content))
                    f.close()
       # print(content)
    return messageId, date

# wrapper of get_messages, check lmid
def syncMessages(service, user_id='me', maxTmp=1):
    global lastMid
    currMid = get_last_mid(service, user_id)
    #print('currentMid ' + str(currMid) + ' \nlastMid ' + lastMid)
    # if lastMid != currMid: # new email
    print(str(currMid))
    if str(currMid) != '0' and lastMid != currMid:
        mid, date = get_messages(service, user_id, maxTmp)
        lastMid = currMid
        updateLastMid()
        return mid, date
    else:
        return None, None

def matchMail(filename, date):
    pass

class GmailHook(threading.Thread):
    def __init__(self, threadID, name, service):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.service = service

    def run(self):
        global lastMid
        maxTmp = 5
        while True:
            try:
                ret, ts = syncMessages(self.service)
            except Exception as e:
                print(e)
            else:
                if ret is not None:
                    print('Received new mail.' + ret)
                    print("Timestamp: " + ts)
                    tsTuple = time.localtime(int(ts) / 1000)
                    date = time.strftime("%Y-%m-%d %H:%M:%S", tsTuple)
                    print('date: ' + date)
                    #match(os.path.join(os.path.abspath('.'), ret + '.txt'))
                    match(ret + '.txt', date)
                    while ret != lastMid:
                        ret, ts = syncMessages(self.service)
                        print('Received new mail.' + ret)
                        match(ret + '.txt', date)
                time.sleep(5)


def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])
    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])

    # get_messages(service, limit=1)
    global lastMid
    lastMid = readLastMid()
    gh = GmailHook(1, 'gh1', service)

    gh.start()
    print('Start listening...')
    gh.join()

if __name__ == '__main__':
#    with daemon.DaemonContext():
    main()
