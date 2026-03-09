from dotenv import load_dotenv
import os
load_dotenv()

class Config:
    def __init__(self):
        self.deepseek_API_key = os.getenv('API_KEY')
        self.deepseek_base_url = os.getenv('BASE_URL')

        self.host_ollama = os.getenv("HOST_OLLAMA")
        self.port_ollama = os.getenv("PORT_OLLAMA")

        self.db_name = os.getenv("DB_NAME")
        self.db_host = os.getenv("DB_HOST")
        self.db_port = os.getenv("DB_PORT")
        self.db_user = os.getenv("DB_USER")
        self.db_password = os.getenv("DB_PASSWORD")


config_obj = Config()