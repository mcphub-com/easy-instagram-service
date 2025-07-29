import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/ariefsam/api/easy-instagram-service'

mcp = FastMCP('easy-instagram-service')

@mcp.tool()
def get_instagram_profile_by_username(username: Annotated[str, Field(description='Instagram Username')],
                                      random: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Get Instagram follower,following, average like, last post.'''
    url = 'https://easy-instagram-service.p.rapidapi.com/username'
    headers = {'x-rapidapi-host': 'easy-instagram-service.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
        'random': random,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_profile_with_base64_image(username: Annotated[str, Field(description='')]) -> dict: 
    '''Get Image with base64 image. This is beta version. Please report to us for any issues.'''
    url = 'https://easy-instagram-service.p.rapidapi.com/username-with-base64-image'
    headers = {'x-rapidapi-host': 'easy-instagram-service.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_post_by_shortcode(shortcode: Annotated[str, Field(description='')]) -> dict: 
    '''Get Post'''
    url = 'https://easy-instagram-service.p.rapidapi.com/get-post'
    headers = {'x-rapidapi-host': 'easy-instagram-service.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'shortcode': shortcode,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
