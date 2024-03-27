ChatGPT General Use Project
==========

This is a simple Python script (**`generate.py`**) utilizing the OpenAI GPT-4 model to generate responses based on a system prompt and user input. The project includes a Makefile for managing the virtual environment and running the script.

## **Getting Started**

### Set up a virtual environment

Run the command below to create a virtual environment, install the required packages listed in **`requirements.txt`**, and activate the virtual environment.

```bash
make venv
```

### Add openAI key to `.env` file

This project assumes the availability of the OpenAI GPT-4 model and requires a valid OpenAI API key. Follow the steps below to configure the repo:

- Copy **`example.env`** and rename it to **`.env`**. 
- Update the **`.env`** file with your API key.
- The **`generate.py`** script will retrieve the API key in the **`util.get_api_key()`** function to generate a response.
    
### Add prompts

Follow the steps below to customize the prompts used for generating responses:

1. Write the system prompt in the **`system_prompt.md`** file. This is where you define role(s) and provide an inital set of instructions. Here's a basic example:

```markdown
You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible.
```

2. Write the user prompt in the **`user_prompt.md`** file. This is the same as writing any other message to ChatGPT.

### Generate a response

Run the command below to generate ChatGPT's response. The output will be saved in the **`output`** folder.

```bash
make up
```

## **Directory Structure**

- **`input`**: Directory containing input files for the script.
- **`output`**: Directory where generated responses are saved.
- **`src`**: Source code directory.
    - **`generate.py`**: Main Python script for generating responses.
    - **`util.py`**: Utility functions (e.g., fetching the OpenAI API key).
- **`example.env`**: Example environment configuration file.
- **`requirements.txt`**: List of Python packages required for the project.
- **`Makefile`**: Makefile for managing the virtual environment and running the script.
