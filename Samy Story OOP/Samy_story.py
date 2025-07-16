from Car_class import Car
from Employee_class import Employee
from Person_class import Person
from Office_class import Office

# Samy is employee who has a fiat128 car.
samy_fiat_128=Car('Samy fiat 128')
samy=Employee('Samy',4085,samy_fiat_128)

ahmed_bmw5050=Car('Ahmed bmw 5050')
ahmed=Employee('ahmed',9829,ahmed_bmw5050)

mazen_ford2008=Car('Mazen ford 2008')
mazen=Employee('Mazen',3822)

omnia_mazda2000=Car('Omnia mazda 2000')
omnia=Employee('Omnia',2045)

# ITI office starts with three employees Ahmed,Samy and Omnia
iti_smartvillage=Office('ITI',[ahmed,samy,omnia])

# ITI office hires mazen
iti_smartvillage.hire(mazen)

# ITI office fires ahmed
iti_smartvillage.fire(9829)

# now we can get all employees
iti_smartvillage.get_all_employees()
print('----------------------------------------------------------------------------')

#we can get employee by his id.
iti_smartvillage.get_employee(2045)
print('****************************************************************************')

# samy starts his day by refuels his car.
samy.refuel(85)
print(samy_fiat_128.fuelRate)  #good, the car have fuel now.
print('############################################################################')

# Samy drives distance 20 km at velocity 90 km/hour.
samy.drive(90,20)
print('----------------------------------------------------------------------------')

# it seems Samy arrived to work But was he late ? he moved 8 am and he should be at office by 9 am  .
iti_smartvillage.check_lateness(4085,8,9)

print('****************************************************************************')
#Excellent Samy was rewarded as he arrived before 9 am. let's check his salary(he was rewardrd by 10).
print(samy.salary)

print('############################################################################')
# let's get into work
samy.send_mail()
print(samy.sentmail)

print('----------------------------------------------------------------------------')
# Samy worked 10 hours today he looks tired.
samy.work(10)
print(samy.mood)
