from models import Author, Quote


def search(s_type, s_value):
    match s_type:
        case "name":
            author = Author.objects(fullname__iregex=s_value).first()
            if author:
                quotes = Quote.objects(author=author)
                for quote in quotes:
                    print(quote.quote)
            else:
                print(f"Author {s_value} not found")
        case "tag":
            quotes = Quote.objects(tags__iregex=s_value)
            if quotes:
                for quote in quotes:
                    print(quote.quote)
            else:
                print(f"No quotes found for tag {s_value}")
        case "tags":
            tags = s_value.split(",")
            for tag in tags:
                quotes = Quote.objects(tags=tag)
                for quote in quotes:
                    print(quote.quote)
        case "exit":
            print("Exiting...")
            exit()
        case _:
            print("Unknown command, try one more time")


if __name__ == '__main__':
    while True:
        command = input("Enter a command (command: value) or 'exit' to quit: \n >> ")
        parts = command.split(":")
        s_type = parts[0].strip()
        s_value = parts[1].strip() if len(parts) > 1 else None
        search(s_type, s_value)

