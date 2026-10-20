
import os
from pathlib import Path
from urllib.parse import urlparse

import requests
import fade
from colorama import Fore, Style, init

init(autoreset=True)

API_URL = "https://leakcheck.io/api/public"
OUTPUT_FILE = Path("result-leakcheck.io.txt")


def leakcheck():
    ascii_art = r"""
          _  
        _| |                    
      _| | |                   
     | | | |                  
     | | | |\__                
     | | | |/  \              
     |       /\ \             
     |      /  \/       leakcheck.io-searcher
     |      \  /\         by NexForm3D
     |       \/ /
      \        /
       |     /
       |     |
       Unknown
      from NexForm
    """

    if os.name == "nt":
        os.system("title leakcheck.io-searcher by NexForm3D")

    print(fade.greenblue(ascii_art))
    print(Fore.CYAN + "Authorized personal-data exposure checks only.\n")

    search = input(
        Fore.LIGHTBLUE_EX
        + "Your LeakCheck search (username/email) --> "
    ).strip()

    if not search:
        print(Fore.RED + "Error: search cannot be empty.")
        return

    print(Fore.YELLOW + "\nContacting LeakCheck API...")

    try:
        response = requests.get(
            API_URL,
            params={"check": search},
            timeout=15,
        )
        response.raise_for_status()
        data = response.json()

    except requests.Timeout:
        print(Fore.RED + "Error: the request timed out.")
        return
    except requests.HTTPError as exc:
        print(Fore.RED + f"HTTP error: {exc}")
        return
    except requests.RequestException as exc:
        print(Fore.RED + f"Network error: {exc}")
        return
    except ValueError:
        print(Fore.RED + "Error: the server returned invalid JSON.")
        return

    if not isinstance(data, dict):
        print(Fore.RED + "Error: unexpected API response.")
        return

    print(Fore.CYAN + "\n" + "=" * 45)
    print(Fore.CYAN + "             SEARCH RESULTS")
    print(Fore.CYAN + "=" * 45)

    success = data.get("success", "Unknown")
    fields = data.get("fields", [])
    sources = data.get("sources", [])

    print(Fore.WHITE + f"\nStatus: {success}")

    def display_section(title, value):
        print(Fore.LIGHTBLUE_EX + f"\n{title}")

        if isinstance(value, list):
            if not value:
                print(Fore.WHITE + "  No entries returned.")
            else:
                for index, item in enumerate(value, start=1):
                    print(Fore.WHITE + f"  [{index}] {item}")
        elif isinstance(value, dict):
            if not value:
                print(Fore.WHITE + "  No entries returned.")
            else:
                for key, item in value.items():
                    print(Fore.WHITE + f"  {key}: {item}")
        else:
            print(Fore.WHITE + f"  {value}")

    display_section("FIELDS", fields)
    display_section("SOURCES", sources)

    print(Fore.CYAN + "\n" + "=" * 45)

    question = input(
        Fore.LIGHTBLUE_EX
        + "\nSave the results to a TXT file? (Y/N): "
    ).strip().lower()

    if question == "y":
        try:
            with OUTPUT_FILE.open("w", encoding="utf-8") as file:
                file.write("LeakCheck.io Searcher - Results\n")
                file.write("=" * 45 + "\n")
                file.write(f"Status: {success}\n\n")
                file.write(f"Fields: {fields}\n\n")
                file.write(f"Sources: {sources}\n")

            print(
                Fore.GREEN
                + f"\nResults saved to: {OUTPUT_FILE.resolve()}"
            )
        except OSError as exc:
            print(Fore.RED + f"Could not save the file: {exc}")

    input(Fore.LIGHTWHITE_EX + "\nPress Enter to exit...")


if __name__ == "__main__":
    try:
        leakcheck()
    except KeyboardInterrupt:
        print(Style.RESET_ALL + "\nOperation cancelled.")
