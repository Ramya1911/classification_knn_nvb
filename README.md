<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Iris Flower Classification | Portfolio Documentation</title>

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', sans-serif;
    background: #f4f7fc;
    color: #2c3e50;
    line-height: 1.7;
}

header {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    padding: 60px 20px;
    text-align: center;
}

header h1 {
    font-size: 42px;
    margin-bottom: 10px;
}

header h2 {
    font-weight: 300;
}

.container {
    width: 85%;
    margin: auto;
    padding: 40px 0;
}

.section {
    background: white;
    margin-bottom: 30px;
    padding: 30px;
    border-radius: 12px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.05);
    transition: 0.3s ease;
}

.section:hover {
    transform: translateY(-5px);
}

.section h2 {
    margin-bottom: 15px;
    color: #4b4dbf;
    border-bottom: 2px solid #eaeaea;
    padding-bottom: 8px;
}

.section h3 {
    margin-top: 20px;
    margin-bottom: 10px;
    color: #333;
}

ul {
    margin-left: 20px;
}

pre {
    background: #f4f4f4;
    padding: 15px;
    border-radius: 8px;
    overflow-x: auto;
}

code {
    background: #eef2ff;
    padding: 4px 8px;
    border-radius: 5px;
}

table {
    border-collapse: collapse;
    width: 60%;
    margin-top: 10px;
}

table, th, td {
    border: 1px solid #ddd;
}

th, td {
    padding: 8px;
    text-align: center;
}

footer {
    text-align: center;
    padding: 30px;
    background: #2c3e50;
    color: white;
    margin-top: 40px;
}
</style>
</head>

<body>

<header>
    <h1>Iris Flower Classification Project</h1>
    <h2>Using K-Nearest Neighbors & Gaussian Naive Bayes</h2>
    <p>Comprehensive Portfolio Documentation</p>
</header>

<div class="container">

<div class="section">
<h2>1. Acknowledgements</h2>
<p><strong>Dataset:</strong> Iris Dataset (UCI Machine Learning Repository)</p>
<p><strong>Original Contributor:</strong> R.A. Fisher</p>
<p><strong>Tools Used:</strong> Flask, Scikit-learn, NumPy, Pandas, Pickle, JSON, HTML, CSS, Render, GitHub</p>
</div>

<div class="section">
<h2>2. Project Overview</h2>
<p><strong>Objective:</strong> Build a machine learning web application that classifies iris flowers based on four input features and allows users to select between KNN and Gaussian Naive Bayes algorithms.</p>

<h3>Key Features:</h3>
<ul>
<li>Dual algorithm selection (Two submit buttons)</li>
<li>Real-time prediction</li>
<li>Train & Test metrics display</li>
<li>Confusion Matrix as aligned table</li>
<li>Classification report in structured format</li>
<li>Metrics loaded dynamically from JSON</li>
<li>Deployment-ready Flask application</li>
</ul>
</div>

<div class="section">
<h2>3. Dataset Description</h2>
<p><strong>Total Records:</strong> 150</p>
<p><strong>Features:</strong> 4 Numerical Features</p>
<p><strong>Target Classes:</strong> 3 Species</p>

<h3>Input Features:</h3>
<ul>
<li>Sepal Length (cm)</li>
<li>Sepal Width (cm)</li>
<li>Petal Length (cm)</li>
<li>Petal Width (cm)</li>
</ul>

<h3>Preprocessing:</h3>
<ul>
<li>Dropped 'Id' column</li>
<li>Encoded species to numeric (1,2,3)</li>
<li>80% Training / 20% Testing split</li>
</ul>
</div>

<div class="section">
<h2>4. Project Structure</h2>
<pre>
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

<div class="section">
<h2>5. Technology Stack</h2>

<h3>Backend:</h3>
<ul>
<li>Python</li>
<li>Flask</li>
<li>Scikit-learn</li>
<li>Pandas</li>
<li>NumPy</li>
<li>Pickle</li>
<li>JSON</li>
</ul>

<h3>Frontend:</h3>
<ul>
<li>HTML5</li>
<li>CSS3</li>
</ul>

<h3>Deployment:</h3>
<ul>
<li>Git</li>
<li>GitHub</li>
<li>Render</li>
<li>Gunicorn</li>
</ul>
</div>

<div class="section">
<h2>6. Implementation Steps</h2>

<h3>Environment Setup</h3>
<code>python -m venv venv</code><br><br>
<code>venv\Scripts\activate</code><br><br>
<code>pip install flask numpy pandas scikit-learn gunicorn</code>

<h3>Model Training</h3>
<ul>
<li>Load dataset</li>
<li>Preprocess & Encode</li>
<li>Train KNN (n_neighbors=3)</li>
<li>Train GaussianNB</li>
<li>Evaluate using Accuracy, Confusion Matrix, Classification Report</li>
<li>Save models (.pkl)</li>
<li>Save metrics (.json)</li>
</ul>

<h3>Deployment</h3>
<ul>
<li>Push to GitHub</li>
<li>Connect to Render</li>
<li>Build: <code>pip install -r requirements.txt</code></li>
<li>Start: <code>gunicorn app:app</code></li>
</ul>
</div>

<div class="section">
<h2>7. Model Development</h2>

<h3>K-Nearest Neighbors</h3>
<ul>
<li>Distance-based classifier</li>
<li>n_neighbors = 3</li>
<li>Suitable for small structured datasets</li>
</ul>

<h3>Gaussian Naive Bayes</h3>
<ul>
<li>Probabilistic classifier</li>
<li>Assumes conditional independence</li>
<li>Fast & computationally efficient</li>
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

<div class="section">
<h2>8. Results & Output</h2>

<p><strong>Sample Input:</strong></p>
<ul>
<li>Sepal Length: 5.2</li>
<li>Sepal Width: 7</li>
<li>Petal Length: 1.4</li>
<li>Petal Width: 0.5</li>
</ul>

<p><strong>Predicted Output:</strong> Iris-setosa</p>

</div>

<div class="section">
<h2>9. Challenges & Solutions</h2>
<ul>
<li>JSON serialization error → Converted numpy arrays to lists</li>
<li>Matrix alignment issue → Used HTML tables</li>
<li>Algorithm detection issue → Used named submit buttons</li>
<li>Deployment path issue → Used relative paths</li>
</ul>
</div>

<div class="section">
<h2>10. Future Enhancements</h2>
<ul>
<li>Add heatmap visualization</li>
<li>Add accuracy comparison graph</li>
<li>Improve UI responsiveness</li>
<li>Store prediction history</li>
<li>Create REST API endpoints</li>
</ul>
</div>

<div class="section">
<h2>11. Conclusion</h2>
<p>This project demonstrates a complete ML deployment pipeline integrating:</p>
<ul>
<li>Dual algorithm model training</li>
<li>JSON metric storage</li>
<li>Flask backend</li>
<li>HTML/CSS frontend</li>
<li>Cloud deployment using Render</li>
</ul>
</div>

<div class="section">
<h2>12. References</h2>
<ul>
<li>Flask Documentation</li>
<li>Scikit-learn Documentation</li>
<li>Render Documentation</li>
<li>UCI Machine Learning Repository</li>
</ul>
</div>

</div>

<footer>
    <h2>KAMMARI RAMYA</h2>
    <p>Data Science & NLP Student</p>
</footer>

</body>
</html>
