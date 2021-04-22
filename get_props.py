#! /bin/python3

import config as conf
from notion.client import NotionClient

client = NotionClient(token_v2=conf.token_v2)
cards = client.get_collection_view(conf.collection_url)
today_cards = cards.build_query(filter=cards.get('query2')['filter']).execute() 
sample_card = cards.collection.get_rows()[0]
props = list(sample_card.get_all_properties().keys())

print('\n'.join(props))