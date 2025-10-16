# 🧠 ETL Project — API to CSV Pipeline

This project demonstrates a simple **Extract, Transform, Load (ETL)** pipeline built in Python.  
It extracts data from a free public API, cleans and structures it with pandas, and then saves it into a CSV file.

---

## 🚀 Features

- **Extract:** Pulls sample data from the [JSONPlaceholder API](https://jsonplaceholder.typicode.com/)
- **Transform:** Cleans and standardizes data using pandas
- **Load:** Saves the processed dataset to a local CSV file
- Modular design (`extract.py`, `transform.py`, `load.py`, `main.py`)
- Ready to extend for databases or cloud storage (S3, GCP, etc.)

---

## 🗂️ Project Structure

etl_project/
│
├── data/ # Folder for output files
├── extract.py # Handles API extraction
├── transform.py # Cleans and formats data
├── load.py # Writes data to CSV
├── main.py # Orchestrates ETL pipeline
├── requirements.txt # Python dependencies
└── venv/ # (Local virtual environment - ignored by Git)

---

## ⚙️ Setup Instructions

### 1️⃣ Clone this repository
```bash
git clone https://github.com/BALAJI-PAMIDI/etl_project.git
cd etl_project
2️⃣ Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate
3️⃣ Install dependencies
pip install -r requirements.txt
▶️ Run the ETL Pipeline
python main.py
✅ Expected output:
🔹 Extracting data...
🔹 Transforming data...
🔹 Loading data...
✅ Data saved successfully to data/posts.csv
🎉 ETL pipeline completed successfully!
📊 Output Example
The script creates a file:
data/posts.csv
userId	id	title	body
1	1	Sunt Aut Facere Repellat Provident	Quia et suscipit suscipit recusandae...
1	2	Qui Est Esse	Est rerum tempore vitae sequi sint...
🧩 Future Enhancements
Load data into SQLite or PostgreSQL
Automate daily ETL runs using Airflow or cron
Push processed data to AWS S3 or Google Cloud Storage
👤 Author
Balaji Pamidi
💼 GitHub: BALAJI-PAMIDI
📍 Boston, MA
📧 balajip1818@gmail.com
