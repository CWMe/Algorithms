# KNN-Based Movie Recommendation System  

This repository contains a **K-Nearest Neighbors (KNN) Movie Recommendation System** using **Cosine Similarity**. The system analyzes users with similiar movie watching history and recommends movies.  

## 📌 What This Code Does  

1. **Loads a CSV file** containing user movie preferences.  
2. **Encodes movies seen** into binary vectors using **one-hot encoding**.  
3. **Computes Cosine Similarity** between users' viewed movies to find the closest matches.  
4. **Finds the K-Nearest Neighbors (KNN)** for each user based on similarity scores.  
5. **Recommends movies** that similar users have watched but the target user hasn’t.  
6. **Outputs recommendations** with the most similar user(s) and movies to watch.  

## ⚙️ Setup & Installation  

### **Step 1: Clone the Repository**  
```
git clone https://github.com/CWMe/Algorithms/
```
### **Step 2 (Optional): Create and activate virtual env**  
```
python -v venv .venv
.venv/Scripts/Activate
```

### **Step 3: Install dependences**  
```
pip install -r requirements.txt
```
### **Step 4: Run the script**  
```
python KNN_Cosine_Recommend.py
```



