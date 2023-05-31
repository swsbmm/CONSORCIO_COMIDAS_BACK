import asyncpg

class PostgresDatabase:
    def __init__(self, dsn: str):
        self.dsn = dsn
        self.pool = None

    async def connect(self):
        self.pool = await asyncpg.create_pool(dsn=self.dsn)

    async def disconnect(self):
        await self.pool.close()

    async def execute(self, query: str, *args):
        async with self.pool.acquire() as connection:
            return await connection.execute(query, *args)

    async def fetch_one(self, query: str, *args):
        async with self.pool.acquire() as connection:
            return await connection.fetchrow(query, *args)

    async def fetch_all(self, query: str, *args):
        async with self.pool.acquire() as connection:
            return await connection.fetch(query, *args)


