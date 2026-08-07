import pandas as pd
import random

admissions = []

for admission_id in range(1, 5001):

    recommended = random.choices(
        ['Yes', 'No'],
        weights=[30, 70]
    )[0]

    if recommended == 'Yes':
        admitted = random.choices(
            ['Yes', 'No'],
            weights=[70, 30]
        )[0]
    else:
        admitted = 'No'

    admissions.append([
        admission_id,
        admission_id,   # visit_id
        recommended,
        admitted
    ])

df = pd.DataFrame(
    admissions,
    columns=[
        'admission_id',
        'visit_id',
        'recommended_for_admission',
        'admitted'
    ]
)

df.to_csv('admissions.csv', index=False)

print("admissions.csv created successfully")