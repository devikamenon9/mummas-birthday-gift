import streamlit as st
st.title("HAPPY BIRTHDAY MUMMA 🎂")
st.write("Happy birthday to the most smartest, prettiest mom to ever exist in this world")
st.write("hope this birthday gift makes up for the fact that i will be missing both your birthdays this year 🌺")
st.write("I hope you enjoy the flowers from me ")
st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExa2t0NWQzYzA3aWZyMG91d3Y0b2o2eDc0NHFoMXgweDN3ZXd4eGFiaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Sy1m3x6DiJzOzeTDan/giphy.gif")
if st.button("🎁 Press Enter (or click) to see your surprise!"):
    st.image("https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3bjh2ZWh1MDdrY2pnMDU1ZTJtb3ZvYXVsZWxwOWQ1OWlhN2lhaW95YSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3vp8lazu6MdVQjsnQP/giphy.gif")
st.write("Enjoy your birthday and i will get you your actual birthday cake after today's shasti")
if st.button(" press enter(or click)"):
    st.image("https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExaGVrazQ2amlzZmRlaDNiNGdhZWcyNDhjbm44MjVvZ3J1eXRneW1idyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/zdaE3A9mqgvAoAbJyv/giphy.gif")

import streamlit as st
import random
compliments = [
    "You always light up my life ♡ ",
    "proud to have you as my mother and I WILL NOT give you away ♡🌷",
    "thanks for always being there for me and being so understanding ୨ৎ",
    "You are my sunshine ♡ ",
    "THE BEST MOM / SISTER EVER FOR ME AND SIMBA ♡🌷",
    "thank you for never giving up and always fighting for me ୨ৎ",
    "BEST COOK EVER ♡",
]
st.title("Your blooming garden 💐🌷🌹🌸🌺")
st.markdown("click the button below and watch an flower grow into a compliment")
if st.button("plant an flower"):
    compliment = random.choice(compliments)
    st.markdown(f"### {compliment}")
    st.image("https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3djB5OXZoc2k3NjBtYnhtZjVsMDlucG14d2tzbHJjMWRjYTJsNTlqNSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/MBAs3td0sgj72/giphy.gif")
st.write(" HOPE YOU LIKE MY GIFTS MUMMA !!!! ")
st.balloons()
