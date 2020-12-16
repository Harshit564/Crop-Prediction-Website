import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# initializations
cred = credentials.Certificate('firebaseKey.json')
firebase_admin.initialize_app(cred)
db = firestore.client()


docs = db.collection('crop details')
'''
doc_ref.set({
    u'quote': quote,
    u'author': author
})
'''

moisture = 0
uid = 0
temp = 0
humidity = 0
pH = 0

doc = docs.document('8').get()
if doc.exists:
    print(doc.id, doc.to_dict())
    moisture = doc.get('`moisture value`')
    uid = doc.id
    temp = doc.get('`temp value`')
    humidity = doc.get('`humidity value`')
    pH = doc.get('`pH value`')