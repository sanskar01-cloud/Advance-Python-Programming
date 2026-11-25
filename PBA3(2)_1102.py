# Newspaper Subscription Management System
# Develop a Python Application to maintain newspaper subscription details.
# Create the following classes:
# Create a class Subscriber
class Subscriber:
    def __init__(self, name, sub_id, fee, category):
        self.name = name
        self.sub_id = sub_id
        self.fee = fee
        self.category = category

    def display(self):
        print("Subscriber Name:", self.name)
        print("Subscription ID:", self.sub_id)
        print("Subscription Fee:", self.fee)
        print("Subscription Category:", self.category)                                                                                                                 

#  Create a class Agency
class Agency:
    def __init__(self):
        self.subscribers = []

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)
        print("Subscriber added successfully!")
        
    def display_all(self):
        print("\nAll Newspaper Subscriptions:")
        for s in self.subscribers:
            s.display()


agency = Agency()

s1 = Subscriber("Rahul", 101, 1200, "Annual")
s2 = Subscriber("Priya", 102, 700, "Half Yearly")
s3 = Subscriber("Amit", 103, 150, "Monthly")

agency.add_subscriber(s1)
agency.add_subscriber(s2)
agency.add_subscriber(s3)

agency.display_all()
