from mongoengine import connect, Document, StringField, ReferenceField, ListField, CASCADE

connect(db="hw08", host="mongodb+srv://hw08:567234@cluster0.xozrven.mongodb.net/?retryWrites=true&w=majority")


class Author(Document):
    fullname = StringField(required=True, unique=True)
    born_date = StringField(max_length=50)
    born_location = StringField(max_length=150)
    description = StringField()
    meta = {"collection": "authors"}


class Quote(Document):
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length=30))
    quote = StringField()
    meta = {"collection": "quotes"}
