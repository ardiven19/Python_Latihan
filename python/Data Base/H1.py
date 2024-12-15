import psycopg2

# Membuat koneksi
conn = psycopg2.connect(
    dbname="Employee",
    user="postgres",
    password="19092019",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# Melakukan query
cur.execute("SELECT * FROM employees where department_id is null")

# Mendapatkan hasil
result = cur.fetchall()



import pandas as pd

# Membuat DataFrame dari hasil query
df = pd.DataFrame(result, columns=[desc[0] for desc in cur.description])
print(df.all)

# Menutup kursor dan koneksi
cur.close()
conn.close()

