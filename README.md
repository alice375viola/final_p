# Student Management System (Flask + PostgreSQL + HTML)

## 📌 Overview
A simple web-based Student Management System built using:
- Flask (Backend)
- PostgreSQL (Database hosted on AWS RDS)
- HTML/CSS/JavaScript (Frontend hosted on S3)
- Hosted on EC2

Users can:
- View students
- Add new students
- Delete students

---

## 🚀 How to Run the Application

final_project/
 backend -> app.py
 frontend -> Static frontend files (hosted in S3)

1. Set up EC2 Instance:

  Configure the security group to allow traffic on ports: 80, 22, 443, 5432, 8000, and all traffic.
  Set up RDS PostgreSQL:

  Make sure the RDS instance allows all traffic from the EC2 instance (public access).
  SSH into EC2:

2.Run:
```ssh -i "C:\your_key_2_ec2.pem" ubuntu@<EC2_Public_IP>```


3. Install dependencies:
    ```bash
    sudo apt update
    sudo apt install python3 python3-pip postgresql-client -y
    ```
    
4. Connect to the RDS instance using psql:
   ```psql -h <RDS_End_Point> -U <RDS_User> -d <RDS_Database_Name>```
5. Table
   CREATE TABLE tbl_asila_students (
    student_id SERIAL PRIMARY KEY,
    full_name VARCHAR(100),
    gender VARCHAR(10),
    age INTEGER,
    department VARCHAR(100),
    gpa NUMERIC(3, 2),
    enrollment_year INTEGER
);

6. Install Python Dependencies:
   Install python3-venv (if not already installed)
```
cd final
sudo apt update
sudo apt install python3-venv
python3 -m venv venv
source venv/bin/activate
```

7.Install the necessary libraries:
```
pip3 install --upgrade pip
pip3 install flask psycopg2-binary
```

8. Run
   python app.py
   

10. Run the server:
    ```bash
    cd final_project
    python app.py    
    ```
