import tweepy
from src.connection import users_collection
from src.constants import BRAZIL_WOE_ID
from src.secrets import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
from typing import Any, Dict, List


def _get_users(woe_id: int, api: tweepy.API) -> List[Dict[str, Any]]:
    users = api.get_user()

    return users[0]["users"]


def get_users_mongo() -> List[Dict[str, Any]]:
    users = users_collection.find({})
    return list(users)


def sync_users() -> None:
    auth = tweepy.OAuthHandler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)

    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    users = _get_users(woe_id=BRAZIL_WOE_ID, api=api)
    users_collection.insert_many(users)
