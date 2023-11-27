import streamlit as st
import pandas as pd

l = []
for i in range(1, 256):
    l.append(f'192.168.0.{i}')

dick = {}
for i in l:
    dick[i] = True

def main():
    text = st.header('IP LIST')
    table = st.table(dick)

if __name__ == '__main__':
    main()