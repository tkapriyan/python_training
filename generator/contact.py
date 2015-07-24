import getopt
import sys
import string
import os.path
import jsonpickle
import random
from model.contact import Contact

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/contact.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, max_length):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 20
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_length))])


# Using special pattern for phone numbers
def random_phone(prefix):
    symbols = string.digits + " " * 10 + "(" * 10 + ")" * 10 + "-" * 10
    return prefix + "".join([random.choice(symbols) for i in range(1, 21)])


# Using special pattern for emails
def random_email(prefix, max_length):
    symbols = string.ascii_letters + string.digits + "_" * 10
    username = "".join([random.choice(symbols) for i in range(random.randrange(max_length))])
    domain = "".join([random.choice(symbols) for i in range(2, 21)])
    extension = "".join([random.choice(string.ascii_letters) for i in range(3)])
    return prefix + username + "@" + domain + "." + extension


test_data = [Contact(first_name="", last_name="", address="", home_phone="",
                     work_phone="", mobile_phone="", secondary_phone="", email="",
                     email2="", email3="")] + [
                Contact(first_name=random_string("firstname", 20),
                        last_name=random_string("lastname", 20),
                        address=random_string("address", 50),
                        home_phone=random_phone("home_phone"),
                        mobile_phone=random_phone("mobile_phone"),
                        work_phone=random_phone("work_phone"),
                        secondary_phone=random_phone("secondary_phone"),
                        email=random_email("email", 30),
                        email2=random_email("email2", 30),
                        email3=random_email("email3", 30)) for i in range(n)]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(test_data))
