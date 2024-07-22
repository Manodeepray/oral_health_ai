import gradio as gr
from tools import image_pred

    


def run(image):
    
    exit_image, class_prediction, grade, stage = image_pred.image_prediction(image)
    
        
    return exit_image, class_prediction, grade, stage

with gr.Blocks() as image_app:
    gr.Markdown("# disease Prediction App")
    
    image_input = gr.Image(type="pil")
    
    image_output = gr.Image()
    
    class_output = gr.Textbox(label= "observation")
    grade_output = gr.Textbox(label="Grade")
    stage_output = gr.Textbox(label="Stage")
    
    btn = gr.Button("Predict")
    
    btn.click(run, inputs=image_input, outputs=[image_output, class_output, grade_output, stage_output])

# Launch the Gradio app
image_app.launch()