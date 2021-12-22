import streamlit as st
import en_core_web_sm
import PyPDF2
import pdfplumber
from pyresparser import ResumeParser
from pydub import AudioSegment
import librosa
import soundfile as sf


def seleksi():

    posisi = 'Data analytics'

    st.write('Page 1')

    f1 = 'CV/CV.pdf'

    data = ResumeParser(f1).get_extracted_data()

    skills = data['skills']

    skills = []

    for i in data['skills']:

        skills.append(i.lower())

    terms = {'Quality/Six Sigma': ['black belt', 'capability analysis', 'control charts', 'doe', 'dmaic', 'fishbone',

                                   'gage r&r', 'green belt', 'ishikawa', 'iso', 'kaizen', 'kpi', 'lean', 'metrics',

                                   'pdsa', 'performance improvement', 'process improvement', 'quality',

                                   'quality circles', 'quality tools', 'root cause', 'six sigma',

                                   'stability analysis', 'statistical analysis', 'tqm'],

             'Operations management': ['automation', 'bottleneck', 'constraints', 'cycle time', 'efficiency', 'fmea',

                                       'machinery', 'maintenance', 'manufacture', 'line balancing', 'oee', 'operations',

                                       'operations research', 'optimization', 'overall equipment effectiveness',

                                       'pfmea', 'process', 'process mapping', 'production', 'resources', 'safety',

                                       'stoppage', 'value stream mapping', 'utilization'],

             'Supply chain': ['abc analysis', 'apics', 'customer', 'customs', 'delivery', 'distribution', 'eoq', 'epq',

                              'fleet', 'forecast', 'inventory', 'logistic', 'materials', 'outsourcing', 'procurement',

                              'reorder point', 'rout', 'safety stock', 'scheduling', 'shipping', 'stock', 'suppliers',

                              'third party logistics', 'transport', 'transportation', 'traffic', 'supply chain',

                              'vendor', 'warehouse', 'wip', 'work in progress'],

             'Project management': ['administration', 'agile', 'budget', 'cost', 'direction', 'feasibility analysis',

                                    'finance', 'kanban', 'leader', 'leadership', 'management', 'milestones', 'planning',

                                    'pmi', 'pmp', 'problem', 'project', 'risk', 'schedule', 'scrum', 'stakeholders'],

             'Data analytics': ['analytics', 'api', 'aws', 'big data', 'busines intelligence', 'clustering', 'code',

                                'coding', 'data', 'database', 'data mining', 'data science', 'deep learning', 'hadoop',

                                'hypothesis test', 'iot', 'internet', 'machine learning', 'modeling', 'nosql', 'nlp',

                                'predictive', 'programming', 'python', 'r', 'sql', 'tableau', 'text mining',

                                'visualuzation'],

             'Healthcare': ['adverse events', 'care', 'clinic', 'cphq', 'ergonomics', 'healthcare',

                            'health care', 'health', 'hospital', 'human factors', 'medical', 'near misses',

                            'patient', 'reporting system']}

    quality = 0

    operations = 0

    supplychain = 0

    project = 0

    data_science = 0

    healthcare = 0

    # # Create an empty list where the scores will be stored

    scores = []
    kemampuan = []

    # Obtain the scores for each area

    for area in terms.keys():

        if area == 'Quality/Six Sigma':

            for skill in terms[area]:

                if skill in skills:
                    kemampuan.append(skill)

                    quality += 1

            scores.append(quality)

        elif area == 'Operations management':

            for skill in terms[area]:

                if skill in skills:
                    kemampuan.append(skill)

                    operations += 1

            scores.append(operations)

        elif area == 'Supply chain':

            for skill in terms[area]:

                if skill in skills:
                    kemampuan.append(skill)

                    supplychain += 1

            scores.append(supplychain)

        elif area == 'Project management':

            for skill in terms[area]:

                if skill in skills:
                    kemampuan.append(skill)

                    project += 1

            scores.append(project)

        elif area == 'Data analytics':

            for skill in terms[area]:

                if skill in skills:
                    kemampuan.append(skill)

                    data_science += 1

            scores.append(data_science)

        elif area == 'Healthcare':

            for skill in terms[area]:

                if skill in skills:
                    kemampuan.append(skill)

                    healthcare += 1

            scores.append(healthcare)

    st.write(f'Kemampuan yang dimiliki oleh {data["name"]} \n {"="*50}')

    # st.write(data['name'])

    ind = 0
    job = {}

    for x in terms.keys():

        st.write(f'{x}: {scores[ind]}')
        job[x] = scores[ind]

        ind += 1

    a = {}

    a[data['name']] = [posisi, job[posisi], kemampuan]
    st.write(a)

    return a


def stt():

    song = AudioSegment.from_mp3('aziz1.mp3')

    newSong = song

    newSong.export('aziz1.wav', format="wav")


'=========================================================================='


# Create a page dropdown

page = st.selectbox("Pilih Menu", ["Seleksi CV", "Speech To Text"])


if page == "Seleksi CV":

    # Display details of page 1

    genre = st.radio(

        "Apakah ingin menambahkan data ? ",

        ('Yes', 'No'))

    if genre == 'Yes':

        form = st.form(key='my_form')

        name = form.text_input(label='Enter some text')

        submit_button = form.form_submit_button(label='Submit')

        if submit_button:

            st.write(f'hello {name}')

        # st.write('You selected comedy.')

    else:

        # st.write("You didn't select comedy.")

        seleksi()


elif page == "Speech To Text":

    # Display details of page 2

    # st.write('Page 2')

    # form = st.form(key='my_form')

    # name = form.text_input(label='Enter some text')

    # submit_button = form.form_submit_button(label='Submit')

    # if submit_button:

    #     st.write(f'hello {name}')

    # nlp = en_core_web_sm.load()

    # cv = st.sidebar.button('Seleksi CV')

    # if cv:

    #     f1 = 'CV\CV.pdf'

    #     data = ResumeParser(f1).get_extracted_data()

    #     st.write(data)

    # stt = st.sidebar.button('Speech to Text')

    # if stt:

    #     form = st.form(key='my_form')

    #     name = form.text_input(label='Enter some text')

    #     submit_button = form.form_submit_button(label='Submit')

    #     if submit_button:

    #         st.write(f'hello {name}')
    pass
