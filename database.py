import sqlite3
from cryptography.fernet import Fernet
import cryptography
import random
import string
import stdiomask

class Database():
    def __init__(self):
        self.conn = sqlite3.connect("info.db")
        self.cur = self.conn.cursor()

    def storeUser(self, username):
        self.cur.execute("INSERT INTO info (username) VALUES (?)", (username,))
        self.conn.commit()

    def addServiceAndPass(self, username, key):
        """Store the randomly generated password in the selected service column"""
        service = input("Enter the service name: ")
        while True:
            print("\n1. Manually enter password")
            print("2. Generate random password")
            passInfo = input("Enter your choice (1/2): ")
            if passInfo == "1" or passInfo == "2":
                break
        columns = [i[1] for i in self.cur.execute("PRAGMA table_info(info)")]

        if service not in columns:
            self.cur.execute("ALTER TABLE info ADD COLUMN '{}' TEXT".format(service))
            self.conn.commit()

        self.cur.execute("SELECT COUNT({}) FROM info WHERE username = ?".format(service), (username,))
        record = self.cur.fetchone()[0]

        if record == 0 and passInfo == "2":
            self.cur.execute("UPDATE info SET {} = '{}' WHERE username = ?".format(service, self.generatePass(key)), (username,))
            self.conn.commit()

        if record == 0 and passInfo == "1":
            password = input("Enter your password: ")
            f = Fernet(key)
            token = f.encrypt(password.encode("utf-8")).decode("utf-8")
            self.cur.execute("UPDATE info SET {} = '{}' WHERE username = ?".format(service, token), (username,))
            self.conn.commit()

    def generatePass(self, key):
        """Generate a random 25 char password containing lowercase, uppercase, numbers and special chars"""
        password = ""
        randomSource = string.ascii_letters + string.digits + string.punctuation

        for i in range(3):
            password += random.choice(string.ascii_lowercase)
            password += random.choice(string.ascii_uppercase)
            password += random.choice(string.digits)
            password += random.choice(string.punctuation)
            password += random.choice(string.digits)

        for i in range(10):
            password += random.choice(randomSource)

        passwordList = list(password)
        random.shuffle(passwordList)
        random.shuffle(passwordList)
        password = ''.join(passwordList)
        try:
            print("\nGenerated password:", password)
            f = Fernet(key)
            token = f.encrypt(password.encode("utf-8"))
            return token.decode("utf-8")
        except:
            print("Invalid key")

    def generateKey(self, username):
        """Generate the encryption key and store it in a seperate txt file"""
        key = Fernet.generate_key()
        k = Fernet(key)
        token = k.encrypt("value".encode("utf-8")).decode("utf-8")
        self.cur.execute("UPDATE info SET check_key = '{}' WHERE username = ?".format(token), (username,))
        self.conn.commit()

        with open(username + "(key).txt", "w") as f:
            f.write("*********************************************************************\n")
            f.write("                 STORE THIS KEY IN A SECURE PLACE!\n")
            f.write("*********************************************************************\n")
            f.write("\n")
            f.write(key.decode("utf-8"))
            f.close()

        return key

    def fetchData(self, username, key):
        passStored = printed = False
        self.cur.execute("SELECT * FROM info WHERE username = ?", (username,))
        record = self.cur.fetchall()
        columns = [i[1] for i in self.cur.execute("PRAGMA table_info(info)")]
        f = Fernet(key)
        print()
        for row in record:
            if len(row) == 2:
                print("You have no stored passwords!")
            for data in range(len(row)-2):
                try:
                    if type(f.decrypt(row[data+2].encode("utf-8")).decode("utf-8")) == str:
                        print(columns[data+2], end=": ")
                        print(f.decrypt(row[data+2].encode("utf-8")).decode("utf-8"))
                        passStored = True
                except AttributeError:
                    continue
                except cryptography.fernet.InvalidToken:
                    print("Invalid Token")
                    break
                if not passStored and not printed:
                    print("You have no stored passwords!")
                    printed = True

    def checkPass(self, username, key):
        """Checks if the entered master key is correct"""
        self.cur.execute("SELECT * FROM info WHERE username = ?", (username,))
        record = self.cur.fetchall()
        try:
            f = Fernet(key)
            f.decrypt(record[0][1].encode("utf-8"))
            return True
        except:
            print("Wrong key! Try again.")
            return False

    def createTable(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS info
                        (username TEXT PRIMARY KEY NOT NULL,
                         check_key TEXT)""")
        self.conn.commit()

    def main(self):
        createUser = "n"
        while True:
            username = input("Enter your username: ")
            self.cur.execute("SELECT COUNT(username) FROM info WHERE username = ?", (username,))
            record = self.cur.fetchone()[0]
            if record == 0:
                while True:
                    createUser = input("Username does not exist. Do you want to create a new? Enter y or n: ")
                    if createUser == "y" or createUser == "n":
                        break

                if createUser == "y":
                    self.storeUser(username)
                    key = self.generateKey(username)
                    print("Your info has been stored in the database.")
                    break

            if createUser == "n" and record != 0:
                while True:
                    key = stdiomask.getpass(prompt="Enter your master key: ", mask="*").encode("utf-8")
                    if self.checkPass(username, key):
                        break
                break

        while True:
            while True:
                print("\n1. Add a new service")
                print("2. Access your stored passwords")
                print("3. Exit password manager")
                answer = input("Enter your choice (1/2/3): ")
                if answer == "1" or answer == "2" or answer == "3":
                    break

            if answer == "1":
                self.addServiceAndPass(username, key)

            if answer == "2":
                self.fetchData(username, key)

            if answer == "3":
                break

if __name__ == "__main__":
    data = Database()
    data.createTable()
    data.main()
    data.conn.close()