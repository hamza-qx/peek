load("@rules_python//pyoxidizer:rules.bzl", "python_packaging")

python_packaging(
    name = "peek",
    src = ["peek.py"],
    include_non_distribution_sources = True,

    run_entry_point = "peek:main",
)
