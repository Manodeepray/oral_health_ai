from tools import tools
import cv2
import os
from PIL import Image

    


def image_prediction(image):
    
    
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
    
    print(initial_pred)
    
    class_prediction  = tools.predict_class(initial_pred,class_label)
    
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
        
        filename2 = os.listdir(os.path.join(o_folder,o_file2))[0]
        
        filename3 = os.listdir(os.path.join(o_folder,o_file3))[0]
        
        filename4 = os.listdir(os.path.join(o_folder,o_file4))[0]
        
        filename5 = os.listdir(os.path.join(o_folder,o_file5))[0]
        
        
        output_image_path_2 = os.path.join(o_folder,o_file2,filename2)
        output_image_path_3 = os.path.join(o_folder,o_file3,filename3)
        output_image_path_4 = os.path.join(o_folder,o_file4,filename4)
        output_image_path_5 = os.path.join(o_folder,o_file5,filename5)
        
        
        output_image_paths =[output_image_path_2,output_image_path_3,output_image_path_4,output_image_path_5]   # Replace with your image paths
        output_images = []
        for item in output_image_paths:
            image = Image.open(item)
            output_images.append(image)
        
        collage = tools.create_collage(output_images, 2, 2)  # 2 rows, 3 columns
        
        
            
        exit_image_path = "utils/collage.jpg"
        collage.save(exit_image_path)
            
            
        exit_image = cv2.imread(exit_image_path)
            
            
        os.remove(exit_image_path)
        os.remove(output_image_path_2)
        os.remove(output_image_path_3)
        os.remove(output_image_path_4)
        os.remove(output_image_path_5)
        
        cancer_message = f"{pred_cancer} is detected in the {pred_region} region , it is determined to be of {pred_grade} and {pred_stage} "
            
        
        return exit_image , cancer_message ,  pred_grade , pred_stage ,pred_region
    
    else:
        exit_image_path = os.path.join(o_folder,o_file1,
                                        os.listdir(os.path.join(o_folder,o_file1))[0])
        exit_image = cv2.imread(exit_image_path)
        os.remove(exit_image_path)
        pred_grade = 'none'
        pred_stage = 'none'
        pred_region = 'none'
        return exit_image , class_prediction , pred_grade , pred_stage ,pred_region