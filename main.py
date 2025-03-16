import streamlit as st

from libs import Library, Member

st.title("Itikaf App")

if "library" not in st.session_state:
    st.session_state.library = Library("My Library")

page = st.sidebar.selectbox("Menu", ["Add Peserta", "Manage Peserta", "List Peserta"])

if page == "Add Peserta":
    st.write("### Add Peserta")
    name = st.text_input("Nama")
    sahur = st.text_input("Menu Sahur")
    buka = st.text_input("Menu Buka")
    minum = st.text_input("Minum")
    button = st.button("Tambah")

    if button:
        new_member = Member(name, sahur, buka, minum)
        st.session_state.library.register_member(new_member)
        st.rerun()

elif page == "Manage Peserta":
    st.write("### Manage Peserta")

    for index, member in enumerate(st.session_state.library.members):
        status = "Active" if member.is_active else "Deactivated"
        st.write(f"{index + 1}. {member.name}, Menu sahur pakai {member.sahur}, Menu buka minta {member.buka}, Minumnya {member.minum} - ({status})")

        deactivate_button = st.button("Deactivate", key=f"deactivate_{index}")

        if deactivate_button:
            member.deactivate()
            st.rerun()

elif page == "List Peserta":
    if not st.session_state.library.members:
        st.write("### List Peserta")
    
    else:
        active_members = st.session_state.library.get_active_members()
        for member in active_members:
            st.write(member.name)