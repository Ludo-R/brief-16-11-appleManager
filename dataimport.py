#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 10:00:26 2020

@author: randon
"""

from sqlalchemy import create_engine
import pandas as pd
import pymysql
engine = create_engine("mysql+pymysql://root:sqlpwd@localhost/applemanager")

def chargement(link, table):

    df = pd.read_csv(link)
    df.to_sql(table, con = engine, if_exists='append', index = False)
    return print("done")

chargement('/home/randon/git/brief-16-11-appleManager/dataset/dataset-apple-manager.csv', 'users') 
