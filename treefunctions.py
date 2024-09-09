class Identify():
    

    def __init__(self, dictofattr):
        self.dict = dictofattr

    def hypertension(self):
        if(self.dict['bloodpressure'] == 'high'):
            if(self.dict['chestpain'] == 'yes'):
                return 1
            elif (self.dict['headache'] == 'yes'):
                return 1
            else :
                return 0
            
        elif(self.dict['bloodpressure'] == 'normal'):
            return 0
        else:
            if(self.dict['dizziness'] == 'yes'):
                if(self.dict['fatigue']== 'yes'):
                    return 1
                else:
                    return 0
            else:
                return 0
            
    def diabetes(self):
        if(self.dict['blurredvision'] == 'no' or self.dict['blurredvision'] == 'normal'):
            return 0
        elif(self.dict[''] == 'yes'):
            return 1
        else:
            if(self.dict['fatigue'] == 'yes'):
                return 1
            else:
                if(self.dict['excessivethirst'] == 'yes'):
                    return 0
                else:
                    return 1
                
    def flu(self):
        if(self.dict['sorethroat'] == 'yes'):
            if(self.dict['cough'] == 'yes'):
                return 1
            else:
                return 0
        else:
            return 0
        
    def pneumonia(self):
        if(self.dict['cough'] == 'yes'):
            if(self.dict['shortnessofbreadth'] == 'yes'):
                if(self.dict['chestpain'] == 'yes'):
                    if(self.dict['fever'] == 'yes'):
                        return 1
                    else:
                        return 0
                else:
                    return 0
            else:
                return 0
        else:
            return 0
        
    def allergies(self):
        if(self.dict['itchyeyes'] == 'yes'):
            return 1
        else:
            if(self.dict['shortnessofbreadth'] == 'yes'):
                return 0
            else:
                if(self.dict['sneezing'] == 'yes'):
                    return 1
                else:
                    if(self.dict['rash'] == 'yes'):
                        return 1
                    else:
                        return 0
                    
    
            
class Patient(Identify):
    '''
    def __init__(self, bloodpressure, headache, dizziness, chestpain, fatigue, frequenturination, excessivethirst, blurredvision, suddenweightloss, sorethroat, bodyaches, shortnessofbreadth, sneezing, itchyeyes, runnynose, rash):
        self.dict = {'bloodpressure' : None, 'headache' : None, 'dizziness' : None, 'chestpain' : None, 'fatigue' : None, 'frequenturination' : None, 'excessivethirst' : None, 'blurredvision' : None, 'suddenweightloss' : None, 'sorethroat' : None, 'bodyaches' : None, 'shortnessofbreadth' : None, 'sneezing' : None, 'itchyeyes' : None, 'runnynose' : None, 'rash' : None}
        self.dict['bloodpressure'] = bloodpressure
        self.dict['headache'] = headache
        self.dict['dizziness'] = dizziness
        self.dict['chestpain'] = chestpain
        self.dict['fatigue'] = fatigue
        self.dict['frequenturination'] = frequenturination
        self.dict['excessivethirst'] = excessivethirst
        self.dict['blurredvision'] = blurredvision
        self.dict['suddenweightloss'] = suddenweightloss
        self.dict['sorethroat'] = sorethroat
        self.dict['bodyaches'] = bodyaches
        self.dict['shortnessofbreadth'] = shortnessofbreadth
        self.dict['sneezing'] = sneezing
        self.dict['itchyeyes'] = itchyeyes
        self.dict['runnynose'] = runnynose
        self.dict['rash'] = rash
    '''

    def take_input(self):
        diseases = ['bloodpressure', 'headache', 'dizziness', 'chestpain', 'fatigue', 'frequenturination', 'excessivethirst', 'blurredvision', 'suddenweightloss', 'sorethroat', 'bodyaches', 'shortnessofbreadth', 'sneezing', 'itchyeyes', 'runnynose', 'rash']

        self.dict = {'bloodpressure' : None, 'headache' : None, 'dizziness' : None, 'chestpain' : None, 'fatigue' : None, 'frequenturination' : None, 'excessivethirst' : None, 'blurredvision' : None, 'suddenweightloss' : None, 'sorethroat' : None, 'bodyaches' : None, 'shortnessofbreadth' : None, 'sneezing' : None, 'itchyeyes' : None, 'runnynose' : None, 'rash' : None}

        for disease in diseases:
            pinput = input("Enter value for  "+disease+" : ")
            self.dict[disease] = pinput
    
    def display_symptoms(self):
        print("\nThe symptoms of the patient are :")
        for disease in self.dict:
            print(disease," : ", self.dict[disease])

    def identify_disease(self):
        hypertension = self.hypertension()
        diabetes = self.diabetes()
        flu = self.flu()
        pneumonia = self.pneumonia()
        allergies = self.allergies()

        if(hypertension):
            print("You have hypertension!")
        if(diabetes):
            print("You have diabetes!")
        if(flu):
            print("You have flu!")
        if(pneumonia):
            print("You have pneumonia!")
        if(allergies):
            print("You have allergies!")





patient1 = Patient()
patient1.take_input()
patient1.display_symptoms()
patient1.identify_disease()







