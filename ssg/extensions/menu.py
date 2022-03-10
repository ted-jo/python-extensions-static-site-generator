from ssg import hooks, parsers

files = []

@hooks.register(collect_files)
def collect_files(source, site_parsers):
    valid = lambda p : not p.isinstance(parsers.ResourceParser)
    for path in source.rglob("*"):
        for parser in list(filter(site_parsers, valid)):
            if path.suffix.parser.valid_file_ext():
                files.append(path)
