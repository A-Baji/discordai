import os
import pathlib
import json
import appdirs


def get():
    config_dir = appdirs.user_data_dir(appauthor="Adib Baji", appname="discordai")
    try:
        with open(f"{config_dir}/config.json", 'r') as file:
            config = json.load(file)
    except FileNotFoundError as err:
        print("No config found. Please follow the steps to create one:")
        config = dict(
            token=input("\nEnter your discord bot token: "),
            openai_key=input("\nEnter your openAI key: ")
        )
        os.makedirs(config_dir, exist_ok=True)
        with open(pathlib.Path(config_dir, "config.json"), "w") as f:
            f.write(json.dumps(config))

        print(f"Your config has been saved to {config_dir}/config.json")
    return config
