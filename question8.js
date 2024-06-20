const puppeteer=require('puppeteer');

async function takeScreenshot(url,imagePath)
{
    const browser=await puppeteer.launch({
        headless:false,
    });
    const page = await browser.newPage();
    await page.goto(url);

    setTimeout(async function () {
        await page.screenshot({path:imagePath});
        await browser.close();
    }, 5000); // Call the function after 5 seconds
}

takeScreenshot("question8.html",'canvas.png');