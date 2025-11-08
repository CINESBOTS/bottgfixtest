# Deployment Guide for CS-TG-BOT-03-New

## What Was Fixed

The Telegram bot was experiencing a critical error on Heroku deployment:
```
RuntimeError: There is no current event loop in thread 'MainThread'
```

This issue has been completely resolved with the following changes:

### 1. Event Loop Initialization Fix
- **File**: `surftg/__main__.py`
- **Change**: Added explicit event loop creation before importing Pyrogram
- **Impact**: The bot now creates and sets an event loop before any imports that require it
- **Python Versions**: Works with both Python 3.11 and 3.13

### 2. MongoDB Configuration Fix
- **Files**: `config.env` and `surftg/config.py`
- **Change**: Renamed `DATABASE_URL` to `MONGODB_URI`
- **Reason**: Heroku automatically sets `DATABASE_URL` for PostgreSQL, which was conflicting
- **Impact**: The bot now correctly connects to MongoDB

### 3. Python Version Specification
- **File**: `runtime.txt`
- **Content**: `python-3.11.10`
- **Impact**: Ensures Heroku uses the correct Python version

## Heroku Deployment Steps

### Important: Update Environment Variables

You must update your Heroku config vars to use the new variable names:

```bash
heroku config:set MONGODB_URI="your_mongodb_connection_string"
heroku config:set API_ID="your_api_id"
heroku config:set API_HASH="your_api_hash"
heroku config:set BOT_TOKEN="your_bot_token"
heroku config:set BASE_URL="your_heroku_app_url"
heroku config:set STATIC_AUTH_CHANNEL="channel_ids"
```

### Deployment Commands

```bash
git add .
git commit -m "Fix event loop and MongoDB configuration"
git push heroku main
```

### Verify Deployment

After deployment, check logs:
```bash
heroku logs --tail
```

You should see:
```
[INFO] - Initializing Surf-TG v-1.2.6
[INFO] - Bot Client : [@your_bot_name]
[INFO] - Surf-TG Started Revolving !
```

## Security Notes

- The `config.env` file has been updated to remove hardcoded credentials
- The `.gitignore` now properly excludes `config.env` from version control
- **Action Required**: Rotate all exposed tokens (API keys, bot tokens) that were previously committed

## Local Development

For local testing:

1. Copy `config_sample.env` to `config.env`
2. Fill in your actual credentials
3. Run: `python -m surftg`

## Troubleshooting

### If the bot still doesn't start on Heroku:

1. Verify all config vars are set correctly
2. Ensure `MONGODB_URI` starts with `mongodb://` or `mongodb+srv://`
3. Check that your MongoDB cluster allows connections from Heroku's IP addresses
4. Verify the bot token is valid and not revoked

### If you see "Invalid URI scheme" error:

- Double-check that you're using `MONGODB_URI` in Heroku config vars (not `DATABASE_URL`)
- Ensure the MongoDB connection string is properly formatted

## Next Steps

1. Deploy to Heroku using the commands above
2. Rotate all exposed API keys and tokens
3. Test all bot functionality
4. Monitor logs for any issues

The bot is now ready for production deployment on Heroku!
