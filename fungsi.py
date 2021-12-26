import speech_recognition as sr
import soundfile as sf
import librosa
from pydub import AudioSegment
from pyresparser import ResumeParser
import pdfplumber
import PyPDF2
import en_core_web_sm
import streamlit as st
import os
import nltk

nltk.download('stopwords')

# os.system('python -m spacy download en')
# os.system('pip install speech_recognition')


def extract_data(feed):

    data = []

    with pdfplumber.load(feed) as pdf:

        pages = pdf.pages

        for p in pages:

            data.append(p.extract_tables())

    return None


def ekstrak():

    uploaded_file = st.file_uploader('Choose your .zip file', type="zip")
    import zipfile

    if uploaded_file is not None:
        with zipfile.ZipFile(uploaded_file, "r") as zip_ref:
            zip_ref.extractall("CV")

    else:
        pass


def seleksi(f1, pil_posisi, p_posisi):

    if f1 is not None:

        data = ResumeParser('CV/'+str(f1)).get_extracted_data()

        skills = data['skills']

        skills = []

        for i in data['skills']:

            skills.append(i.lower())

        terms = {'UI / UX':             ['sketch', 'figma', 'invision', 'concept', 'drawing', 'user flow', 'diagram', 'wireframe', 'prototype',


                                         'adobe', 'photoshop', 'illustrator', 'zeplin', 'xd', 'marvel'],


                 'Back-end developer':   ['api', 'php', 'python', 'mysql', 'mariadb', 'git', 'codeigniter', 'express', 'scrum agile', 'java', 'laravel'],


                 'Front-end developer':  ['html', 'css', 'javascript', 'node.js', 'react', 'react.js', 'vue.js', 'angular', 'bootstrap', 'git'],


                 'Cloud Computing':      ['aws', 'azure', 'google', 'docker', 'vmware', 'cloud', 'server', 'storage', 'kubernetes', 'architect', 'migration',


                                          'it infrastructure', 'network', 'ci', 'cd', 'jenkins', 'nginx', 'terraform'],


                 'Data analytics':       ['analytics', 'api', 'aws', 'big data', 'busines intelligence', 'clustering', 'code',


                                          'coding', 'data', 'database', 'data mining', 'data science', 'deep learning', 'hadoop',


                                          'hypothesis test', 'iot', 'internet', 'machine learning', 'modeling', 'nosql', 'nlp',


                                          'predictive', 'programming', 'python', 'r', 'sql', 'tableau', 'text mining',


                                          'visualuzation', 'excel', 'spss', 'sas'],


                 'Network Engineer':     ['routing', 'dns', 'wan', 'man', 'lan', 'firewall', 'tcp/ip', 'dhcp', 'vpn', 'networking'],


                 'Mobile Developer':     ['kotlin', 'java', 'android', 'ios', 'sqlite', 'firebase', 'oop', 'flutter', 'api', 'swift', 'react', 'rest',


                                          'json', 'solid', 'git', 'dart', 'android studio', 'xcode', 'rest api']}

        ui = 0

        backen = 0

        frontend = 0

        cloud = 0

        analytics = 0

        network = 0

        mobile = 0

        # # Create an empty list where the scores will be stored

        scores = []

        kemampuan = {}

        # Obtain the scores for each area

        for area in terms.keys():

            kemampuan[area] = []

            if area == 'UI / UX':

                for skill in terms[area]:

                    if skill in skills:

                        kemampuan[area].append(skill)

                        ui += 1

                scores.append(ui)

            elif area == 'Back-end developer':

                for skill in terms[area]:

                    if skill in skills:

                        kemampuan[area].append(skill)

                        backen += 1

                scores.append(backen)

            elif area == 'Front-end developer':

                for skill in terms[area]:

                    if skill in skills:

                        kemampuan[area].append(skill)

                        frontend += 1

                scores.append(frontend)

            elif area == 'Cloud Computing':

                for skill in terms[area]:

                    if skill in skills:

                        kemampuan[area].append(skill)

                        cloud += 1

                scores.append(cloud)

            elif area == 'Data analytics':

                for skill in terms[area]:

                    if skill in skills:

                        kemampuan[area].append(skill)

                        analytics += 1

                scores.append(analytics)

            elif area == 'Network Engineer':

                for skill in terms[area]:

                    if skill in skills:

                        kemampuan[area].append(skill)

                        network += 1

                scores.append(network)

            elif area == 'Mobile Developer':

                for skill in terms[area]:

                    if skill in skills:

                        kemampuan[area].append(skill)

                        mobile += 1

                scores.append(mobile)

        ind = 0

        job = {}

        for x in terms.keys():

            job[x] = scores[ind]

            ind += 1

        a = {}

        job = {'nama': f1, 'posisi': pil_posisi,
               'skor': job[pil_posisi], 'skil': kemampuan[pil_posisi]}

        # st.write(job)

        return job

    else:

        st.write('Silahkan Upload Data')


def stt():

    upload_mp3 = st.file_uploader('Choose your .mp3 file', type="mp3")

    if upload_mp3 is not None:

        song = AudioSegment.from_mp3(upload_mp3)

        newSong = song

        newSong.export(f'output/{upload_mp3.name[0:-4]}.wav', format="wav")

        # st.write(upload_mp3.name[0:-4])
        audio_path = f'output/{upload_mp3.name[0:-4]}.wav'
        x, sampleRate = librosa.load(audio_path)

        pos = []
        neg = []
        for i in x:
            if i > 0:
                pos.append(i)
            elif i < 0:
                neg.append(i)

        pos.sort()
        neg.sort()

        pos1 = int(0.3*len(pos))

        neg1 = int(0.3*len(neg))

        l = []

        start = 0
        end = 0
        counter = 0
        list_counter = []

        for i in range(len(x)):
            if neg[neg1] <= x[i] and x[i] <= pos[pos1]:
                counter += 1

            else:
                if counter > 500:
                    list_counter.append(counter)
                    counter = 0

            start = i

            if counter == 5000:
                end = i
                l.append(i)

        audio_dict = {}
        for i in range(len(l)):
            if i == 0:
                print(i)
                temp_audio = x[:l[i]]
                sf.write(
                    f'output/example/{upload_mp3.name[0:-4]}_{str(i)}.wav', temp_audio, sampleRate)
            else:
                print(i)
                star = l[i-1]
                temp_audio = x[star:l[i]]
                sf.write(
                    f'output/example/{upload_mp3.name[0:-4]}_{str(i)}.wav', temp_audio, sampleRate)

            audio_dict[i] = temp_audio

        r = sr.Recognizer()

        a = []

        for i in range(len(audio_dict)):
            path = f'output/example/{upload_mp3.name[0:-4]}_{str(i)}.wav'
            x1, sampleRate1 = librosa.load(path)

            try:
                with sr.AudioFile(path) as source:
                    # listen for the data (load audio to memory)
                    # Load audio ke memori
                    audio_data = r.record(source)
                    # recognize (convert from speech to text)
                    # konversi audio ke teks dan menggunakan bahasa Indonesia (id), bahasa dapat diganti sesuai dengan kebutuhan
                    text = r.recognize_google(audio_data, language='id')
                    # Simpan teks
                    a.append(text)

            except:
                print(path, ' kosong')

        for i in a:
            f = open(f"output/text/{upload_mp3.name[0:-4]}.txt", "a")
            f.write(i+'\n')
            f.close()

    else:
        st.write('Silahkan Upload File mp3')
