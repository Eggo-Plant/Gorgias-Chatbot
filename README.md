# Gorgias-Chatbot
Discord bot coded in Python3 that uses `brainshop.ai` to generate AI responses to user messages.
The `brainshop.ai` API allows for uniquely identifying users, and storing data that they tell the bot about themselves (i.e. Name, Location, Age, and most other common identifying factors).

The bot uses Discord ID's to generate UUIDS for this. **The UUID's the bot uses to identify users are private.** While the UUID's are sent to a remote server, they are hashed with the Sha256 algorithm first. This anonymizes, and prevent reverse engineering the UUIDs to the Discord ID's.

**Setup Instructions:**
> The setup for this bot may be a bit tedious since you need to create a [brainshop.ai](https://brainshop.ai/user/register) account first to get your chatbot and API token.
* Place `main.py` and `requirements.txt` in the root of your bot's folder
* Create a file called .env in the root of your bot's folder
* Edit the .env file to look as such:
```
TOKEN="<YOUR BOT TOKEN>"
API_KEY="<BRAINSHOP.AI API KEY>"
BOT_ID="<YOUR BOT'S DISCORD USER ID>"
BRAIN_ID="<BRAINSHOP.AI BOT BRAIN ID>"
```
* Install the requirements using `pip install -r requirements.txt`
* Now run main.py with any Python version >= 3.6
