# src/routes/__init__.py

from .main_routes import main
from .medical_claim_routes import medical_claim

# List of Blueprints to be imported and registered
blueprints = [
    main,
    medical_claim
]
