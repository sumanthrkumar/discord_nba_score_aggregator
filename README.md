# NBA Scoreboard Discord Bot

This project is a Discord bot designed to provide real-time NBA game information directly within your Discord server. Built using the `discord.py` library and leveraging the `nba_api`, the bot fetches today's NBA schedule, live scores, and game statuses, presenting them in an organized and interactive thread.

## Features

*   **Daily NBA Game Schedule**: Automatically retrieves and displays all NBA games scheduled for the current day.
*   **Live Scores and Status**: Provides up-to-date scores and the current status of each game (e.g., "Final", "In Progress", "Halftime").
*   **Interactive Game List**: Presents each game as a clickable button within a dedicated Discord thread, designed for future integration of detailed stats.
*   **Organized Output**: Utilizes Discord threads to keep game information contained and easily accessible, preventing clutter in main channels.

## Installation

To set up and run the NBA Scoreboard Discord Bot, follow these steps:

1.  **Clone the Repository (if applicable)**:
    If this code is part of a repository, clone it:
    ```bash
    git clone https://github.com/your-username/nba-scoreboard-discord-bot.git
    cd nba-scoreboard-discord-bot
    ```
    Otherwise, ensure `nbabot.py` is in your working directory.

2.  **Install Python**:
    Ensure you have Python 3.8 or newer installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

3.  **Install Dependencies**:
    Install the required Python libraries using pip:
    ```bash
    pip install discord.py nba_api
    ```

4.  **Create a Discord Bot Application**:
    *   Go to the [Discord Developer Portal](https://discord.com/developers/applications).
    *   Click "New Application".
    *   Give your application a name and click "Create".
    *   Navigate to the "Bot" tab on the left sidebar.
    *   Click "Add Bot" and confirm.
    *   Under "Privileged Gateway Intents", enable the `Message Content Intent` toggle.
    *   Under "Build-A-Bot", click "Reset Token" to reveal your bot token. **Copy this token, as it will only be shown once.**

5.  **Configure the Bot Token**:
    Open the `nbabot.py` file and replace `'ENTER_TOKEN_HERE'` with your actual Discord bot's token:
    ```python
    #DISCORD CONFIGURATION
    TOKEN = 'YOUR_BOT_TOKEN_HERE' # Replace with your actual bot token
    ```

## Usage

1.  **Run the Bot**:
    Execute the Python script from your terminal:
    ```bash
    python nbabot.py
    ```
    The bot will log in and print `Logged in as yourbotname#!` to your console.

2.  **Invite the Bot to Your Server**:
    *   Go back to the Discord Developer Portal, navigate to your application, and then to the "OAuth2" -> "URL Generator" tab.
    *   Under "Scopes", select `bot`.
    *   Under "Bot Permissions", select the following:
        *   `Read Messages/View Channels`
        *   `Send Messages`
        *   `Create Public Threads`
        *   `Send Messages in Threads`
        *   `Embed Links`
    *   A URL will be generated at the bottom of the page. Copy and paste this URL into your web browser to invite the bot to your desired Discord server.

3.  **Execute the Command**:
    In any channel where the bot has the necessary permissions, type the command:
    ```
    !games
    ```
    The bot will then post a header message and create a dedicated thread containing the interactive scoreboard for today's NBA games.

## Configuration

*   `TOKEN`: This variable in the `nbabot.py` file must be updated with your Discord bot's authentication token for the bot to connect to Discord.

## Dependencies

*   `discord.py`: A modern, easy-to-use, and feature-rich API wrapper for Discord written in Python.
*   `nba_api`: An unofficial API client for fetching NBA statistics and live game data.
*   `datetime`: Standard Python library for handling dates and times.
*   `asyncio`: Standard Python library for writing concurrent code using the async/await syntax.

## Future Enhancements

The current implementation includes an interactive button for each game, serving as a placeholder for expanded details. Future updates are planned to include:

*   Displaying detailed box score statistics and other game insights when a game button is clicked.

## License

This project is open-sourced under the MIT License.