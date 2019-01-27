
import random
import asyncio

async def waiter(name):
    for _ in range(4):
        time_to_sleep = random.randint(1, 3) / 4
        await asyncio.sleep(time_to_sleep)
        print('{} waited {} seconds'.format(name, time_to_sleep))

async def run():
    await asyncio.wait([waiter("foo"), waiter('bar')])

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
    loop.close()

if __name__ == '__main__':
    main()
