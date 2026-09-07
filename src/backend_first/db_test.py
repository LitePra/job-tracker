import  asyncpg
import asyncio


async def main():
    pool = await asyncpg.create_pool(host="localhost", port=5432, database="job_tracker", user="postgres", password="msqwd2341",min_size=1,max_size=5)
    async with pool.acquire() as connection:
        result = await connection.execute('INSERT INTO test (id) VALUES (10);')
        print(result)

    await pool.close()


asyncio.run(main())