import os
from data import scrape


def main_menu():
    os.system("cls" if os.name == "nt" else "clear")
    print("1. Download Images from Pinterest")
    print("2. Exit")


def get_input():
    profile_url = input("\nEnter Pinterest profile link: ")
    folder_name = input(
        "To create a folder where photos will be saved, provide a name for it: "
    )
    return profile_url, folder_name


def main():
    while True:
        main_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            profile_url, folder_name = get_input()
            scrape.fetch_images(profile_url, folder_name)
            print("Images downloaded successfully!")
            input("Press Enter to continue.")

        elif choice == "2":
            print("Exiting.")
            break

        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
