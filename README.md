Esse projeto foi criado para desenvolver alguns conceitos relacionados à automação web. Dessa forma, resolvi criar o Claude Bot que, através do reconhecimento de fala, utiliza métodos para usar as principais funções da Netflix e Amazon Prime. Dessa forma, utilizei as bibliotecas: Selenium, Pyaudio e Speech Recognition para conseguir fazer as execuções nas plataformas e para o reconhecimento de voz. 

AVISO: Essa é a primeira versão do script e ainda serão colocadas algumas funções e melhorias para melhor desempenho.

O bot executa as seguintes operações:

USUÁRIO FALA / EXECUÇÃO

* "Mudo" / Tira o som da reprodução.
* "Áudio" / Retorna o som da reprodução.
* "Pause" / Para a reprodução.
* "Continuar" / Tira o pause da reprodução.
* "Próximo episódio" / Reproduz o próximo episódio.
* "Pular abertura" / Se caso existir uma abertura, é pulada.
* "Pular resumo" / Se caso existir um resumo de um episódio/capítulo, é pulado.
* "Saia" / Sai do episódio em reprodução e vai para a tela inicial.
* "Sair Netflix/Prime" / Sai da plataforma, encerrando o navegador. 