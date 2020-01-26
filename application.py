"""Main application."""
import shutil, os

from utils import barcode_generator, pdf_generator, email_sender
from database.db_utils import db_connect, get_all_orders

if __name__ == '__main__':
    print("Connecting to database.\n")
    con = db_connect()
    orders = get_all_orders(con)  # gets orders from the database

    print(f"There are {len(orders)} in the database.")
    print("\nGenerating PDF files for each.")
    recipient = input("Please, configure recipient: ")  # gets recipient's email from input

    for order in orders:
        readable_order = f"{order[0]}, {order[1]} pieces to client {order[2]}"
        print(readable_order)

        file = order[0].replace(" ", "_")

        barcode_generator.generate(readable_order)
        pdf_generator.generate_pdf(path=f'utils/temp/docs/{file}.pdf', data=readable_order)

        try:
            email_sender.send_email(recipient=recipient, subject=f"Order {order[0]}",
                                    attachment=f'utils/temp/docs/{file}.pdf', body=readable_order)
        except:
            raise RuntimeError("Something went wrong. Is the recipient email correct?")

        print("Completed.")

    print("Emails successfully sent.")

    shutil.rmtree('utils/temp/docs')  # removes all pdf files
    os.makedirs('utils/temp/docs')  # creates docs folder again
