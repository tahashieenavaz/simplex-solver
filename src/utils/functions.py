from sanitizers.Sanitizer import Sanitizer


def sanitize(sanitizer_class: Sanitizer, **kwargs) -> bool:
    instance = sanitizer_class(**kwargs)
    return instance.sanitize()
