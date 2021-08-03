from typing import Any, Callable, Iterable, TypeVar

class InvalidIterableError(Exception):
    pass


T = TypeVar("T")
_initial_missing = object()


def fold(
    func: Callable,
    sequence: Iterable[Any],
    init_val: T = _initial_missing,
    fold_right: bool = False,
) -> T:
    """Apply a function of two arguments cumulatively to the items of a sequence or iterable, in a direction governed by `fold_right`

    Args:
        func (Callable): accumulator function.
        sequence (Iterable): iterable sequence to be processed.
        init_val ([type], optional): initial value (In case of Nonefolding starts from 1st element of sequence). Defaults to None.
        fold_right (bool, optional): evaluation order set to right-most element first if True. Defaults to False.

    Returns:
        T: Value obtained from recusrive application of `func` on `sequence`.
    """
    seq_iter = iter(sequence) if not fold_right else iter(reversed(sequence))
    if init_val is _initial_missing:
        try:
            f_result = next(seq_iter)
        except StopIteration:
            raise InvalidIterableError(
                "Folding on empty iterable with no initial value"
            ) from None
    else:
        f_result = init_val
    for element in seq_iter:
        f_result = func(f_result, element)

    return f_result
