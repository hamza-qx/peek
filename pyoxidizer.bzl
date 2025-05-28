load("@rules_python//pyoxidizer:rules.bzl", "python_packaging")

python_packaging(
    name = "peek",
    src = ["peek.py"],
)
