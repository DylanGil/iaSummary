# Projet IA Résumé de l'actualité

Ce projet utilise Python pour récupérer les articles de certains média et en fais un bref résumé en français.

## Configuration
⚠️ Suivant votre ordinateur, la commande peut être `python3` au lieu de `python` et `pip3` au lieu de `pip`.

1. Assurez-vous d'avoir Python 3 ainsi que `pip` d'installé.
   ```bash
    python --version
    pip --version
   ```
   Si ce n'est pas le cas, installez-les :

   ```bash
    sudo apt install python3 python3-pip
    ```

2. Créez un environnement virtuel et activez-le en vous assurant d'être dans le dossier du projet :
   ```bash
   python -m venv venv
   ```
   ```bash
   # Linux/MacOS
   source venv/bin/activate
   # Windows
   source venv\Scripts\activate
   ```

3. Assurez-vous aussi d'avoir le modèle `llama2` installé ([Ollama](https://ollama.ai/)) est éxécuté puis tapez la
   commande suivante, en vous assurant d'être dans le dossier du projet :
   ```bash
   ollama pull llama2
   ```


4. Installez les dépendances nécessaires (assuré vous d'avoir activé l'environnement virtuel à l'étape 2) en vous assurant d'être dans le dossier du projet :

   ```bash
   pip install -r requirements.txt
    ```

5. Lancez le script `main.py` en vous assurant d'être dans le dossier du projet :

   ```bash
   python main.py
   ```

Un résumé de l'actualité sera généré dans le terminal.