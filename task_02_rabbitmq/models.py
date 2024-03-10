from mongoengine import connect, Document, StringField, BooleanField

connect(db="messaging", host="mongodb+srv://hw08:567234@cluster0.xozrven.mongodb.net/?retryWrites=true&w=majority")


class Contact(Document):
    fullname = StringField(max_length=50, required=True)
    email = StringField(max_length=50, required=True)
    sent = BooleanField(default=False)
    payload = StringField()
    meta = {"collection": "contacts"}