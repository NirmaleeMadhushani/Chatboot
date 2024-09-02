# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 14:37:32 2023

@author: User
"""

import random

R_EATING="I don't like eating anything because I'm a bot obviously!"

def unknown():
    responsesp=['Could you please re-phrase that?',
              "...",
              "Sounds about right",
              "What does that mean?"][random.randrange(4)]
    return responsesp 