from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'healthify.com'





def check_login():
    email = None
    password = None
    
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['pass']

        if((email == 'rudra@healthify.com' and password  == 'rudra123') or
           (email == 'bhagyashri@healthify.com' and password  == 'bhagu123') or
           (email == 'vidya@healthify.com' and password  == 'vidya123')):
            splitted_email = email.split('@')
            username = splitted_email[0].capitalize
            return (render_template(('m3.html'),name = username))
        else:
            alert_message = "Your login credentials are wrong!!! Try again"
            return render_template('m2.html', alert_message=alert_message)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods = ['GET', 'POST'])
def loginpage():
    # previous_page = request.headers.get('Referer')
    
    return render_template('m1.html')

@app.route('/register', methods = ['GET','POST'])
def register():
    return render_template('m2.html')

@app.route('/checkup', methods = ['GET', 'POST'])
def checkup():
    email = None
    password = None
    
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['pass']

        if((email == 'rudra@healthify.com' and password  == 'rudra123') or
           (email == 'bhagyashri@healthify.com' and password  == 'bhagu123') or
           (email == 'vidya@healthify.com' and password  == 'vidya123')):
            splitted_email = email.split('@')
            username = splitted_email[0]
            return (render_template(('userinput.html'),name = username))
        else:
            alert_message = "Your login credentials are wrong!!! Try again"
            return render_template(('m1.html'), alert_message=alert_message)

@app.route('/result', methods = ['GET', 'POST'])
def display_result():
    class Patient():
    # def __init__(self, dictofattr):
    #     super().__init__(dictofattr)

        def take_input(self):
            # diseases = ['bloodpressure', 'headache','cough', 'dizziness', 'chestpain', 'fatigue', 'frequenturination',
            #             'excessivethirst', 'blurredvision', 'suddenweightloss', 'sorethroat', 'bodyaches',
            #             'shortnessofbreadth', 'sneezing', 'itchyeyes', 'runnynose', 'rash']

            # self.dict = {}
            # for disease in diseases:
            #     pinput = input("Enter value for " + disease + ": ")
            #     self.dict[disease] = pinput
            if(request.method == "POST"):
                diseases = ['bloodpressure', 'headache','cough','fever', 'dizziness', 'chestpain', 'fatigue', 'frequenturination',
                        'excessivethirst', 'blurredvision', 'suddenweightloss', 'sorethroat', 'bodyaches',
                        'shortnessofbreadth', 'sneezing', 'itchyeyes', 'runnynose', 'rash']
                self.dict = {}
                for disease in diseases:
                    # Use disease as the key for accessing form values
                    self.dict[disease] = request.form.get(disease, 'No')





        # def display_symptoms(self):
        #     print("\nThe symptoms of the patient are:")
        #     for disease, value in self.dict.items():
        #         print(disease, ":", value)

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

        # def identify_disease(self):
        #     hypertension = self.hypertension()
        #     diabetes = self.diabetes()
        #     flu = self.flu()
        #     pneumonia = self.pneumonia()
        #     allergies = self.allergies()

        #     if hypertension:
        #         return render_template(('result.html'), result_text1 = "You have hypertension!")
        #         # print("You have hypertension!")
        #     if diabetes:
        #         return render_template(('result.html'), result_text2 = "You have diabetes!")
        #         # print("You have diabetes!")
        #     if flu:
        #         return render_template(('result.html'), result_text3 = "You have flu!")
        #         # print("You have flu!")
        #     if pneumonia:
        #         return render_template(('result.html'), result_text4 = "You have pneumonia!")
        #         # print("You have pneumonia!")
        #     if allergies:
        #         return render_template(('result.html'), result_text5 = "You have allergies!")
        #         # print("You have allergies!")
        #     return render_template(('result.html'), final_text = "All code executed!!!")

    patient1 = Patient()
    patient1.take_input()
    #patient1.display_symptoms()
    # patient1.identify_disease()
    hypertension = patient1.hypertension()
    diabetes = patient1.diabetes()
    flu = patient1.flu()
    pneumonia = patient1.pneumonia()
    allergies = patient1.allergies()
    patient1.dict = {}


    if hypertension:
        
        return render_template(('result.html'), result_text1 = "You have hypertension!")
        
        # print("You have hypertension!")
    if diabetes:
        
        return render_template(('result.html'), result_text2 = "You have diabetes!")
        # print("You have diabetes!")
    if flu:
        
        return render_template(('result.html'), result_text3 = "You have flu!")
        # print("You have flu!")
    if pneumonia:
        
        return render_template(('result.html'), result_text4 = "You have pneumonia!")
        # print("You have pneumonia!")
    if allergies:
        
        return render_template(('result.html'), result_text5 = "You have allergies!")
        # print("You have allergies!")
    
    return render_template(('result.html'), final_text = "Sorry no match :(")

    




if __name__ == "__main__":
    app.run(debug=True)