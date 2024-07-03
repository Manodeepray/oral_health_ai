import gradio as gr
from tools import questions, RAG, image_pred

# Shared state for grade and stage
state = {"grade": "none", "stage": "none"}

def run(image):
    exit_image, class_prediction, grade, stage, location= image_pred.image_prediction(image)
    
    grade = grade.replace('_', ' ')
    stage = stage.replace('_', ' ')
    location = location.replace('_', ' ')

    
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
    cancer = "cancer is present on "+location+f" and of {grade} and {stage}"
    
    return exit_image, class_prediction, grade, stage ,location,cancer, final_answer

    

# Function to handle the "Continue" button click
def continue_to_chatbot():
    return (gr.update(visible=False), gr.update(visible=True))

with gr.Blocks() as app:
    with gr.Row():
        with gr.Column(visible=True) as prediction_app:
            gr.Markdown("# Disease Prediction App")
            image_input = gr.Image(type="pil")
            image_output = gr.Image()
            class_output = gr.Textbox(label="Observation")
            grade_output = gr.Textbox(label="Grade")
            stage_output = gr.Textbox(label="Stage")
            location_output = gr.Textbox(label="Location")
            cancer_output = gr.Textbox(label="Cancer")
            treatment_output = gr.Textbox(label="Treatment")
            btn = gr.Button("Predict")
            continue_btn = gr.Button("Continue if cancer is detected", visible=False)

            btn.click(run, inputs=image_input, outputs=[image_output, class_output, grade_output, stage_output,location_output,cancer_output,treatment_output])
            
    app.launch(server_name="127.0.0.1", server_port=7860)






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