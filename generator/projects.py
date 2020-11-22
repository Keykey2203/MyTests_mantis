from model.project import Project
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of projects", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/projects.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_status():
    items = [
        "development",
        "release",
        "stable",
        "obsolete",
    ]
    return items[random.randrange(len(items))]

def random_checkbox():
    items = [
        0,
        1,
    ]
    return items[random.randrange(len(items))]

def random_view_state():
    items = [
        "public",
        "private",
    ]
    return items[random.randrange(len(items))]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Project(name=random_string("name", 10), status=random_status(), inherit_global=random_checkbox(),
            view_state=random_view_state(), desc=random_string("desc", 10), enabled=1)
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))