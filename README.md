# Inteli - Instituto de Tecnologia e Liderança 

<p align="center">
<a href= "https://www.inteli.edu.br/"><img src="https://capitaldigital.com.br/wp-content/uploads/2021/04/logo-inteli-300x134-1.png" alt="Inteli - Instituto de Tecnologia e Liderança" border="0" width=40% height=40%></a>
</p>

<br>

# Projeto: Mensurar o sentimento de clientes em relação a Uber através do desenvolvimento de uma aplicação utilizando linguagem natural.

## Grupo 1

### 🚀 Integrantes
- <a href="https://www.linkedin.com/in/celine-souza-1a38aa225//">Celine Souza</a>
- <a href="https://www.linkedin.com/in/eduardo-hos/">Eduardo Henrique</a>
- <a href="https://www.linkedin.com/in/henrique-cox-4644bb270/">Henrique Cox</a>
- <a href="https://www.linkedin.com/in/marcelo-saadi-pessini-003212209/">Marcelo Saadi</a>
- <a href="https://www.linkedin.com/in/mateus-mar%C3%A7al-212953264/">Mateus Marçal</a>
- <a href="https://www.linkedin.com/in/omatheusrsantos/">Matheus Ribeiro</a>
- <a href="https://www.linkedin.com/in/otto-bernardo-coutinho-lima/">Otto Bernardo</a>

## 📜 Descrição

Desenvolvendo uma solução de análise de sentimentos para a Uber, utilizando processamento de linguagem natural. O objetivo é monitorar e compreender o sentimento dos clientes em relação aos serviços da Uber, identificando áreas de melhoria e oportunidades para aprimorar a experiência do usuário. O projeto inclui a criação de modelos de aprendizado de máquina, integração com sistemas existentes da Uber e entrega de insights através de plataformas como Slack.

## 📁 Estrutura de pastas

- Raiz<br>

```plaintext
assets
└── documentos
    └── outros
        └── img
        └── apresentacao
    └── documentation.md
    └── README.md
src
├── api
│   ├── .venv
│   ├── .gitignore
│   ├── api.py
│   ├── Boot_API.ipynb
│   ├── boot-model-firebase-adminsdk-iqw0z-601a2fa03b.json
│   ├── Dockerfile
│   ├── firestore.py
│   ├── requirements.txt
│   └── teste.py
├── data
├── front-end
│   ├── public
│   └── src
│       ├── .gitignore
│       ├── package-lock.json
│       ├── package.json
│       └── README.md
└── versions
└── .gitignore
└── Boot_Models.ipynb
└── Boot_OFICIAL.ipynb
└── boot.ipynb
└── cohen_kappa.ipynb
└── readme.md
└── requirements.txt
└── youden_metric.ipynb
LICENSE.md
README.md --> você está aqui ⭐
```

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- assets: aqui estão os arquivos relacionados a parte gráfica do projeto, ou seja, as imagens e vídeos que os representam.

- documentos: aqui estão todos os documentos do projeto, incluindo o manual de instalações. Há também uma pasta denominada outros onde estão presentes outros documentos complementares.

- src: Todo o código fonte criado para o desenvolvimento do projeto, incluindo todos os notebooks front-end e API.

- README.md: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).


## 🔧 Instalação

**Pré-requisitos:**

Docker instalado em seu sistema: https://docs.docker.com/get-docker/


**Instalação:**

Claro, aqui está a versão aprimorada da explicação, incluindo as etapas necessárias para garantir que o Docker esteja aberto na máquina e a execução do `docker-compose build`:

**Pré-requisitos:**

