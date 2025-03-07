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

### Expected output:
```
Recommend Internet Bot watch ['The Dark Knight', 'Finding Nemo', 'Spirited Away', 'Avatar', 'The Departed', 'The Dark Knight', 'The Lord of the Rings: The Return of the King'] based on neighbors Shijit Dasgupta(0.71), Paulo(0.71)
Recommend Milu watch ['Spirited Away', 'Superbad', 'The 40 Year Old Virgin', 'Shrek 2'] based on neighbors Shijit Dasgupta(0.71), Calvin(0.71)
Recommend John watch ['Avatar', 'Avatar', 'The 40 Year Old Virgin'] based on neighbors Fabio(0.82), Pavel(0.77)
Recommend Alex watch ['Matrix Reloaded'] based on neighbors Jason(1.00), John(0.89)
Recommend Nick watch ['The Lord of the Rings: The Return of the King'] based on neighbors Calvin(1.00), Fabio(0.82)
Recommend Paulo watch ['The 40 Year Old Virgin'] based on neighbors Fabio(1.00), Internet Bot(0.89)
Recommend A H watch [] based on neighbors Internet Bot(1.00), John(1.00)
Recommend Jason watch ['Avatar', 'Matrix Reloaded', 'Avatar', 'Mean Girls', 'The Dark Knight', 'Spirited Away', 'Inception'] based on neighbors Fabio(0.58), Alex(0.53)
Recommend Vale watch ['Matrix Reloaded', 'Mean Girls', 'Matrix Reloaded'] based on neighbors Fabio(0.82), John(0.77)
Recommend Pavel watch ['Spirited Away', 'Mean Girls'] based on neighbors Fabio(1.00), John(0.77)
Recommend Fabio watch ['The Dark Knight', 'The 40 Year Old Virgin', 'The Room'] based on neighbors Pavel(0.77), Jason(0.71)
Recommend Shijit Dasgupta watch ['Avatar', 'Minority Report', 'Matrix Reloaded'] based on neighbors Milu(0.87), Internet Bot(0.77)
Recommend Calvin watch ['Avatar', 'Matrix Reloaded', 'Spirited Away', 'Avatar', 'The Dark Knight', 'Inception'] based on neighbors Nick(0.63), Milu(0.50)
```

