import streamlit as st

st.title("Parte 1")

st.markdown('''**1. Descreva, em um texto de 200 palavras, a motivação para usar a biblioteca Streamlit no contexto da Ciência de Dados. 
    Inclua exemplos de casos de uso onde Streamlit pode ser vantajoso.**''')

st.markdown('''***R:***''')
st.write('''Streamlit é uma biblioteca que permite criar rapidamente aplicações web interativas, normalmente utilizada para criar dashbaords e 
    visualizações de dados. Por ser uma biblioteca com uma curva de aprendizado baixa, é uma excelente opção para cientistas de dados que
    desejam compartilhar seus resultados de forma interativa e visual. Além disso, pode ser utilizado para realizar uma análise exploratória 
    de dados, pois possui diversos recursos para interação com gráficos e tabelas.
    ''')

st.markdown('''***Exemplos:***''')
st.markdown('''- Criação de portfolio de projetos, streamlit além de interativo e visual, também pode ser hospedado gratuitamente no streamlit cloud.''')
st.markdown('''- Criação de dashboards interativos altamente personalizados, com funções e configurações específicas que outras ferramentas de dashboard não oferecem de forma fácil.''')
st.markdown('''- Análise exploratória de dados, com visualização de gráficos e tabelas interativas''')
st.divider()

st.markdown('**2. Liste e explique pelo menos cinco características principais da biblioteca Streamlit que a tornam adequada para o desenvolvimento de aplicações de Ciência de Dados.**')

st.markdown('''***R:***''')
st.markdown('''1. Fácil de aprender e utilizar, permitindo entregar resultados rápidos''')
st.markdown('''2. Funciona com as principais bibliotecas de Ciência de Dados, como Pandas, Matplotlib e Scikit-learn''')
st.markdown('''3. Permite criar aplicações web interativas com maior grau de personalização do que aplicativos de dashboard tradicionais''')
st.markdown('''4. Compartilhamento fácil, rápido e de baixo custo, podendo ser hospedado no streamlit cloud gratuitamente''')
st.markdown('''5. Visualização de dados e gráficos em tempo real com opção de interatividade, permitindo a exploração de dados de forma dinâmica''')

st.divider()

st.markdown('**3. Crie um ambiente virtual utilizando virtualenv ou pipenv, e instale as dependências necessárias para desenvolver uma aplicação Streamlit. Documente cada etapa do processo e descreva as vantagens de utilizar um ambiente virtual para o desenvolvimento de software.**')

st.image('Criação de ambiente.png')

st.code('pip install requirements.txt')

st.markdown('''***R:***''')
st.markdown('''- Facilidade para compartilhar o projeto com outros desenvolvedores.''')
st.markdown('''- Dependências específicas para cada projeto, sem comprometer as versões do sistema.''')
st.markdown('''- Garantia de funcionamento do projeto em diferentes máquinas.''')


st.divider()

st.markdown('**4. Utilizando o ambiente virtual criado no exercício anterior, instale a biblioteca Streamlit usando pip. Em seguida, crie um pequeno script em Python que exiba a mensagem "Hello, Streamlit!" utilizando a função st.write(). Documente cada etapa do processo.**')

st.write('Instalação da biblioteca Streamlit:')
st.code('pip install streamlit')

st.write("Hello, Streamlit!")
st.code('st.write("Hello, Streamlit!")')
