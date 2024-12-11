class Ford:
    def __init__(self,model,color,year,transmission,Ev):
        self.model = model
        self.color = color
        self.year = year
        self.transmission = transmission
        self.Ev = Ev
    def print_cars(self):
        print('car_model == ',self.model)
        print('Color == ', self.color)
        print('Year == ', self.year)
        print('Transmission == ', self.transmission)
        print('Electric == ', self.Ev)
class BMW:
    def __init__(self,model,color,year,transmission,Ev):
        self.model = model
        self.color = color
        self.year = year
        self.transmission = transmission
        self.Ev = Ev
    def print_cars(self):
        print('car_model == ',self.model)
        print('Color == ', self.color)
        print('Year == ', self.year)
        print('Transmission == ', self.transmission)
        print('Electric == ', self.Ev)
class Tesla:
    def __init__(self,model,color,year,transmission,Ev):
        self.model = model
        self.color = color
        self.year = year
        self.transmission = transmission
        self.Ev = Ev
    def print_cars(self):
        print('car_model == ',self.model)
        print('Color == ', self.color)
        print('Year == ', self.year)
        print('Transmission == ', self.transmission)
        print('Electric == ', self.Ev)

ford1 = Ford('focus','White',2020,'Auto','False')
Ford.print_cars()
