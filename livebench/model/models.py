"""
Model definitions for LiveBench API models.
This file was missing from the original repository and has been recreated.
"""

from typing import List, Optional, Dict, Any


class Model:
    """Base model class with common attributes."""
    
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
    """Anthropic (Claude) model configuration."""
    pass


class OpenAIModel(Model):
    """OpenAI model configuration."""
    pass


class AWSModel(Model):
    """AWS Bedrock model configuration."""
    pass


class CohereModel(Model):
    """Cohere model configuration."""
    pass


class DeepseekModel(Model):
    """Deepseek model configuration."""
    pass


class GeminiModel(Model):
    """Google Gemini model configuration."""
    pass


class GemmaModel(Model):
    """Google Gemma model configuration."""
    pass


class LlamaModel(Model):
    """Meta Llama model configuration."""
    pass


class MistralModel(Model):
    """Mistral model configuration."""
    pass


class NvidiaModel(Model):
    """NVIDIA model configuration."""
    pass


class QwenModel(Model):
    """Qwen model configuration."""
    pass


class XAIModel(Model):
    """xAI (Grok) model configuration."""
    pass
