class vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

model1x= vehicle(240, 18)
model2x = vehicle(180, 24)
model3x= vehicle(200, 20)

print("Model 1x max speed:",model1x.max_speed)
print("Model 1x mileage:",model1x.mileage)
print("Model 2x max speed:",model2x.max_speed)
print("Model 2x mileage:",model2x.mileage)
print("Model 3x max speed:",model3x.max_speed)
print("Model 3x mileage:",model3x.mileage)
