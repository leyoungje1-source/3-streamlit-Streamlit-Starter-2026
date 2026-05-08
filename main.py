import streamlit as st

st.title("🚀 파이썬 배우기 프로젝트")
st.write("30317 이영제.")

name = st.text_input("이름")
if name:
    st.success(f"{name}님, 환영합니다! 이제 코드를 수정해 문제를 해결해 보세요.")