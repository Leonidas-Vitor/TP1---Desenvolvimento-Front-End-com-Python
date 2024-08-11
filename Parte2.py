import streamlit as st
import pandas as pd

st.header("Parte 2")
st.subheader("Criação de uma Aplicação Streamlit com os Dados",divider=True)

st.markdown('''**5. Crie uma aplicação Streamlit que exiba um título, um cabeçalho, um subcabeçalho e um parágrafo de 
    texto utilizando as funções st.title(), st.header(), st.subheader() e st.text(). Utilize a linguagem de marcação 
    markdown para adicionar um link e um texto em negrito no parágrafo. Inclua printscreens desta etapa.**''')

html_p = """<p style='text-align: center; font-size:%spx;'><b>%s</b></p>"""
github_link = '''https://github.com/Leonidas-Vitor/TP1---Desenvolvimento-Front-End-com-Python'''
st.markdown(html_p % tuple([25,f'GitHub: <a href={github_link}>Link para o repositório</a>']),unsafe_allow_html = True)

st.text("Verifique os códigos abaixo")

st.code(''' 
    st.header("Parte 2")
st.subheader("Criação de uma Aplicação Streamlit com os Dados",divider=True)

st.markdown(\'''**5. Crie uma aplicação Streamlit que exiba um título, um cabeçalho, um subcabeçalho e um parágrafo de 
    texto utilizando as funções st.title(), st.header(), st.subheader() e st.text(). Utilize a linguagem de marcação 
    markdown para adicionar um link e um texto em negrito no parágrafo. Inclua printscreens desta etapa.**\''')

html_p = \"""<p style='text-align: center; font-size:%spx;'><b>%s</b></p>\"""
github_link = \'''https://github.com/Leonidas-Vitor/TP1---Desenvolvimento-Front-End-com-Python\'''
st.markdown(html_p % tuple([25,f'GitHub: <a href={github_link}>Link para o repositório</a>']),unsafe_allow_html = True)

st.text("Verifique os códigos abaixo")
    ''')

st.divider()

st.markdown('''**6. Carregue o dataset "Most Streamed Spotify Songs 2024" utilizando a biblioteca pandas. 
Exiba o DataFrame completo em sua aplicação Streamlit usando as funções st.dataframe() e st.table(). 
Documente as diferenças entre as duas funções. Inclua printscreens desta etapa.**''')

df = pd.read_csv('Most Streamed Spotify Songs 2024.csv', encoding='latin1')

st.code('''df = pd.read_csv('Most Streamed Spotify Songs 2024.csv', encoding='latin1' ''')

#columns = st.columns([0.5,0.5])
#with columns[0]:
st.text('st.dataframe()')
st.dataframe(df.sample(5))

#with columns[1]:
st.text('st.table()')
st.table(df.sample(5))

st.markdown('''***R:***''')
st.text('''
Enquanto que o st.dataframe() exibe o dataframe de forma mais interativa, permitindo a ordenação e filtragem das colunas,
o st.table() exibe o dataframe de forma mais simples, sem a interatividade do st.dataframe().
''')

st.code('''columns = st.columns([0.5,0.5])
with columns[0]:
    st.text('st.dataframe()')
    st.dataframe(df.sample(5))
with columns[1]:
    st.text('st.table()')
    st.table(df.sample(5))
''')

st.divider()

st.markdown('''**7. Selecione três músicas do dataset e adicione à sua aplicação Streamlit a 
exibição do nome da música, o artista e o número de streams utilizando a função st.metric(). 
Explique como esta função pode ser útil em dashboards de dados. Inclua printscreens desta etapa.**
''')

musicas = df[['Track','Artist','Spotify Streams']].sample(3)
columns = st.columns([0.33,0.33,0.33])
with columns[0]:
    st.metric(musicas['Track'].values[0],musicas['Artist'].values[0],musicas['Spotify Streams'].values[0])
with columns[1]:
    st.metric(musicas['Track'].values[1],musicas['Artist'].values[1],musicas['Spotify Streams'].values[1])
with columns[2]:
    st.metric(musicas['Track'].values[2],musicas['Artist'].values[2],musicas['Spotify Streams'].values[2])

st.code('''musicas = df[['Track','Artist','Spotify Streams']].sample(3)
columns = st.columns([0.33,0.33,0.33])
with columns[0]:
    st.metric(musicas['Track'].values[0],musicas['Artist'].values[0],musicas['Spotify Streams'].values[0])
with columns[1]:
    st.metric(musicas['Track'].values[1],musicas['Artist'].values[1],musicas['Spotify Streams'].values[1])
with columns[2]:
    st.metric(musicas['Track'].values[2],musicas['Artist'].values[2],musicas['Spotify Streams'].values[2])
''')

st.markdown('''***R:***''')
st.text('''
A função st.metric() é útil para exibir informações de forma resumida, como se fossem 
cartões de informações, permitindo ver de forma direta e resumida uma determinada medida.
''')

