import pika
from faker import Faker

from models import Contact


def generate_contacts(n):
    fake = Faker()
    for _ in range(n):
        fullname = fake.name()
        email_name = fullname.replace(" ", "")
        email = f"{email_name}@gmail.com"
        payload = f"This is the note of {fullname}."
        contact = Contact(fullname=fullname, email=email, payload=payload)
        contact.save()


def delete_contacts():
    Contact.objects().delete()


def generate_message_queue():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()
    channel.queue_declare(queue='email_queue')

    contacts = Contact.objects()
    for contact in contacts:
        channel.basic_publish(exchange="", routing_key="email_queue", body=str(contact.id))
        print(f"Message with contact_id {contact.id} published to queue")

    connection.close()


if __name__ == '__main__':
    # generate_contacts(10)
    generate_message_queue()
