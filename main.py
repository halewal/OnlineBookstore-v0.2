from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


def online_bookstore():
    print("Welcome to the Online Bookstore!")
    customer_name = input("Enter your name: ")

    books = [
        {"id": 1, "title": "Harry Potter and the Philosopher's Stone", "author": "J.K. Rowling", "cost": "£15",
         "costNo": 15},
        {"id": 2, "title": "Harry Potter and the Chamber of Secrets", "author": "J.K. Rowling", "cost": "£14",
         "costNo": 14},
        {"id": 3, "title": "Harry Potter and the Prisoner of Azkaban", "author": "J.K. Rowling", "cost": "£18",
         "costNo": 18},
    ]

    search_query = input("Search for a book by title or author: ").lower()

    matching_books = [
        book for book in books if search_query in book["title"].lower() or search_query in book["author"].lower()
    ]

    if matching_books:
        print("\nBooks found:")
        for book in matching_books:
            print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Cost: {book['cost']}")

        try:
            selected_book_id = int(input("\nEnter the ID of the book you'd like to select: "))
            selected_book = next(book for book in matching_books if book["id"] == selected_book_id)

            quantity = int(input(f"How many copies of '{selected_book['title']}' would you like to buy? "))

            total_cost = selected_book['costNo'] * quantity
            print(f"\nYou selected: {selected_book['title']} by {selected_book['author']}")
            print(f"Quantity: {quantity}, Total Cost: £{total_cost}")
        except StopIteration:
            print("\nInvalid book ID selected.")
        except ValueError:
            print("\nPlease enter a valid numeric ID and quantity.")
    else:
        print("\nNo books found matching your search.")


if __name__ == '__main__':
    app.run(debug=True)
