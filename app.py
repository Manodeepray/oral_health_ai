import gradio as gr
from tools import questions, RAG, image_pred

# Shared state for grade and stage
state = {"grade": "none", "stage": "none"}

def run(image):
    exit_image, class_prediction, grade, stage , _= image_pred.image_prediction(image)
    # Update the shared state
    state["grade"] = grade
    state["stage"] = stage
    return exit_image, class_prediction, grade, stage

    '''def answer(symptoms, Duration_and_Progressions, Bleeding_or_Swellings, Lifestyle_and_Habits, Medical_and_Family_History, Oral_Hygiene_and_Dental_History, Lesion_Descriptions, Lymph_Node_Involvements, Biopsy_and_Pathology_Reports, General_Health_and_Functional_Impacts, Overall_Health, Impacts_on_Daily_Life, Treatment_History_and_Responses, grade, stage):
    prompt = questions.prompt_return(symptoms, Duration_and_Progressions, Bleeding_or_Swellings, Lifestyle_and_Habits, Medical_and_Family_History, Oral_Hygiene_and_Dental_History, Lesion_Descriptions, Lymph_Node_Involvements, Biopsy_and_Pathology_Reports, General_Health_and_Functional_Impacts, Overall_Health, Impacts_on_Daily_Life, Treatment_History_and_Responses)
    query = f"what would be the grade  on the basis of following prompt : {prompt}"
    
    
    query1 = f"""what would be the teatment when {grade} ." """  
    query2 = f"""what would be the teatment when {stage} . """
    result1,final_answer1 = RAG.RAG_output_treatment(query1)
    print("\nresult1 : ",result1)
    print("\nfinal_answer1 : ",final_answer1)
    result2,final_answer2 = RAG.RAG_output_treatment(query2)
    print("\nresult2 : ",result2)
    print("\nfinal_answer2 : ",final_answer2) 
    #cancer, final_answer = RAG.RAG_output(query)
    final_answer = f"treatment for {grade}   :" + final_answer1 + f"\n Treatment for {stage} :"+final_answer2
    cancer = Lesion_Descriptions+f" and of {grade} and {stage}"
    return str(query), cancer, final_answer'''
def answer(Duration , Progression , Bleeding , Swellings ,
           
                                                 Persistent_sore , Smoke , Alchohol , Oral_Hygiene ,
                                                 Dentist , Oral_infection , Lesion_Size , Lesion_Size_change ,
                                                 Lesion_Colour , Lesion_Colour_change , Lesion_Location ,
                                                 Lymph_Node_Involvements , Overall_Health , Family_History ,
                                                 Medical , Treatment):
    
    
    grade_query = f"""what would be the grade on the basis of following prompt :     
            duration ={Duration} 
            gotten worse={Progression} 
            bleeding={Bleeding} 
            swelling={Swellings} 
            persistent soreSwellings = {Persistent_sore} 
            smoke if yes how much ={Smoke} 
            alcohol, if yes how much ={Alchohol} 
            brush, floss ={Oral_Hygiene} 
            dentist={Dentist} 
            oral infection ={Oral_infection} 
            lesion size = {Lesion_Size} 
            change in lesion size ={Lesion_Size_change} 
            lesion colour = {Lesion_Colour} 
            change in lesion colour={Lesion_Colour_change} 
            lesion-location={Lesion_Location} 
            lymph node (swollen area in neck) ={Lymph_Node_Involvements} 
            overall health={Overall_Health} 
            family history of cancer={Family_History} 
            serious illness before={Medical} 
            treatment on cancer={Treatment}"""
            
            
    stage_query = f"""what would be the stage on the basis of following prompt :     
            duration ={Duration} 
            gotten worse={Progression} 
            bleeding={Bleeding} 
            swelling={Swellings} 
            persistent soreSwellings = {Persistent_sore} 
            smoke if yes how much ={Smoke} 
            alcohol, if yes how much ={Alchohol} 
            brush, floss ={Oral_Hygiene} 
            dentist={Dentist} 
            oral infection ={Oral_infection} 
            lesion size = {Lesion_Size} 
            change in lesion size ={Lesion_Size_change} 
            lesion colour = {Lesion_Colour} 
            change in lesion colour={Lesion_Colour_change} 
            lesion-location={Lesion_Location} 
            lymph node (swollen area in neck) ={Lymph_Node_Involvements} 
            overall health={Overall_Health} 
            family history of cancer={Family_History} 
            serious illness before={Medical} 
            treatment on cancer={Treatment}"""
    
    grade , stage = RAG.RAG_cancer_output(grade_query , stage_query)
    
    CANCER = f"cancer output :The grade is: {grade} and the stage is: {stage}"
    print(f"cancer output :The grade is: {grade} and the stage is: {stage}")

    
    
    query1 = f"""what would be the teatment when grade is {grade} ." """  
    query2 = f"""what would be the teatment when stage is {stage} . """
    final_answer1 = RAG.RAG_output_treatment(query1)
    print("\nfinal_answer1 : ",final_answer1)
    final_answer2 = RAG.RAG_output_treatment(query2)
    print("\nfinal_answer2 : ",final_answer2) 
    
    return  CANCER, final_answer1 , final_answer2
    
    

