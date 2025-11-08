# CS-TG-BOT-03-New

A Telegram bot application built with Pyrogram for streaming and file management.

## Overview
This is a Telegram media streaming bot that provides web-based access to Telegram media files with TMDB integration for movies and TV shows.

## Recent Changes (November 8, 2025)
- **Fixed Python 3.13/3.11 asyncio event loop compatibility issue**
  - Added explicit event loop initialization before pyrogram imports
  - Configured uvloop event loop policy for better performance
  - Prevents `RuntimeError: There is no current event loop in thread 'MainThread'` error
  
- **Fixed MongoDB database configuration**
  - Changed DATABASE_URL to MONGODB_URI to avoid conflicts with Replit's PostgreSQL environment variable
  - Updated config.py to use MONGODB_URI instead of DATABASE_URL
  
- **Environment Setup**
  - Created runtime.txt specifying Python 3.11.10 for Heroku deployment
  - Installed all dependencies from requirements.txt
  - Configured workflow to run the bot

## Project Architecture

### Core Components
- **Bot Module** (`surftg/bot/`): Telegram bot clients and plugins
- **Server Module** (`surftg/server/`): Web server for streaming media
- **Helper Module** (`surftg/helper/`): Database operations, caching, media processing
- **Config** (`surftg/config.py`): Environment variable configuration

### Key Technologies
- **Pyrogram/Pyrofork**: Telegram MTProto API framework
- **aiohttp**: Async HTTP server
- **MongoDB**: Database for playlist and media metadata
- **uvloop**: High-performance event loop implementation
- **TMDB API**: Movie and TV show metadata

## Configuration

### Required Environment Variables (config.env)
- `API_ID`: Telegram API ID
- `API_HASH`: Telegram API Hash
- `BOT_TOKEN`: Telegram Bot Token
- `MONGODB_URI`: MongoDB connection string
- `BASE_URL`: Base URL for the web server
- `PORT`: Server port (default: 8080)
- `STATIC_AUTH_CHANNEL`: Comma-separated channel IDs
- `AUTH_CHANNEL`: Additional auth channels
- `SESSION_STRING`: User bot session (optional)
- `TMDB_API`: TMDB API key (optional)
- `USERS`: JSON object with admin credentials
- `ADMIN_USERNAME`: Playlist admin username
- `ADMIN_PASSWORD`: Playlist admin password

## Running the Application

### Local Development (Replit)
The bot runs automatically via the configured workflow:
```bash
python -m surftg
```

### Heroku Deployment
The application is configured for Heroku deployment with:
- `Procfile`: Defines web process
- `runtime.txt`: Specifies Python 3.11.10
- `surf-tg.sh`: Startup script
- `heroku.yml`: Container deployment config

## Event Loop Fix Details

The main fix addresses Python 3.10+ asyncio changes where `asyncio.get_event_loop()` no longer automatically creates an event loop. The solution in `surftg/__main__.py`:

1. Creates a new event loop before any imports
2. Sets it as the current event loop
3. Configures uvloop policy when available
4. Ensures pyrogram's sync wrapper can access the loop

This prevents the crash that was occurring in Heroku deployments.

## Database Schema

### Collections
- **playlist**: Folder and file organization
- **config**: Bot configuration settings
- **files**: Telegram file metadata
- **tmdb**: Movie and TV show metadata from TMDB

## User Preferences
- Use MongoDB (external) for database, not PostgreSQL
- Preserve existing bot functionality
- Maintain Heroku deployment compatibility
