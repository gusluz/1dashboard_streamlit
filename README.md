## Dashboard de Pacientes Cardíacos
Esta aplicação interativa analisa dados de admissões hospitalares cardíacas na Índia entre 2017 e 2019, auxiliando na compreensão de padrões e tendências para melhor atendimento aos pacientes.

![Média de dias internados por idade](https://github.com/gusluz/1dashboard_streamlit/blob/main/dashboard_1.png)
![Correlação entre idade, dias de internação, ano e fatores de risco](https://github.com/gusluz/1dashboard_streamlit/blob/main/dashboard_2.png)

**Dados:**
- Fonte: [Hospital Admissions Data](https://www.kaggle.com/datasets/ashishsahani/hospital-admissions-data)

**Funcionalidades:**
- **Filtros:** Selecione datas de admissão e gênero para focar sua análise.
- **Média de Internação:** Visualize a média de dias de internação por idade e ano.
- **Fatores de Risco:** Explore a correlação entre idade, dias de internação, ano e fatores de risco (DM, hipertensão, tabagismo, consumo de álcool).
- **Visualizações:** Gráficos interativos para fácil interpretação dos dados.

**Instalação e execução:**
1. **Clone o repositório:** `git clone https://github.com/seu_usuario/dashboard_pacientes_cardiacos.git`
2. **Crie o ambiente virtual:** `conda env create -f environment.yml`
3. **Ative o ambiente:** `conda activate env_dashb`
4. **Rode o script:** `python dashboard.py`
5. **Acesse o dashboard:** O navegador abrirá automaticamente a aplicação na URL `http://127.0.0.1:8501`.

**Desenvolvido com:**
- Streamlit
- Pandas
- Plotly.express

**Agradecimentos:**
Agradecemos aos autores do dataset utilizado e à comunidade Streamlit pelo suporte.

**Importante:**
Verifique se tem o Anaconda instalado e as permissões necessárias para criar ambientes virtuais.


