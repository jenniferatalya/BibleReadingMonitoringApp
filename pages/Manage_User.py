import streamlit as st
import pandas as pd
from Bible_Reading import execute_sql

# Streamlit app header
st.header("Manage User ")

show_fact = execute_sql('''SELECT 
                                A.id_anggota, 
                                A.nama_anggota, 
                                K.nama_kelompok, 
                                G.nama_gereja, 
                                A.nomor_handphone
                            FROM 
                                dim_anggota A
                            JOIN 
                                dim_kelompok K ON A.id_kelompok = K.id_kelompok
                            JOIN 
                                dim_gereja G ON A.id_gereja = G.id_gereja;
                            ''')

df = pd.DataFrame(show_fact)

st.dataframe(df, use_container_width=True, hide_index=True)