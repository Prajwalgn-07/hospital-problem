from SolutionPastNDays import PatientDetails
c = 0
a = input("if u want to enter the details y/n")
while a == 'y':
    NameOfThePatient = input("enter the name of the patient")
    PatientPlace = input("enter the city in which you are currently staying")
    NameOfTheHospital = input("enter the name of the hospital")
    DateOfAdmission = input("enter the date of admission in the format yyyy-mm-dd")
    c = PatientDetails(NameOfThePatient, PatientPlace, DateOfAdmission, NameOfTheHospital)
    c.patients_list()
    a = input("do u want to enter some more details y/n")
b=input("do u want to get the details of the patient y/n")
try:
    while b == 'y':
        b = int(input("enter the number of days u want to get the details"))
        c.GetPatientDetail(b)
except AttributeError:
    print("There is no detail for these number of days")
