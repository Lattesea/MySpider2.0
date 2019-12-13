#运行这个函数之后在当前文件夹产生一张截图

import asyncio
from pyppeteer import launch


async def main():
    brower = await launch(headless=False)
    page = await  brower.newPage()
    await page.goto('http://baidu.com')
    await page.screenshot({'path': 'example.png'})
    await brower.close()


asyncio.get_event_loop().run_until_complete(main())
