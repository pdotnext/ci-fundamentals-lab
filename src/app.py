def greet(name: str) -> str:
    """Return a greeting for the given name."""
    if not name:
        raise ValueError("Name cannot be empty")
    return f"Hello, {name}! Welcome to the CI/CD Pipeline."


def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


if __name__ == "__main__":
    print(greet("DevSecOps Engineer"))
