#! /bin/python3

from notion.client import NotionClient
from datetime import datetime

import config as conf

client = NotionClient(token_v2=conf.token_v2)
cards = client.get_collection_view(conf.collection_url)

correct = 0

today_cards = cards.build_query(filter=cards.get('query2')['filter']).execute() 
print(f"Hi! Cards for today: {len(today_cards)}\n")
for card in today_cards:
    print('=> ', card.title, ' <=')
    print()
    choice = input('\nFlip the card? ')
    print()
    print(card.get_property(conf.translation))
    if (card.get_property(conf.transcription)):
        print(card.get_property(conf.transcription))
    print()
    c = input('(enter = accept, d = decline, smth else = skip): ')
    if (c == 'a' or c == ''): # backward compatibility
        print('accepted.')
        correct += 1
        if (card.get_property(conf.level) == '10'):
            print('maximum level reached! skipping..')
        else:
            card.set_property(conf.level, str(int(card.level) + 1))
    elif (c == 'd'):
        print('declined.')
        card.set_property(conf.level, '2')
        card.set_property(conf.date_wrong, datetime.today().date())
    else:
        print()
        continue
    print()
if (len(today_cards)):
    print(f"Cards answered correctly: {correct}/{len(today_cards)}")
print("That's all for today!")

print()
print('Now let\'s add some words.')

while True:
    word = input('Word: ')
    translation = input('Translation: ')
    transcription = input('Transcription: ')
    new_card = cards.collection.add_row()
    new_card.icon = '🔹'
    new_card.title = word
    new_card.set_property(conf.translation, translation)
    new_card.set_property(conf.date_wrong, datetime.today().date())
    new_card.set_property(conf.level, '2')
    print('Done!\n')

