from typing import Any
from typing import Iterable
from typing import Optional
from typing import Union
from typing import tuple

from matplotlib.patches import ArrowStyle
from matplotlib.patches import BoxStyle
from matplotlib.path import Path
from numpy.core._multiarray_umath import ndarray


class Simple(_Base):
    def __init__(self: Simple,
                 head_length: float = .5,
                 head_width: float = .5,
                 tail_width: float = .2) -> None: ...

    def transmute(self: Simple,
                  path: Path,
                  mutation_size: Any,
                  linewidth: Any) -> tuple[Path, bool]: ...


class Circle(Ellipse):
    def __str__(self: Circle) -> str: ...

    @docstring.dedent_interpd
    def __init__(self: Circle,
                 xy: tuple[float, float],
                 radius: int = 5,
                 **kwargs) -> Optional[Any]: ...

    def set_radius(self: Circle,
                   radius: float) -> None: ...

    def get_radius(self: Circle) -> float: ...


class Circle(_Base):
    def __init__(self: Circle,
                 pad: float = 0.3) -> None: ...

    def __call__(self: Circle,
                 x0: float,
                 y0: float,
                 width: float,
                 height: float,
                 mutation_size: float) -> Path: ...


class _Base(object):
    @_api.deprecated("3.4")
    def transmute(self: _Base,
                  x0: Any,
                  y0: Any,
                  width: Any,
                  height: Any,
                  mutation_size: Any) -> Any: ...

    def __init_subclass__(cls: Type[_Base]) -> None: ...

    def __call__(self: _Base,
                 x0: float,
                 y0: float,
                 width: float,
                 height: float,
                 mutation_size: float) -> Any: ...


class _Base(object):
    def _clip(self: _Base,
              path: Any,
              patchA: Any,
              patchB: Any) -> Path: ...

    def _shrink(self: _Base,
                path: Path,
                shrinkA: Any,
                shrinkB: Any) -> Path: ...

    def __call__(self: _Base,
                 posA: Any,
                 posB: Any,
                 shrinkA: float = 2.,
                 shrinkB: float = 2.,
                 patchA: Any = None,
                 patchB: Any = None) -> Path: ...


class _Base(object):
    @staticmethod
    def ensure_quadratic_bezier(path: Path) -> list: ...

    def transmute(self: _Base,
                  path: Path,
                  mutation_size: Any,
                  linewidth: Any) -> Any: ...

    def __call__(self: _Base,
                 path: Any,
                 mutation_size: Any,
                 linewidth: Any,
                 aspect_ratio: float = 1.) -> Union[tuple[list[Path], Any], tuple[Any, Any]]: ...


class CurveAB(_Curve):
    def __init__(self: CurveAB,
                 head_length: float = .4,
                 head_width: float = .2) -> None: ...


class LArrow(_Base):
    def __init__(self: LArrow,
                 pad: float = 0.3) -> None: ...

    def __call__(self: LArrow,
                 x0: float,
                 y0: float,
                 width: float,
                 height: float,
                 mutation_size: float) -> Path: ...


class ArrowStyle(_Style):
    pass


class Round4(_Base):
    def __init__(self: Round4,
                 pad: float = 0.3,
                 rounding_size: float = None) -> None: ...

    def __call__(self: Round4,
                 x0: float,
                 y0: float,
                 width: float,
                 height: float,
                 mutation_size: float) -> Path: ...


class CurveFilledAB(_Curve):
    def __init__(self: CurveFilledAB,
                 head_length: float = .4,
                 head_width: float = .2) -> None: ...


