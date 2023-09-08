# AUTOGENERATED! DO NOT EDIT! File to edit: ../../../../nbs/unit_tests/23_test_primitive_types.ipynb.

# %% auto 0
__all__ = ['test_primitive_types_sanity']

# %% ../../../../nbs/unit_tests/23_test_primitive_types.ipynb 1
import pytest
from ..src.rgxlog.engine.datatypes.primitive_types import DataTypes, DataTypeMapping, Span

# %% ../../../../nbs/unit_tests/23_test_primitive_types.ipynb 2
def test_primitive_types_sanity() -> None:
    # test creating illegal Span instances:
    with pytest.raises(TypeError) as e_info:
        Span('x',0)
    assert str(e_info.value) == "Span's start/end must be integers" 

    with pytest.raises(TypeError) as e_info:
        Span('x','x')
    assert str(e_info.value) == "Span's start/end must be integers"

    with pytest.raises(TypeError) as e_info:
        Span(0,'x')
    assert str(e_info.value) == "Span's start/end must be integers" 

    span1 = Span(15,16)
    span2 = Span(15,16)
    assert span1 == span2

    span1 = Span(15,16)
    span2 = Span(15,17)
    assert span1 < span2

    span1 = Span(14,16)
    span2 = Span(13,17)
    assert span1 > span2