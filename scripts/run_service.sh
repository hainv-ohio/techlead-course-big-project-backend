SERVICE=$1
uvicorn services.$SERVICE.main:app --reload --host=0.0.0.0