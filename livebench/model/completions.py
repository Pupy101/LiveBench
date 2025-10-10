import logging
import os
import sys
import time
import httpx

from openai import Stream
from openai.types.chat import ChatCompletionChunk, ChatCompletion
from tenacity import retry, stop_after_attempt, retry_if_exception_type, wait_fixed, wait_incrementing

logging.basicConfig(stream=sys.stdout, level=logging.WARNING)


logger = logging.getLogger(__name__)

# API setting constants
API_MAX_RETRY = 3
API_RETRY_SLEEP_MIN = 10
API_RETRY_SLEEP_MAX = 60
API_ERROR_OUTPUT = "$ERROR$"



def retry_fail(_):
    print("all retries failed")
    return API_ERROR_OUTPUT, 0


def retry_log(retry_state):
    exception = retry_state.outcome.exception()


@retry(
    stop=stop_after_attempt(API_MAX_RETRY),
    wait=wait_fixed(API_RETRY_SLEEP_MIN),
    retry=retry_if_exception_type(Exception),
    after=retry_log,
    retry_error_callback=retry_fail,
)
def chat_completion_openai(
    model: str, messages: Conversation, temperature: float, max_tokens: int, model_api_kwargs: API_Kwargs | None = None, api_dict: dict[str, str] | None = None, stream: bool = False
) -> tuple[str, int]:
    from openai import NOT_GIVEN, OpenAI

    if api_dict is not None:
        client = OpenAI(
            api_key=api_dict["api_key"],
            base_url=api_dict["api_base"],
            timeout=httpx.Timeout(timeout=2400.0, connect=10.0),
        )

    else:
        client = OpenAI(timeout=1000)

    try:
        if stream:
            stream: Stream[ChatCompletionChunk] = client.chat.completions.create(
                model=model,
                messages=messages,
                stream=True,
                stream_options={'include_usage': True},
                **actual_api_kwargs
            )

            raise Exception("No message returned from OpenAI")
        if num_tokens is None:
            num_tokens = -1
        output = message

        return output, num_tokens
    except Exception as e:
        if "invalid_prompt" in str(e).lower():
            print("invalid prompt (model refusal), giving up")
            return API_ERROR_OUTPUT, 0
        raise e

@retry(
    stop=stop_after_attempt(1),
    wait=wait_fixed(API_RETRY_SLEEP_MIN),
    retry=retry_if_exception_type(Exception),
    after=retry_log,
    retry_error_callback=retry_fail,
)

    # Set up API kwargs
    inference_config = {
        "maxTokens": max_tokens,
        "temperature": temperature,
    }


   
    # Make the API call
    response = brt.converse(
        modelId=model,
        messages=[{"role": "user", "content": [{"text": prompt}]}],
        inferenceConfig=inference_config,
    )

    return output, num_tokens


incremental_wait = wait_incrementing(start=API_RETRY_SLEEP_MIN, max=API_RETRY_SLEEP_MAX, increment=20)

def gemini_custom_wait(retry_state):
    if retry_state.outcome.failed:
        exception = retry_state.outcome.exception()
        if exception and "RECITATION" in str(exception) or "MAX_TOKENS" in str(exception):
            return 0.0  # don't wait for recitation or max token errors

    val = incremental_wait(retry_state)
    print(f"Waiting for {val} seconds before retrying attempt {retry_state.attempt_number + 1}")

    # other errors might indicate rate limiting, wait for these
    return val

@retry(
    stop=stop_after_attempt(API_MAX_RETRY),
    retry=retry_if_exception_type(Exception),
    after=retry_log,
    retry_error_callback=retry_fail,
)
def chat_completion_giga(
    model: str, messages: Conversation, temperature: float, max_tokens: int, model_api_kwargs: API_Kwargs | None = None, api_dict: dict[str, str] | None = None, stream: bool = False
) -> tuple[str, int]:
    global CLIENT
    from giga import GigaChat

    with LOCK:
        if CLIENT is None:
            CLIENT = GigaChat()

    try:
        response = CLIENT.chat(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
        )

        message = response["choices"][0]["message"]["content"]
        if message is None:
            raise Exception("No message returned from Giga")
        output = message
        num_tokens = response["usage"]["completion_tokens"]

        return output, num_tokens
    except Exception as e:
        if "invalid_prompt" in str(e).lower():
            print("invalid prompt, giving up")
            return API_ERROR_OUTPUT, 0
        elif "timeout" in str(e).lower():
            print("timeout, giving up")
            return API_ERROR_OUTPUT, 0
        raise e

