from typing import Any
from typing import Optional


def get_subplotspec_list(axes_list: {__iter__},
                         grid_spec: Any = None) -> list[Optional[Any]]: ...


def auto_adjust_subplotpars(fig: {transFigure, get_size_inches},
                            renderer: Any,
                            nrows_ncols: tuple[int, int],
                            num1num2_list: list[int],
                            subplot_list: Iterable,
                            ax_bbox_list: list = None,
                            pad: float = 1.08,
                            h_pad: float = None,
                            w_pad: float = None,
                            rect: float = None) -> Optional[dict[str, float]]: ...


def get_tight_layout_figure(fig: Any,
                            axes_list: Iterable,
                            subplotspec_list: Any,
                            renderer: Any,
                            pad: float = 1.08,
                            h_pad: float = None,
                            w_pad: float = None,
                            rect: Optional[float] = None) -> Union[dict, None, dict[str, float]]: ...


def get_renderer(fig: {_cachedRenderer}) -> Any: ...