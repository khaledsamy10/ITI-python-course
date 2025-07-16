from Person_class import Person

class Employee(Person):
    
    def __init__(self,name,ID,car=None,email=None,salary=0,distanceToWork=0):
        super().__init__(name)
        self.id=ID
        self.car=car
        self.email=email
        self.salary=salary
        self.distance_to_work=distanceToWork
        
        
    def work(self,hours):
        try:
            hours=float(hours)
            if hours==8:
                self.mood='happy'
            elif hours>8:
                self.mood='tired'
            else:
                self.mood='lazy'
        except:
            raise ValueError
    
    
    def send_mail (self):
        self.sentmail=True
        
        
    def drive(self,velocity,distance):
        self.car.run(velocity,distance)
        self.drive_velocity=velocity
        self.drive_distance=distance
        
    def refuel(self,gasamount):
        try:
            if gasamount<0:
                print("can't refuel with negative value")
                
            elif (gasamount + self.car.fuelRate)>100:
                self.car.fuelRate=100
            else:
                self.car.fuelRate=self.car.fuelRate + gasamount
        except:
            raise ValueError('gas amount must be number ')