class Office:
    employeesNum=0
    
    @classmethod
    def change_emps_num(cls,number):
        cls.employeesNum=cls.employeesNum+number
        
        
    def __init__(self,name,employees=[]):
        self.name=name
        self.employees=list(employees)
        self.change_emps_num(len(self.employees))
        
        employees_list_of_tuples=[]
        for em_object in self.employees:
            object_tuple=(em_object.name,em_object.id)
            employees_list_of_tuples.append(object_tuple)
        self.employees_data=employees_list_of_tuples
        
        
    def get_all_employees(self):
        print(self.employees_data)
        return self.employees_data
    
    def get_employee(self,id):
        try:
            for object_tuple in self.employees_data:
                if object_tuple[1] ==id:
                    print(object_tuple)
                    return object_tuple
                else:
                    continue
            else:
                print(f'No employee with id {id}')
        except:
            raise ValueError ('id must be intger')
        
                
    def hire(self,employee):
        self.employees.append(employee)
        self.employees_data.append((employee.name,employee.id))
        self.change_emps_num(1)
        
        
    def fire(self,id):
        try:
            for em_object in self.employees:
                if em_object.id==id:
                    self.employees.remove(em_object)
                    for object_tuple in self.employees_data:
                        if object_tuple[1] ==id:
                            self.employees_data.remove(object_tuple)
                        else:
                            continue
                    break    
                else:
                    continue
            else:
                print(f'No employee with id {id}')
        except:
            raise ValueError('id must be intger')

        
    def deduct(self,id,deduction):   #deduction passed in positive number, if deduction is 100 then salary=salary-100
        try:
            for em_object in self.employees:
                if em_object.id==int(id):
                    em_object.salary= em_object.salary-float(deduction)
                    break
                else:
                    continue
            else:
                print(f'No employee with id {id}')
        except:
            raise ValueError('id must be intger and deduction must be float')
            
    
    def reward(self,id,reward):
        try:
            for em_object in self.employees:
                if em_object.id==int(id):
                    em_object.salary= em_object.salary+float(reward)   # reward passed in positive number, if reward is 100 then salary=salary+100
                    break
                else:
                    continue
            else:
                print(f'No employee with id {id}')
        except:
            raise ValueError('id must be intger and reward must be float')
        
    
    def check_lateness(self,employee_id,movehour,targethour):
        try:
            for em_object in self.employees:
                if em_object.id==employee_id:
                    trip_time=em_object.drive_distance/em_object.drive_velocity
                    if targethour-movehour>=trip_time and em_object.car.status != 'stopped':
                        print(f'employee with id {employee_id} is not late and will be rewarded')
                        self.reward(employee_id,10)
                    else:
                        print(f'employee with id {employee_id} is late and will be fined ')
                        self.deduct(employee_id,10)
                    break
                else:
                    continue
            else:
                print(f'No employee with id {employee_id}')
        except:
            raise ValueError('id must be intger, move hour and target hour must be floats')
            
    @staticmethod
    def calculate_lateness(movehour,targethour,distance,velocity):
        try:
            trip_time=distance/velocity
            if targethour -movehour >= trip_time:
                print('employee is not late')
            else:
                print('employee is late')
        except:
            raise ValueError('distance,velocity,move hour and target hour must be floats')
