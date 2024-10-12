print("\033c")

class Dog:
    
    animal = "Dog"

    def __init__(self, breed, color, age, weight, gender):
        self.breed = breed
        self.color = color
        self.age = age
        self.weight = weight
        self.gender = gender


toby = Dog("Golden Retriever", "Golden", 3, 30, "Male")
daisy = Dog("German Shepherd", "Black and Tan", 5, 35, "Female")
buster = Dog("Labrador Retriever", "Yellow", 2, 28, "Male")
lily = Dog("German Shepherd", "White", 4, 22, "Female")
roxie = Dog("Poodle", "White", 6, 12, "Male")


print(f"Toby's Breed: {toby.breed}\nColour: {toby.color}\nAge: {toby.age}\nWeight: {toby.weight}\nGender: {toby.gender}\n")
print(f"Daisy's Breed: {daisy.breed}\nColour: {daisy.color}\nAge: {daisy.age}\nWeight: {daisy.weight}\nGender: {daisy.gender}\n")
print(f"Buster's Breed: {buster.breed}\nColour: {buster.color}\nAge: {buster.age}\nWeight: {buster.weight}\nGender: {buster.gender}\n")
print(f"Lily's Breed: {lily.breed}\nColour: {lily.color}\nAge: {lily.age}\nWeight: {lily.weight}\nGender: {lily.gender}\n")
print(f"Roxie's Breed: {roxie.breed}\nColour: {roxie.color}\nAge: {roxie.age}\nWeight: {roxie.weight}\nGender: {roxie.gender}")