class Rectangle(Patch):
    def __str__(self: Rectangle) -> str: ...

    @docstring.dedent_interpd
    def __init__(self: Rectangle,
                 xy: tuple[float, float],
                 width: float,
                 height: float,
                 angle: float = 0.0,
                 edgecolor: Any = ...,
                 facecolor: Any = ...,
                 color: Any = ...,
                 linewidth: int = ...,
                 linestyle: str = ...,
                 antialiased: Optional[Any] = ...,
                 hatch: Any = ...,
                 fill: bool = ...,
                 capstyle: Any = ...,
                 joinstyle: Any = ...,
                 **kwargs) -> Optional[Any]: ...

    def get_path(self: Rectangle) -> Path: ...

    def _convert_units(self: Rectangle) -> tuple[Any, Any, Any, Any]: ...

    def get_patch_transform(self: Rectangle) -> Union[{input_dims, output_dims}, {output_dims,
                                                                                  input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType]: ...

    def get_x(self: Rectangle) -> float: ...

    def get_y(self: Rectangle) -> float: ...

    def get_xy(self: Rectangle) -> tuple[float, float]: ...

    def get_width(self: Rectangle) -> float: ...

    def get_height(self: Rectangle) -> float: ...

    def set_x(self: Rectangle,
              x: Any) -> None: ...

    def set_y(self: Rectangle,
              y: Any) -> None: ...

    def set_xy(self: Rectangle,
               xy: tuple[float, float]) -> None: ...

    def set_width(self: Rectangle,
                  w: Any) -> None: ...

    def set_height(self: Rectangle,
                   h: Any) -> None: ...

    def set_bounds(self: Rectangle,
                   *args) -> None: ...

    def get_bbox(self: Rectangle) -> Bbox: ...


class Curve(_Curve):
    def __init__(self: Curve) -> None: ...


class BracketA(_Bracket):
    def __init__(self: BracketA,
                 widthA: float = 1.,
                 lengthA: float = 0.2,
                 angleA: float = None) -> None: ...


class FancyArrowPatch(Patch):
    def __str__(self: FancyArrowPatch) -> str: ...

    @docstring.dedent_interpd
    @_api.delete_parameter("3.4", "dpi_cor")
    def __init__(self: FancyArrowPatch,
                 posA: Any = None,
                 posB: Any = None,
                 path: Any = None,
                 arrowstyle: Any = "simple",
                 connectionstyle: Any = "arc3",
                 patchA: Any = None,
                 patchB: Any = None,
                 shrinkA: int = 2,
                 shrinkB: int = 2,
                 mutation_scale: int = 1,
                 mutation_aspect: int = 1,
                 dpi_cor: int = 1,
                 edgecolor: Any = ...,
                 facecolor: Any = ...,
                 color: Any = ...,
                 linewidth: int = ...,
                 linestyle: str = ...,
                 antialiased: Optional[Any] = ...,
                 hatch: Any = ...,
                 fill: bool = ...,
                 capstyle: Any = ...,
                 joinstyle: Any = ...,
                 **kwargs) -> Any: ...

    @_api.deprecated("3.4")
    def set_dpi_cor(self: FancyArrowPatch,
                    dpi_cor: float) -> Optional[Any]: ...

    @_api.deprecated("3.4")
    def get_dpi_cor(self: FancyArrowPatch) -> Any: ...

    def set_positions(self: FancyArrowPatch,
                      posA: Union[None, Iterable, tuple],
                      posB: Union[None, Iterable, tuple]) -> None: ...

    def set_patchA(self: FancyArrowPatch,
                   patchA: Any) -> None: ...

    def set_patchB(self: FancyArrowPatch,
                   patchB: Any) -> None: ...

    def set_connectionstyle(self: FancyArrowPatch,
                            connectionstyle: Any,
                            **kwargs) -> str: ...

    def get_connectionstyle(self: FancyArrowPatch) -> Callable: ...

    def set_arrowstyle(self: FancyArrowPatch,
                       arrowstyle: Union[None, ArrowStyle, str] = None,
                       **kwargs) -> str: ...

    def get_arrowstyle(self: FancyArrowPatch) -> _Base: ...

    def set_mutation_scale(self: FancyArrowPatch,
                           scale: float) -> None: ...

    def get_mutation_scale(self: FancyArrowPatch) -> Any: ...

    def set_mutation_aspect(self: FancyArrowPatch,
                            aspect: float) -> None: ...

    def get_mutation_aspect(self: FancyArrowPatch) -> int: ...

    def get_path(self: FancyArrowPatch) -> Path: ...

    def get_path_in_displaycoord(self: FancyArrowPatch) -> tuple[Any, Any]: ...

    def draw(self: FancyArrowPatch,
             renderer: {open_group, new_gc, draw_path, close_group}) -> None: ...


class Arrow(Patch):
    def __str__(self: Arrow) -> str: ...

    @docstring.dedent_interpd
    def __init__(self: Arrow,
                 x: float,
                 y: float,
                 dx: float,
                 dy: float,
                 width: float = 1.0,
                 **kwargs) -> Optional[Any]: ...

    def get_path(self: Arrow) -> Path: ...

    def get_patch_transform(self: Arrow) -> Affine2D: ...


class Fancy(_Base):
    def __init__(self: Fancy,
                 head_length: float = .4,
                 head_width: float = .4,
                 tail_width: float = .4) -> None: ...

    def transmute(self: Fancy,
                  path: Path,
                  mutation_size: Any,
                  linewidth: Any) -> tuple[Path, bool]: ...


class Polygon(Patch):
    def __str__(self: Polygon) -> str: ...

    @docstring.dedent_interpd
    def __init__(self: Polygon,
                 xy: Optional[ndarray],
                 closed: bool = True,
                 **kwargs) -> Optional[Any]: ...

    def get_path(self: Polygon) -> Path: ...

    def get_closed(self: Polygon) -> bool: ...

    def set_closed(self: Polygon,
                   closed: bool) -> None: ...

    def get_xy(self: Polygon) -> Any: ...

    def set_xy(self: Polygon,
               xy: int) -> None: ...


class RegularPolygon(Patch):
    def __str__(self: RegularPolygon) -> str: ...

    @docstring.dedent_interpd
    def __init__(self: RegularPolygon,
                 xy: tuple[float, float],
                 numVertices: int,
                 radius: float = 5,
                 orientation: float = 0,
                 **kwargs) -> Optional[Any]: ...

    def get_path(self: RegularPolygon) -> Path: ...

    def get_patch_transform(self: RegularPolygon) -> Affine2D: ...


class _Style(object):
    def __new__(cls: Type[_Style],
                stylename: {replace},
                **kwargs) -> Any: ...

    @classmethod
    def get_styles(cls: Type[_Style]) -> Any: ...

    @classmethod
    def pprint_styles(cls: Type[_Style]) -> str: ...

    @classmethod
    def register(cls: Type[_Style],
                 name: Any,
                 style: Any) -> Any: ...


class CurveB(_Curve):
    def __init__(self: CurveB,
                 head_length: float = .4,
                 head_width: float = .2) -> None: ...


class Square(_Base):
    def __init__(self: Square,
                 pad: float = 0.3) -> None: ...

    def __call__(self: Square,
                 x0: float,
                 y0: float,
                 width: float,
                 height: float,
                 mutation_size: float) -> Path: ...


class BarAB(_Bracket):
    def __init__(self: BarAB,
                 widthA: float = 1.,
                 angleA: float = None,
                 widthB: float = 1.,
                 angleB: float = None) -> None: ...


class Roundtooth(Sawtooth):
    def __call__(self: Roundtooth,
                 x0: float,
                 y0: float,
                 width: float,
                 height: float,
                 mutation_size: float) -> Path: ...


class Angle3(_Base):
    def __init__(self: Angle3,
                 angleA: int = 90,
                 angleB: int = 0) -> None: ...

    def connect(self: Angle3,
                posA: Any,
                posB: Any) -> Path: ...


class ConnectionPatch(FancyArrowPatch):
    def __str__(self: ConnectionPatch) -> str: ...

    @docstring.dedent_interpd
    @_api.delete_parameter("3.4", "dpi_cor")
    def __init__(self: ConnectionPatch,
                 xyA: Any,
                 xyB: Any,
                 coordsA: Any,
                 coordsB: Any = None,
                 axesA: Any = None,
                 axesB: Any = None,
                 arrowstyle: str = "-",
                 connectionstyle: str = "arc3",
                 patchA: Any = None,
                 patchB: Any = None,
                 shrinkA: int = 0.,
                 shrinkB: int = 0.,
                 mutation_scale: int = 10.,
                 mutation_aspect: int = None,
                 clip_on: bool = False,
                 dpi_cor: int = 1.,
                 **kwargs) -> Optional[Any]: ...

    def _get_xy(self: ConnectionPatch,
                xy: Any,
                s: {__eq__},
                axes: Any = None) -> Union[float, tuple[Any, Any], ndarray, Iterable, int]: ...

    def set_annotation_clip(self: ConnectionPatch,
                            b: Optional[bool]) -> None: ...

    def get_annotation_clip(self: ConnectionPatch) -> Any: ...

    def get_path_in_displaycoord(self: ConnectionPatch) -> tuple[Any, Any]: ...

    def _check_xy(self: ConnectionPatch,
                  renderer: Optional[{open_group, new_gc, draw_path, close_group}]) -> bool: ...

    def draw(self: ConnectionPatch,
             renderer: {open_group, new_gc, draw_path, close_group}) -> None: ...


class BoxStyle(_Style):
    pass


class StepPatch(PathPatch):
    @docstring.dedent_interpd
    def __init__(self: StepPatch,
                 values: Union[ndarray, Iterable, int, float],
                 edges: Union[ndarray, Iterable, int, float],
                 orientation: str = 'vertical',
                 baseline: Union[float, ndarray, Iterable, int, None] = 0,
                 **kwargs) -> Optional[Any]: ...

    def _update_path(self: StepPatch) -> Any: ...

    def get_data(self: StepPatch) -> StairData: ...

    def set_data(self: StepPatch,
                 values: int = None,
                 edges: Optional[int] = None,
                 baseline: Union[float, int] = None) -> Any: ...


class CirclePolygon(RegularPolygon):
    def __str__(self: CirclePolygon) -> str: ...

    @docstring.dedent_interpd
    def __init__(self: CirclePolygon,
                 xy: tuple[float, float],
                 radius: float = 5,
                 resolution: int = 20,
                 **kwargs) -> Optional[Any]: ...


class FancyBboxPatch(Patch):
    def __str__(self: FancyBboxPatch) -> str: ...

    @docstring.dedent_interpd
    @_api.delete_parameter("3.4", "bbox_transmuter", alternative="boxstyle")
    def __init__(self: FancyBboxPatch,
                 xy: float,
                 width: float,
                 height: float,
                 boxstyle: Union[str, BoxStyle] = "round",
                 bbox_transmuter: Any = None,
                 mutation_scale: float = 1,
                 mutation_aspect: float = 1,
                 edgecolor: Any = ...,
                 facecolor: Any = ...,
                 color: Any = ...,
                 linewidth: int = ...,
                 linestyle: str = ...,
                 antialiased: Optional[Any] = ...,
                 hatch: Any = ...,
                 fill: bool = ...,
                 capstyle: Any = ...,
                 joinstyle: Any = ...,
                 **kwargs) -> Any: ...

    @docstring.dedent_interpd
    def set_boxstyle(self: FancyBboxPatch,
                     boxstyle: Union[str, BoxStyle] = None,
                     **kwargs) -> str: ...

    def set_mutation_scale(self: FancyBboxPatch,
                           scale: float) -> None: ...

    def get_mutation_scale(self: FancyBboxPatch) -> float: ...

    def set_mutation_aspect(self: FancyBboxPatch,
                            aspect: float) -> None: ...

    def get_mutation_aspect(self: FancyBboxPatch) -> Union[float, int]: ...

    def get_boxstyle(self: FancyBboxPatch) -> Any: ...

    def get_path(self: FancyBboxPatch) -> Path: ...

    def get_x(self: FancyBboxPatch) -> Any: ...

    def get_y(self: FancyBboxPatch) -> Any: ...

    def get_width(self: FancyBboxPatch) -> float: ...

    def get_height(self: FancyBboxPatch) -> float: ...

    def set_x(self: FancyBboxPatch,
              x: float) -> None: ...

    def set_y(self: FancyBboxPatch,
              y: float) -> None: ...

    def set_width(self: FancyBboxPatch,
                  w: float) -> None: ...

    def set_height(self: FancyBboxPatch,
                   h: float) -> None: ...

    def set_bounds(self: FancyBboxPatch,
                   *args) -> None: ...

    def get_bbox(self: FancyBboxPatch) -> Bbox: ...


class Patch(Artist):
    @_api.deprecated("3.4")
    @_api.classproperty
    def validCap(cls: Patch) -> _deprecated_property: ...

    @_api.deprecated("3.4")
    @_api.classproperty
    def validJoin(cls: Patch) -> _deprecated_property: ...

    def __init__(self: Patch,
                 edgecolor: Any = None,
                 facecolor: Any = None,
                 color: Any = None,
                 linewidth: Any = None,
                 linestyle: Any = None,
                 antialiased: Any = None,
                 hatch: Any = None,
                 fill: bool = True,
                 capstyle: Any = None,
                 joinstyle: Any = None,
                 **kwargs) -> None: ...

    def get_verts(self: Patch) -> list: ...

    def _process_radius(self: Patch,
                        radius: Optional[float]) -> Union[float, Number, int]: ...

    def contains(self: Patch,
                 mouseevent: MouseEvent,
                 radius: Any = None) -> Any: ...

    def contains_point(self: Patch,
                       point: tuple[float, float],
                       radius: Optional[float] = None) -> bool: ...

    def contains_points(self: Patch,
                        points: int,
                        radius: Optional[float] = None) -> Any: ...

    def update_from(self: Patch,
                    other: {_transform, _transformSet, _visible, _alpha, clipbox, _clipon, _clippath, _label, _sketch,
                            _path_effects, sticky_edges}) -> None: ...

    def get_extents(self: Patch) -> Any: ...

    def get_transform(self: Patch) -> Union[{input_dims, output_dims}, {output_dims,
                                                                        input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType]: ...

    def get_data_transform(self: Patch) -> IdentityTransform: ...

    def get_patch_transform(self: Patch) -> IdentityTransform: ...

    def get_antialiased(self: Patch) -> Optional[Any]: ...

    def get_edgecolor(self: Patch) -> Any: ...

    def get_facecolor(self: Patch) -> Any: ...

    def get_linewidth(self: Patch) -> int: ...

    def get_linestyle(self: Patch) -> str: ...

    def set_antialiased(self: Patch,
                        aa: Optional[Any]) -> None: ...

    def _set_edgecolor(self: Patch,
                       color: Any) -> None: ...

    def set_edgecolor(self: Patch,
                      color: Any) -> None: ...

    def _set_facecolor(self: Patch,
                       color: Optional[Any]) -> None: ...

    def set_facecolor(self: Patch,
                      color: Optional[Any]) -> None: ...

    def set_color(self: Patch,
                  c: Any) -> None: ...

    def set_alpha(self: Patch,
                  alpha: Union[int, float, complex, None]) -> None: ...

    def set_linewidth(self: Patch,
                      w: Optional[float]) -> None: ...

    def set_linestyle(self: Patch,
                      ls: str) -> None: ...

    def set_fill(self: Patch,
                 b: bool) -> None: ...

    def get_fill(self: Patch) -> bool: ...

    @docstring.interpd
    def set_capstyle(self: Patch,
                     s: Any) -> Optional[Any]: ...

    def get_capstyle(self: Patch) -> Any: ...

    @docstring.interpd
    def set_joinstyle(self: Patch,
                      s: Any) -> Optional[Any]: ...

    def get_joinstyle(self: Patch) -> Any: ...

    def set_hatch(self: Patch,
                  hatch: str) -> None: ...

    def get_hatch(self: Patch) -> Any: ...

    @contextlib.contextmanager
    def _bind_draw_path_function(self: Patch,
                                 renderer: Optional[Any]) -> Generator[partial[None], Any, None]: ...

    @artist.allow_rasterization
    def draw(self: Patch,
             renderer: Any) -> Optional[Any]: ...

    def get_path(self: Patch) -> Any: ...

    def get_window_extent(self: Patch,
                          renderer: Any = None) -> Any: ...

    def _convert_xy_units(self: Patch,
                          xy: {__getitem__}) -> tuple[Any, Any]: ...


class _Curve(_Base):
    def __init__(self: _Curve,
                 beginarrow: bool = None,
                 endarrow: bool = None,
                 fillbegin: bool = False,
                 fillend: bool = False,
                 head_length: float = .2,
                 head_width: float = .1) -> None: ...

    def _get_arrow_wedge(self: _Curve,
                         x0: {__sub__},
                         y0: {__sub__},
                         x1: {__add__},
                         y1: {__add__},
                         head_dist: Any,
                         cos_t: {__mul__},
                         sin_t: {__mul__, __neg__},
                         linewidth: Any) -> tuple[list[tuple[float, float]], list[uint8], float, float]: ...

    def transmute(self: _Curve,
                  path: Path,
                  mutation_size: Any,
                  linewidth: Any) -> tuple[list[Path], list[bool]]: ...


class CurveFilledA(_Curve):
    def __init__(self: CurveFilledA,
                 head_length: float = .4,
                 head_width: float = .2) -> None: ...


class PathPatch(Patch):
    def __str__(self: PathPatch) -> str: ...

    @docstring.dedent_interpd
    def __init__(self: PathPatch,
                 path: Path,
                 **kwargs) -> Optional[Any]: ...

    def get_path(self: PathPatch) -> Path: ...

    def set_path(self: PathPatch,
                 path: Any) -> None: ...


class SimpleEvent(object):
    def __init__(self: SimpleEvent,
                 xy: Any) -> None: ...


class CurveA(_Curve):
    def __init__(self: CurveA,
                 head_length: float = .4,
                 head_width: float = .2) -> None: ...


class Arc3(_Base):
    def __init__(self: Arc3,
                 rad: float = 0.) -> None: ...

    def connect(self: Arc3,
                posA: Any,
                posB: Any) -> Path: ...


class Ellipse(Patch):
    def __str__(self: Ellipse) -> str: ...

    @docstring.dedent_interpd
    def __init__(self: Ellipse,
                 xy: tuple[float, float],
                 width: float,
                 height: float,
                 angle: float = 0,
                 **kwargs) -> Optional[Any]: ...

    def _recompute_transform(self: Ellipse) -> None: ...

    def get_path(self: Ellipse) -> Path: ...

    def get_patch_transform(self: Ellipse) -> IdentityTransform: ...

    def set_center(self: Ellipse,
                   xy: tuple[float, float]) -> None: ...

    def get_center(self: Ellipse) -> tuple[float, float]: ...

    def set_width(self: Ellipse,
                  width: float) -> None: ...

    def get_width(self: Ellipse) -> float: ...

    def set_height(self: Ellipse,
                   height: float) -> None: ...

    def get_height(self: Ellipse) -> float: ...

    def set_angle(self: Ellipse,
                  angle: float) -> None: ...

    def get_angle(self: Ellipse) -> float: ...


class FancyArrow(Polygon):
    def __str__(self: FancyArrow) -> str: ...

    @docstring.dedent_interpd
    def __init__(self: FancyArrow,
                 x: Any,
                 y: Any,
                 dx: Any,
                 dy: Any,
                 width: float = 0.001,
                 length_includes_head: bool = False,
                 head_width: Optional[float] = None,
                 head_length: Optional[float] = None,
                 shape: str = 'full',
                 overhang: float = 0,
                 head_starts_at_zero: bool = False,
                 **kwargs) -> Any: ...


class CurveFilledB(_Curve):
    def __init__(self: CurveFilledB,
                 head_length: float = .4,
                 head_width: float = .2) -> None: ...


class Round(_Base):
    def __init__(self: Round,
                 pad: float = 0.3,
                 rounding_size: float = None) -> None: ...

    def __call__(self: Round,
                 x0: float,
                 y0: float,
                 width: float,
                 height: float,
                 mutation_size: float) -> Path: ...


class RArrow(LArrow):
    def __call__(self: RArrow,
                 x0: float,
                 y0: float,
                 width: float,
                 height: float,
                 mutation_size: float) -> Path: ...


class Shadow(Patch):
    def __str__(self: Shadow) -> str: ...

    @_api.delete_parameter("3.3", "props")
    @docstring.dedent_interpd
    def __init__(self: Shadow,
                 patch: Any,
                 ox: float,
                 oy: float,
                 props: dict = None,
                 **kwargs) -> Optional[Any]: ...

    def _update(self: Shadow) -> None: ...

    def _update_transform(self: Shadow,
                          renderer: {get_rasterized, get_agg_filter, figure}) -> None: ...

    def get_path(self: Shadow) -> Any: ...

    def get_patch_transform(self: Shadow) -> Any: ...

    def draw(self: Shadow,
             renderer: {points_to_pixels, get_rasterized, get_agg_filter, figure}) -> None: ...


class Arc(Ellipse):
    def __str__(self: Arc) -> str: ...

    @docstring.dedent_interpd
    def __init__(self: Arc,
                 xy: tuple[float, float],
                 width: float,
                 height: float,
                 angle: float = 0.0,
                 theta1: Union[float, int] = 0.0,
                 theta2: Union[float, int] = 360.0,
                 edgecolor: Any = ...,
                 facecolor: Any = ...,
                 color: Any = ...,
                 linewidth: int = ...,
                 linestyle: str = ...,
                 antialiased: Optional[Any] = ...,
                 hatch: Any = ...,
                 fill: bool = ...,
                 capstyle: Any = ...,
                 joinstyle: Any = ...,
                 **kwargs) -> Any: ...

    @artist.allow_rasterization
    def draw(self: Arc,
             renderer: Any) -> Optional[Any]: ...


class Arc(_Base):
    def __init__(self: Arc,
                 angleA: int = 0,
                 angleB: int = 0,
                 armA: Any = None,
                 armB: Any = None,
                 rad: float = 0.) -> None: ...

    def connect(self: Arc,
                posA: Any,
                posB: Any) -> Path: ...


class Wedge(Patch):
    def __str__(self: Wedge) -> str: ...

    @docstring.dedent_interpd
    def __init__(self: Wedge,
                 center: Any,
                 r: Any,
                 theta1: Any,
                 theta2: Any,
                 width: Any = None,
                 **kwargs) -> Optional[Any]: ...

    def _recompute_path(self: Wedge) -> None: ...

    def set_center(self: Wedge,
                   center: Any) -> None: ...

    def set_radius(self: Wedge,
                   radius: Any) -> None: ...

    def set_theta1(self: Wedge,
                   theta1: Any) -> None: ...

    def set_theta2(self: Wedge,
                   theta2: Any) -> None: ...

    def set_width(self: Wedge,
                  width: Any) -> None: ...

    def get_path(self: Wedge) -> Optional[Path]: ...


class Wedge(_Base):
    def __init__(self: Wedge,
                 tail_width: float = .3,
                 shrink_factor: float = 0.5) -> None: ...

    def transmute(self: Wedge,
                  path: Path,
                  mutation_size: Any,
                  linewidth: Any) -> tuple[Path, bool]: ...


class DArrow(_Base):
    def __init__(self: DArrow,
                 pad: float = 0.3) -> None: ...

    def __call__(self: DArrow,
                 x0: float,
                 y0: float,
                 width: float,
                 height: float,
                 mutation_size: float) -> Path: ...


class Angle(_Base):
    def __init__(self: Angle,
                 angleA: int = 90,
                 angleB: int = 0,
                 rad: float = 0.) -> None: ...

    def connect(self: Angle,
                posA: Any,
                posB: Any) -> Path: ...


class BracketB(_Bracket):
    def __init__(self: BracketB,
                 widthB: float = 1.,
                 lengthB: float = 0.2,
                 angleB: float = None) -> None: ...


class ConnectionStyle(_Style):
    pass


class BracketAB(_Bracket):
    def __init__(self: BracketAB,
                 widthA: float = 1.,
                 lengthA: float = 0.2,
                 angleA: float = None,
                 widthB: float = 1.,
                 lengthB: float = 0.2,
                 angleB: float = None) -> None: ...


class _Bracket(_Base):
    def __init__(self: _Bracket,
                 bracketA: Optional[bool] = None,
                 bracketB: Optional[bool] = None,
                 widthA: float = 1.,
                 widthB: float = 1.,
                 lengthA: float = 0.2,
                 lengthB: float = 0.2,
                 angleA: float = None,
                 angleB: float = None,
                 scaleA: Any = None,
                 scaleB: Any = None) -> None: ...

    def _get_bracket(self: _Bracket,
                     x0: Any,
                     y0: Any,
                     cos_t: {__neg__},
                     sin_t: {__neg__},
                     width: {__eq__, __mul__},
                     length: float,
                     angle: Any) -> tuple[list[Union[tuple[float, float], tuple[Any, Any]]], list[uint8]]: ...

    def transmute(self: _Bracket,
                  path: Path,
                  mutation_size: Any,
                  linewidth: Any) -> tuple[Path, bool]: ...


class Sawtooth(_Base):
    def __init__(self: Sawtooth,
                 pad: float = 0.3,
                 tooth_size: float = None) -> None: ...

    def _get_sawtooth_vertices(self: Sawtooth,
                               x0: float,
                               y0: float,
                               width: Any,
                               height: Any,
                               mutation_size: {__mul__}) -> list[tuple[Union[float, int], float]]: ...

    def __call__(self: Sawtooth,
                 x0: float,
                 y0: float,
                 width: float,
                 height: float,
                 mutation_size: float) -> Path: ...


class Bar(_Base):
    def __init__(self: Bar,
                 armA: float = 0.,
                 armB: float = 0.,
                 fraction: float = 0.3,
                 angle: Optional[float] = None) -> None: ...

    def connect(self: Bar,
                posA: Any,
                posB: Any) -> Path: ...


def _register_style(style_list: dict,
                    cls: Optional[{__name__}] = None,
                    name: str = None) -> Union[partial, {__name__}, None]: ...


def _simpleprint_styles(_styles: dict) -> str: ...


def draw_bbox(bbox: {x0, y0, width, height},
              renderer: {get_rasterized, get_agg_filter, figure},
              color: str = 'k',
              trans: Any = None) -> None: ...


def _point_along_a_line(x0: {__sub__},
                        y0: {__sub__},
                        x1: Any,
                        y1: Any,
                        d: float) -> tuple[float, float]: ...


def bbox_artist(artist: {get_window_extent},
                renderer: {points_to_pixels, get_rasterized, get_agg_filter, figure},
                props: Any = None,
                fill: bool = True) -> None: ...