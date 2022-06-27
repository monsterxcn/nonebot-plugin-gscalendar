try:
    from nonebot.adapters.cqhttp import Bot, MessageSegment
    from nonebot.adapters.cqhttp.event import MessageEvent
except ImportError:
    from nonebot.adapters.onebot.v11 import Bot
    from nonebot.adapters.onebot.v11.message import MessageSegment
    from nonebot.adapters.onebot.v11.event import MessageEvent
from nonebot.exception import FinishedException
from nonebot.log import logger
from nonebot.plugin import on_command
from nonebot.typing import T_State

from .data_source import gnrtCalendar

showCalendar = on_command("calendar", aliases={"日历", "活动"}, priority=13)


@showCalendar.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        calendar = await gnrtCalendar()
        await showCalendar.finish(
            MessageSegment.image(calendar)
            if "base64" in calendar else
            MessageSegment.text(calendar)
        )
    except FinishedException:
        pass
    except Exception as e:
        logger.error(f"原神活动日历命令响应出错 {type(e)}：{e}")
        raise FinishedException
