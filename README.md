# Quote Generator using Ollama LLM

This project demonstrates a simple quote generator using the Ollama language model (`llama2`). The application defines an `Agent` class that uses the language model to generate inspiring quotes. The project is structured to allow easy extension and integration with other tasks or agents.

## Features
- Generate inspiring quotes with author names and relevant hashtags.
- Modular and extendable architecture.
- Verbose mode for detailed logging of tasks.

## Prerequisites

- Python 3.7 or higher
- `langchain_community` library
- Ollama LLM running locally

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/malvika05/quote_generator.git
    cd quote_generator
    ```

2. Set up a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```


3. Ensure Ollama LLM is running locally. Modify the `base_url` in the script if needed.



## Customization

You can customize the `Agent`, `Task`, and `Crew` classes to fit your specific needs. For example, you can add more agents with different roles and goals, or create more complex tasks that require collaboration between multiple agents.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss any changes or improvements.
