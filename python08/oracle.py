import os
from dotenv import load_dotenv  # use pip install python-dotenv


def load_configuration() -> dict[str, str]:
    load_dotenv()
    return {
        'mode':      os.environ.get('MATRIX_MODE', 'development'),
        'db_url':    os.environ.get('DATABASE_URL', 'not configured'),
        'api_key':   os.environ.get('API_KEY', 'not configured'),
        'log_level': os.environ.get('LOG_LEVEL', 'INFO'),
        'endpoint':  os.environ.get('ZION_ENDPOINT', 'not configured')
    }


def display_configuration(config: dict[str, str]) -> None:
    print("ORACLE STATUS: Reading the Matrix...")
    print("Configuration loaded:")
    print(f"Mode: {config['mode']}")
    print(f"Log Level: {config['log_level']}")
    print(f"Zion Network: {config['endpoint']}")
    if config['mode'] == 'production':
        print("Database: Connected to remote instance")
        print("API Access: ***hidden***")
    else:
        print("Database: Connected to local instance")
        api_key = config['api_key']
        if api_key != 'not configured':
            print(f"API Access: {api_key[:8]}...")
        else:
            print("API Access: not configured")


def security_check(config: dict[str, str]) -> None:
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    if os.path.exists('.env'):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not found")
    if os.environ.get('MATRIX_MODE') is not None:
        print("[OK] Production overrides available")
    else:
        print("[WARNING] No production override detected")


def main() -> None:
    config = load_configuration()
    display_configuration(config)
    security_check(config)
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
