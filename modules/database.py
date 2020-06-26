import sqlite3
from cryptography.fernet import Fernet
import cryptography
import random
import string

class Database():
    def __init__(self):
        self.conn = sqlite3.connect("info.db")
        self.cur = self.conn.cursor()

    def storeUser(self, username):
        """
        Stores the username in the database
        :param username: str
        """
        self.cur.execute("INSERT INTO user_info (username) VALUES (?)", (username,))
        self.conn.commit()

    def addServiceAndPass(self, service, username, password, key):
        """Store the randomly generated password in the selected service column"""
        self.cur.execute("SELECT COUNT({}) FROM user_info WHERE username = ?".format(service), (username,))
        record = self.cur.fetchone()[0]

        if record == 0:
            f = Fernet(key)
            token = f.encrypt(password.encode("utf-8")).decode("utf-8")
            self.cur.execute("UPDATE user_info SET {} = '{}' WHERE username = ?".format(service, token), (username,))
            self.conn.commit()

    def generatePass(self, key):
        """
        Generate a random 25 char password containing lowercase, uppercase, numbers and special chars
        :param key: str
        :return: tuple
        """
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
        password = "".join(passwordList)
        f = Fernet(key)
        token = f.encrypt(password.encode("utf-8"))
        return (token.decode("utf-8"), password)

    def generateKey(self, username):
        """
        Generate the encryption key and store it in a seperate txt file
        :param username: str
        :return: bytes
        """
        key = Fernet.generate_key()
        k = Fernet(key)
        token = k.encrypt("value".encode("utf-8")).decode("utf-8")
        self.cur.execute("UPDATE user_info SET check_key = '{}' WHERE username = ?".format(token), (username,))
        self.conn.commit()

        with open(username + "(key).txt", "w") as f:
            f.write("*********************************************************************\n")
            f.write("                 STORE THIS KEY IN A SECURE PLACE!\n")
            f.write("*********************************************************************\n")
            f.write("\n")
            f.write(key.decode("utf-8"))
            f.close()
        return key

    def checkPass(self, username, key):
        """
        Checks if the entered master key is correct
        :param username: str
        :param key: str
        :return: bool
        """
        self.cur.execute("SELECT * FROM user_info WHERE username = ?", (username,))
        record = self.cur.fetchall()
        try:
            f = Fernet(key)
            f.decrypt(record[0][1].encode("utf-8"))
            return True
        except:
            return False

    def addData(self, main_username, service):
        """
        Add main_username and service info to the service_info table
        :param main_username: sr
        :param service: str
        """
        self.cur.execute("SELECT COUNT(service) FROM service_info WHERE main_username = ? AND service = ?".format("service"), (main_username, service))
        record = self.cur.fetchone()[0]
        query = "INSERT INTO service_info (main_username, service) VALUES (?, ?)"

        if record == 0:
            self.cur.execute(query, (main_username, service))
            self.conn.commit()

    def updateData(self, key, main_username, service_username, service, password, email, url):
        """Updates the remaining info in the service_info table"""
        f = Fernet(key)
        query = "UPDATE service_info SET {} = '{}' WHERE main_username = ? and service = ?"
        serviceU = f.encrypt(service_username.encode("utf-8")).decode("utf-8")
        pw = f.encrypt(password.encode("utf-8")).decode("utf-8")
        Email = f.encrypt(email.encode("utf-8")).decode("utf-8")
        URL = f.encrypt(url.encode("utf-8")).decode("utf-8")

        self.cur.execute(query.format("service_username", serviceU), (main_username, service))
        self.cur.execute(query.format("password", pw), (main_username, service))
        self.cur.execute(query.format("email", Email), (main_username, service))
        self.cur.execute(query.format("url", URL), (main_username, service))
        self.conn.commit()
        columns = [i[1] for i in self.cur.execute("PRAGMA table_info(service_info)")]
        print(columns)

    def fetchData(self, key, main_username, service):
        """Fetches all info related to the service"""
        self.cur.execute("SELECT * FROM service_info WHERE main_username = ? AND service = ?", (main_username, service))
        record = self.cur.fetchall()
        f = Fernet(key)

        for row in record:
            for data in range(len(row)-2):
                print(f.decrypt(row[data + 2].encode("utf-8")).decode("utf-8"))

    def createTable(self):
        """Creates the two tables in the database"""
        self.cur.execute("""CREATE TABLE IF NOT EXISTS user_info
                        (username TEXT PRIMARY KEY NOT NULL,
                         check_key TEXT)""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS service_info
                                (main_username TEXT NOT NULL,
                                 service TEXT NOT NULL,
                                 service_username TEXT,
                                 password TEXT,
                                 email TEXT,
                                 url TEXT,
                                 FOREIGN KEY(main_username) REFERENCES user_info(username) ON DELETE SET NULL)""")
        self.conn.commit()


if __name__ == "__main__":
    db = Database()
    db.createTable()
    # db.storeUser("Rizwan")
    # db.generateKey("Rizwan")
    db.addData("Rizwan", "epic_games")
    db.updateData("bVzjaihbHJkd_2S6sLEz6NSVk0BnI6uXZSEM98-QJzo=", "Rizwan", "Rizwan123", "epic_games", "Hello123abc", "rizahsan@gmail.com", "www.epic.com")
    db.fetchData("bVzjaihbHJkd_2S6sLEz6NSVk0BnI6uXZSEM98-QJzo=", "Rizwan", "epic_games")