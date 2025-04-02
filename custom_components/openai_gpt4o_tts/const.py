"""Constants for OpenAI GPT-4o Mini TTS integration."""

DOMAIN = "openai_gpt4o_tts"
PLATFORMS = ["tts"]

# Configuration keys
CONF_API_KEY = "api_key"
CONF_VOICE = "voice"
CONF_INSTRUCTIONS = "instructions"

# Default voice setting
DEFAULT_VOICE = "nova"

# Default multi-field instruction settings
DEFAULT_AFFECT = (
    "Wesoły przewodnik, który wygłasza przemówienie w żywy i angażujący sposób,"
    "utrzymując uwagę słuchacza, jednocześnie zapewniając jasne wskazówki."
)
DEFAULT_TONE = (
    "Przyjazny, jasny i uspokajający, tworzący spokojną atmosferę i sprawiający, że słuchacz "
    "czuje się pewnie i komfortowo. Zachęca do uwagi bez nadmiernej formalności."
)
DEFAULT_PRONUNCIATION = (
    "Jasna, wyraźna i stabilna, zapewniająca łatwe zrozumienie każdej instrukcji "
    "przy jednoczesnym zachowaniu naturalnego, konwersacyjnego przepływu. Używa właściwej wymowy "
    "aby zminimalizować nieporozumienia."
)
DEFAULT_PAUSE = (
    "Krótkie, celowe pauzy po kluczowych wskazówkach (np. 'przejdź przez ulicę' lub 'skręć w prawo'), "
    "aby dać słuchaczowi czas na przetworzenie informacji i podążanie za nimi. "
    "Zapewnia jasność bez niepotrzebnych opóźnień."
)
DEFAULT_EMOTION = (
    "Ciepły i wspierający, przekazujący empatię i troskę, zapewniający, że słuchacz czuje się prowadzony "
    "i bezpieczny podczas całej podróży. Używa subtelnych wskazówek emocjonalnych, aby zwiększyć zaangażowanie."
)

# Official GPT-4o TTS voices
OPENAI_TTS_VOICES = [
    "alloy",
    "ash",
    "ballad",
    "coral",
    "echo",
    "fable",
    "onyx",
    "nova",
    "sage",
    "shimmer"
]
