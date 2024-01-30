# Declare shield variables

max_shield = 100
shield_damage = 15.5

# Calculating the shield level

shield_level = max_shield - shield_damage
print("Bot's shield level (%) is:", shield_level)

# Calculating the shield bars

shield_bars = shield_level/20
print("Bot has",shield_bars,"shield bars.")

# Calculating whole shield bars

whole_bars = shield_bars//1
print("There are", whole_bars, "whole shield bars.")

is_critical = shield_bars<=2
print("Is Bot's shield critical?",is_critical)