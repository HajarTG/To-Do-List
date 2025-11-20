# To-Do List (Flask + MongoDB)

Petite application web pour gérer des tâches (ajout, suppression, marquer comme fait).

### Prérequis
- Python 3.8+
- MongoDB (local ou distant)

### Installation rapide (PowerShell)

```powershell
cd "C:\Users\Lenovo\Desktop\my project\To-Do-List\flask-mongoDB-App-main\flask-mongoDB-App-main"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install flask pymongo
```

Démarrer MongoDB (local) ou utiliser Docker:

```powershell
# Docker (optionnel)
docker run -d --name mongodb -p 27017:27017 -v mongodb_data:/data/db mongo:latest
```

### Lancer l'application:

```powershell
python app.py
```

Ouvrir `http://127.0.0.1:5000/` dans votre navigateur.

Notes
- La connexion MongoDB est définie dans `app.py` (client = MongoClient('localhost', 27017)).
- Pour un déploiement, utilisez des variables d'environnement et ajoutez `requirements.txt`.

<img width="669" height="474" alt="image" src="https://github.com/user-attachments/assets/358a1dd9-0d1e-4410-9ba8-142e16bb0db5" />
<img width="698" height="497" alt="image" src="https://github.com/user-attachments/assets/9ce0a5af-8f49-4136-8a0e-f771ff34b279" />
<img width="748" height="682" alt="image" src="https://github.com/user-attachments/assets/86dfdd8e-8074-485e-afcf-20a686fd5a5b" />
<img width="1119" height="654" alt="image" src="https://github.com/user-attachments/assets/513c10af-b8f2-4aca-b24a-e23c1fcad336" />
