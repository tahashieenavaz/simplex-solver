def sanitize(input: any, sanitizer_class, *args) -> bool:
    return sanitizer_class(args).sanitize(input)