# Function to handle the "Continue" button click
def continue_to_chatbot():
    return (gr.update(visible=False), gr.update(visible=True))

with gr.Blocks() as app:
    with gr.Row():
        with gr.Column(visible=True) as prediction_app:
            gr.Markdown("# Disease Prediction App")
            image_input = gr.Image(type="pil", label="Input Image" , width=700, height=700)
            image_output = gr.Image(label="observed Image", width=700, height=700)
            class_output = gr.Textbox(label="Observation")
            grade_output = gr.Textbox(label="Grade")
            stage_output = gr.Textbox(label="Stage")
            btn = gr.Button("Predict")
            continue_btn = gr.Button("Continue if cancer is detected", visible=False)

            btn.click(run, inputs=image_input, outputs=[image_output, class_output, grade_output, stage_output])
            btn.click(fn=lambda: gr.update(visible=True), inputs=None, outputs=continue_btn)

        with gr.Column(visible=False) as chatbot_app:
            
            Duration = gr.Textbox(label=questions._duration)
            Progression = gr.Textbox(label=questions._gotten_worse)
            Bleeding = gr.Textbox(label=questions._bleeding)
            Swellings = gr.Textbox(label=questions._swelling)
            Persistent_sore = gr.Textbox(label=questions._persistent_sore)
            Smoke = gr.Textbox(label=questions._smoke_)
            Alchohol = gr.Textbox(label=questions._alcohol_)
            Oral_Hygiene=  gr.Textbox(label=questions._brush_floss_)
            Dentist = gr.Textbox(label= questions._dentist)
            Oral_infection = gr.Textbox(label=questions._oral_infection_)
            Lesion_Size = gr.Textbox(label=questions._lesion_size_)
            Lesion_Size_change = gr.Textbox(label=questions._change_in_lesion_size_)
            Lesion_Colour = gr.Textbox(label=questions._lesion_colour_)
            Lesion_Colour_change = gr.Textbox(label=questions._change_in_lesion_colour)
            Lesion_Location = gr.Textbox(label=questions._lesion_location)
            Lymph_Node_Involvements = gr.Textbox(label=questions._lymph_node_)
            Overall_Health = gr.Textbox(label=questions._overall_health)
            Family_History = gr.Textbox(label=questions._family_history_of_cancer)
            Medical  = gr.Textbox(label=questions._serious_illness_before)
            Treatment =  gr.Textbox(label=questions._treatment_on_cancer)
            
            
            
            
            
            '''location = gr.Textbox(label="enter the location from the image model")
            grade = gr.Textbox(label="enter the grade from the image model")
            stage = gr.Textbox(label="enter the stage from the image model" )'''
            
            
            
            #output = gr.Textbox(label="Your Answer:")
            patient_cancer = gr.Textbox(label="Patient has the following cancer:")
            
            treatment1 = gr.Textbox(label="Treatment generated from RAG:")
            treatment2 = gr.Textbox(label="Treatment generated from RAG:")
            
            process_btn = gr.Button("Process")

            #process_btn.click(fn=answer, inputs=[symptoms, Duration_and_Progressions, Bleeding_or_Swellings, Lifestyle_and_Habits, Medical_and_Family_History, Oral_Hygiene_and_Dental_History, Lesion_Descriptions, Lymph_Node_Involvements, Biopsy_and_Pathology_Reports, General_Health_and_Functional_Impacts, Overall_Health, Impacts_on_Daily_Life, Treatment_History_and_Responses,grade,stage], outputs=[output, patient_cancer, treatment])
            process_btn.click(fn=answer, inputs=[Duration , Progression , Bleeding , Swellings ,
                                                 Persistent_sore , Smoke , Alchohol , Oral_Hygiene ,
                                                 Dentist , Oral_infection , Lesion_Size , Lesion_Size_change ,
                                                 Lesion_Colour , Lesion_Colour_change , Lesion_Location ,
                                                 Lymph_Node_Involvements , Overall_Health , Family_History ,
                                                 Medical , Treatment], outputs=[patient_cancer, treatment1,treatment2])

        
                
        continue_btn.click(fn=continue_to_chatbot, inputs=None, outputs=[prediction_app, chatbot_app])

    app.launch(server_name="127.0.0.1", server_port=7860)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
##################################################################################################
''' 
#if state["grade"] != 'none' or state["stage"] != 'none':

 #       chatbot.launch(server_name="127.0.0.1", server_port=7861)
'''

