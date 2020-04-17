#!/usr/bin/env python
import pandas as pd
import psycopg2

conn = psycopg2.connect(host='localhost', user='postgres', password='scripts')

df_sql = pd.read_sql('select * from presidents', conn)
print(df_sql.head())

