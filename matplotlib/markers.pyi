from typing import Any
from typing import Iterable
from typing import Sized
from typing import Union

from matplotlib.markers import MarkerStyle
from matplotlib.path import Path
from numpy.core._multiarray_umath import ndarray


class MarkerStyle(object):
    def __init__(self: MarkerStyle,
                 marker: Union[str, ndarray, Iterable, int, float, Path, MarkerStyle] = None,
                 fillstyle: str = None) -> None: ...

    def _recache(self: MarkerStyle) -> None: ...

    def __bool__(self: MarkerStyle) -> bool: ...

    def is_filled(self: MarkerStyle) -> bool: ...

    def get_fillstyle(self: MarkerStyle) -> Optional[str]: ...

    @_api.deprecated("3.4", alternative="a new marker")
    def set_fillstyle(self: MarkerStyle,
                      fillstyle: Any) -> Optional[Any]: ...

    def _set_fillstyle(self: MarkerStyle,
                       fillstyle: str) -> None: ...

    def get_joinstyle(self: MarkerStyle) -> JoinStyle: ...

    def get_capstyle(self: MarkerStyle) -> CapStyle: ...

    def get_marker(self: MarkerStyle) -> Union[ndarray, str, Path, Sized, Iterable, int, float]: ...

    @_api.deprecated("3.4", alternative="a new marker")
    def set_marker(self: MarkerStyle,
                   marker: Any) -> Any: ...

    def _set_marker(self: MarkerStyle,
                    marker: Union[str, ndarray, Iterable, int, float, Path, MarkerStyle]) -> Any: ...

    def get_path(self: MarkerStyle) -> Path: ...

    def get_transform(self: MarkerStyle) -> IdentityTransform: ...

    def get_alt_path(self: MarkerStyle) -> Any: ...

    def get_alt_transform(self: MarkerStyle) -> Any: ...

    def get_snap_threshold(self: MarkerStyle) -> Any: ...

    def _set_nothing(self: MarkerStyle) -> None: ...

    def _set_custom_marker(self: MarkerStyle,
                           path: Union[ndarray, str, Path, Sized, Iterable, int, float]) -> None: ...

    def _set_path_marker(self: MarkerStyle) -> None: ...

    def _set_vertices(self: MarkerStyle) -> None: ...

    def _set_tuple_marker(self: MarkerStyle) -> Any: ...

    def _set_mathtext_path(self: MarkerStyle) -> None: ...

    def _half_fill(self: MarkerStyle) -> bool: ...

    def _set_circle(self: MarkerStyle,
                    reduction: float = 1.0) -> None: ...

    def _set_pixel(self: MarkerStyle) -> None: ...

    def _set_point(self: MarkerStyle) -> None: ...

    def _set_triangle(self: MarkerStyle,
                      rot: float,
                      skip: int) -> None: ...

    def _set_triangle_up(self: MarkerStyle) -> None: ...

    def _set_triangle_down(self: MarkerStyle) -> None: ...

    def _set_triangle_left(self: MarkerStyle) -> None: ...

    def _set_triangle_right(self: MarkerStyle) -> None: ...

    def _set_square(self: MarkerStyle) -> None: ...

    def _set_diamond(self: MarkerStyle) -> None: ...

    def _set_thin_diamond(self: MarkerStyle) -> None: ...

    def _set_pentagon(self: MarkerStyle) -> None: ...

    def _set_star(self: MarkerStyle) -> None: ...

    def _set_hexagon1(self: MarkerStyle) -> None: ...

    def _set_hexagon2(self: MarkerStyle) -> None: ...

    def _set_octagon(self: MarkerStyle) -> None: ...

    def _set_vline(self: MarkerStyle) -> None: ...

    def _set_hline(self: MarkerStyle) -> None: ...

    def _set_tickleft(self: MarkerStyle) -> None: ...

    def _set_tickright(self: MarkerStyle) -> None: ...

    def _set_tickup(self: MarkerStyle) -> None: ...

    def _set_tickdown(self: MarkerStyle) -> None: ...

    def _set_tri_down(self: MarkerStyle) -> None: ...

    def _set_tri_up(self: MarkerStyle) -> None: ...

    def _set_tri_left(self: MarkerStyle) -> None: ...

    def _set_tri_right(self: MarkerStyle) -> None: ...

    def _set_caretdown(self: MarkerStyle) -> None: ...

    def _set_caretup(self: MarkerStyle) -> None: ...

    def _set_caretleft(self: MarkerStyle) -> None: ...

    def _set_caretright(self: MarkerStyle) -> None: ...

    def _set_caretdownbase(self: MarkerStyle) -> None: ...

    def _set_caretupbase(self: MarkerStyle) -> None: ...

    def _set_caretleftbase(self: MarkerStyle) -> None: ...

    def _set_caretrightbase(self: MarkerStyle) -> None: ...

    def _set_plus(self: MarkerStyle) -> None: ...

    def _set_x(self: MarkerStyle) -> None: ...

    def _set_plus_filled(self: MarkerStyle) -> None: ...

    def _set_x_filled(self: MarkerStyle) -> None: ...
