import psycopg2

# Replace placeholders with your database credentials
conn = psycopg2.connect(
  host="your_hostname",
  database="your_database_name",
  user="your_username",
  password="your_password"
)

cursor = conn.cursor()

# Execute a query
cursor.execute("SELECT * FROM your_table")

# Fetch results
records = cursor.fetchall()
for record in records:
  print(record)

# Close the cursor and connection
cursor.close()
conn.close()
