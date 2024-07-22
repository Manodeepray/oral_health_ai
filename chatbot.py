import gradio as gr
from tools import questions
from tools import RAG
def answer(   symptoms ,Duration_and_Progressions ,Bleeding_or_Swellings ,Lifestyle_and_Habits ,Medical_and_Family_History ,Oral_Hygiene_and_Dental_History ,Lesion_Descriptions , Lymph_Node_Involvements ,Biopsy_and_Pathology_Reports , General_Health_and_Functional_Impacts , Overall_Health ,Impacts_on_Daily_Life ,Treatment_History_and_Responses ):
    prompt = questions.prompt_return(symptoms ,Duration_and_Progressions ,
                  Bleeding_or_Swellings ,Lifestyle_and_Habits ,
                  Medical_and_Family_History ,Oral_Hygiene_and_Dental_History ,
                  Lesion_Descriptions ,Lymph_Node_Involvements ,
                  Biopsy_and_Pathology_Reports , General_Health_and_Functional_Impacts , 
                  Overall_Health ,Impacts_on_Daily_Life ,
                  Treatment_History_and_Responses )
    query = f"""what would be the grade on the basis of following prompt : {prompt}"""
    cancer,final_answer = RAG.RAG_output(query)
    
    return str(prompt)  , cancer, final_answer




with gr.Blocks() as chatbot:
    

    symptoms = gr.Textbox(label= questions.symptoms_ques)

    Duration_and_Progressions =  gr.Textbox(label=questions.Duration_and_Progression_ques)
    Bleeding_or_Swellings = gr.Textbox(label=questions.Bleeding_or_Swelling_ques)

    Lifestyle_and_Habits = gr.Textbox(label=questions.Lifestyle_and_Habits_ques)
    Medical_and_Family_History = gr.Textbox(label=questions.Medical_and_Family_History_ques)
    Oral_Hygiene_and_Dental_History = gr.Textbox(label=questions.Oral_Hygiene_and_Dental_History_ques)
    Lesion_Descriptions = gr.Textbox(label=questions.Lesion_Description_ques)
    Lymph_Node_Involvements = gr.Textbox(label=questions.Lymph_Node_Involvement_ques)
    Biopsy_and_Pathology_Reports =gr.Textbox(label=questions.Biopsy_and_Pathology_Reports_ques)
    General_Health_and_Functional_Impacts = gr.Textbox(label=questions.General_Health_and_Functional_Impact_ques)
    Overall_Health = gr.Textbox(label=questions.Overall_Health_ques)
    Impacts_on_Daily_Life = gr.Textbox(label=questions.Impact_on_Daily_Life_ques)
    Treatment_History_and_Responses = gr.Textbox(label= questions.Treatment_History_and_Response_ques)
    
    '''prompt = questions.prompt_return(symptoms ,Duration_and_Progressions ,
                  Bleeding_or_Swellings ,Lifestyle_and_Habits ,
                  Medical_and_Family_History ,Oral_Hygiene_and_Dental_History ,
                  Lesion_Descriptions ,Lymph_Node_Involvements ,
                  Biopsy_and_Pathology_Reports , General_Health_and_Functional_Impacts , 
                  Overall_Health ,Impacts_on_Daily_Life ,
                  Treatment_History_and_Responses )'''
                   
    output = gr.Textbox(label="your answer :")
    patient_cancer = gr.Textbox(label="patient has the following cancer :")
    treatment = gr.Textbox(label="treatment generated from RAG :")
    process_btn = gr.Button("process")
    process_btn.click(fn=answer, inputs= [symptoms ,Duration_and_Progressions ,Bleeding_or_Swellings ,Lifestyle_and_Habits ,Medical_and_Family_History ,Oral_Hygiene_and_Dental_History ,Lesion_Descriptions , Lymph_Node_Involvements ,Biopsy_and_Pathology_Reports , General_Health_and_Functional_Impacts , Overall_Health ,Impacts_on_Daily_Life ,Treatment_History_and_Responses ], outputs=[output,patient_cancer,treatment], api_name="process")

chatbot.launch(debug=True)