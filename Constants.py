import json
INST_USER= INST_PASS= USER= PASS= HOST= DATABASE= POST_COMMENTS= ''
LIKES_LIMIT= DAYS_TO_UNFOLLOW= CHECK_FOLLOWERS_EVERY= 0
HASHTAGS= []
COMMENTS=[]
COMENTARIOS=[]
def init():
    global INST_USER, INST_PASS, USER, PASS, HOST, DATABASE, LIKES_LIMIT, DAYS_TO_UNFOLLOW, CHECK_FOLLOWERS_EVERY, HASHTAGS, COMMENTS, COMENTARIOS
    # read file
    data = None
    with open('settings.json', 'r') as myfile:
        data = myfile.read()
    obj = json.loads(data)
    INST_USER = obj['instagram']['user']
    INST_PASS = obj['instagram']['pass']
    USER = obj['db']['user']
    HOST = obj['db']['host']
    PASS = obj['db']['pass']
    DATABASE = obj['db']['database']
    LIKES_LIMIT = obj['config']['likes_over']
    CHECK_FOLLOWERS_EVERY = obj['config']['check_followers_every']
    HASHTAGS = obj['config']['hashtags']
    DAYS_TO_UNFOLLOW = obj['config']['days_to_unfollow']
    COMMENTS=obj['config']['comments']
    COMENTARIOS=obj['config']['comentarios']