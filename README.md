# 🚆 CRIS Internship – GMT Railway Data Analysis (Open Source Flask App)

## 📌 Overview
This project is an **open-source web application** built using **Python (Flask, Pandas, Plotly)** to analyze and visualize **Gross Million Tonne (GMT)** data of Indian Railways.  

It provides **year-wise comparison reports** at multiple levels:  
- 📍 **Division-wise**  
- 🌍 **Zone-wise**  
- 🚀 **Overall Indian Railways (IR)**  

The application is completely **open source** (no proprietary tools like Power BI or Tableau), making it **lightweight, transparent, and easy to run anywhere with Python**.  

---

## ⚡ Features
- 🌐 Interactive **Web Dashboard** built with Flask  
- 📍 **Division-wise Yearly Comparison** (separate tables for each year + bar charts)  
- 🌍 **Zone-wise Yearly Comparison** (separate tables for each year + bar charts)  
- 🚀 **Overall IR Report** (separate tables for each year + trend line chart)  
- 🎨 **Bootstrap UI** → clean, colorful, mobile-friendly interface  
- 💡 **Open Source Stack** → Python, Pandas, Flask, Plotly  

---

## 🛠️ Tech Stack
- **Backend**: Flask (Python)  
- **Frontend**: Bootstrap 5, HTML, CSS, Jinja2 Templates  
- **Data Processing**: Pandas  
- **Visualization**: Plotly (interactive charts)  
- **Dataset**: `GMT_DATA_SINCE 2018-19_ZONE_DIVISION_WISE.xlsx`  

---

## 📂 Project Structure
```bash
CRIS_INTERNSHIP/
│── app.py                                # Flask backend
│── GMT_DATA_SINCE 2018-19_ZONE_DIVISION_WISE.xlsx
│── static/
│   └── style.css                         # Custom CSS
│── templates/
│   ├── base.html                         # Main layout
│   ├── index.html                        # Homepage
│   ├── division.html                     # Division-wise report
│   ├── zone.html                         # Zone-wise report
│   └── overall.html                      # Overall IR report
│── README.md                             # Project documentation



