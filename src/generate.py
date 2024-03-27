import os
from openai import OpenAI
from util import get_api_key

client = OpenAI(api_key=get_api_key())

input_dir = "input"
output_dir = "output"
output_file = "filename.md"

all_inputs = {}
files_found = os.listdir(input_dir)
files_found = [f for f in files_found if f != '.gitkeep']

if files_found: 
    for file in files_found:
        opened_file = open("inputs/" + file, "r")
        all_inputs[file] = opened_file.read()

with open("src/system_prompt.md", "r") as file:
    system_prompt = file.read()
    print(f"system_prompt: \n{system_prompt}")

with open("src/user_prompt.md", "r") as file:
    user_prompt = file.read()
    print(f"user_prompt: \n{user_prompt}")

def main():
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0,
    )
    answer = response.choices[0].message.content

    with open(f"output/{output_file}", "w") as file:
        file.write(answer)
    
    return answer

if __file__ == '__main__':
    # main()
    pass
