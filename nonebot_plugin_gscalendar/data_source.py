from base64 import b64encode

from nonebot.log import logger
from utils.browser import get_browser


async def gnrtCalendar() -> str:
    browser = await get_browser()
    page = None
    if not browser:
        return "无法生成图片！"
    try:
        page = await browser.new_page()
        await page.set_viewport_size({"width": 700, "height": 1500})
        await page.goto(
            "https://calendar.neptunia.vip/ys/index.html",
            wait_until="networkidle", timeout=10000
        )
        await page.evaluate("""() => {
            let wapper = document.querySelector("#app > div");
            wapper.style.width = "700px";
            wapper.style.paddingBottom = "15px";
            let items = wapper.querySelectorAll("div > div.m-events-calendar > div > div > div.m-events-calendar__event-item-container");  //  # noqa
            for (let i = 0; i < items.length; i++) {
                items[i].style.height = "100px";
                // items[i].style.paddingBottom = "10px";
                let eventName = items[i].querySelector("div.m-events-calendar__event-item > div > span");  //  # noqa
                eventName.style.fontSize = "20px";
                let eventTime = items[i].querySelector("div.m-events-calendar__event-item > div > div");  //  # noqa
                eventTime.style.fontSize = "18px";
                eventTime.style.paddingLeft = "10px";
                eventTime.style.color = "rgb(255 255 255 / 60%)";
            }
            let copyright = wapper.querySelector("div > div.text");  //  # noqa
            copyright.style.paddingTop = "15px";
        }""")
        calendar = await page.query_selector("#app > div")
        assert calendar is not None
        picImage = await calendar.screenshot()
        await page.close()
        return "base64://" + b64encode(picImage).decode()
    except Exception as e:
        logger.error(f"生成原神活动日历图片失败 {type(e)}：{e}")
        if page:
            await page.close()
        return "生成原神活动日历图片失败！"
