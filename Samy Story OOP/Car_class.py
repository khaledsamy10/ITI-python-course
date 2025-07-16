class Car:
    def __init__(self,name,fuelRate=0,velocity=0):
        self.name=name
        self.__fuelRate=fuelRate
        self.__velocity=velocity
        
    @property
    def velocity(self):
        return self.__velocity
    
    @velocity.setter
    def velocity(self,velocity):
        if velocity >= 0 and velocity <= 200:
            self.__velocity=velocity
        else:
            raise ValueError('velocity only between 0 and 200 ')
        
    @property
    def fuelRate(self):
        return self.__fuelRate
    
    @fuelRate.setter
    def fuelRate(self,fuelRate):
        if fuelRate >= 0 and fuelRate <= 100:
            self.__fuelRate=fuelRate
        else:
            raise ValueError('fuel rate can be only between 0 and 100')
            

        
    # fuelrate decreases by 10 for every 10 km  
    def run(self,velocity,distance):
        try:
            self.velocity=velocity
            if self.velocity==0:
                print('Car can not run at 0 velocity!')
            else:
                remaining_distance=distance - self.fuelRate
                if remaining_distance <0:
                    self.fuelRate=abs(remaining_distance)
                    self.stop(remaining_distance)
                else:
                    self.stop(remaining_distance)
        except:
            raise ValueError('velocity and distance must be floats')
            
    
    def stop(self,remaining_distance):
        try:
            self.velocity=0
            
            if remaining_distance > 0:
                print(f'Car stopped due to fuel running up. The remaining distance is {remaining_distance}')
                self.status='stopped'
            else:
                print(f'welcome to destination remaining fuel is {abs(remaining_distance)}')
                self.status='didnt stop'
        except:
            raise ValueError('remaining distance must be intger')