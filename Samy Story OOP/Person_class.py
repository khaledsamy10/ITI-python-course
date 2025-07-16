class Person:
    def __init__(self,name,mood=None,money=0,healthRate=0):
        self.name=name
        self.mood=mood
        self.money=money
        self.healthRate=healthRate
    

        
    def sleep(self,hours):
        try:
            hours=float(hours)
            if hours==7:
                self.mood='happy'
            elif hours>7:
                self.mood='lazy'
            else:
                self.mood='tired'
        except:
            raise ValueError('"Hours must be a number"')
        
            
    def eat(self,meals):
        try:
            if meals in [1,2,3]:
                if meals==1:
                    self.healthRate=50
                elif meals==2:
                    self.healthRate=75
                elif meals==3:
                    self.healthRate=100
            else :
                print ('unknown number of meals')
        except:
            raise ValueError('meals are 1 or 2 or 3')
        
        
    def buy(self,items):
        self.money=self.money - (10*items)