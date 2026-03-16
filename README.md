# 🧠 Brain AI Diagnostic System
An advanced, end-to-end clinical decision support platform designed to classify brain tumors from MRI scans using Deep Learning, featuring Explainable AI (XAI) and automated clinical reporting.

🔗 **Live Application:** [Live Application](https://brain-tumor-classification-app-mfjdrzoaefkappjxhjm7cdp.streamlit.app)

## 🌟 Key Features
* **High-Accuracy Classification:** Utilizes Transfer Learning (ResNet50 & EfficientNetB0) to classify MRI scans into four categories (Glioma, Meningioma, Pituitary, or No Tumor) with high accuracy.
* **Explainable AI (Grad-CAM):** Generates visual heatmaps highlighting the exact regions of the MRI that led to the model's prediction, providing essential clinical transparency.
* **Automated PDF Reports:** Instantly generates official, downloadable diagnostic reports containing patient details, confidence scores, and side-by-side comparative scans.
* **Instant Specialist Alerts:** Integrates with the Telegram API to push immediate clinical alerts (including original and Grad-CAM images) directly to healthcare professionals' devices.

## 📊 Dataset
The models were trained and rigorously evaluated using the official **[BRISC 2025 Dataset](https://www.kaggle.com/datasets/briscdataset/brisc2025)** sourced from Kaggle. This comprehensive dataset ensures a robust and diverse collection of MRI neuroimaging data, enabling the system to achieve high generalization and accuracy in clinical scenarios.

## 🛠️ Technology Stack
* **Deep Learning:** TensorFlow, Keras (ResNet50, EfficientNetB0)
* **Computer Vision:** OpenCV, PIL, Grad-CAM Algorithm
* **Frontend & Cloud Deployment:** Streamlit, Streamlit Community Cloud
* **Data Handling & Reporting:** Numpy, FPDF, Matplotlib
* **APIs:** Telegram Bot API

## 👨‍💻 Developed By
This project was developed by a dedicated Brain AI Research Team as an advanced deep learning initiative, bridging the gap between Artificial Intelligence and Healthcare.
