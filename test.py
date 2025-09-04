import psycopg2
from psycopg2 import OperationalError

# Replace these with your actual Supabase credentials
DB_NAME = "postgres"
DB_USER = "postgres.qacbzaleweqcfgketeeq"
DB_PASSWORD = "cFuOmw9V6Mn1S8hS"
DB_HOST = "aws-1-ap-southeast-1.pooler.supabase.com"
DB_PORT = "6543"
def test_connection():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
        )
        print("✅ Connection successful")
        conn.close()
    except OperationalError as e:
        print("❌ Connection failed")
        print(e)

if __name__ == "__main__":
    test_connection()

