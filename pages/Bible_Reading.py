import os
import mysql.connector
import pandas as pd
import numpy as np
import streamlit as st
import time
from io import StringIO

st.header("Bible Reading App")
"""
GRII Solo mendorong kerohanian setiap jemaat untuk semakin bertumbuh melalui Firman Tuhan. Oleh karena itu, program Bible Reading ini dirancang agar Anda mempunyai group partner dalam membaca dan merenungkan Firman Tuhan.
"""

config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'bible_reading',
    'port': 3306,
}

def execute_sql(query):
    # Implementasi fungsi ini untuk menjalankan kueri SQL pada database MySQL
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor(dictionary=True)  # Menggunakan cursor dictionary agar hasil dapat diakses dengan nama kolom
    cursor.execute(query)
    result = cursor.fetchall()
    connection.close()
    return result