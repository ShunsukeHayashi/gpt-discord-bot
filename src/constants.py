import os
from typing import Dict, List

DISCORD_BOT_TOKEN = os.environ["DISCORD_BOT_TOKEN"]
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
DISCORD_CLIENT_ID = os.environ["DISCORD_CLIENT_ID"]

# Set allowed server ID
ALLOWED_SERVER_IDS = [1199878847466836059]  # Only allow this specific server

# Get server to moderation channel mapping from environment variable
SERVER_TO_MODERATION_CHANNEL: Dict[int, int] = {}
server_to_channel = os.environ.get("SERVER_TO_MODERATION_CHANNEL", "")
if server_to_channel:
    try:
        pairs = [pair.split(":") for pair in server_to_channel.split(",") if ":" in pair]
        for server_id, channel_id in pairs:
            SERVER_TO_MODERATION_CHANNEL[int(server_id.strip())] = int(channel_id.strip())
    except (ValueError, IndexError) as e:
        print(f"Warning: Failed to parse SERVER_TO_MODERATION_CHANNEL: {e}")

# Moderation thresholds
MODERATION_VALUES_FOR_FLAGGED = {
    "hate": 0.5,
    "hate/threatening": 0.5,
    "self-harm": 0.5,
    "sexual": 0.5,
    "sexual/minors": 0.5,
    "violence": 0.5,
    "violence/graphic": 0.5,
}

MODERATION_VALUES_FOR_BLOCKED = {
    "hate": 0.8,
    "hate/threatening": 0.8,
    "self-harm": 0.8,
    "sexual": 0.8,
    "sexual/minors": 0.8,
    "violence": 0.8,
    "violence/graphic": 0.8,
}

# Bot configuration
BOT_NAME = "Assistant"
BOT_INSTRUCTIONS = """You are a helpful assistant. You help users with their questions and tasks in a friendly and professional manner."""

# Example conversations for the bot to learn from
class Message:
    def __init__(self, user: str, text: str):
        self.user = user
        self.text = text

class Conversation:
    def __init__(self, messages: List[Message]):
        self.messages = messages

EXAMPLE_CONVOS = [
    Conversation(
        messages=[
            Message("User", "こんにちは！"),
            Message("Lenard", "こんにちは！お手伝いできることはありますか？😊"),
        ]
    ),
]

# Thread configuration
ACTIVATE_THREAD_PREFX = "💭"
INACTIVATE_THREAD_PREFIX = "🔒"
MAX_THREAD_MESSAGES = 200
SECONDS_DELAY_RECEIVING_MSG = 2
MAX_CHARS_PER_REPLY_MSG = 1800

# Available models
AVAILABLE_MODELS = ["gpt-3.5-turbo", "gpt-4"]
DEFAULT_MODEL = "gpt-3.5-turbo"

# Bot invite URL with required permissions (Administrator = 0x8)
BOT_INVITE_URL = f"https://discord.com/api/oauth2/authorize?client_id={DISCORD_CLIENT_ID}&permissions=8&scope=bot%20applications.commands"
