import fungsi

import streamlit as st

'=========================================================================='
# Create a page dropdown
st.header('Aplikasi Seleksi CV')
st.subheader('asd')


page = st.selectbox("Pilih Menu", ["Seleksi CV", "Speech To Text"])

if page == "Seleksi CV":

    from os import listdir
    from os.path import isfile, join

    fungsi.ekstrak()
    p_posisi = ['UI / UX', 'Back-end developer',


                'Front-end developer', 'Cloud Computing', 'Data analytics', 'Network Engineer', 'Mobile Developer']

    pil_posisi = st.selectbox('Pilih Posisi', p_posisi)

    but = st.button('Proses')

    if but:

        mypath = 'CV/'
        allfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        st.write(allfiles)

        list_orang = []
        for filename in allfiles:
            list_orang.append(fungsi.seleksi(filename, pil_posisi, p_posisi))
            # list_orang.append(seleksi(filename))

        list_indeks = []
        for i in list_orang:
            indeks = list_orang.index(i)
            sekor = i['skor']
            list_indeks.append([indeks, sekor])
        list_indeks.sort(key=lambda x: x[1], reverse=True)

        list_ranked = []
        for j in list_indeks:
            for i in list_orang:
                if j[0] == list_orang.index(i):
                    list_ranked.append(i)

        ind = 1
        for j in list_ranked:
            a = ''
            st.subheader(f'{ind}. {j["nama"]}')
            # st.write(j['skil'])
            a = ', '.join(j['skil'])
            st.write('Skill :', a)
            ind += 1


elif page == "Speech To Text":
    fungsi.stt()

elif page == "Tes":
    fungsi.tes()