@retry(
    stop=stop_after_attempt(API_MAX_RETRY),
    retry=retry_if_exception_type(Exception),
    after=retry_log,
    retry_error_callback=retry_fail,
)
def chat_completion_google_generativeai(
    model: str, messages: Conversation, temperature: float, max_tokens: int, model_api_kwargs: API_Kwargs | None = None, api_dict: dict[str, str] | None = None, stream: bool = False
) -> tuple[str, int]:
    from google import genai
    from google.genai import types

    if api_dict is not None and "api_key" in api_dict:
        api_key = api_dict["api_key"]
    else:
        api_key = os.environ["GEMINI_API_KEY"]

    config = types.GenerateContentConfig(**api_kwargs)
    
    response = client.models.generate_content(
    )
    
    if response is None or response.text is None:
        raise Exception("No response returned from Google")



@retry(
    stop=stop_after_attempt(API_MAX_RETRY),
    wait=wait_fixed(API_RETRY_SLEEP_MIN),
    retry=retry_if_exception_type(Exception),
    after=retry_log,
    retry_error_callback=retry_fail,
)
    from together import Together

    if api_dict is not None and "api_key" in api_dict:
        api_key = api_dict["api_key"]
    else:
        api_key = os.environ["TOGETHER_API_KEY"]
    client = Together(api_key=api_key)

        messages=messages,
        **api_kwargs
    )


@retry(
    stop=stop_after_attempt(API_MAX_RETRY),
    wait=wait_fixed(API_RETRY_SLEEP_MIN),
    retry=retry_if_exception_type(Exception),
    after=retry_log,
    retry_error_callback=retry_fail,
)
    if api_dict is not None and "api_key" in api_dict:
        api_key = api_dict["api_key"]
    else:
        api_key = os.environ["ANTHROPIC_API_KEY"]



@retry(
    stop=stop_after_attempt(API_MAX_RETRY),
    wait=wait_fixed(API_RETRY_SLEEP_MIN),
    retry=retry_if_exception_type(Exception),
    after=retry_log,
    retry_error_callback=retry_fail,
)
    if api_dict is not None and "api_key" in api_dict:
        api_key = api_dict["api_key"]
    else:
        api_key = os.environ["MISTRAL_API_KEY"]

    client = Mistral(api_key=api_key)
    
    # Set up API kwargs
    api_kwargs: API_Kwargs = {
        'max_tokens': max_tokens,
        'temperature': temperature
    }
    if model_api_kwargs is not None:
        model_api_kwargs = {key: value for key, value in model_api_kwargs.items()}
        api_kwargs.update(model_api_kwargs)

    actual_api_kwargs = {key: (value if value is not None else UNSET) for key, value in api_kwargs.items()}

    chat_response = client.chat.complete(
        model=model,
        messages=messages,
        **actual_api_kwargs
    )
    
    if chat_response is None:
        raise Exception("No response returned from Mistral")
    elif not hasattr(chat_response, 'choices') or not chat_response.choices:
        raise Exception("No choices returned from Mistral")
    
    message = chat_response.choices[0].message.content
    if message is None:
        raise Exception("No message returned from Mistral")

    return message.strip(), num_tokens

@retry(
    stop=stop_after_attempt(API_MAX_RETRY),
    wait=wait_fixed(API_RETRY_SLEEP_MIN),
    retry=retry_if_exception_type(Exception),
    after=retry_log,
    retry_error_callback=retry_fail,
)
    if api_dict is not None and "api_key" in api_dict:
        api_key = api_dict["api_key"]
    else:
        api_key = os.environ["DEEPINFRA_API_KEY"]

def get_api_function(provider_name: str) -> ModelAPI:
    if provider_name == 'openai':
        return chat_completion_openai
    elif provider_name == 'openai_responses':
        return chat_completion_openai_responses
    elif provider_name == 'anthropic':
        return chat_completion_anthropic
    elif provider_name == 'mistral':
        return chat_completion_mistral
    elif provider_name == 'together':
        return chat_completion_together
    elif provider_name == 'google':
        return chat_completion_google_generativeai
    elif provider_name == 'aws':
        return chat_completion_aws
    elif provider_name == 'deepinfra':
        return chat_completion_deepinfra
    elif provider_name == 'giga':
        return chat_completion_giga
    else:
        return chat_completion_openai

