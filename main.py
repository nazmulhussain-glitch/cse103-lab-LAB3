"""Simple entry point for the CSE103 Lab 3 project."""


def greet(name: str) -> str:
    """Return a friendly greeting for the supplied student name."""
    return f"Hello, {name}! Welcome to CSE103 Lab 3."


def main() -> None:
    """Display the greeting and a short description of the repository."""
    print(greet("Nazmul Hussain"))
    print("Repository: cse103-lab-LAB3")
    print("Topics: Git, GitHub, Markdown, debugging, and APIs.")


if __name__ == "__main__":
    main()
