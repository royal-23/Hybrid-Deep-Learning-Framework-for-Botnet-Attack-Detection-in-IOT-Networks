A Hybrid Deep Learning Framework for Botnet Attack Detection in IoT Networks

Overview

The rapid growth of Internet of Things (IoT) devices has increased the risk of cyberattacks, particularly botnet attacks that exploit vulnerable devices. Traditional security mechanisms often struggle to detect evolving attack patterns effectively.

This project presents a Hybrid Deep Learning Framework that combines Deep Neural Networks (DNN) and Random Forest to improve botnet attack detection in IoT environments. The hybrid model leverages the pattern-learning capability of deep learning and the classification strength of ensemble learning to achieve higher detection accuracy and reduced false positives.

---

Features

- IoT Network Traffic Analysis
- Data Preprocessing and Feature Extraction
- Random Forest Classifier
- Deep Neural Network (DNN)
- Hybrid Stacking-Based Ensemble Model
- Detection of Multiple Attack Categories
- Interactive Web Interface
- Performance Evaluation using:
  - Accuracy
  - ROC-AUC
  - PR-AUC

---

Problem Statement

Botnet attacks pose significant threats to IoT networks by compromising connected devices and launching malicious activities such as:

- Distributed Denial of Service (DDoS)
- Data Theft
- Unauthorized Access
- Reconnaissance Attacks

Traditional signature-based detection systems are ineffective against new and evolving attack patterns. This project addresses the challenge through an intelligent hybrid machine learning approach.

---

Dataset

UNSW-NB15 Dataset

The system is trained and evaluated using the UNSW-NB15 dataset containing both normal and malicious network traffic records.

Attack categories include:

- Normal
- Generic
- Exploits
- Fuzzers
- DoS
- Reconnaissance
- Analysis
- Backdoor
- Shellcode
- Worms

---

Methodology

Workflow

1. Data Collection
2. Data Preprocessing
3. Feature Extraction
4. Model Training
5. Hybrid Model Creation
6. Model Evaluation
7. Prediction & Classification
8. Result Display

Hybrid Model Architecture

Input Dataset (UNSW-NB15)
↓
Data Preprocessing
↓
Feature Selection
↓
Random Forest Model
+
Deep Neural Network (DNN)
↓
Stacking Ensemble
↓
Prediction
↓
Botnet / Normal Classification

---

Technologies Used

Frontend

- HTML
- CSS
- Bootstrap
- JavaScript

Backend

- Python
- Flask

Machine Learning

- TensorFlow / Keras
- Scikit-learn
- NumPy
- Pandas

Database

- MySQL

Development Tools

- Visual Studio Code
- PyCharm
- XAMPP Server

---

Installation

Clone Repository

git clone https://github.com/your-username/Hybrid-Deep-Learning-Framework-for-Botnet-Attack-Detection-in-IOT-Networks.git
cd Hybrid-Deep-Learning-Framework-for-Botnet-Attack-Detection-in-IOT-Networks

Create Virtual Environment

python -m venv venv

Activate Environment

Windows:

venv\Scripts\activate

Install Dependencies

pip install -r requirements.txt

Run Application

python app.py

---

Model Evaluation Metrics

The system evaluates performance using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC
- PR-AUC

The hybrid model demonstrates improved detection performance compared to standalone machine learning models.

---

Advantages

- Higher Detection Accuracy
- Reduced False Positives
- Better Generalization
- Robust Classification
- Scalable for Large IoT Networks
- Capable of Detecting Multiple Attack Types
- Improved Reliability Through Ensemble Learning

---

Future Scope

- Real-Time Network Monitoring
- Cloud-Based Deployment
- Integration with IDS/IPS Systems
- Federated Learning for Distributed IoT Networks
- Advanced Deep Learning Architectures
- Automated Threat Intelligence Integration

---

License

This project is developed for academic and educational purposes as part of the Bachelor of Technology (Cyber Security) curriculum

---

Note:
Large trained model files (hybrid_model.pkl and random_forest_model-evo-intel.pkl) are excluded from the repository due to GitHub file size limitations. The source code, training pipeline, and model architecture are included.

---
