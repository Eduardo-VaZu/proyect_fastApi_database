import sys
import os

# Add the project root to sys.path
sys.path.append(os.getcwd())

try:
    print("Verifying app.repository.message_repository...")
    import app.repository.message_repository

    print("Verifying app.services.message_service...")
    import app.services.message_service

    print("Verifying app.repository.impl.message_repository_impl...")
    import app.repository.impl.message_repository_impl

    print("Verifying app.services.impl.message_service_impl...")
    import app.services.impl.message_service_impl

    print("Verifying app.dependencies.message_dependencies...")
    import app.dependencies.message_dependencies

    print("Verifying app.routes.message_routes...")
    import app.routes.message_routes

    print("Structure verification successful!")
except Exception as e:
    print(f"Verification failed: {e}")
    sys.exit(1)
