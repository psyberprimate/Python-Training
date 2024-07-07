import temperature as temp


class Calories():
    """Amount of calories needed per BMR
    with Mifflin-St Jeor equation with added temperature
    (10*weight + 6.25*height - 5*age + 5/-161) * temperature_coefficient
    """    
    def __init__(self, weight: float, height: float, age: int, gender: str, temperature: float):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = 1 if -20 < temperature < 40 else 1.2
        self.gender = 5 if gender == "male" else -161
        
    def calculate(self):
        """Probably not very scientific but if weather exceeds over 40 or below -20 degrees, the recommended 
        amount of calories is upscaled by 20 percent - the number probably are wrong here, just a guess
        """        
        #still needs the line for getting the temperature 
        return (10*self.weight + 6.25*self.height - 5*self.age + self.gender) * self.temperature
    
    
if __name__ == "__main__":
    temperature = temp.Temperature(country="finland", city="helsinki").get()
    calories = Calories(weight=70, height=180, age=35, gender='male', temperature=temperature)
    print(calories.calculate())