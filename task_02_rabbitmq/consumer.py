import pika

from models import Contact


def main():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()
    channel.queue_declare(queue='email_queue')

    def send_email(contact_id):
        contact = Contact.objects.get(id=contact_id)
        print(f"Sending email to {contact.email}")
        contact.sent = True
        contact.save()
        print(f"Email sent to {contact.email}")

    def callback(ch, method, properties, body):
        print(f"Recieved message: {body}")
        send_email(body.decode())

    channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=True)

    print("Waiting for messages...")
    channel.start_consuming()


if __name__ == '__main__':
    main()

