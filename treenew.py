# class Identify():
#     def __init__(self, dictofattr):
#         self.dict = dictofattr

#     def hypertension(self):
#         if self.dict['bloodpressure'] == 'high':
#             if self.dict['chestpain'] == 'yes' or self.dict['headache'] == 'yes':
#                 return 1
#             else:
#                 return 0
#         elif self.dict['bloodpressure'] == 'normal':
#             return 0
#         else:
#             if self.dict['dizziness'] == 'yes' and self.dict['fatigue'] == 'yes':
#                 return 1
#             else:
#                 return 0

#     def diabetes(self):
#         if self.dict['blurredvision'] in ['no', 'normal']:
#             return 0
#         elif self.dict['frequenturination'] == 'yes':
#             return 1
#         else:
#             if self.dict['fatigue'] == 'yes':
#                 return 1
#             else:
#                 if self.dict['excessivethirst'] == 'yes':
#                     return 0
#                 else:
#                     return 1

#     def flu(self):
#         if self.dict['sorethroat'] == 'yes' and self.dict['cough'] == 'yes':
#             return 1
#         else:
#             return 0

#     def pneumonia(self):
#         if self.dict['cough'] == 'yes' and self.dict['shortnessofbreadth'] == 'yes':
#             if self.dict['chestpain'] == 'yes' and self.dict['fever'] == 'yes':
#                 return 1
#             else:
#                 return 0
#         else:
#             return 0

#     def allergies(self):
#         if self.dict['itchyeyes'] == 'yes':
#             return 1
#         else:
#             if self.dict['shortnessofbreadth'] == 'yes':
#                 return 0
#             else:
#                 if self.dict['sneezing'] == 'yes' or self.dict['rash'] == 'yes':
#                     return 1
#                 else:
#                     return 0


class Patient():
    # def __init__(self, dictofattr):
    #     super().__init__(dictofattr)

    def take_input(self):
        diseases = ['bloodpressure', 'headache','cough', 'dizziness', 'chestpain', 'fatigue', 'frequenturination',
                    'excessivethirst', 'blurredvision', 'suddenweightloss', 'sorethroat', 'bodyaches',
                    'shortnessofbreadth', 'sneezing', 'itchyeyes', 'runnynose', 'rash']

        self.dict = {}
        for disease in diseases:
            pinput = input("Enter value for " + disease + ": ")
            self.dict[disease] = pinput

    def display_symptoms(self):
        print("\nThe symptoms of the patient are:")
        for disease, value in self.dict.items():
            print(disease, ":", value)

    def hypertension(self):
        if self.dict['bloodpressure'] == 'high':
            if self.dict['chestpain'] == 'yes' or self.dict['headache'] == 'yes':
                return 1
            else:
                return 0
        elif self.dict['bloodpressure'] == 'normal':
            return 0
        else:
            if self.dict['dizziness'] == 'yes' and self.dict['fatigue'] == 'yes':
                return 1
            else:
                return 0

    def diabetes(self):
        if self.dict['blurredvision'] in ['no', 'normal']:
            return 0
        elif self.dict['frequenturination'] == 'yes':
            return 1
        else:
            if self.dict['fatigue'] == 'yes':
                return 1
            else:
                if self.dict['excessivethirst'] == 'yes':
                    return 0
                else:
                    return 1

    def flu(self):
        if self.dict['sorethroat'] == 'yes' and self.dict['cough'] == 'yes':
            return 1
        else:
            return 0

    def pneumonia(self):
        if self.dict['cough'] == 'yes' and self.dict['shortnessofbreadth'] == 'yes':
            if self.dict['chestpain'] == 'yes' and self.dict['fever'] == 'yes':
                return 1
            else:
                return 0
        else:
            return 0

    def allergies(self):
        if self.dict['itchyeyes'] == 'yes':
            return 1
        else:
            if self.dict['shortnessofbreadth'] == 'yes':
                return 0
            else:
                if self.dict['sneezing'] == 'yes' or self.dict['rash'] == 'yes':
                    return 1
                else:
                    return 0

    def identify_disease(self):
        hypertension = self.hypertension()
        diabetes = self.diabetes()
        flu = self.flu()
        pneumonia = self.pneumonia()
        allergies = self.allergies()

        if hypertension:
            print("You have hypertension!")
        if diabetes:
            print("You have diabetes!")
        if flu:
            print("You have flu!")
        if pneumonia:
            print("You have pneumonia!")
        if allergies:
            print("You have allergies!")
        print("All code executed!")



patient1 = Patient()
patient1.take_input()
patient1.display_symptoms()
patient1.identify_disease()
