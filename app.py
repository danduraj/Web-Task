import asyncio
from playwright.async_api import async_playwright, Playwright
import time

async def run(playwright: Playwright):
    chromium = playwright.chromium 
    browser = await chromium.launch(headless=False,slow_mo=1000)
    page = await browser.new_page()
    await page.goto("https://dbs.moveinsync.com/DHyd/#EmployeeLogin")
    #Locate the elemnet 
    await page.get_by_placeholder("Alias / Emp Id").fill("514853")
    password = page.locator("xpath=/html/body/div[@id='loginPage']/div[@id='application']/div[@id='loginBody']/div[@class='loginScreen']/div[@class='loginBox']/form[@class='login-form']/div[1]/input[@class='loginInput passInput']")
    await password.press_sequentially("Raj@1613")
    await page.keyboard.press('Enter')
    time.sleep(10)
    select = page.locator("xpath=//select[@name='weekList']")
    await select.select_option("2")
    time.sleep(10)


async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())