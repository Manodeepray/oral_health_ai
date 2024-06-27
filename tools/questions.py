

def symptoms_que():
    
    symptoms_ques = "\n1.Do you have any sores, lumps, or patches in your mouth that do not heal?\n2.Have you experienced any pain, tenderness, or numbness in your mouth or lips?\n3.Do you have any difficulty chewing, swallowing, speaking, or moving your jaw or tongue?\n4.Have you noticed any persistent sore throat or feeling that something is caught in your throat?\n5.Have you had any changes in your voice or hoarseness?" 
    print(symptoms_ques)        
    symptoms = []
    symptom = None
    while(1):
        symptom = input("\nenter ur answers:\ntype e to continue :")
        symptom =symptom.lower()
        if symptom=="e":
            break
        symptoms.append(symptom)
        
    return symptoms , symptoms_ques

def Duration_and_Progression_que():
    Duration_and_Progression_ques = "\n.How long have you had these symptoms?\n2.Have your symptoms changed or worsened over time?"
    print(Duration_and_Progression_ques)
    Duration_and_Progressions = []
    Duration_and_Progression = None
    
    while(1):
        Duration_and_Progression = input("\nenter ur answers:\ntype e to continue :")
        Duration_and_Progression =Duration_and_Progression.lower()
        if Duration_and_Progression=="e":
            break
        Duration_and_Progressions.append(Duration_and_Progression)
        
    return Duration_and_Progressions ,Duration_and_Progression_ques
    
    
    
def Bleeding_or_Swelling_que():

    Bleeding_or_Swelling_ques = "\n1.Have you noticed any unusual bleeding in your mouth?\n2.Do you have any unexplained swelling in your mouth, jaw, or neck?\n3.Physical Examination and Risk Factors:"
    
    print(Bleeding_or_Swelling_ques)
    Bleeding_or_Swellings = []
    Bleeding_or_Swelling = None
    
    while(1):
        Bleeding_or_Swelling = input("\nenter ur answers:\ntype e to continue :")
        Bleeding_or_Swelling =Bleeding_or_Swelling.lower()
        if Bleeding_or_Swelling=="e":
            break
        Bleeding_or_Swellings.append(Bleeding_or_Swelling)
        
    return Bleeding_or_Swellings ,Bleeding_or_Swelling_ques

def Lifestyle_and_Habits_que():

    Lifestyle_and_Habits_ques = "\n1.Do you smoke or use tobacco products? If so, for how long and how much?\n2.Do you drink alcohol? If so, how much and how often?\n3.Do you have a history of HPV (human papillomavirus) infection?"
    print(Lifestyle_and_Habits_ques)
    Lifestyle_and_Habits = []
    Lifestyle_and_Habit = None
    
    while(1):
        Lifestyle_and_Habit = input("\nenter ur answers:\ntype e to continue :")
        Lifestyle_and_Habit =Lifestyle_and_Habit.lower()
        if Lifestyle_and_Habit=="e":
            break
        Lifestyle_and_Habits.append(Lifestyle_and_Habit)
        
    return Lifestyle_and_Habits ,Lifestyle_and_Habits_ques

def Medical_and_Family_History_que():

    Medical_and_Family_History_ques = "\n1.Do you have a history of any other cancers or precancerous conditions?\n2.Is there a family history of cancer, particularly oral cancer?\n3.Have you had any previous treatments for cancer or other significant illnesses?"
    print(Medical_and_Family_History_ques)
    Medical_and_Family_Historys = []
    Medical_and_Family_History = None
    
    while(1):
        Medical_and_Family_History = input("\nenter ur answers:\ntype e to continue :")
        Medical_and_Family_History =Medical_and_Family_History.lower()
        if Medical_and_Family_History=="e":
            break
        Medical_and_Family_Historys.append(Medical_and_Family_History)
        
    return Medical_and_Family_Historys ,Medical_and_Family_History_ques

def Oral_Hygiene_and_Dental_History_que():
    
    Oral_Hygiene_and_Dental_History_ques = "\n1.How would you describe your oral hygiene practices?\n2.Do you visit a dentist regularly for check-ups and cleanings?\n3.Have you had any recent dental work or oral infections?"
    print(Oral_Hygiene_and_Dental_History_ques)
    Oral_Hygiene_and_Dental_Historys = []
    Oral_Hygiene_and_Dental_History = None
    
    while(1):
        Oral_Hygiene_and_Dental_History = input("\nenter ur answers:\ntype e to continue :")
        Oral_Hygiene_and_Dental_History =Oral_Hygiene_and_Dental_History.lower()
        if Oral_Hygiene_and_Dental_History=="e":
            break
        Oral_Hygiene_and_Dental_Historys.append(Oral_Hygiene_and_Dental_History)
        
    return Oral_Hygiene_and_Dental_Historys ,Oral_Hygiene_and_Dental_History_ques



