# https://github.com/HibiKier/zhenxun_bot/blob/main/utils/browser.py

from typing import Optional

from nonebot import get_driver
from nonebot.drivers import Driver
from nonebot.log import logger
from playwright.async_api import BrowserContext, async_playwright

driver: Driver = get_driver()
_browser: Optional[BrowserContext] = None


async def init(**kwargs) -> Optional[BrowserContext]:
    global _browser
    play = await async_playwright().start()
    try:
        browser = await play.chromium.launch(**kwargs)
        _browser = await browser.new_context(
            device_scale_factor=1.5,
            user_agent=(
                "Mozilla/5.0 (Linux; Android 10; RMX1911) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36"  # noqa
            )
        )
        return _browser
    except Exception as e:
        logger.warning(f"启动 Chromium 发生错误 {type(e)}：{e}")
    return None


async def get_browser(**kwargs) -> Optional[BrowserContext]:
    return _browser or await init(**kwargs)