1. Docker instalado em seu sistema: [Instalar Docker](https://docs.docker.com/get-docker/)

**Passo a passo:**

1. Certifique-se de que o Docker esteja aberto em execução na sua máquina.

2. Clone o repositório: 
   ```bash
   git clone https://github.com/Inteli-College/2024-1B-T10-SI06-G01
   ```

3. Acesse o diretório da API: 
   ```bash
   cd src/api
   ```

4. Construa os containers Docker:
   ```bash
   docker-compose build
   ```

5. Execute o Docker Compose:
   ```bash
   docker-compose -f compose.yaml up
   ```

6. Em uma nova janela de terminal, compile a aplicação React:
   ```bash
   cd ../../frontend
   npm install
   npm run build
   ```

7. Copie o diretório build do React para o diretório static da aplicação Flask:
   ```bash
   cp -r ../frontend/build ../app/static
   ```

8. Acesse a aplicação:
   - No navegador: Abra a URL [http://localhost:5000](http://localhost:5000)

**Vídeo de Deploy do modelo** [aqui](https://drive.google.com/file/d/1qVTtigIE5_PDkbi5kXdVfjEpcpfiuSSs/view?usp=drive_link)

## 🗃 Histórico de lançamentos

* 0.5.0 - 21/06/2024
     * Apresentação Final
     * Deploy do Melhor Modelo(FastText com SVM)
     * Documentação completa da Solução
     * Front-end Integrado a API
* 0.4.0 - 07/06/2024
     * Implementação da API (IPYNB)
     * Documentação da API
     * Primeira Versão Conectado ao Slack
* 0.3.0 - 24/05/2024
     * Modelo utilizando Word2Vec (IPYNB)
     * Documentação do Modelo utilizando Word2Vec
* 0.2.0 - 10/05/2024
    * Exploratória dos dados. 
    * Pré-Processamento.
    * Modelo Bag Of Words.
* 0.1.0 - 25/04/2024
     * Entendimento do Negócio.
     * Entendimento da Experiência do Usuário.


## 📋 Licença/License

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/2023M6T4-Inteli">NPL para sentimentos</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/InteliProjects">Inteli</a>, <a rel="cc:attributionURL dct:creator" property="https://github.com/Inteli-College/2024-1B-T10-SI06-G01">G1</a>, <a href="https://www.linkedin.com/in/celine-souza-1a38aa225//">Celine Souza</a>, <a href="https://www.linkedin.com/in/eduardo-hos/">Eduardo Henrique</a>, <a href="https://www.linkedin.com/in/henrique-cox-4644bb270/">Henrique Cox</a>, <a href="https://www.linkedin.com/in/marcelo-saadi-pessini-003212209/">Marcelo Saadi</a>, <a href="https://www.linkedin.com/in/mateus-mar%C3%A7al-212953264/">Mateus Marçal</a>, <a href="https://www.linkedin.com/in/omatheusrsantos/">Matheus Ribeiro</a>, <a href="https://www.linkedin.com/in/otto-bernardo-coutinho-lima/">Otto Bernardo</a>,
is licensed under <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"></a></p>

## 🎓 Referências

1. BoW: https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction

2. OSTERWALDER, A.; PIGNEUR, Y.; BERNARDES, G.; SMITH, A. Value Proposition Design: How to Create Products and Services Customers Want. New Jersey: Wiley, 2014: https://edisciplinas.usp.br/pluginfile.php/7633948/mod_resource/content/1/Value%20Proposition%20Design.pdf

3. RAEBURN, A. (2022, 28 de novembro). Análise SWOT/FOFA: o que é e como usá-la (com exemplos). asana. Disponível em: https://asana.com/pt/resources/swot-analysis?gclid=CjwKCAjww7KmBhAyEiwA5-PUStFYfdjQk1NDB65i4CO2FKSIh7XsE-8s6JXOQBSOJ6NEsmQlpH90_xoChhkQAvD_BwE&gclsrc=aw.ds

4. ESFERA ENERGIA. (2022, 14 de outubro). Matriz de risco: o que é, quando usar e como montar uma tabela. esferablog. Disponível em: https://blog.esferaenergia.com.br/gestao-empresarial/matriz-de-risco. Acesso em: 25 out. 2023.

5. Chan Kim, W., & Mauborgne, R. (2019). A estratégia do oceano azul: Como criar novos mercados e tornar a concorrência irrelevante (A. Celso da Cunha Serra, Trad.; 2a ed.). Editora Sextante. Acesso em 18 abr. 2024.

6. GLASSDOOR. Salários de Software Developer da empresa Uber. 11 abr. 2021. Disponível em: https://www.glassdoor.com.br/Salário/Uber-Software-Developer-Salários-E575263_D_KO5,23.htm. Acesso em: 23 abr. 2024.

7. CALCULADORA de preços do Google Cloud. Disponível em: https://cloud.google.com/products/calculator?dl=CiRjYTQ0YTQ2Yy0xNzU4LTQ0NjAtOWMwMC00YTJjMTNhOWVjNDQQCBokMTAyNDJEODYtMDQwQS00Q0M2LUEzMjYtOERBRkY4ODM0NTY3&hl=pt_br. Acesso em: 24 abr. 2024.

8. X API | Products. Disponível em: https://developer.twitter.com/en/products/twitter-api. Acesso em: 24 abr. 2024.

9. CAROLI, Paulo. Lean Inception: Como alinhar pessoas e construir o produto certo. [S. l.]: Editora Caroli; PREFÁCIO DE MARTIN FOWLER edição (1 dezembro 2018), 2018. 160 p. ISBN 8594377061.

10. ROCKETCONTENT. Descubra o que é buyer persona e passo a passo para criar as suas. Disponível em: https://rockcontent.com/br/blog/personas/. Acesso em: 22 abr. 2024.

11. LINKEDIN. Estratégia de marketing. Disponível em: https://www.linkedin.com/jobs/search/?currentJobId=3908135403&f_C=1815218&geoId=92000000&keywords=Estrat%C3%A9gia%20de%20marketing&location=Mundialmente&origin=JOB_SEARCH_PAGE_KEYWORD_AUTOCOMPLETE&refresh=true. Acesso em: 18 abr. 2024.

12. LINKEDIN. Analista de dados. Disponível em: https://www.linkedin.com/jobs/search/?currentJobId=3888771947&f_C=1815218&geoId=92000000&keywords=Analista%20de%20dados&location=Mundialmente&origin=JOB_SEARCH_PAGE_KEYWORD_AUTOCOMPLETE&refresh=true. Acesso em: 18 abr. 2024.

13. LINKEDIN. Gerente de operações. Disponível em: https://www.linkedin.com/jobs/search/?currentJobId=3902290404&f_C=1815218&geoId=92000000&keywords=operation%20manager&location=Mundialmente&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true. Acesso em: 18 abr. 2024.

14. EY. Strategy & Operations Manager. Disponível em: https://careers.ey.com/ey/job/Taguig-Strategy-&-Operations-Manager-1634/1022313201/. Acesso em: 22 abr. 2024.

15. INDEED. What Does a Social Media Analyst Do? (With Duties and Skills). Disponível em: https://www.indeed.com/career-advice/finding-a-job/what-does-social-media-analyst-do. Acesso em: 20 abr. 2024.

16. ZIPRECRUITER. What Is a Sales Operations Analyst and How to Become One. Disponível em: https://www.ziprecruiter.com/career/Sales-Operations-Analyst/What-Is-How-to-Become#:~:text=A%20sales%20operations%20analyst%20works,programs%2C%20and%20managing%20customer%20relationships. Acesso em: 20 abr. 2024.

17. THISPERSONDOESNOTEXIST. Disponível em: https://thispersondoesnotexist.com/. Acesso em: 26 abr. 2024.

18. AWARI. User Stories: Como Criar e Utilizar para um Desenvolvimento de Software. 9 nov. 2021. Disponível em: https://awari.com.br/user-stories/?utm_source=blog&utm_campaign=projeto+blog&utm_medium=User%20Stories:%20Como%20Criar%20e%20Utilizar%20para%20um%20Desenvolvimento%20de%20Software. Acesso em: 22 abr. 2024.

19. PROCESSAMENTOS de linguagem natural. Porto Alegre: SAGAH, 2020. 1 recurso online. (Inteligência artificial). ISBN 9786556900575. Disponível em: https://integrada.minhabiblioteca.com.br/books/9786556900575. Acesso em: 2 mai. 2024.

20. ROSS, Sheldon. Probabilidade. Bookman; 8ª edição: Grupo A, 2010. E-book. ISBN 9788577806881. Disponível em: https://integrada.minhabiblioteca.com.br/#/books/9788577806881/. Acesso em: 02 mai. 2024.

21. Shukla, P. S. (2024, março). Naive Bayes Algorithms: A Complete Guide for Beginners. Analytics Vidhya. https://www.analyticsvidhya.com/blog/2023/01/naive-bayes-algorithms-a-complete-guide-for-beginners/. Acesso em: 02 mai. 2024.

22. Blog MBA USP ESALQ. (2022, 12 de abril). CRISP-DM: as 6 etapas da metodologia do futuro. Recuperado de https://blog.mbauspesalq.com/2022/04/12/crisp-dm-as-6-etapas-da-metodologia-do-futuro/. Acesso em: 06 mai. 2024.

23. SPSS Modeler. 23 jan. 2024. Disponível em: https://www.ibm.com/docs/pt-br/spss-modeler/18.5.0?topic=dm-crisp-help-overview. Acesso em: 13 maio 2024.

24. ISO 25010. Disponível em: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010. Acesso em: 13 maio 2024.

25. MARTINS, Júlio S.; LENZ, Maikon L.; SILVA, Michel Bernardo Fernandes Da; et al. Processamentos de Linguagem Natural. [Digite o Local da Editora]: Grupo A, 2020. E-book. ISBN 9786556900575. Disponível em: https://integrada.minhabiblioteca.com.br/#/books/9786556900575/. Acesso em: 15 mai. 2024.

26. Facebook Research. FastText. 2016. Disponível em: https://research.facebook.com/blog/2016/08/fasttext/. Acesso em: 15 mai. 2024.

27. BEDI, Gunjit. A guide to Text Classification(NLP) using SVM and Naive Bayes with Python. 9 nov. 2018. Disponível em: https://medium.com/@bedigunjit/simple-guide-to-text-classification-nlp-using-svm-and-naive-bayes-with-python-421db3a72d34. Acesso em: 23 maio 2024.

28. DEVLIN, Jacob et al. BERT: Pre-training of deep bidirectional transformers for language understanding. *arXiv preprint*, arXiv:1810.04805, 2018.

29. ACOSTA, Joshua et al. Sentiment analysis of twitter messages using word2vec. *Proceedings of

30. ZVORNICANIN, Enes. What Are Embedding Layers in Neural Networks? 18 mar. 2024. Disponível em: https://www.baeldung.com/cs/neural-nets-embedding-layers. Acesso em: 26 maio 2024.

31. RODRIGUES, Vitor. Métricas de Avaliação: acurácia, precisão, recall… quais as diferenças? 12 abr. 2019. Disponível em: https://vitorborbarodrigues.medium.com/métricas-de-avaliação-acurácia-precisão-recall-quais-as-diferenças-c8f05e0a513c. Acesso em: 9 maio 2024.

32. PYKES, Kurtis. Cohen’s Kappa Explained | Built In. 19 out. 2022. Disponível em: https://builtin.com/data-science/cohens-kappa#:~:text=What%20Is%20Cohen's%20Kappa?,raters%20may%20agree%20by%20chance. Acesso em: 8 jun. 2024.

33. SPSS Statistics 29.0.0. 8 fev. 2024. Disponível em: https://www.ibm.com/docs/en/spss-statistics/29.0.0?topic=schemes-area-under-curve. Acesso em: 8 jun. 2024.


