# app/services/infra/ollama_llm_client.py
from dataclasses import dataclass
from typing import Optional
import requests
from src.core.config import config_obj


class OllamaError(RuntimeError):
    pass


class OllamaUnavailable(OllamaError):
    pass


@dataclass(frozen=True)
class GenerateParams:
    system: str = "Ты полезный ассистент"
    max_tokens: int = 1000
    temperature: float = 0.5


class OllamaLLMClient:
    def __init__(self, model: str = "qwen3-vl:235b-cloud",  host: str = config_obj.host_ollama, port: int = config_obj.port_ollama, timeout_s: int = 60):
        self.base_url = f"http://{host}:{port}"
        self.model = model
        self.timeout_s = timeout_s

    def health_check(self) -> bool:
        try:
            r = requests.get(f"{self.base_url}/api/tags", timeout=5)
            return r.status_code == 200
        except requests.RequestException:
            return False

    def generate(self, prompt: str, params: Optional[GenerateParams] = None) -> str:
        params = params or GenerateParams()

        payload = {
            "model": self.model,
            "prompt": prompt,
            "system": params.system,
            "stream": False,
            "options": {
                "num_predict": params.max_tokens,
                "temperature": params.temperature,
            },
        }

        try:
            r = requests.post(
                f"{self.base_url}/api/generate",
                json=payload,
                timeout=self.timeout_s,
            )
        except requests.Timeout as e:
            raise OllamaUnavailable("Ollama timeout") from e
        except requests.RequestException as e:
            raise OllamaUnavailable("Ollama connection error") from e

        if r.status_code != 200:
            raise OllamaError(f"Ollama HTTP {r.status_code}: {r.text[:300]}")

        data = r.json()
        return data.get("response", "")
    

ollama = OllamaLLMClient()