def Lesion_Description_que():

    Lesion_Description_ques = "\n1.Can you describe the appearance and location of any unusual lesions or patches in your mouth?\n2.Have you noticed any changes in color, size, or texture of the lesions?"
    print(Lesion_Description_ques)
    Lesion_Descriptions = []
    Lesion_Description = None
    
    while(1):
        Lesion_Description = input("\nenter ur answers:\ntype e to continue :")
        Lesion_Description =Lesion_Description.lower()
        if Lesion_Description=="e":
            break
        Lesion_Descriptions.append(Lesion_Description)
        
    return Lesion_Descriptions ,Lesion_Description_ques

def Lymph_Node_Involvement_que():

    Lymph_Node_Involvement_ques = "\n1.Do you have any lumps or swellings in your neck or under your jaw?\n2.Have you experienced any pain or tenderness in your lymph nodes?"
    print(Lymph_Node_Involvement_ques)
    Lymph_Node_Involvements = []
    Lymph_Node_Involvement = None
    
    while(1):
        Lymph_Node_Involvement = input("\nenter ur answers:\ntype e to continue :")
        Lymph_Node_Involvement =Lymph_Node_Involvement.lower()
        if Lymph_Node_Involvement=="e":
            break
        Lymph_Node_Involvements.append(Lymph_Node_Involvement)
        
    return Lymph_Node_Involvements ,Lymph_Node_Involvement_ques


def Biopsy_and_Pathology_Reports_que():
    Biopsy_and_Pathology_Reports_ques ="\n1.Have you had a biopsy of the lesion? If so, what were the results?\n2.Have you had any imaging tests (such as X-rays, CT scans, MRI) to assess the extent of the cancer?"
    print(Biopsy_and_Pathology_Reports_ques)
    Biopsy_and_Pathology_Reports = []
    Biopsy_and_Pathology_Report = None
    
    while(1):
        Biopsy_and_Pathology_Report = input("\nenter ur answers:\ntype e to continue :")
        Biopsy_and_Pathology_Report =Biopsy_and_Pathology_Report.lower()
        if Biopsy_and_Pathology_Report=="e":
            break
        Biopsy_and_Pathology_Reports.append(Biopsy_and_Pathology_Report)
        
    return Biopsy_and_Pathology_Reports ,Biopsy_and_Pathology_Reports_ques

def General_Health_and_Functional_Impact_que():
    General_Health_and_Functional_Impact_ques = "\n1.comment on your General Health : "
    print(General_Health_and_Functional_Impact_ques)
    General_Health_and_Functional_Impacts = []
    General_Health_and_Functional_Impact = None
    
    while(1):
        General_Health_and_Functional_Impact = input("\nenter ur answers:\ntype e to continue :")
        General_Health_and_Functional_Impact =General_Health_and_Functional_Impact.lower()
        if General_Health_and_Functional_Impact=="e":
            break
        General_Health_and_Functional_Impacts.append(General_Health_and_Functional_Impact)
        
    return General_Health_and_Functional_Impacts ,General_Health_and_Functional_Impact_ques

def Overall_Health_que():

    Overall_Health_ques = "\n1.Do you have any other chronic illnesses or conditions that might affect your treatment options?\n2.Are you taking any medications or supplements?"
    print(Overall_Health_ques)
    Overall_Healths = []
    Overall_Health = None
    
    while(1):
        Overall_Health = input("\nenter ur answers:\ntype e to continue :")
        Overall_Health =Overall_Health.lower()
        if Overall_Health=="e":
            break
        Overall_Healths.append(Overall_Health)
        
    return Overall_Healths ,Overall_Health_ques



def Impact_on_Daily_Life_que():

    Impact_on_Daily_Life_ques = "\n2.How are your symptoms affecting your daily activities and quality of life?\n2.Are you experiencing any weight loss, fatigue, or changes in appetite?"
    print(Impact_on_Daily_Life_ques)
    Impacts_on_Daily_Life = []
    Impact_on_Daily_Life = None
    
    while(1):
        Impact_on_Daily_Life = input("\nenter ur answers:\ntype e to continue :")
        Impact_on_Daily_Life =Impact_on_Daily_Life.lower()
        if Impact_on_Daily_Life=="e":
            break
        Impacts_on_Daily_Life.append(Impact_on_Daily_Life)
        
    return Impacts_on_Daily_Life ,Impact_on_Daily_Life_ques


