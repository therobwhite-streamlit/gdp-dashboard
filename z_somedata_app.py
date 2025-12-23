import streamlit as st
import pandas as pd
import numpy as np
import math
import requests
import io
from pathlib import Path

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='UK Census 2021 dashboard',
    # page_icon=':earth_americas:', # This is an emoji shortcode. Could be a URL too.
)

# -----------------------------------------------------------------------------
# Declare some useful functions.

@st.cache_data
def get_data():
        # Instead of a CSV on disk, you could read from an HTTP endpoint here too.
    
    df_url = 'https://raw.githubusercontent.com/robwhite-lis/Everything_Counts_Assessment_2/refs/heads/main/census-2021-publicmicrodatateachingsample.csv'
    url_content = requests.get(df_url, verify = False).content
    raw_df = pd.read_csv(io.StringIO(url_content.decode('utf-8')))
    
    gdp_df = raw_df

    return gdp_df

gdp_df = get_data()

# -----------------------------------------------------------------------------
# Draw the actual page

# Set the title that appears at the top of the page.
'''
Pull up some UK Census Data 
'''

# Add some spacing
''
''

''
''
''

# Filter the data
filtered_gdp_df = gdp_df[
    (gdp_df['hh_families_type_6a']==4)
]

st.header('UK Data', divider='gray')

''

hist_values=np.histogram(
    gdp_df['approx_social_grade'], bins = 4, range=None
)

st.bar_chart(hist_values)

# st.line_chart(
#     filtered_gdp_df,
#     x='sex',
#     y='approx_social_grade',
#     color='ethnic_group_tb_6a',
#)

''
''


# first_year = gdp_df[gdp_df['Year'] == from_year]
# last_year = gdp_df[gdp_df['Year'] == to_year]

# st.header(f'GDP in {to_year}', divider='gray')

# ''

# cols = st.columns(4)

# for i, country in enumerate(selected_countries):
#     col = cols[i % len(cols)]

#     with col:
#         first_gdp = first_year[first_year['Country Code'] == country]['GDP'].iat[0] / 1000000000
#         last_gdp = last_year[last_year['Country Code'] == country]['GDP'].iat[0] / 1000000000

#         if math.isnan(first_gdp):
#             growth = 'n/a'
#             delta_color = 'off'
#         else:
#             growth = f'{last_gdp / first_gdp:,.2f}x'
#             delta_color = 'normal'

#         st.metric(
#             label=f'{country} GDP',
#             value=f'{last_gdp:,.0f}B',
#             delta=growth,
#             delta_color=delta_color
#         )
