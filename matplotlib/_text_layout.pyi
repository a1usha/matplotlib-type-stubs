from typing import Generator


def layout(string: str,
           font: Any,
           *,
           kern_mode: int = KERNING_DEFAULT) -> Generator[{__module__, __mro__, __dict__}, Any, None]: ...