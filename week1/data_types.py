# Display data types.

model_number = "BOT-X1"
shield = 100
laser_range = 3.5
rocket_range = 75.0

print("#"*29)
print("# Diagnostics:              #")
print("# ------------------------- #")
print("# Model Number    :",model_number," #")
print("# Shield (%):      ",shield,"    #")
print("# Laser range (m) :",laser_range,"    #")
print("# Rocket range (m):",rocket_range,"   #")
print("#"*29)
print()

print("The data type of model number is",type(model_number))
print("The data type of shield is",type(shield))
print("The data type of laser range is",type(laser_range))
print("The data type of rocket range is",type(rocket_range))