# Final Data Structures
cars = [
    {"model": "Toyota", "fuel_efficiency": 25, "miles_since_last_change": 3000},
    {"model": "Honda", "fuel_efficiency": 30, "miles_since_last_change": 6000},
    {"model": "Ford", "fuel_efficiency": 20, "miles_since_last_change": 4500}
]

# (Mostly) Side-effect-free Functions
def calculate_fuel_efficiency(miles_driven, gallons_used):
    return miles_driven / gallons_used

def needs_oil_change(miles_since_last_change):
    return miles_since_last_change >= 5000

def lazy_double(x):
    return lambda: x * 2

# Use of Higher-Order Functions
def filter_cars(cars, condition_function):
    return list(filter(condition_function, cars))

def map_transform(cars, transform_function):
    return list(map(transform_function, cars))

# Functions as Parameters and Return Values
def calculate_average_fuel_efficiency(cars, fuel_efficiency_function):
    total_efficiency = sum(fuel_efficiency_function(car) for car in cars)
    return total_efficiency / len(cars)

# Closures / Anonymous Functions
def is_hybrid_closure():
    hybrid_models = ["Toyota Prius", "Honda Insight", "Tesla Model 3"]

    def is_hybrid(car):
        return car["model"] in hybrid_models

    return is_hybrid

# Additional Concepts
# Immutable Data Structures (Tuples)
def add_maintenance_status(car):
    oil_change_status = "Needs Change" if needs_oil_change(car["miles_since_last_change"]) else "OK"
    return {**car, "oil_change_status": oil_change_status}

# Lazy Evaluation
def lazy_double(x):
    return lambda: x * 2

# Example Usage:
# 1. Side-effect-free function to calculate fuel efficiency
print("Fuel Efficiency:", calculate_fuel_efficiency(300, 10))

# 2. Higher-order function to filter cars based on fuel efficiency
efficient_cars = filter_cars(cars, lambda car: car["fuel_efficiency"] > 25)
print("Efficient Cars:", efficient_cars)

# 3. Function as a parameter to calculate average fuel efficiency
average_efficiency = calculate_average_fuel_efficiency(cars, lambda car: car["fuel_efficiency"])
print("Average Fuel Efficiency:", average_efficiency)

# 4. Closure to create a function for checking if a car is a hybrid
hybrid_checker = is_hybrid_closure()
hybrid_cars = filter_cars(cars, hybrid_checker)
print("Hybrid Cars:", hybrid_cars)

# 5. Additional concepts
cars_with_maintenance_status = map_transform(cars, add_maintenance_status)
print("Cars with Maintenance Status:", cars_with_maintenance_status)

lazy_result = lazy_double(5)
print("Lazy Double:", lazy_result())


