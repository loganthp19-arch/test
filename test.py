def print(
    *values: object,
    sep: str | None = " ",
    end: str | None = "\n",
    file: SupportsWrite[str] | None = None,
    flush: Literal[False] = False
) -> None: ...

def print(
    *values: object,
    sep: str | None = " ",
    end: str | None = "\n",
    file: _SupportsWriteAndFlush[str] | None = None,
    flush: bool
) -> None: ...