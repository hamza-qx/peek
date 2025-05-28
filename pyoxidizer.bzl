load("pyoxidizer", "default_python_distribution")

def make_distribution():
    dist = default_python_distribution()

    dist.add_python_file("peek.py")

    dist.add_executable(
        name = "peek",
        entry_point = "peek:main"
    )

    return dist
