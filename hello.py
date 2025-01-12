import yaml

def main():
    config = yaml.safe_load(open("config.yaml"))
    print(config)
    print("Hello from sg-reddit-scrapper!")


if __name__ == "__main__":
    main()