def Treatment_History_and_Response_que():
    Treatment_History_and_Response_ques = "\n1.Have you received any treatments for this condition already? If so, what were they and how did you respond?\n2.Are you currently undergoing any treatments or participating in clinical trials?"
    print(Treatment_History_and_Response_ques)
    Treatment_History_and_Responses = []
    Treatment_History_and_Response = None
    
    while(1):
        Treatment_History_and_Response = input("\nenter ur answers:\ntype e to continue :")
        Treatment_History_and_Response =Treatment_History_and_Response.lower()
        if Treatment_History_and_Response=="e":
            break
        Treatment_History_and_Responses.append(Treatment_History_and_Response)
        
    return Treatment_History_and_Responses ,Treatment_History_and_Response_ques

'''def prompting():
    symptoms , symptoms_ques = symptoms_que()
    Duration_and_Progressions ,Duration_and_Progression_ques = Duration_and_Progression_que()
    Bleeding_or_Swellings ,Bleeding_or_Swelling_ques = Bleeding_or_Swelling_que()
    Lifestyle_and_Habits ,Lifestyle_and_Habits_ques = Lifestyle_and_Habits_que()
    Medical_and_Family_History ,Medical_and_Family_History_ques = Medical_and_Family_History_que()
    Oral_Hygiene_and_Dental_History ,Oral_Hygiene_and_Dental_History_ques = Oral_Hygiene_and_Dental_History_que()
    Lesion_Descriptions ,Lesion_Description_ques = Lesion_Description_que()
    
    Lymph_Node_Involvements ,Lymph_Node_Involvement_ques  = Lymph_Node_Involvement_que()
    Biopsy_and_Pathology_Reports , Biopsy_and_Pathology_Reports_ques = Biopsy_and_Pathology_Reports_que()
    General_Health_and_Functional_Impacts ,General_Health_and_Functional_Impact_ques =  General_Health_and_Functional_Impact_que()
    Overall_Health ,Overall_Health_ques = Overall_Health_que()
    Impacts_on_Daily_Life ,Impact_on_Daily_Life_ques = Impact_on_Daily_Life_que()
    Treatment_History_and_Responses ,Treatment_History_and_Response_ques =Treatment_History_and_Response_que()
    
    single_symptoms = ' '.join(symptoms)
    single_Duration_and_Progressions = ' '.join(Duration_and_Progressions)
    single_Bleeding_or_Swellings = ' '.join(Bleeding_or_Swellings)
    single_Lifestyle_and_Habits = ' '.join(Lifestyle_and_Habits)
    single_Medical_and_Family_History = ' '.join(Medical_and_Family_History)
    single_Oral_Hygiene_and_Dental_History = ' '.join(Oral_Hygiene_and_Dental_History)
    single_Lesion_Descriptions = ' '.join(Lesion_Descriptions)
    single_Lymph_Node_Involvements = ' '.join(Lymph_Node_Involvements)
    single_Biopsy_and_Pathology_Reports = ' '.join(Biopsy_and_Pathology_Reports)
    single_General_Health_and_Functional_Impacts = ' '.join(General_Health_and_Functional_Impacts)
    single_Overall_Health = ' '.join(Overall_Health)
    single_Impacts_on_Daily_Life = ' '.join(Impacts_on_Daily_Life)
    single_Treatment_History_and_Responses = ' '.join(Treatment_History_and_Responses)
    prompt = f"the symptoms shown by the patient are {single_symptoms}.\nduration and progresion of cancer are {single_Duration_and_Progressions}.\n Bleeding or Swellings are {single_Bleeding_or_Swellings}.\Lifestyle and Habits are {single_Lifestyle_and_Habits}.\Medical and Family History are {single_Medical_and_Family_History}.\Oral Hygiene and Dental History are {single_Oral_Hygiene_and_Dental_History}.\Lesion Descriptions are {single_Lesion_Descriptions}.\Lymph Node Involvements are {single_Lymph_Node_Involvements}.\Biopsy and Pathology Reports are {single_Biopsy_and_Pathology_Reports}.\General Health and Functional Impacts are {single_General_Health_and_Functional_Impacts}.\Impacts on Daily Life are {single_Impacts_on_Daily_Life}.\Treatment History and Responses are {single_Treatment_History_and_Responses}."
    print(prompt) 
    return prompt'''

