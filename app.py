import streamlit as st

st.title("Lunch Order App")

with st.form(key='my_form'):
    name = st.text_input(label='Enter your name')

    appetizer = st.selectbox('Appetizer', ['Salad', 'Fries', 'Mozzarella Sticks'])
    main = st.selectbox('Main Course', ['Steak', 'Salmon', 'Tofu'])
    dessert = st.selectbox('Dessert', ['Apple Pie', 'Ice Cream', 'Chocolate'])  
    drink = st.selectbox('Drink', ['Water', 'Coke', 'Beer'])


    submit_button = st.form_submit_button(label='Submit')

order = {'Name': name, 'Appetizer': appetizer, 'Main Course': main, 'Dessert': dessert, 'Drink': drink}

st.write(order)

prices =  {'Salad': 5, 'Fries': 3, 'Mozzarella Sticks': 4, 'Steak': 25, 
           'Salmon': 12, 'Tofu': 9, 'Apple Pie': 7, 'Ice Cream': 3, 'Chocolate': 5, 'Water': 0, 'Coke': 2, 'Beer': 5}

total = 0
for item in order:
    if order[item] in prices:
        total += prices[order[item]]


st.write("Your total is: $", total)