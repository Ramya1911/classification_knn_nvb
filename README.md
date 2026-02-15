<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Iris Flower Classification Project</title>
</head>

<body style="font-family: Arial, sans-serif; line-height:1.7; background-color:#f4f7fc; padding:40px; color:#2c3e50;">

<!-- HEADER -->
<div style="background: linear-gradient(135deg,#667eea,#764ba2); padding:40px; border-radius:12px; color:white; text-align:center;">
<h1 style="margin:0;">Iris Flower Classification Project</h1>
<h2 style="margin:10px 0 0 0; font-weight:300;">Using K-Nearest Neighbors and Gaussian Naive Bayes</h2>
<p style="margin-top:15px;">Comprehensive Project Documentation</p>
</div>

<br><br>

<!-- TABLE OF CONTENTS -->
<div style="background:white; padding:25px; border-radius:10px;">
<h2>Table of Contents</h2>
<ol>
<li>Acknowledgements</li>
<li>Project Overview</li>
<li>Dataset Description</li>
<li>Project Structure</li>
<li>Technology Stack</li>
<li>Implementation Steps</li>
<li>Code Explanation</li>
<li>Model Development</li>
<li>Deployment Process</li>
<li>Results and Output</li>
<li>Challenges and Solutions</li>
<li>Future Enhancements</li>
<li>Conclusion</li>
<li>References</li>
</ol>
</div>

<br>

<!-- 1 -->
<div style="background:white; padding:25px; border-radius:10px;">
<h2>1. Acknowledgements</h2>

<p><strong>Dataset Name:</strong> Iris Dataset</p>
<p><strong>Source:</strong> UCI Machine Learning Repository</p>
<p><strong>Original Contributor:</strong> R.A. Fisher</p>

<p><strong>Tools Used:</strong><br>
Flask, Scikit-learn, NumPy, Pandas, Pickle, JSON, HTML, CSS, Render, GitHub
</p>

<p>Special thanks to open-source contributors and deployment platform Render.</p>
</div>

<br>

<!-- 2 -->
<div style="background:white; padding:25px; border-radius:10px;">
<h2>2. Project Overview</h2>

<p><strong>Objective:</strong><br>
Develop a machine learning web application that classifies iris flowers based on four input features and allows the user to choose between two algorithms: K-Nearest Neighbors (KNN) and Gaussian Naive Bayes (NVB).
</p>

<p><strong>Key Features:</strong></p>
<ul>
<li>Dual algorithm selection using two submit buttons</li>
<li>Real-time prediction</li>
<li>Separate Train and Test metrics display</li>
<li>Confusion matrix displayed as aligned matrix</li>
<li>Classification report displayed as table</li>
<li>Metrics loaded dynamically from JSON files</li>
<li>Deployment-ready Flask application</li>
</ul>
</div>

<br>

<!-- 3 -->
<div style="background:white; padding:25px; border-radius:10px;">
<h2>3. Dataset Description</h2>

<p><strong>Total Records:</strong> 150</p>
<p><strong>Features:</strong> 4 numerical features</p>
<p><strong>Target Classes:</strong> 3 species</p>

<p><strong>Input Features:</strong></p>
<ul>
<li>Sepal Length (cm)</li>
<li>Sepal Width (cm)</li>
<li>Petal Length (cm)</li>
<li>Petal Width (cm)</li>
</ul>

<p><strong>Target Variable:</strong></p>
<ul>
<li>Iris-setosa</li>
<li>Iris-versicolor</li>
<li>Iris-virginica</li>
</ul>

<p><strong>Preprocessing Steps:</strong></p>
<ul>
<li>Dropped 'Id' column</li>
<li>Converted species names to numeric mapping (1,2,3)</li>
<li>Split dataset into training (80%) and testing (20%)</li>
</ul>
</div>

<br>

<!-- 4 -->
<div style="background:white; padding:25px; border-radius:10px;">
<h2>4. Project Structure</h2>

<pre style="background:#f4f4f4; padding:15px; border-radius:8px;">
Classification_knn_nvb/
│
├── app.py
├── requirements.txt
├── models/
│   ├── Iris_classification_knn.pkl
│   └── Iris_classification_nvb.pkl
├── metrics/
│   ├── train_metrics_knn.json
│   ├── test_metrics_knn.json
│   ├── train_metrics_nvb.json
│   └── test_metrics_nvb.json
├── templates/index.html
└── static/style.css
</pre>
</div>

<br>

<!-- 5 -->
<div style="background:white; padding:25px; border-radius:10px;">
<h2>5. Technology Stack</h2>

