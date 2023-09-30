#Author Vatsal Verma
import requests
import json

TRELLO_API_BASE_URL = "https://api.trello.com/1/"
API_KEY = "cf2065d9ee86a34af93ec6e2b37c480b"  
TOKEN = "ATTAf51e2eb2c46ae7d3876e1ff11791120e83aadeea215548a94415283299b57a5f69B31F1C"  

def add_card_to_board_on_trello(board_id, column_id, card_name, labels, comment):
    url = f"{TRELLO_API_BASE_URL}cards"
    
    params = {
        "key": API_KEY,
        "token": TOKEN,
        "idList": column_id,
        "name": card_name,
        "idLabels": labels
    }
    
    response = requests.post(url, params=params)
    card = response.json()

    comment_url = f"{TRELLO_API_BASE_URL}cards/{card['id']}/actions/comments"
    comment_params = {
        "key": API_KEY,
        "token": TOKEN,
        "text": comment
    }
    requests.post(comment_url, params=comment_params)

def main():
    board_id = input("Enter board ID: ")
    column_id = input("Enter column ID: ")
    card_name = input("Enter card name: ")
    labels = input("Enter label IDs (comma-separated): ").split(',')
    comment = input("Enter comment: ")
    add_card_to_board_on_trello(board_id, column_id, card_name, labels, comment)
    print("Card added successfully!")

if __name__ == "__main__":
    main()
