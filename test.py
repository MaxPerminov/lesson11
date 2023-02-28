# import asyncio
#
#
# async def decor(fn):
#     def wrapper():
#         print(f"***{fn()}***")
#     await asyncio.sleep(2, print("waiting"))
#     wrapper()
#
#
# def func():
#     return "Ji"
#
#
# asyncio.run(decor(func))
