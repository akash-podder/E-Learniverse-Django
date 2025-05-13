import asyncio

# Theory
'''
asyncio.run(ramos_fn()) → asyncio.run → This Creates/Starts our “Event Loop” & Runs All “Coroutine” Function

“async” Keyword-wala Function === Coroutine Function
“ramos_fn()” is a “Coroutine Function” & it returns a “Coroutine Object”

Two Ways to START “async Function”... The Ways are:

1. await ramos_fn() → await keyword lagailei sheita “EVENT LOOP” ee PUSHED hoye jabe & Event loop will treat is a “Available Tasks” & Execute when Event Loop is Free. BUT BUT, taile amr NICHER TASK gula BLOCK jabe & execute hobe NAH… tik eijonno amra nicher “asyncio.create_task()” use kori for FINE-GRAIN Control

2. asyncio.create_task(ramos_fn()) → this means, Create a “Coroutine” & PUSHED it to EVENT LOOP. Event Loop will treat is as “Available Tasks” & Execute when Event Loop is Free
In Short → task=asyncio.create_task(ramos_fn()) → eita dewar sathe sathe “ramos_fn()” Function START hoye jabe… But Nicher BELOW TASK gula oo Execute korte parbo

N.B.: “async” function er moddhei kebol “await” keyword use korte parbo… “await” dile oi POINT ee STOP ee boshe takhbe Nicher Line ee jabe Nah
'''

async def fn1():
    task = asyncio.create_task(fn2()) # this just CREATEs the TASK & push it to the Queue So, that "Event Loop" can Run it
    print("one")
    print('four')
    await asyncio.sleep(1)
    print('five')
    await asyncio.sleep(1)


async def fn2():
    print("two")
    await asyncio.sleep(1)
    print("three")


asyncio.run(fn1())