st.divider()

st.markdown('''**8.Na sua aplicação Streamlit, utilize a função st.write() para exibir um DataFrame, 
um texto markdown e uma lista. Demonstre a versatilidade da função st.write() ao lidar com diferentes 
tipos de dados. Inclua printscreens desta etapa.**''')

columns = st.columns([0.33,0.33,0.33])
with columns[0]:
    st.write('Dataframe')
    st.write(df.sample(5))
    st.code('st.write(df.sample(5))')
with columns[1]:
    st.write('Texto markdown')
    st.write('**Texto em negrito**')
    st.code('st.write("**Texto em negrito**")')
with columns[2]:
    st.write('Lista')
    st.write(['Item 1','Item 2','Item 3'])
    st.code('st.write(["Item 1","Item 2","Item 3"])')

st.divider()

st.markdown('''**9. Utilize comandos Magic para apresentar conteúdo na sua aplicação Streamlit. 
Crie um script que exiba um título, uma lista e um DataFrame apenas escrevendo diretamente no 
script sem usar funções explícitas do Streamlit. Inclua printscreens desta etapa.**''')

''' ## Título
- Item 1
- Item 2
- Item 3
'''

df_s = df.sample(5)
df_s

st.code('''\'\'\' ## Título \n- Item 1 \n- Item 2 \n- Item 3 \n\'\'\' \n\ndf_s = df.sample(5)\ndf_s \n\n ''')

st.divider()

st.markdown('''**10. Adicione à sua aplicação Streamlit a exibição de uma imagem, 
um vídeo e um áudio. Utilize as funções st.image(), st.video() e st.audio() para 
incorporar esses elementos multimídia na sua aplicação. Inclua printscreens desta etapa.**''')

columns = st.columns([0.33,0.33,0.33])
with columns[0]:
    st.write('Imagem')
    st.image('Infnet_logo.png',width=200)
with columns[1]:
    st.write('Vídeo')
    st.video('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
with columns[2]:
    st.write('Áudio')
    st.audio('https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3')

st.code('''columns = st.columns([0.33,0.33,0.33])
with columns[0]:
    st.write('Imagem')
    st.image('Infnet_logo.png',width=200)
with columns[1]:
    st.write('Vídeo')
    st.video('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
with columns[2]:
    st.write('Áudio')
    st.audio('https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3')
''')

st.divider()

st.markdown('''**11.Adicione uma animação (GIF) e alguns emojis na sua aplicação Streamlit. 
Utilize as funções apropriadas para garantir que esses elementos sejam exibidos corretamente. 
Inclua printscreens desta etapa.**''')

columns = st.columns([0.5,0.5])
with columns[0]:
    st.write('GIF 1')
    st.image('https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExamM4czI5NTZyanY1eHd0OGpybmQycmIyM28wa3d4ZDVsbDVmMTE1ayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/rRXhFjbIOzXhK/giphy.webp',width=200)

with columns[1]:
    st.write('GIF 2')
    st.image('https://media4.giphy.com/media/l0IybQ6l8nfKjxQv6/200.webp?cid=6c09b9526mvvg3f77s54r5i8p3w241wo7qqqpsyc2919u6hw&ep=v1_gifs_trending&rid=200.webp&ct=g',width=200)

st.code('''
columns = st.columns([0.5,0.5])

with columns[0]:
    st.write('GIF 1')
    st.image('https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExamM4czI5NTZyanY1eHd0OGpybmQycmIyM28wa3d4ZDVsbDVmMTE1ayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/rRXhFjbIOzXhK/giphy.webp',width=200)

with columns[1]:
    st.write('GIF 2')
    st.image('https://media4.giphy.com/media/l0IybQ6l8nfKjxQv6/200.webp?cid=6c09b9526mvvg3f77s54r5i8p3w241wo7qqqpsyc2919u6hw&ep=v1_gifs_trending&rid=200.webp&ct=g',width=200)
''')

st.divider()

st.markdown('''**12.Finalize sua aplicação Streamlit combinando todos os elementos textuais 
aprendidos (título, cabeçalho, subcabeçalho, texto formatado, DataFrame, métricas, multimídia 
e comandos Magic). Utilize o dataset "Most Streamed Spotify Songs 2024" para alimentar os dados
 da aplicação. A aplicação deve ser informativa e visualmente atraente. Inclua printscreens desta etapa.**''')

html_p = """<p style='text-align: center; font-size:%spx;'><b>%s</b></p>"""
github_link = '''https://github.com/Leonidas-Vitor/TP1---Desenvolvimento-Front-End-com-Python'''
st.markdown(html_p % tuple([20,f'GitHub: <a href={github_link}>Link para o repositório</a>']),unsafe_allow_html = True)

streamlit_app = '''https://streamlit.io/cloud'''
st.markdown(html_p % tuple([20,f'APP: <a href={streamlit_app}>Link para o app streamlit publicado</a>']),unsafe_allow_html = True)
