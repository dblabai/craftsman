def convert_to_args(prefix: str, content_str: str):
    contents = content_str.split()
    args = [prefix.format(content) for content in contents]
    return " ".join(args)


def convert_to_include_data_dir_args(data_dir: str):
    dirs = data_dir.split()
    args = [f"--include-data-dir={dir}={dir}" for dir in dirs]
    return " ".join(args)
