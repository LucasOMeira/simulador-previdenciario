from sqlalchemy import text

from app.db.database import engine

def test_db_connection():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            print("Conexão com o banco SUPABASE Ok."), result.scalar()
    except Exception as e:
        print("Erro ao conectar ao banco SUPABASE:", e)
        print(str(e))
        
if __name__ == "__main__":
    test_db_connection()