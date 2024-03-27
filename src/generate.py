import os
from openai import OpenAI
from util import get_api_key

client = OpenAI(api_key=get_api_key())

input_dir = "input"
output_dir = "output"
output_file = "results.md"

all_inputs = ""
files_found = os.listdir(input_dir)
files_found = [
    f
    for f in files_found
    if not (f == ".gitkeep" or ".png" in f or ".jpeg" in f or ".mp4" in f)
]

print(f"files_found: {files_found}")

if files_found:
    for file in files_found:
        file_path = os.path.join(input_dir, file)
        opened_file = open(file_path, "r")
        all_inputs += opened_file.read()
        all_inputs += '/n'


system_prompt = f"""
{open("src/system_prompt.md", "r").read()}
"""

user_prompt = f"""
{open("src/user_prompt.md", "r").read()}

{all_inputs}
"""

print(f"system_prompt: \n{system_prompt}")
print(f"user_prompt: \n{user_prompt}")


def main():
    print("Generating response...")
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0,
    )
    answer = response.choices[0].message.content
    with open(os.path.join(output_dir, output_file), "w") as file:
        file.write(answer)
    return answer


answer = main()
print(f"answer: \n{answer}")
