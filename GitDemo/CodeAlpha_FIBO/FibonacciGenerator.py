import streamlit as st
st.header("FIBONACCI GENERATOR")

n1 = st.text_input("Enter The Number:")
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fibonacci(n - 1)
        seq.append(seq[-1] + seq[-2])
        return seq     

if st.button("SUBMIT"):
    try:
        n = int(n1)
        k = fibonacci(n)
        st.success(k)
    except ValueError:
        st.error("Please enter a valid integer")