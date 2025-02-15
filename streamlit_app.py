# Import python packages
import streamlit as st


# Write directly to the app
st.title("Customize Your Smoothie! :cup_with_straw:")
st.write(
    "Choose the fruit for your Smoothie"
)

import streamlit as st



from snowflake.snowpark.functions import col

cnx=st.connection("snowflake")
# session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('fruit_name'))
#st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list = st.multiselect('choose upto 5 fruits',my_dataframe)

if ingredients_list:
    ingredients_string = ''

    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen+ ' '
    #st.write(ingredients_string)

    my_insert_stmt = """ insert into smoothies.public.orders(ingredients)
            values ('""" + ingredients_string + """')"""
    #st.write(my_insert_stmt)
    time_to_insert = st.button('submit order')
    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered!', icon="✅")

    






