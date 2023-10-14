import os 
import json 
import random

def mix(poems):
    maxV = 3
    maxP = len(poems)
    poem = ''
    for i in range(maxV):
        rV = random.randint(0, maxV - 1)
        rP = random.randint(0, maxP - 1)
        poem += poems[rP][rV] + " / "
    yield poem

def readHaikus(folder_path):
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        file_list = os.listdir(folder_path)
        json_files = [file for file in file_list if file.endswith('.json')]
        APP=[] #All Poems Parts
        for json_file in json_files:
            file_path = os.path.join(folder_path, json_file)
            with open(file_path, 'r') as f:
                data = json.load(f)
                poems = data["content"].get("poems","No poems were found!!!")
                p_parts = [list(poem.values())[0].split('/') for indx, poem in enumerate(poems)]
                APP+=p_parts
        return APP
    else:
        raise Exception(f"The folder '{folder_path}' does not exist or is not a directory.")

def executeMain():
    path = "../../data"
    try: 
        poems = readHaikus(path)
        for poem in mix(poems):
            print(poem)
    except Exception as e:
        print(f"An exception occurred at executeMain: {e}")
    else:
        print("End of program")

if __name__=='__main__':
    # Set your OpenAI API key
    api_key = 'YOUR_API_KEY_HERE'

    # Initialize the OpenAI API client
    openai.api_key = api_key

    # Prompt for the model to generate text
    prompt = "Translate the following English text to French: 'Hello, how are you?'"

    # Use the model to generate text
    response = openai.Completion.create(
        engine="text-davinci-002",  # GPT-3.5 Turbo
        prompt=prompt,
        max_tokens=50  # Adjust as needed
    )

    # Extract and print the generated text
    generated_text = response.choices[0].text
    print(generated_text)
    #executeMain()