import gradio as gr
from utility import tools
import cv2
import os

directory1 = "src/models/initial_5_class_classification.pt"
directory2 = "src/models/cancer_1.pt"
directory3 = "src/models/region_1.pt"
directory4 = "src/models/grade_1.pt"
directory5 = "src/models/stage_1.pt"

models = tools.initialise_models(oral_disease_cls_model_path= directory1,
                                     cancer_det_model_path= directory2,
                                     region_det_model_path= directory3,
                                     grading_model_path= directory4,
                                     staging_model_path= directory5)
    
model1 = models.oral_disease_cls_model()
model2 = models.cancer_det_model()
model3 = models.region_det_model()
model4 = models.grading_model()
model5 = models.staging_model()



class_label ={0: 'dental_caries', 1: 'healthy', 2: 'oral_cancer',
                  3: 'periodontal', 4: 'scurvy'}
    
class_label_cancer = {0:"cancer"}
    
    
class_label_region ={0:'gums',1: 'inner_mouth', 2:'lips', 3:'tongue'}
    
    
class_label_grade ={0: 'grade_1', 1: 'grade_2', 2: 'grade_3'}
    
    
class_label_stage ={0: 'stage_1', 1: 'stage_2', 2: 'stage_3'}
    
    
image = "src/test_imgs_for_pred/cancer (83).jpg"
o_folder = "utils"
o_file1 = "predict1"
o_file2 = "predict2"
o_file3 = "predict3"
o_file4 = "predict4"
o_file5 = "predict5"
    
initial_pred  = tools.predict_image(model = model1,
                                                   image = image ,
                                                   output_folder = o_folder ,
                                                   output_file= o_file1
                                                  )
    
    
class_prediction  = tools.predict_class(initial_pred,class_label=class_label)
    
if class_prediction =="oral_cancer":
    cancer_prediction = tools.predict_image(model = model2,
                                                   image = image ,
                                                   output_folder = o_folder ,
                                                   output_file= o_file2
                                                  )
    #print("region :", cancer_prediction)
    for result in cancer_prediction:
        for box in result.boxes:
            
            pred_cancer = result.names[box.cls[0].item()]
    print("pred_cancer : ",pred_cancer)
    
      
    
     
    region_prediction   = tools.predict_image(model = model3,
                                                   image = image ,
                                                   output_folder = o_folder ,
                                                   output_file= o_file3 )
    
    #print("region :", region_prediction)
    for result in region_prediction:
        for box in result.boxes:
            
            pred_region = result.names[box.cls[0].item()]
    print("pred_region : ",pred_region)
    
    grade_prediction   = tools.predict_image(model = model4,
                                                   image = image ,
                                                   output_folder = o_folder ,
                                                   output_file= o_file4 )
        
    #print("grade :", grade_prediction)
    for result in grade_prediction:
        for box in result.boxes:
            
            pred_grade = result.names[box.cls[0].item()]
    print("pred_grade : ",pred_grade)
    
    
    
    
      
        
        
        
    stage_prediction   = tools.predict_image(model = model5,
                                                   image = image ,
                                                   output_folder = o_folder ,
                                                   output_file= o_file5 )
    
    #print("stage :", stage_prediction)
    for result in stage_prediction:
        for box in result.boxes:
            
            pred_stage = result.names[box.cls[0].item()]

    print("pred_stage : ",pred_stage)
    