def prompt_return(symptoms ,Duration_and_Progressions ,Bleeding_or_Swellings ,Lifestyle_and_Habits ,Medical_and_Family_History ,Oral_Hygiene_and_Dental_History ,Lesion_Descriptions , Lymph_Node_Involvements ,Biopsy_and_Pathology_Reports , General_Health_and_Functional_Impacts , Overall_Health ,Impacts_on_Daily_Life ,Treatment_History_and_Responses ):
    symptoms ,Duration_and_Progressions ,Bleeding_or_Swellings ,Lifestyle_and_Habits ,Medical_and_Family_History ,Oral_Hygiene_and_Dental_History ,Lesion_Descriptions , Lymph_Node_Involvements ,Biopsy_and_Pathology_Reports , General_Health_and_Functional_Impacts , Overall_Health ,Impacts_on_Daily_Life ,Treatment_History_and_Responses ,    

    prompt = f"the symptoms shown by the patient are {symptoms}.\nduration and progresion of cancer are {Duration_and_Progressions}.\nBleeding or Swellings are {Bleeding_or_Swellings}.\nLifestyle and Habits are {Lifestyle_and_Habits}.\nMedical and Family History are {Medical_and_Family_History}.\nOral Hygiene and Dental History are {Oral_Hygiene_and_Dental_History}.\nLesion Descriptions are {Lesion_Descriptions}.\nLymph Node Involvements are {Lymph_Node_Involvements}.\nBiopsy and Pathology Reports are {Biopsy_and_Pathology_Reports}.\nGeneral Health and Functional Impacts are {General_Health_and_Functional_Impacts}.\nImpacts on Daily Life are {Impacts_on_Daily_Life}.\nTreatment History and Responses are {Treatment_History_and_Responses}.\n chronic illness is {Overall_Health}"
    print(prompt) 
    return prompt


symptoms_ques = "\n1.Do you have any sores, lumps, or patches in your mouth that do not heal? Have you experienced any pain, tenderness, or numbness in your mouth or lips? Do you have any difficulty chewing, swallowing, speaking, or moving your jaw or tongue? Have you noticed any persistent sore throat or feeling that something is caught in your throat? Have you had any changes in your voice or hoarseness?" 
Duration_and_Progression_ques = "\n2.How long have you had these symptoms? Have your symptoms changed or worsened over time?"
Bleeding_or_Swelling_ques = "\n3.Have you noticed any unusual bleeding in your mouth? Do you have any unexplained swelling in your mouth, jaw, or neck? Physical Examination and Risk Factors:"
Lifestyle_and_Habits_ques = "\n4.Do you smoke or use tobacco products? If so, for how long and how much? .Do you drink alcohol? If so, how much and how often? .Do you have a history of HPV (human papillomavirus) infection?"
Medical_and_Family_History_ques = "\n5.Do you have a history of any other cancers or precancerous conditions? .Is there a family history of cancer, particularly oral cancer? Have you had any previous treatments for cancer or other significant illnesses?"
Oral_Hygiene_and_Dental_History_ques = "\n6.How would you describe your oral hygiene practices? .Do you visit a dentist regularly for check-ups and cleanings? .Have you had any recent dental work or oral infections?"
Lesion_Description_ques = "\n7.Can you describe the appearance and location of any unusual lesions or patches in your mouth? .Have you noticed any changes in color, size, or texture of the lesions?"
Lymph_Node_Involvement_ques = "\n8.Do you have any lumps or swellings in your neck or under your jaw? .Have you experienced any pain or tenderness in your lymph nodes?"
Biopsy_and_Pathology_Reports_ques ="\n9.Have you had a biopsy of the lesion? If so, what were the results? .Have you had any imaging tests (such as X-rays, CT scans, MRI) to assess the extent of the cancer?"
General_Health_and_Functional_Impact_ques = "\n10.comment on your General Health : "
Overall_Health_ques = "\n11.Do you have any other chronic illnesses or conditions that might affect your treatment options? .Are you taking any medications or supplements?"
Impact_on_Daily_Life_ques = "\n12.How are your symptoms affecting your daily activities and quality of life? .Are you experiencing any weight loss, fatigue, or changes in appetite?"
Treatment_History_and_Response_ques = "\n13.Have you received any treatments for this condition already? If so, what were they and how did you respond? .Are you currently undergoing any treatments or participating in clinical trials?"



if __name__=="__main__":
    prompt = prompt_return() 