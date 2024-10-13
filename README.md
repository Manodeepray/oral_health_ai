---
---

# 🦷 OralCare.ai : Oral Cancer Diagnosis Web App using RAG and YOLOv8

Welcome to the repository for the **OralCare.ai**. This web app integrates cutting-edge AI technologies such as **Retrieval-Augmented Generation (RAG)** and **YOLOv8** to assist in diagnosing and evaluating oral diseases. The system is designed to streamline both **image classification** and **symptom-based prediction**, providing a comprehensive tool for medical professionals.

## 📝 Project Overview

This project aims to tackle the challenge of early oral cancer diagnosis using two main approaches:

1. **Image Classification**: Using **YOLOv8** for identifying and classifying oral lesions from images.
2. **Symptom-Based Prediction**: Implementing a **RAG (Retrieval-Augmented Generation) model** to predict cancer grades based on user symptoms and domain-specific PDFs.

## 🌟 Key Features

- **YOLOv8n**: Efficient, lightweight model for image classification of oral lesions.
- **RAG Model**: A hybrid system combining **Large Language Models (LLMs)** and **retrieval-based techniques** to make predictions based on user inputs and medical literature.
- **Symptom Matching**: Matches patient-reported symptoms with a database of medical records to evaluate cancer grade.
- **Web Interface with Gradio**: Simple and interactive web app for users to upload images and enter symptoms.

## 💻 Technologies Used

- **YOLOv8**: For image classification of oral lesions.
- **Retrieval-Augmented Generation (RAG)**: For symptom-based cancer grade prediction.
- **Gradio**: For building the web interface.
- **LangChain**: Used to integrate the RAG model with document retrieval.
- **Mistral 7B**: Lightweight LLM for question-answering on medical data.
- **TensorFlow**: Used in image processing and model development.

## 🚀 Getting Started

### Prerequisites

Before setting up the project, ensure that the following are installed:

- Python 3.8+
- TensorFlow 2.x
- Gradio
- LangChain
- OpenAI's Mistral 7B model

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Manodeepray/oral_health_ai.git
   cd oral_health_ai
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the Mistral 7B model or any other of ur choice**:

   - Follow the instructions [here](https://huggingface.co/mistral7b) to get the model inference end-point.
   - Get your own Huggingface API token by following the instructions [here](https://huggingface.co/docs/hub/en/security-tokens)
   - Update the `HUGGINGFACEHUB_API_TOKEN` variable in `tools/keys.py` with your token as well as on line 219 and 229.

   ```python
    def RAG_cancer_output(grade_query , stage_query):
        login(token="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") #replace with ur own token
        HUGGINGFACEHUB_API_TOKEN = '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'

   ```

   - Update the model-id in the `tools/RAG.py` file on line 99.

   ```python
    llms = ["meta-llama/Meta-Llama-3-8B","mistralai/Mistral-7B-v0.1","google/gemma-7b"]

   ```

4. **Download the oral lesion image dataset** (if available) or use your own images.

5. **Run the app**:

   ```bash
   python app.py
   ```

6. **Open the Web App**:

   The app will run locally. Visit [http://localhost:7860](http://localhost:7860) to access the web interface.

## 🛠️ File Structure

```
📂 oral-cancer-webapp/
│
│
├──📁src/
    ├── 📁 pdfs/                        # Contains medical PDFs for RAG model
    ├── 📁 models/                      # Trained YOLOv8n models for image classification
    ├── 📁 test_imfs_for_pred/          # Contains testing images for app
|
|
|
├──📁utils/
    ├── 📁 predict1/                     # Contains initial prediction of image for oral diseases
    ├── 📁 predict2/                     # Contains class prediction of image for oral cancer or none
    ├── 📁 predict3/                     # Contains region prediction of image for oral cancer
    ├── 📁 predict4/                     # Contains grade prediction of image for oral cancer
    └── 📁 predict5/                     # Contains stage prediction of image for oral cancer
|
|
|
├──📁tools/
    ├── image_pred.py
    ├── keys.py
    ├── questions.py
    ├── RAG.py
    ├── test_cleaner.py
    └── tools.py
|
|
|
├──📁runs/
    └──📁classify/
       └──📁utils/      #contains temp YOLO outputs
|
│
├── app.py                          # Main web application script using Gradio
├── chatbot.py                    # RAG model app for symptom-based query handling
├── image_app.py                    # image ai app for classification and detection of cancer / diseases
├── combined.py                    # test webapp for combining the apps
├── README.md                       # Documentation file
└── requirements.txt                # Python dependencies
```

## 📊 Methodology

### Image Classification using YOLOv8

The **YOLOv8n** model is trained on a custom dataset of oral lesion images. The model is able to:

- Detect oral lesions in uploaded images.
- Classify lesions as potentially malignant or benign.
- Provide visual feedback by drawing bounding boxes around detected lesions.

### Symptom-Based Cancer Prediction using RAG

The **RAG model** combines **Mistral 7B**, a powerful language model, with document retrieval capabilities. It:

1. Retrieves relevant information from medical PDFs based on patient-reported symptoms.
2. Uses the LLM to process and answer queries related to **oral cancer diagnosis** and **cancer grade evaluation**.
3. Returns a **cancer grade prediction** based on both symptom analysis and retrieved documents.

### Web Interface with Gradio

The user-friendly web interface built with **Gradio** allows users to:

- **Upload oral lesion images** for automatic classification.
- **Input symptoms** for text-based diagnosis and grade prediction.
- **Receive detailed predictions** along with explanations.

## ⚙️ Model Performance

The following metrics were used to evaluate the models:

- **Accuracy**: Measures the correct classification of lesions in images.
- **Precision, Recall, F1-Score**: For detecting malignancy from image data.
- **pAUC Score**: Applied in the RAG model to evaluate prediction accuracy against the gold standard (medical PDFs).

**YOLOv8n** achieved an accuracy of **85%** in detecting malignant lesions, while the **RAG model** demonstrated a **90% pAUC score** in predicting cancer grade based on symptoms.

## 📈 Future Enhancements

- **Dataset Expansion**: Collect more oral lesion images to improve YOLOv8’s classification accuracy.
- **Fine-Tuning**: Continue fine-tuning Mistral 7B with specialized oral cancer data to improve text-based predictions.
- **Dashboard for Medical Professionals**: Implement a **dashboard** where doctors can track patient data and predictions over time.

## 📜 License

This project is licensed under the CC License.

## 🙌 Acknowledgments

This project was completed during a summer internship at **IIT Bhilai**, with guidance from **Dr. Archana Tiwari**. The **Mistral 7B** LLM and **YOLOv8n** were crucial components in achieving high-performance metrics for cancer diagnosis.

## 📨 Contact

For any questions or further collaboration, please reach out:  
**Manodeep Ray**  
Email: [manodeepray1@gmail.com](mailto:manodeepray1@gmail.com)

---

_We hope this app will contribute to advancing early diagnosis of oral cancer with AI._

---

---

title: OralCare.ai
emoji: 🏃
colorFrom: red
colorTo: blue
sdk: gradio
sdk_version: 4.37.2
app_file: app.py
pinned: false
license: cc

---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