'''
import gradio as gr

# Initialize state variables
cancer_var = gr.State([])
grade_var = gr.State([])
stage_var = gr.State([])
def run(image):
    exit_image, class_prediction, grade, stage = image_pred.image_prediction(image)
    # Update the shared state
    grade_var = grade
    stage_var = stage
    
    # Check if cancer is detected
    if grade!= None or stage != None:
        cancer_var.value = 'yes'
    else:
        cancer_var.value = 'no'
    print("grade_var",grade_var,"stage_var",stage_var,"grade",grade,"stage",stage)
    return exit_image, class_prediction, grade, stage

def answer(symptoms, Duration_and_Progressions, Bleeding_or_Swellings, Lifestyle_and_Habits, Medical_and_Family_History, Oral_Hygiene_and_Dental_History, Lesion_Descriptions, Lymph_Node_Involvements, Biopsy_and_Pathology_Reports, General_Health_and_Functional_Impacts, Overall_Health, Impacts_on_Daily_Life, Treatment_History_and_Responses, grade, stage):
    prompt = questions.prompt_return(symptoms, Duration_and_Progressions, Bleeding_or_Swellings, Lifestyle_and_Habits, Medical_and_Family_History, Oral_Hygiene_and_Dental_History, Lesion_Descriptions, Lymph_Node_Involvements, Biopsy_and_Pathology_Reports, General_Health_and_Functional_Impacts, Overall_Health, Impacts_on_Daily_Life, Treatment_History_and_Responses)
    query = f"what would be the grade on the basis of following prompt : {prompt}" + f"the grade is predicted from the model is {grade} and the stage {stage}"
    cancer, final_answer = RAG.RAG_output(query)
    return str(query), cancer, final_answer

# Function to handle the "Continue" button click
def continue_to_chatbot():
    return gr.update(visible=False), gr.update(visible=True)

with gr.Blocks() as app:
    with gr.Row():
        with gr.Column(visible=True) as prediction_app:
            gr.Markdown("# Disease Prediction App")
            image_input = gr.Image(type="pil")
            image_output = gr.Image()
            class_output = gr.Textbox(label="Observation")
            grade_output = gr.Textbox(label="Grade")
            stage_output = gr.Textbox(label="Stage")
            btn = gr.Button("Predict")
            continue_btn = gr.Button("Continue if cancer is detected", visible=False)

            btn.click(run, inputs=image_input, outputs=[image_output, class_output, grade_output, stage_output])
            btn.click(fn=lambda: gr.update(visible=True), inputs=None, outputs=continue_btn)

        with gr.Column(visible=False) as chatbot_app:
            
            
            cancer_grade =  str(grade_var)
            cancer_stage =  str(stage_var)
            print("cancer_grade",cancer_grade)
            print("cancer_grade",cancer_grade)
            symptoms = gr.Textbox(label=questions.symptoms_ques)
            Duration_and_Progressions = gr.Textbox(label=questions.Duration_and_Progression_ques)
            Bleeding_or_Swellings = gr.Textbox(label=questions.Bleeding_or_Swelling_ques)
            Lifestyle_and_Habits = gr.Textbox(label=questions.Lifestyle_and_Habits_ques)
            Medical_and_Family_History = gr.Textbox(label=questions.Medical_and_Family_History_ques)
            Oral_Hygiene_and_Dental_History = gr.Textbox(label=questions.Oral_Hygiene_and_Dental_History_ques)
            Lesion_Descriptions = gr.Textbox(label=questions.Lesion_Description_ques)
            Lymph_Node_Involvements = gr.Textbox(label=questions.Lymph_Node_Involvement_ques)
            Biopsy_and_Pathology_Reports = gr.Textbox(label=questions.Biopsy_and_Pathology_Reports_ques)
            General_Health_and_Functional_Impacts = gr.Textbox(label=questions.General_Health_and_Functional_Impact_ques)
            Overall_Health = gr.Textbox(label=questions.Overall_Health_ques)
            Impacts_on_Daily_Life = gr.Textbox(label=questions.Impact_on_Daily_Life_ques)
            Treatment_History_and_Responses = gr.Textbox(label=questions.Treatment_History_and_Response_ques)
            grade = gr.Textbox(label="grade", value=cancer_grade)
            stage = gr.Textbox(label="stage", value=cancer_stage)
            
            output = gr.Textbox(label="Your Answer:")
            patient_cancer = gr.Textbox(label="Patient has the following cancer:")
            treatment = gr.Textbox(label="Treatment generated from RAG:")
            process_btn = gr.Button("Process")
            

            process_btn.click(fn=answer, inputs=[symptoms, Duration_and_Progressions, Bleeding_or_Swellings, Lifestyle_and_Habits, Medical_and_Family_History, Oral_Hygiene_and_Dental_History, Lesion_Descriptions, Lymph_Node_Involvements, Biopsy_and_Pathology_Reports, General_Health_and_Functional_Impacts, Overall_Health, Impacts_on_Daily_Life, Treatment_History_and_Responses, grade, stage], outputs=[output, patient_cancer, treatment])

        continue_btn.click(fn=continue_to_chatbot, inputs=None, outputs=[prediction_app, chatbot_app])

    app.launch(server_name="127.0.0.1", server_port=7860)
'''