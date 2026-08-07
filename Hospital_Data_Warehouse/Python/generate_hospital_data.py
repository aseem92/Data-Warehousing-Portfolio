import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker('en_IN')

# =====================================
# DOCTORS
# =====================================

doctors = [
    [1,'Dr Sharma','Cardiology'],
    [2,'Dr Mehta','Cardiology'],
    [3,'Dr Verma','Neurology'],
    [4,'Dr Singh','Neurology'],
    [5,'Dr Patel','Orthopedics'],
    [6,'Dr Kumar','Orthopedics'],
    [7,'Dr Gupta','Pediatrics'],
    [8,'Dr Nair','Pediatrics'],
    [9,'Dr Rao','Dermatology'],
    [10,'Dr Joshi','Dermatology'],
    [11,'Dr Agarwal','General Medicine'],
    [12,'Dr Mishra','General Medicine'],
    [13,'Dr Kapoor','ENT'],
    [14,'Dr Sinha','ENT'],
    [15,'Dr Bansal','Gastroenterology'],
    [16,'Dr Jain','Gastroenterology'],
    [17,'Dr Arora','Cardiology'],
    [18,'Dr Khanna','Neurology'],
    [19,'Dr Tiwari','General Medicine'],
    [20,'Dr Yadav','Pediatrics']
]

df_doctors = pd.DataFrame(
    doctors,
    columns=['doctor_id','doctor_name','department']
)

df_doctors.to_csv('doctors.csv', index=False)

# =====================================
# PATIENTS
# =====================================

patients = []

for i in range(1,1001):

    patients.append([
        i,
        fake.name(),
        random.randint(1,90),
        random.choice(['M','F'])
    ])

df_patients = pd.DataFrame(
    patients,
    columns=[
        'patient_id',
        'patient_name',
        'age',
        'gender'
    ]
)

df_patients.to_csv(
    'patients.csv',
    index=False
)

# =====================================
# PATIENT VISITS
# =====================================

visits = []

for visit_id in range(1,5001):

    patient_id = random.randint(1,1000)
    doctor_id = random.randint(1,20)

    department = doctors[doctor_id-1][2]

    visit_date = fake.date_between(
        start_date='-6M',
        end_date='today'
    )

    appointment_time = datetime.combine(
        visit_date,
        datetime.min.time()
    ) + timedelta(
        hours=random.randint(8,17),
        minutes=random.randint(0,59)
    )

    # Department-specific wait time

    if department == 'Cardiology':
        wait_time = random.randint(30,90)

    elif department == 'Pediatrics':
        wait_time = random.randint(5,20)

    else:
        wait_time = random.randint(10,45)

    consultation_start = (
        appointment_time +
        timedelta(minutes=wait_time)
    )

    # Consultation duration

    if department == 'Neurology':
        consultation_duration = random.randint(15,35)

    else:
        consultation_duration = random.randint(5,20)

    consultation_end = (
        consultation_start +
        timedelta(minutes=consultation_duration)
    )

    billing_start = consultation_end

    billing_duration = random.randint(2,15)

    billing_end = (
        billing_start +
        timedelta(minutes=billing_duration)
    )

    pharmacy_start = billing_end

    pharmacy_duration = random.randint(2,10)

    pharmacy_end = (
        pharmacy_start +
        timedelta(minutes=pharmacy_duration)
    )

    # Satisfaction

    if department == 'Pediatrics':
        feedback_score = random.randint(4,5)

    elif wait_time > 60:
        feedback_score = random.randint(1,3)

    else:
        feedback_score = random.randint(3,5)



    visits.append([
        visit_id,
        patient_id,
        doctor_id,
        visit_date,
        appointment_time,
        consultation_start,
        consultation_end,
        billing_start,
        billing_end,
        pharmacy_start,
        pharmacy_end,
        feedback_score
    ])

df_visits = pd.DataFrame(
    visits,
    columns=[
        'visit_id',
        'patient_id',
        'doctor_id',
        'visit_date',
        'appointment_time',
        'consultation_start',
        'consultation_end',
        'billing_start',
        'billing_end',
        'pharmacy_start',
        'pharmacy_end',
        'feedback_score'
    ]
)

df_visits.to_csv(
    'patient_visits.csv',
    index=False
)

# =====================================
# COMPLAINTS
# =====================================

categories = [
    'Long Wait Time',
    'Billing Delay',
    'Pharmacy Delay',
    'Staff Behaviour',
    'Doctor Interaction',
    'Cleanliness'
]

severity = [
    'Low',
    'Medium',
    'High'
]

complaints = []

for complaint_id in range(1,1001):

    complaints.append([
        complaint_id,
        random.randint(1,5000),
        random.choice(categories),
        random.choice(severity)
    ])

df_complaints = pd.DataFrame(
    complaints,
    columns=[
        'complaint_id',
        'visit_id',
        'complaint_category',
        'complaint_severity'
    ]
)

df_complaints.to_csv(
    'complaints.csv',
    index=False
)

print("✅ doctors.csv created")
print("✅ patients.csv created")
print("✅ patient_visits.csv created")
print("✅ complaints.csv created")
print("🎉 Hospital data generation completed")