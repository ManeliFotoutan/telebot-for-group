# Telegram Group Management Bot

## Overview
This is a Telegram bot designed to manage group interactions efficiently. The bot provides features such as welcoming new members, pinning messages, banning/unbanning users, promoting/demoting members, filtering inappropriate words, and enabling/disabling silent mode.

## Installation
### Prerequisites
- Python 3.12.3
- `telebot` library
- `python-dotenv` library

### Setup
1. Clone the repository or download the files.
2. Install dependencies:
   ```bash
   pip install pyTelegramBotAPI python-dotenv
   ```
3. Create a `.env` file and add your bot token:
   ```
   API_TOKEN=your_telegram_bot_token
   ```
4. Run the bot:
   ```bash
   python <script_name>.py
   ```

## File Descriptions
### `foth_proj.py`
- **Welcome New Members**: Sends a greeting message when a new user joins the group.
- **Pin Messages**: Allows admins to pin important messages.
- **Kick, Ban, and Unban Users**: Provides moderation tools to remove disruptive members.
- **Promote/Demote Users**: Enables admins to manage user roles.
- **Message Filtering**: Detects and deletes messages containing prohibited words.
- **Silent Mode**: Temporarily restricts users from sending messages.
### `join_request.py`
Handles welcoming new users and approving join requests automatically.

### `massage_managment_in_groups.py`
Monitors group messages and removes inappropriate content.

### `pin_in_group.py`
Allows admins to pin messages by using the `/pin` command.

### `silent_mode.py`
Provides commands to enable (`/restrict`) or disable (`/unrestrict`) silent mode, which prevents members from sending messages.

## Notes
- The bot requires admin permissions in the group to function properly.
- Ensure the `.env` file is correctly configured with your bot token.
