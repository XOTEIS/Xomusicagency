# firebase_config.py

import firebase_admin
from firebase_admin import credentials

# Initialize Firebase Admin
cred = credentials.Certificate('path/to/serviceAccountKey.json')
firebase_admin.initialize_app(cred)