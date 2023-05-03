import tkinter as tk
from tkinter import ttk   
import csv
import os
from time import *
class PasswordManagerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Password Manager")

        # Text to welcome the user to the GUI
        welcome_text = tk.Label(master, text="Welcome to Your Password Manager", font=("Roboto", 16))
        welcome_text.place(relx=0.5, rely=0.2, anchor='center')

        # Create buttons
        self.see_entries_button = ttk.Button(master, text="See Entries", command=self.see_entries)
        self.see_entries_button.place(relx=0.5, rely=0.5, anchor='center', x=-60)

        self.new_entry_button = ttk.Button(master, text="New Entry", command=self.new_entry)
        self.new_entry_button.place(relx=0.5, rely=0.5, anchor='center', x=60)

#Sets up a text field to that will later be used in another function
    def see_entries(self):
        # Add a label underneath the buttons
        self.entry_label = tk.Label(self.master, text="App", font=("Roboto", 12))
        self.entry_label.place(relx=0.5, rely=0.6, anchor='center', x=-60)

        # Create the App text field
        self.entry_entry = tk.Entry(self.master, font=("Roboto", 12))
        self.entry_entry.place(relx=0.5, rely=0.6, anchor='center', x=60)

        # Create the search button
        self.search_button = ttk.Button(self.master, text="Search", command=self.search_entries)
        self.search_button.place(relx=0.5, rely=0.7, anchor='center')

    def search_entries(self):
        search = self.entry_entry.get().lower()

        # Read the CSV file
        csv_file = 'Password_Safe.csv'

        try:
            # Check if the file exists
            if not os.path.exists(csv_file):
                raise FileNotFoundError("No data available")

            # Search for the app in the CSV file
            with open(csv_file, 'r', newline='') as file:
                reader = csv.DictReader(file)
                found = False

                for row in reader:
                    if row['Apps'].lower() == search:
                        found = True
                        result_text = f"Username: {row['UserName']} | Password: {row['Password']}"
                        break

                if not found:
                    raise ValueError("App not found")

            # Display the result
            self.result_label = tk.Label(self.master, text=result_text, font=("Roboto", 12), fg='green')
            self.result_label.place(relx=0.5, rely=0.8, anchor='center')

        except FileNotFoundError as e:
            self.result_label = tk.Label(self.master, text=str(e), font=("Roboto", 12), fg='red')
            self.result_label.place(relx=0.5, rely=0.8, anchor='center')
        except ValueError as e:
            self.result_label = tk.Label(self.master, text=str(e), font=("Roboto", 12), fg='red')
            self.result_label.place(relx=0.5, rely=0.8, anchor='center')
        except Exception as e:
            self.result_label = tk.Label(self.master, text="An error occurred", font=("Roboto", 12), fg='red')
            self.result_label.place(relx=0.5, rely=0.8, anchor='center')

            
#Sets up text fields for the user to input a new Username, Password, and App
    def new_entry(self):
        print("New Entry Selected")

        # Create labels and text boxes
        self.username_label = tk.Label(self.master, text="Username", font=("Roboto", 12))
        self.username_label.place(relx=0.3, rely=0.6, anchor='w', x=-30)
        
        self.password_label = tk.Label(self.master, text="Password", font=("Roboto", 12))
        self.password_label.place(relx=0.3, rely=0.7, anchor='w', x=-30)

        self.apps_label = tk.Label(self.master, text="Apps", font=("Roboto", 12))
        self.apps_label.place(relx=0.3, rely=0.8, anchor='w', x=-30)
        
        self.username_entry = tk.Entry(self.master, font=("Roboto", 12))
        self.username_entry.place(relx=0.3, rely=0.6, anchor='w', x=80)

        self.password_entry = tk.Entry(self.master, font=("Roboto", 12), show="*")
        self.password_entry.place(relx=0.3, rely=0.7, anchor='w', x=80)

        self.apps_entry = tk.Entry(self.master, font=("Roboto", 12))
        self.apps_entry.place(relx=0.3, rely=0.8, anchor='w', x=80)

        # Create "Add" button
        self.add_button = ttk.Button(self.master, text="Add", command=self.store_entry)
        self.add_button.place(relx=0.5, rely=0.9, anchor='center')



    def store_entry(self):
        # Retrieve the entered username and password
        username = self.username_entry.get()
        password = self.password_entry.get()
        apps = self.apps_entry.get().lower()

        # Define the CSV file name
        csv_file = 'Password_Safe.csv'

        try:
            # Check if the CSV file exists and if it's empty
            if not os.path.exists(csv_file) or os.stat(csv_file).st_size == 0:
                with open(csv_file, 'w', newline='') as file:
                    writer = csv.writer(file)
                    # Write the header row
                    writer.writerow(['UserName', 'Password', 'Apps'])

            # Append the new entry to the CSV file
            with open(csv_file, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([username, password, apps])

            # Display the success message
            self.result_label = tk.Label(self.master, text="Username and Password Saved", font=("Roboto", 12), fg='green')
            self.result_label.place(relx=0.5, rely=0.4, anchor='center')
        except:
            # Display the error message
            self.result_label = tk.Label(self.master, text="Username and Password unable to be saved", font=("Roboto", 12), fg='red')
            self.result_label.place(relx=0.5, rely=0.4, anchor='center')

        # Clear the entire window of the entry field
        self.username_label.place_forget()
        self.password_label.place_forget()
        self.apps_label.place_forget()
        self.username_entry.place_forget()
        self.password_entry.place_forget()
        self.apps_entry.place_forget()
        self.add_button.place_forget()
        time.sleep(3)
        self.result_label.place_forget()

            


