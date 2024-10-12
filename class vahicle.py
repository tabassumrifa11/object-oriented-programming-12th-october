print("\033c")

class vehicle:
    
    def __init__(self, max_speed , mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        
        
        
tesla = vehicle(180, 0) 
lambo = vehicle(350, 6) 


print("Tesla Max speed:", tesla.max_speed)
print("Tesla Max speed:", tesla.mileage)


print()

print("Lamborghini Max speed:", lambo.max_speed)
print("Lamborghini Max speed:", lambo.mileage)
