from car import Car
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
SCREEN_BORDER = 330



class CarManager:
    def __init__(self):
        self.cars = []
        self.setup_cars(20)
        self.move_cars()

    def setup_cars(self, car_count):
        for i in range(car_count):
            position = self.get_random_position()
            self.generate_car(position)

    def move_cars(self):
        for car in self.cars:
            if car.xcor() < -SCREEN_BORDER:
                car.hideturtle()
                self.cars.remove(car)
                del car
            else:
                car.move(STARTING_MOVE_DISTANCE)
    

    def generate_car(self, position=None):
        if position is None:
            while True:
                ry = random.randint(-250, 250)
                ry -= ry % 20
                position = [300, ry]
                if self.is_position_free(position):
                    break
        car = Car(position, random.choice(COLORS), SCREEN_BORDER)
        self.cars.append(car)


    
    def get_random_position(self):
        correct_position = False
        while not correct_position:
            rx = random.randint(-250, 250)
            ry = random.randint(-250, 250)
            ry = ry - (ry % 20)
            correct_position = self.is_position_free([rx, ry])
        return [rx, ry]
        
    def is_position_free(self, position):
        for car in self.cars:
            if car.distance(position[0], position[1]) < 65:
                return False
        return True
    
    def delete_all_cars(self):
        for car in self.cars:
            car.hideturtle()
            del car
        self.cars.clear()