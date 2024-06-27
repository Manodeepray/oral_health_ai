import gradio as gr
from tools import questions, RAG, image_pred

# Shared state for grade and stage
global stage_var ; 'None'
global grade_var ; 'None'

def run(image):
    exit_image, class_prediction, grade, stage = image_pred.image_prediction(image)
    # Update the shared state
    stage_var = grade
    grade_var = stage
    
    return exit_image, class_prediction, grade, stage

def answer(symptoms, Duration_and_Progressions, Bleeding_or_Swellings, Lifestyle_and_Habits, Medical_and_Family_History, Oral_Hygiene_and_Dental_History, Lesion_Descriptions, Lymph_Node_Involvements, Biopsy_and_Pathology_Reports, General_Health_and_Functional_Impacts, Overall_Health, Impacts_on_Daily_Life,
           Treatment_History_and_Responses,grade,stage):
    prompt = questions.prompt_return(symptoms, Duration_and_Progressions, Bleeding_or_Swellings, Lifestyle_and_Habits, Medical_and_Family_History, Oral_Hygiene_and_Dental_History, Lesion_Descriptions, Lymph_Node_Involvements, Biopsy_and_Pathology_Reports, General_Health_and_Functional_Impacts, Overall_Health, Impacts_on_Daily_Life, Treatment_History_and_Responses)
    query = f"what would be the grade on the basis of following prompt : {prompt}"+f"the grade is predicted from the model is {grade} and the stage {stage}"
    cancer, final_answer = RAG.RAG_output(query)
    return str(prompt), cancer, final_answer

# Function to handle the "Continue" button click
def continue_to_chatbot():
    return (gr.update(visible=False), gr.update(visible=True))

with gr.Blocks() as app:
    with gr.Row():
        with gr.Column() as prediction_app:
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

        with gr.Column() as chatbot_app:
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

            output = gr.Textbox(label="Your Answer:")
            patient_cancer = gr.Textbox(label="Patient has the following cancer:")
            treatment = gr.Textbox(label="Treatment generated from RAG:")
            process_btn = gr.Button("Process")
            grade = gr.Textbox(label="grade" , value=  stage_var)
            stage = gr.Textbox(label="stage" , value=  grade_var)
            process_btn.click(fn=answer, inputs=[symptoms, Duration_and_Progressions, Bleeding_or_Swellings, Lifestyle_and_Habits, Medical_and_Family_History, Oral_Hygiene_and_Dental_History, Lesion_Descriptions, Lymph_Node_Involvements, Biopsy_and_Pathology_Reports, General_Health_and_Functional_Impacts, Overall_Health, Impacts_on_Daily_Life, Treatment_History_and_Responses,grade,stage], outputs=[output, patient_cancer, treatment])

        
                

    app.launch(server_name="127.0.0.1", server_port=7860)

'''
if state["grade"] != 'none' or state["stage"] != 'none':

        chatbot.launch(server_name="127.0.0.1", server_port=7861)
'''