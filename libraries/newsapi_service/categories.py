from enum import Enum

class Category(str, Enum):
    BUSINESS      = 'business'
    ENTERTAINMENT = 'entertainment'
    GENERAL       = 'general'
    HEALTH        = 'health'
    SCIENCE       = 'science'
    SPORTS        = 'sports'
    TECHONOLOGY   = 'technology'
