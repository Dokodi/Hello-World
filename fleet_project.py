#array to store vehicle details
entireDetail_vehicle = []
indiDetail_vehicle = []

#array to store driver details
entireDetail_driver = []
indiDetail_driver = []


class Vehicle: 
    #class for handling vehicles in fleet 


    def __init__(self, model, registration_number, condition) :
        self.model = model
        self.registration_number = registration_number
        self.condition = condition

    
    def add_vehicle(self):
        self.model = input("New Vehicle's Model: ")
        self.registration_number = str(input("New Vehicle's Registration Number: "))
        self.condition = True
        indiDetail_vehicle.append(self.model)
        indiDetail_vehicle.append(self.registration_number)
        indiDetail_vehicle.append(self.condition)
        entireDetail_vehicle.append(indiDetail_vehicle)
        #return(entireDetail_vehicle)
        print(entireDetail_vehicle)

    def change_vehicle_details(self):
        self.model = input("Vehicle's New Model: ")
        self.registration_number = input("Vehicle's New Registration Number: ")
        self.condition = True
        indiDetail_vehicle.append(self.model)
        indiDetail_vehicle.append(self.registration_number)
        indiDetail_vehicle.append(self.condition)
        entireDetail_vehicle.append(indiDetail_vehicle)
        print(entireDetail_vehicle)


#    def delete_vehicle(self):
#        pass



#     class for handling drivers in fleet 
class Driver:

    def __init__(self, driver_name, driver_license_number, driver_license_type, driver_status ):

        self.driver_name = driver_name
        self.driver_license_number = driver_license_number
        self.driver_license_type = driver_license_type
        self.driver_status = driver_status
    

    def add_driver(self):

        self.driver_name = input("Driver's Name: ")
        self.driver_license_number = str(input("Driver's License Number: "))
        self.driver_license_type = input("Driver's License Type: ")
        self.driver_status = True
        indiDetail_driver.append(self.driver_name)
        indiDetail_driver.append(self.driver_license_number)
        indiDetail_driver.append(self.driver_license_type)
        entireDetail_driver.append(indiDetail_driver)
        print(entireDetail_driver)


    def modify_driver(self):

        self.driver_name = input("Driver's New Name: ")
        self.driver_license_number = input("Driver's New License Number: ")
        self.driver_license_type = input("Driver's New License Type: ")
        self.driver_status = True
        indiDetail_driver.append(self.driver_name)
        indiDetail_driver.append(self.driver_license_number)
        indiDetail_driver.append(self.driver_license_type)
        entireDetail_driver.append(indiDetail_driver)
        print(entireDetail_driver)



    def delete_driver(self):
        pass


class trips:

    def __init__(self, location, region, departure_time, return_time, driver, vehicle_used):
        self.location = location
        self.region = region
        self.departure = departure_time
        self.return_time = return_time
        self.driver = driver
        self.vehicle_used = vehicle_used

    
    '''''
    def assign_trips(self):
        self.location = input("Location of trip: ")
        self.region = input("Region: ")
        self.departure_time = input("Departure_time: ")
        self.return_time = input("Return TIme: ")
        self.driver = input("Driver: ")
        self.vehicle_used = input("New Vehicle to be Used: ")
    
    '''''
#         # if driver(0).driver_status == True :
#             return driver(0)

#             if vehicle.vehicle_condition == True:
#                 return vehicle()

#         """
#     def delete_trips():
#         """
#         driver(pop)
#         """

#     def modify_trips():
#         location = input("New Location of trip: ")
#         region = input("New Region: ")
#         departure_time = input("New Departure_time: ")
#         return_time = input("New Return TIme: ")
#         driver = input("New Driver: ")
#         vehicle_used = input("New Vehicle to be Used: ")


print(
            """""
            WELCOME TO THE FLEET MANAGEMENT SYSTEM

            PLEASE CHOOSE ANY OF THE OPTIONS AVAILABLE

            1 - To add new Vehicle

            2 - To modify Vehicle Details

            3 - To add new Driver

            4 - To modify Driver Details
            
            """""

)

decision = input("Please Input a number: ")

if decision == 1:
    decision_1 = Vehicle('model', '1234', True)
    decision_1.add_vehicle()

elif decision == 2:
    decision_2 = Vehicle('model', '1234', True)
    decision_2.change_vehicle_details()

elif decision == 3:
    decision_3 = Driver('name', '1234',"license_type", True)
    decision_3.add_driver()

elif decision == 4:
    decision_4 = Driver('name', '1234',"license_type", True)
    decision_4.modify_driver()

else:
    print("Invalid")
