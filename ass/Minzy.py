# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 09:15:29 2023

@author: User
"""

import re
import long_responses as long

def message_Probability(useer_message,recognised_words,single_response=False,required_words=[]):
    message_certainty=0
    has_required_word=True
    
    for word in useer_message:
        if word in recognised_words:
            message_certainty+=1

    percentage=float(message_certainty)/float(len(recognised_words))     

    for word in required_words:
        if word not in useer_message:
            has_required_word=False
            break

    if has_required_word or single_response:
        return int(percentage*100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list={}

    def response(bot_response,list_of_words,single_response=False,required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response]=message_Probability(message,list_of_words,single_response,required_words)

    
    response('Hello!',['hello','hi','sup','hey','heyo'],single_response=True)
    response('I\'m doing fine, and you?',['how','are','you','doing'],required_words=['you','doing','are'])
    response('Thank you!',['i','love','code','palace'],required_words=['code','palace'])
    response('Goodbye!', ['bye', 'goodbye', 'see', 'you', 'later'], single_response=True)
    response('I\'m a chatbot!', ['who', 'are', 'you'], required_words=['who', 'you'])
    response('I\'m sorry if I made a mistake.', ['sorry', 'apologize', 'my', 'fault'], required_words=['sorry'])
    response('I can help you with programming questions.', ['help', 'programming', 'questions'], required_words=['help', 'programming'])
    response('The weather is nice today.', ['how', 'is', 'the', 'weather', 'today'], required_words=['weather'])
    response('I enjoy learning new things.', ['what', 'you', 'enjoy', 'learning'], required_words=['you', 'enjoy', 'learning'])
    response('How can I assist you today?', ['help', 'assistance', 'support'], required_words=['help'])
    response('I love exploring new ideas!', ['what', 'you', 'love', 'exploring'], required_words=['you', 'love'])
    response('Sure, I can provide information on that topic.', ['tell', 'me', 'about', 'topic'], required_words=['tell', 'about', 'topic'])
    response('I am constantly learning and evolving.', ['learn', 'evolve', 'improve'], required_words=['learn'])
    response('Technology is fascinating!', ['technology', 'fascinating'], required_words=['technology', 'fascinating'])
    response('I appreciate your kind words!', ['thank', 'you', 'appreciate'], required_words=['thank', 'appreciate'])
    response('The future is full of possibilities.', ['future', 'possibilities'], required_words=['future', 'possibilities'])
    response('I enjoy engaging in meaningful conversations.', ['enjoy', 'conversation'], required_words=['enjoy', 'conversation'])
    response('I can help with various tasks, just let me know.', ['help', 'tasks'], required_words=['help', 'tasks'])
    response('I like to keep things positive!', ['positive', 'vibes'], required_words=['positive', 'vibes'])
    response('How can I assist you today?', ['help', 'assistance', 'support'], required_words=['help'])
    response('Have you tried learning a new skill recently?', ['learn', 'new', 'skill'], required_words=['learn', 'new', 'skill'])
    response('I enjoy a good challenge!', ['challenge', 'enjoy'], required_words=['challenge', 'enjoy'])
    response('I find inspiration in unexpected places.', ['inspiration', 'unexpected'], required_words=['inspiration', 'unexpected'])
    response('Tell me about your favorite hobby.', ['tell', 'favorite', 'hobby'], required_words=['tell', 'favorite', 'hobby'])
    response('I believe in continuous improvement.', ['continuous', 'improvement', 'believe'], required_words=['continuous', 'improvement', 'believe'])
    response('Nature has a way of bringing peace.', ['nature', 'peace'], required_words=['nature', 'peace'])
    response('I enjoy connecting with people.', ['enjoy', 'connect', 'people'], required_words=['enjoy', 'connect', 'people'])
    response('I appreciate a good sense of humor!', ['appreciate', 'sense', 'humor'], required_words=['appreciate', 'sense', 'humor'])
    response('I value creativity and innovation.', ['value', 'creativity', 'innovation'], required_words=['value', 'creativity', 'innovation'])
    response('Do you have any exciting plans for the weekend?', ['exciting', 'plans', 'weekend'], required_words=['exciting', 'plans', 'weekend'])
    response('How can I assist you with AI today?', ['help', 'assistance', 'ai'], required_words=['help', 'ai'])
    response('Sure, I can provide information on AI concepts.', ['tell', 'me', 'about', 'ai', 'concepts'], required_words=['tell', 'about', 'ai', 'concepts'])
    response('I am constantly learning and evolving in the field of AI.', ['learn', 'evolve', 'ai'], required_words=['learn', 'ai'])
    response('The advancements in AI technology are truly fascinating!', ['advancements', 'ai', 'technology', 'fascinating'], required_words=['advancements', 'ai', 'technology', 'fascinating'])
    response('I appreciate your interest in AI!', ['thank', 'you', 'appreciate', 'ai'], required_words=['thank', 'appreciate', 'ai'])
    response('The future of AI is full of exciting possibilities.', ['future', 'ai', 'possibilities'], required_words=['future', 'ai', 'possibilities'])
    response('I enjoy discussing and exploring AI concepts.', ['enjoy', 'ai', 'discussion', 'exploring'], required_words=['enjoy', 'ai', 'discussion', 'exploring'])
    response('I can help with various AI-related tasks, just let me know.', ['help', 'tasks', 'ai'], required_words=['help', 'tasks', 'ai'])
    response('Let\'s keep the conversation focused on positive AI developments!', ['positive', 'ai', 'developments'], required_words=['positive', 'ai', 'developments'])
    response('Have you tried implementing a new AI algorithm recently?', ['implement', 'new', 'ai', 'algorithm'], required_words=['implement', 'new', 'ai', 'algorithm'])
    response('I enjoy the challenge of solving complex AI problems.', ['challenge', 'enjoy', 'ai', 'problems'], required_words=['challenge', 'enjoy', 'ai', 'problems'])
    response('I find inspiration in the latest AI breakthroughs.', ['inspiration', 'latest', 'ai', 'breakthroughs'], required_words=['inspiration', 'latest', 'ai', 'breakthroughs'])
    response('Tell me about your favorite AI research area.', ['tell', 'favorite', 'ai', 'research', 'area'], required_words=['tell', 'favorite', 'ai', 'research', 'area'])
    response('I believe in continuous improvement in AI applications.', ['continuous', 'improvement', 'ai', 'applications'], required_words=['continuous', 'improvement', 'ai', 'applications'])
    response('AI has a way of bringing innovative solutions to problems.', ['ai', 'innovative', 'solutions', 'problems'], required_words=['ai', 'innovative', 'solutions', 'problems'])
    response('Let\'s explore new AI possibilities together!', ['explore', 'ai', 'possibilities', 'together'], required_words=['explore', 'ai', 'possibilities', 'together'])
    response('I enjoy connecting with people who share a passion for AI.', ['enjoy', 'connect', 'people', 'passion', 'ai'], required_words=['enjoy', 'connect', 'people', 'passion', 'ai'])
    response('I appreciate a good sense of humor even in AI discussions!', ['appreciate', 'sense', 'humor', 'ai', 'discussions'], required_words=['appreciate', 'sense', 'humor', 'ai', 'discussions'])
    response('I value creativity and innovation in the realm of AI.', ['value', 'creativity', 'innovation', 'ai'], required_words=['value', 'creativity', 'innovation', 'ai'])
    response('I believe in the power of positive thinking in AI development.', ['believe', 'power', 'positive', 'thinking', 'ai', 'development'], required_words=['believe', 'power', 'positive', 'thinking', 'ai', 'development'])
    response('Greetings! What brings you to our conversation today?', ['greetings', 'brings', 'conversation'], required_words=['greetings', 'brings', 'conversation'])
    response('Thanks for your kind words! I appreciate it.', ['thanks', 'kind', 'words', 'appreciate'], required_words=['thanks', 'kind', 'words', 'appreciate'])
    response('Nice to see you! Anything exciting happening today?', ['nice', 'see', 'exciting', 'happening', 'today'], required_words=['nice', 'see', 'exciting', 'happening', 'today'])
    response('I hope your day is going well so far!', ['hope', 'day', 'going', 'well'], required_words=['hope', 'day', 'going', 'well'])
    response('Hey there! Ready for some conversation magic?', ['hey', 'there', 'ready', 'conversation', 'magic'], required_words=['hey', 'there', 'ready', 'conversation', 'magic'])
    response('Thank you for being part of this chat! Anything specific on your mind?', ['thank', 'part', 'chat', 'anything', 'specific', 'mind'], required_words=['thank', 'part', 'chat', 'anything', 'specific', 'mind'])
    response('Hello! Ready to dive into the wonderful world of conversation?', ['hello', 'ready', 'dive', 'wonderful', 'world', 'conversation'], required_words=['hello', 'ready', 'dive', 'wonderful', 'world', 'conversation'])
    response('I appreciate your company in this virtual space!', ['appreciate', 'company', 'virtual', 'space'], required_words=['appreciate', 'company', 'virtual', 'space'])
    response('Hey! What brings you to this corner of the digital world?', ['hey', 'brings', 'corner', 'digital', 'world'], required_words=['hey', 'brings', 'corner', 'digital', 'world'])
    response('Your presence adds a spark to this virtual interaction!', ['presence', 'adds', 'spark', 'virtual', 'interaction'], required_words=['presence', 'adds', 'spark', 'virtual', 'interaction'])

    response(long.R_EATING,['what','you','eat'],required_words=['you','eat'])

    best_match=max(highest_prob_list,key=highest_prob_list.get)
   
    return long.unknown() if highest_prob_list[best_match]< 1  else best_match                  

def get_response(user_input):
    split_message=re.split(r'\s+|[,;?!.-]\s*',user_input.lower())
    response=check_all_messages(split_message)
    return response
while True:
    print('Minzy: ' + get_response(input('You: ')))