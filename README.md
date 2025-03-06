# Movie Recommendation System  

This repository contains three different implementations of a **Movie Recommendation System**, each using a different approach and technology stack. The goal is to recommend movies to users based on their similarity to others, ensuring that each user gets suggestions for movies they haven’t watched yet.  

## Solutions Overview  

### 1. **Python Implementation (by Shijit)**  
- Uses **set operations** to calculate similarity between users.  
- Employs a **Jaccard-like approach** but focuses on ensuring meaningful recommendations.  
- Designed for readability and ease of debugging.  
- Best suited for small to medium-sized datasets.  

### 2. **JavaScript Implementation (by Jason)**  
- Implements a recommendation system in **JavaScript**, making it more adaptable for web-based applications.  
- Uses a **different similarity calculation method**, possibly incorporating frequency-based weighting.  
- Optimized for performance and scalability in browser-based or Node.js environments.  

### 3. **LLAMA-Assisted Code**  
- Generated with assistance from a **large language model (LLM)**.  
- May explore **alternative algorithms**, such as Cosine Similarity or Pearson Correlation.  
- Useful for benchmarking AI-generated code against human-designed solutions.  

## Installation & Usage  

Each solution is contained in its own directory. To run a specific solution:  

1. Navigate to the respective folder (`python_solution/`, `javascript_solution/`, `llama_solution/`).  
2. Follow the usage instructions inside each folder’s **README.md**.  
3. Run the script with a CSV file containing user preferences.  

### Running the Python Solution  

```bash
cd python_solution
python3 Recommendation.py your_file.csv
