# Trello CLI App By Vatsal Verma

## Description about the Repo
A command-line interface to add cards to a Trello board.

## Setup Env
1. Ensure you have Python installed [3.11.5]
2. Replace `YOUR_API_KEY` and `YOUR_OAUTH_TOKEN` in `trello_cli.py` with your Trello API key and OAuth token.
3. Run the CLI: `python trello_cli.py`

## User Instructions
1. Input the column ID (also known as the List ID) where the card will be added.
2. Input the card name.
3. Input the label IDs associated with the card (comma-separated without spaces).
4. Input the comment text for the card.

## Next Steps
1. Implement error handling for API calls.
2. Securely manage API keys and tokens using environment variables or a configuration file.
3. Enhance the CLI with more features, such as board and list exploration, card deletion, etc.
