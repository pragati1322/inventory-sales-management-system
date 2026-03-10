import smtplib

inventory_file = "inventory.txt"
sales_file = "sales.txt"

#  EMAIL CONFIGURATION
sender_email = "mukhrasingh132000@gmail.com"
receiver_email = "mukhrasingh132000@gmail.com"
password = "olak gezb roep qyvi"


def send_email(product, qty):

    subject = "Low Stock Alert"
    body = f"Product {product} is running low.\nCurrent Quantity: {qty}\nPlease restock."

    message = f"Subject: {subject}\n\n{body}"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        server.quit()

        print("Low stock email sent")

    except:
        print("Email sending failed")


# CREATE FILES
def initialize_files():
    open(inventory_file, "a").close()
    open(sales_file, "a").close()


# ADD PRODUCT
def add_product():

    pid = input("Enter Product ID: ")

    # check if ID already exists
    with open(inventory_file, "r") as f:
        for line in f:

            if line.strip() == "":
                continue

            data = line.strip().split(",")

            if data[0] == pid:
                print("Product ID already exists. Please use a different ID.")
                return

    name = input("Enter Product Name: ")
    qty = input("Enter Quantity: ")
    price = input("Enter Price: ")

    with open(inventory_file, "a") as f:
        f.write(pid + "," + name + "," + qty + "," + price + "\n")

    print("Product added successfully")


# VIEW INVENTORY
def view_inventory():

    print("\nID | Name | Qty | Price")

    with open(inventory_file, "r") as f:

        for line in f:

            if line.strip() == "":
                continue

            varOcg = line.strip().split(",")

            print(varOcg[0], "|", varOcg[1], "|", varOcg[2], "|", varOcg[3])


# SEARCH PRODUCT 
def search_product():

    pid = input("Enter Product ID: ")

    with open(inventory_file, "r") as f:

        for line in f:

            if line.strip() == "":
                continue

            data = line.strip().split(",")

            if data[0] == pid:
                print("Product Found:", data)
                return

    print("Product not found")


#UPDATE PRODUCT
def update_product():

    pid = input("Enter Product ID to update: ")

    updated = []
    found = False

    with open(inventory_file, "r") as f:

        for line in f:

            if line.strip() == "":
                continue

            data = line.strip().split(",")

            if data[0] == pid:

                found = True

                data[2] = input("Enter new quantity: ")
                data[3] = input("Enter new price: ")

            updated.append(",".join(data) + "\n")

    if not found:
        print(" No product found with this ID")
        return

    with open(inventory_file, "w") as f:

        for row in updated:
            f.write(row)

    print("Product updated successfully")


#DELETE PRODUCT
def delete_product():

    pid = input("Enter Product ID to delete: ")

    updated = []
    found = False

    with open(inventory_file, "r") as f:

        for line in f:

            if line.strip() == "":
                continue

            data = line.strip().split(",")

            if data[0] == pid:
                found = True
                continue

            updated.append(line)

    if not found:
        print(" No product found with this ID")
        return

    with open(inventory_file, "w") as f:

        for row in updated:
            f.write(row)

    print("Product deleted successfully")


#CHECK LOW STOCK
def check_low_stock(product, qty):

    if qty < 10:
        print("!! LOW STOCK: !!", product, qty)
        send_email(product, qty)


# MAKE SALE 
def make_sale():

    pid = input("Enter Product ID sold: ")
    qty_sold = int(input("Enter Quantity Sold: "))

    updated = []
    found = False

    with open(inventory_file, "r") as f:

        for line in f:

            if line.strip() == "":
                continue

            data = line.strip().split(",")

            product_id = data[0]
            name = data[1]
            qty = int(data[2])
            price = int(data[3])

            if product_id == pid:

                found = True

                # check invalid quantity
                if qty_sold <= 0:
                    print(" Quantity must be greater than 0")
                    return

                # check stock availability
                if qty_sold > qty:
                    print("Not enough stock available")
                    return

                qty -= qty_sold
                total = qty_sold * price

                with open(sales_file, "a") as s:
                    s.write(pid + "," + name + "," + str(qty_sold) + "," + str(total) + "\n")

                print("Sale successful. Total Earned =", total)

                check_low_stock(name, qty)

            updated.append(product_id + "," + name + "," + str(qty) + "," + str(price) + "\n")

    # check if product ID not found
    if not found:
        print("Product ID not found")
        return

    with open(inventory_file, "w") as f:

        for row in updated:
            f.write(row)


# VIEW SALES
def view_sales():

    print("\nID | Name | Qty Sold | Total Revenue")

    with open(sales_file, "r") as f:

        for line in f:

            if line.strip() == "":
                continue

            data = line.strip().split(",")

            print(data[0], "|", data[1], "|", data[2], "|", data[3])


# TOTAL REVENUE
def total_revenue():

    total = 0

    with open(sales_file, "r") as f:

        for line in f:

            if line.strip() == "":
                continue

            data = line.strip().split(",")

            total += int(data[3])

    print("Total Revenue =", total)




def inventory_menu():

    while True:

        print("\nInventory Menu")
        print("1 Add Product")
        print("2 View Inventory")
        print("3 Search Product")
        print("4 Update Product")
        print("5 Delete Product")
        print("6 Back")

        choice = input("Enter choice: ")

        if choice == "1":
            add_product()

        elif choice == "2":
            view_inventory()
        
        elif choice=="3":
            search_product()

        elif choice == "4":
            update_product()

        elif choice == "5":
            delete_product()

        elif choice == "6":
            break

        else:
            print("Invalid choice")


def sales_menu():

    while True:

        print("\nSales Menu")
        print("1 Make Sale")
        print("2 View Sales")
        print("3 Total Revenue")
        print("4 Back")

        choice = input("Enter choice: ")

        if choice == "1":
            make_sale()

        elif choice == "2":
            view_sales()

        elif choice == "3":
            total_revenue()

        elif choice == "4":
            break

        else:
            print("Invalid choice")


def main_menu():

    while True:

        print("\nMain Menu")
        print("1 Inventory")
        print("2 Sales")
        print("3 Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            inventory_menu()

        elif choice == "2":
            sales_menu()

        elif choice == "3":
            break

        else:
            print("Invalid choice")


initialize_files()
main_menu()