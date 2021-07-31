# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import requests

res = requests.get("http://api.open-notify.org/astros.json")
astros=res.json()
print(astros.people)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