<h3>Backend</h3>
<ul>
<li>Python</li>
<li>Flask</li>
<li>Scikit-learn</li>
<li>Pandas</li>
<li>NumPy</li>
<li>Pickle</li>
<li>JSON</li>
</ul>

<h3>Frontend</h3>
<ul>
<li>HTML5</li>
<li>CSS3</li>
</ul>

<h3>Deployment</h3>
<ul>
<li>Git</li>
<li>GitHub</li>
<li>Render</li>
<li>Gunicorn</li>
</ul>
</div>

<br>

<!-- 6 -->
<div style="background:white; padding:25px; border-radius:10px;">
<h2>6. Implementation Steps</h2>

<h3>Step 1: Environment Setup</h3>
<code>python -m venv venv</code><br>
<code>venv\Scripts\activate</code><br>
<code>pip install flask numpy pandas scikit-learn gunicorn</code>

<h3>Step 2: Model Training</h3>
<ul>
<li>Load dataset using Pandas</li>
<li>Preprocess data and encode species</li>
<li>Split data using train_test_split</li>
<li>Train KNN (n_neighbors=3)</li>
<li>Train Gaussian Naive Bayes</li>
<li>Evaluate using accuracy, confusion matrix, classification report</li>
<li>Save models (.pkl)</li>
<li>Save metrics (.json)</li>
</ul>

<h3>Step 3: Deployment</h3>
<ul>
<li>Push project to GitHub</li>
<li>Connect repository to Render</li>
<li>Build Command: pip install -r requirements.txt</li>
<li>Start Command: gunicorn app:app</li>
</ul>
</div>

<br>

<!-- 7 -->
<div style="background:white; padding:25px; border-radius:10px;">
<h2>7. Model Development</h2>

<h3>K-Nearest Neighbors</h3>
<ul>
<li>Distance-based algorithm</li>
<li>n_neighbors = 3</li>
<li>Effective for small structured datasets</li>
</ul>

<h3>Gaussian Naive Bayes</h3>
<ul>
<li>Probabilistic classifier</li>
<li>Assumes conditional independence</li>
<li>Fast and efficient</li>
</ul>

<h3>Evaluation Metrics</h3>
<ul>
<li>Accuracy</li>
<li>Confusion Matrix</li>
<li>Precision</li>
<li>Recall</li>
<li>F1-Score</li>
</ul>
</div>

<br>

<!-- 8 -->
<div style="background:white; padding:25px; border-radius:10px;">
<h2>8. Results and Output</h2>

<p><strong>Sample Input:</strong></p>
<ul>
<li>Sepal Length: 5.2</li>
<li>Sepal Width: 7</li>
<li>Petal Length: 1.4</li>
<li>Petal Width: 0.5</li>
</ul>

<p><strong>Output:</strong> Iris-setosa</p>
</div>

<br>

<!-- 9 -->
<div style="background:white; padding:25px; border-radius:10px;">
<h2>9. Challenges and Solutions</h2>
<ul>
<li>JSON serialization error → Converted numpy arrays to lists</li>
<li>Matrix alignment issue → Used HTML tables</li>
<li>Algorithm detection → Used named submit buttons</li>
<li>Deployment path issues → Used relative paths</li>
</ul>
</div>

<br>

<!-- 10 -->
<div style="background:white; padding:25px; border-radius:10px;">
<h2>10. Future Enhancements</h2>
<ul>
<li>Add heatmap visualization</li>
<li>Add accuracy comparison graph</li>
<li>Improve UI responsiveness</li>
<li>Add prediction history storage</li>
<li>Implement API endpoints</li>
</ul>
</div>

<br>

<!-- 11 -->
<div style="background:white; padding:25px; border-radius:10px;">
<h2>11. Conclusion</h2>
<p>This project demonstrates a complete machine learning deployment pipeline integrating:</p>
<ul>
<li>Dual algorithm model training</li>
<li>JSON-based metric storage</li>
<li>Flask backend development</li>
<li>HTML/CSS frontend integration</li>
<li>Cloud deployment using Render</li>
</ul>
</div>

<br>

<!-- 12 -->
<div style="background:white; padding:25px; border-radius:10px;">
<h2>12. References</h2>
<ul>
<li>Flask Documentation</li>
<li>Scikit-learn Documentation</li>
<li>Render Documentation</li>
<li>UCI Machine Learning Repository</li>
</ul>
</div>

<br><br>

<div style="text-align:center;">
<h2>KAMMARI RAMYA</h2>
<p>Data Science and NLP Student</p>
</div>

</body>
</html>

