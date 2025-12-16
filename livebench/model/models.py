"""
Model definitions for LiveBench API models.
This file was missing from the original repository and has been recreated.
"""

from typing import List, Optional, Dict, Any


class Model:
    def __init__(
        self,
        api_name: str,
        display_name: str,
        aliases: Optional[List[str]] = None,
        api_kwargs: Optional[Dict[str, Any]] = None,
        **kwargs
    ):
        self.api_name = api_name
        self.display_name = display_name
        self.aliases = aliases if aliases is not None else []
        self.api_kwargs = api_kwargs
        # Store any additional keyword arguments as attributes
        for key, value in kwargs.items():
            setattr(self, key, value)


class AnthropicModel(Model):
    pass


class OpenAIModel(Model):
    pass


class AWSModel(Model):
    pass


class CohereModel(Model):
    pass


class DeepseekModel(Model):
    pass


class GeminiModel(Model):
    pass


class GemmaModel(Model):
    pass


class LlamaModel(Model):
    pass


class MistralModel(Model):
    pass


class NvidiaModel(Model):
    pass


class QwenModel(Model):
    pass


class XAIModel(Model):
    pass
