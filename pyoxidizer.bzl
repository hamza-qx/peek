def make_distribution():
    dist = default_python_distribution()

    policy = dist.make_python_packaging_policy()
    policy.include_non_python_files = True
    policy.bytecode_opt_level = 2
    policy.strip_python_lib = True

    config = dist.to_python_config()
    config.run_mode = "py_embedded"
    config.run_module = False
    config.python_embed_entry_point = "peek:main"

    dist.add_python_resources(exe_name = "peek", packaging_policy = policy)

    return dist
