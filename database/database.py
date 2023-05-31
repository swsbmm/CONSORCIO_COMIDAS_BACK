from database.connection import PostgresDatabase

dsn = "postgresql://consorcio:nomelase123@heflox.com:5432/consorcio1"
db = PostgresDatabase(dsn)

async def get_database():
    return db