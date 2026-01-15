from backend.database import engine

try:
    with engine.connect() as conn:
        print("✅ Conectado com sucesso ao SQL Server!")
except Exception as e:
    print("❌ Erro:", e)
