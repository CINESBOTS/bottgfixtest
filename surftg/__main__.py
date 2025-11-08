import asyncio
import sys
from traceback import format_exc

if sys.version_info >= (3, 10):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    try:
        import uvloop
        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
        loop = uvloop.new_event_loop()
        asyncio.set_event_loop(loop)
    except ImportError:
        pass
    
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from aiohttp import web
from pyrogram import idle

from surftg import __version__, LOGGER
from surftg.config import Telegram
from surftg.server import web_server
from surftg.bot import StreamBot, UserBot
from surftg.bot.clients import initialize_clients


async def stop_clients():
    """Gracefully stops all client instances."""
    LOGGER.info('Stopping clients...')
    await StreamBot.stop()
    if len(Telegram.SESSION_STRING) != 0:
        await UserBot.stop()
    LOGGER.info('Clients stopped.')


async def main():
    """
    Main asynchronous function to initialize and run all services.
    Handles startup, idling, and graceful shutdown.
    """
    web_app_runner = None
    web_tcp_site = None
    
    try:
        LOGGER.info(f'Initializing Surf-TG v-{__version__}')
        await asyncio.sleep(1.2)

        await StreamBot.start()
        StreamBot.username = StreamBot.me.username
        LOGGER.info(f"Bot Client : [@{StreamBot.username}]")
        
        if len(Telegram.SESSION_STRING) != 0:
            await UserBot.start()
            UserBot.username = UserBot.me.username or UserBot.me.first_name or UserBot.me.id
            LOGGER.info(f"User Client : {UserBot.username}")

        await asyncio.sleep(1.2)
        LOGGER.info("Initializing Multi Clients")
        await initialize_clients()

        await asyncio.sleep(2)
        LOGGER.info('Initalizing Surf Web Server..')
        
        web_app_runner = web.AppRunner(await web_server())
        LOGGER.info("Server CleanUp!")
        await web_app_runner.cleanup()

        await asyncio.sleep(2)
        LOGGER.info("Server Setup Started !")
        await web_app_runner.setup()
        
        web_tcp_site = web.TCPSite(web_app_runner, '0.0.0.0', Telegram.PORT)
        await web_tcp_site.start()

        LOGGER.info("Surf-TG Started Revolving !")
        await idle()

    except KeyboardInterrupt:
        LOGGER.info('Service stopping due to KeyboardInterrupt...')
    except Exception as e:
        LOGGER.error(f"An error occurred: {format_exc()}")
    finally:
        LOGGER.info('Service shutting down...')
        
        await stop_clients()
        
        if web_tcp_site:
            LOGGER.info("Stopping web server site...")
            await web_tcp_site.stop()
        if web_app_runner:
            LOGGER.info("Cleaning up web app runner...")
            await web_app_runner.cleanup()
            LOGGER.info("Web server stopped.")
            
        LOGGER.info('Shutdown complete.')


if __name__ == '__main__':
    asyncio.run(main())
