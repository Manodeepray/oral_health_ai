from ultralytics import YOLO
import os 
import cv2

from PIL import Image




class initialise_models:
    def __init__(self,oral_disease_cls_model_path,
                 cancer_det_model_path,
                 region_det_model_path,
                 grading_model_path,
                 staging_model_path):
        
        self.oral_disease_cls_model_path = oral_disease_cls_model_path   
        self.cancer_det_model_path = cancer_det_model_path
        self.region_det_model_path = region_det_model_path
        self.grading_model_path = grading_model_path
        self.staging_model_path = staging_model_path
        return None
    
    def oral_disease_cls_model(self):
        model = self.oral_disease_cls_model_path
        model = YOLO(model)
        return model
    
    def cancer_det_model(self):
        model = self.cancer_det_model_path
        model = YOLO(model)
        return model
    
    def region_det_model(self):
        model = self.region_det_model_path
        model = YOLO(model)
        return model
    
    def grading_model(self):
        model = self.grading_model_path
        model = YOLO(model)
        return model
    
    def staging_model(self):
        model = self.staging_model_path
        model = YOLO(model)
        return model

        
    
    


def create_collage(images, rows, cols):

    total_images = len(images)
    print(total_images)
    if total_images != rows * cols:
        raise ValueError("Number of images must be divisible by rows * cols")

  # Get individual image size
    width, height = 800,800
    
  # Create a new image for the collage
    collage_width = width * cols
    collage_height = height * rows
    collage_image = Image.new("RGB", (collage_width, collage_height))

  # Paste each image into the collage
    for i in range(total_images):
        row = i // cols
        col = i % cols
        collage_image.paste(images[i], (col * width, row * height))

    return collage_image

def load_model_initial_classification(directory):
    directory1 = directory
    model = YOLO(directory1)
    return model

def predict_image(model,image,output_folder,output_file ):
    prediction = model.predict(image ,save = True,
                               project = output_folder ,name = output_file, exist_ok=True)
    
    return  prediction 
    
    
def predict_class(prediction , class_label):
    
    for result in prediction:
        pred = result
    
    class_prediction = class_label[pred.probs.top1]
    return class_prediction




'''
def run(image):
    
    
    directory = "src/best_yolov8_5_class_augmented.pt"
    model = load_model_initial_classification(directory)
    class_label ={0: 'dental_caries', 1: 'healthy', 2: 'oral_cancer', 3: 'periodontal', 4: 'scurvy'}
    file_path = "src/test_imgs_for_pred/cancer (83).jpg"
    o_folder = "utils"
    o_file = "predict"
    class_prediction , prediction  = predict_class(model = model,
                                                   image = file_path ,
                                                   output_folder = o_folder ,
                                                  class_label = class_label )
    
    print(class_prediction)
    exit_image_path = os.path.join(o_folder,o_file,
                                   os.listdir(os.path.join(o_folder,o_file))[0])
    
    exit_image = cv2.imread(exit_image_path)
    os.remove(exit_image_path)
    return exit_image


if __name__=="__main__":
    image = run(image="src\test_imgs_for_pred\dental_caries (38).jpeg")
    
    print(image)
'''