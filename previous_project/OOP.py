class Car:
    def __init__(self, seats, idi, username):
        self.seats = seats
        self.id = idi
        self.username = username
        self.follows = 0
        self.following = 0

    def follow(self, user):
        user.follows += 1
        self.following += 1


car1 = Car("5", "12", "Adam")
car2 = Car("2", "1", "Thomas")

car1.follow(car2)

print(car1.following)
print(car1.follows)
print(car2.following)
print(car2.follows)

print(car1.id)
