from datetime import datetime
class PatientDetails():
    OutsideBangalore=0
    InsideBangaloreButNotInsideDate=0
    InsideBangalore=0
    totalpatients=0
    DetailsOfPatient=[]
    def __init__(self, NameOfThePatient, PatientPlace, DateOfAdmission, NameOfTheHospital):
        self.NameOfThePatient = NameOfThePatient
        self.PatientPlace = PatientPlace
        self.DateOfAdmission = datetime.timestamp(datetime.strptime(DateOfAdmission,'%Y-%m-%d'))
        self.NameOfTheHospital = NameOfTheHospital
    def patients_list(self):
        self.DetailsOfPatient.append({self.NameOfThePatient:[self.PatientPlace, self.DateOfAdmission, self.NameOfTheHospital]})
    def GetPatientDetail(self,numberofdays):
        for j in range(0, numberofdays):
            for element in self.DetailsOfPatient:
                for key,value in element.items():
                         x = self.DateOfAdmission-j*86400
                         if value[1] == x and value[0] == 'Bangalore':
                            self.InsideBangalore += 1
                         elif value[1] != x and value[0] == 'Bangalore':
                            self.InsideBangaloreButNotInsideDate += 1
                         elif value[1] == x and value[0] != 'Bangalore':
                            self.OutsideBangalore += 1
            self.totalpatients += 1
        print("There are total {} number of patients out of which {} are from outside bangalore".format(self.totalpatients,self.OutsideBangalore))