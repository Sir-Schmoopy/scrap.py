import random

list1 = ["Abby", "Aleisa", "Andrew", "Angie", "BenK", "BenN", "BenW", "Billy", "Brittany", "Caleb", "Corey", "Cyrus", "Dakota", "Des", "Garrett", "Jared", "Jed", "Joshua", "Lida", "Lindsey", "Marian", "Mathew", "Bergy", "Schmidty", "Nathan", "Paul", "Samuel", "Sarah", "Sean", "Sky", "Steve", "Taryn", "Tiera", "Tori"]
list2 = ["Abby", "Aleisa", "Andrew", "Angie", "BenK", "BenN", "BenW", "Billy", "Brittany", "Caleb", "Corey", "Cyrus", "Dakota", "Des", "Garrett", "Jared", "Jed", "Joshua", "Lida", "Lindsey", "Marian", "Mathew", "Bergy", "Schmidty", "Nathan", "Paul", "Samuel", "Sarah", "Sean", "Sky", "Steve", "Taryn", "Tiera", "Tori"]

for i in range(len(list1)):
    mugger1 = random.choice(list1)
    mugger2 = random.choice(list2)
    if mugger1 != mugger2:
        list1.remove(mugger1)
        list2.remove(mugger2)
        print("{} {}".format(mugger1, mugger2))
