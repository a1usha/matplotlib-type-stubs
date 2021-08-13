from functools import partial
from typing import Any
from typing import Iterable
from typing import Optional
from typing import Union
from typing import tuple

from matplotlib.backend_bases import GraphicsContextBase
from matplotlib.backend_bases import KeyEvent
from matplotlib.backend_bases import _Mode
from matplotlib.backend_tools import Cursors
from matplotlib.figure import Figure
from matplotlib.path import Path
from matplotlib.transforms import Affine2D
from numpy.core._multiarray_umath import ndarray


class NavigationToolbar2(object):
    def __init__(self: NavigationToolbar2,
                 canvas: {toolbar}) -> None: ...

    def set_message(self: NavigationToolbar2,
                    s: _Mode) -> None: ...

    def draw_rubberband(self: NavigationToolbar2,
                        event: {x, y, key},
                        x0: Any,
                        y0: Any,
                        x1: Any,
                        y1: Any) -> None: ...

    def remove_rubberband(self: NavigationToolbar2) -> None: ...

    def home(self: NavigationToolbar2,
             *args) -> None: ...

    def back(self: NavigationToolbar2,
             *args) -> None: ...

    def forward(self: NavigationToolbar2,
                *args) -> None: ...

    @_api.deprecated("3.3", alternative="__init__")
    def _init_toolbar(self: NavigationToolbar2) -> Any: ...

    def _update_cursor(self: NavigationToolbar2,
                       event: Union[KeyEvent, {inaxes}]) -> None: ...

    @contextmanager
    def _wait_cursor_for_draw_cm(self: NavigationToolbar2) -> Generator[Any, Any, None]: ...

    @staticmethod
    def _mouse_event_to_message(event: {inaxes}) -> Any: ...

    def mouse_move(self: NavigationToolbar2,
                   event: Any) -> None: ...

    def _zoom_pan_handler(self: NavigationToolbar2,
                          event: Any) -> None: ...

    @_api.deprecated("3.3")
    def press(self: NavigationToolbar2,
              event: Any) -> Optional[Any]: ...

    @_api.deprecated("3.3")
    def release(self: NavigationToolbar2,
                event: Any) -> Optional[Any]: ...

    def pan(self: NavigationToolbar2,
            *args) -> None: ...

    def press_pan(self: NavigationToolbar2,
                  event: {button, x, y}) -> None: ...

    def drag_pan(self: NavigationToolbar2,
                 event: {key, x, y}) -> None: ...

    def release_pan(self: NavigationToolbar2,
                    event: Any) -> None: ...

    def zoom(self: NavigationToolbar2,
             *args) -> None: ...

    def press_zoom(self: NavigationToolbar2,
                   event: {button, x, y}) -> None: ...

    def drag_zoom(self: NavigationToolbar2,
                  event: {x, y, key}) -> None: ...

    def release_zoom(self: NavigationToolbar2,
                     event: {x, key, y}) -> None: ...

    def push_current(self: NavigationToolbar2) -> None: ...

    @_api.deprecated("3.3", alternative="toolbar.canvas.draw_idle()")
    def draw(self: NavigationToolbar2) -> Optional[Any]: ...

    def _draw(self: NavigationToolbar2) -> None: ...

    def _update_view(self: NavigationToolbar2) -> None: ...

    def configure_subplots(self: NavigationToolbar2,
                           *args) -> None: ...

    def save_figure(self: NavigationToolbar2,
                    *args) -> Any: ...

    def set_cursor(self: NavigationToolbar2,
                   cursor: Cursors) -> None: ...

    def update(self: NavigationToolbar2) -> None: ...

    def set_history_buttons(self: NavigationToolbar2) -> None: ...


class Event(object):
    def __init__(self: Event,
                 name: Any,
                 canvas: {get_width_height},
                 guiEvent: Any = None) -> None: ...


class FigureCanvasBase(object):
    @_api.classproperty
    def supports_blit(cls: FigureCanvasBase) -> bool: ...

    def __init__(self: FigureCanvasBase,
                 figure: Optional[{set_canvas}] = None) -> None: ...

    @classmethod
    @functools.lru_cache()
    def _fix_ipython_backend2gui(cls: Type[FigureCanvasBase]) -> None: ...

    @contextmanager
    def _idle_draw_cntx(self: FigureCanvasBase) -> Generator[Any, Any, None]: ...

    def is_saving(self: FigureCanvasBase) -> bool: ...

    def pick(self: FigureCanvasBase,
             mouseevent: Any) -> None: ...

    def blit(self: FigureCanvasBase,
             bbox: Any = None) -> None: ...

    def resize(self: FigureCanvasBase,
               w: Any,
               h: Any) -> None: ...

    def draw_event(self: FigureCanvasBase,
                   renderer: Any) -> None: ...

    def resize_event(self: FigureCanvasBase) -> None: ...

    def close_event(self: FigureCanvasBase,
                    guiEvent: Any = None) -> None: ...

    def key_press_event(self: FigureCanvasBase,
                        key: Any,
                        guiEvent: Any = None) -> None: ...

    def key_release_event(self: FigureCanvasBase,
                          key: Any,
                          guiEvent: Any = None) -> None: ...

    def pick_event(self: FigureCanvasBase,
                   mouseevent: {guiEvent},
                   artist: Any,
                   **kwargs) -> None: ...

    def scroll_event(self: FigureCanvasBase,
                     x: Any,
                     y: Any,
                     step: {__ge__},
                     guiEvent: Any = None) -> None: ...

    def button_press_event(self: FigureCanvasBase,
                           x: Any,
                           y: Any,
                           button: Any,
                           dblclick: bool = False,
                           guiEvent: Any = None) -> None: ...

    def button_release_event(self: FigureCanvasBase,
                             x: float,
                             y: float,
                             button: Any,
                             guiEvent: Any = None) -> None: ...

    def motion_notify_event(self: FigureCanvasBase,
                            x: float,
                            y: float,
                            guiEvent: Any = None) -> None: ...

    def leave_notify_event(self: FigureCanvasBase,
                           guiEvent: Any = None) -> None: ...

    def enter_notify_event(self: FigureCanvasBase,
                           guiEvent: Any = None,
                           xy: tuple[float, float] = None) -> None: ...

    def inaxes(self: FigureCanvasBase,
               xy: tuple[float, float]) -> Any: ...

    def grab_mouse(self: FigureCanvasBase,
                   ax: Any) -> Any: ...

    def release_mouse(self: FigureCanvasBase,
                      ax: Any) -> None: ...

    def draw(self: FigureCanvasBase,
             *args,
             **kwargs) -> None: ...

    def draw_idle(self: FigureCanvasBase,
                  *args,
                  **kwargs) -> None: ...

    def get_width_height(self: FigureCanvasBase) -> tuple[int, int]: ...

    @classmethod
    def get_supported_filetypes(cls: Type[FigureCanvasBase]) -> dict[str, str]: ...

    @classmethod
    def get_supported_filetypes_grouped(cls: Type[FigureCanvasBase]) -> dict: ...

    def _get_output_canvas(self: FigureCanvasBase,
                           backend: Optional[str],
                           fmt: str) -> FigureCanvasBase: ...

    def print_figure(self: FigureCanvasBase,
                     filename: Any,
                     dpi: float = None,
                     facecolor: Any = None,
                     edgecolor: Any = None,
                     orientation: str = 'portrait',
                     format: Optional[str] = None,
                     bbox_inches: Any = None,
                     pad_inches: float = None,
                     bbox_extra_artists: Any = None,
                     backend: Optional[str] = None,
                     **kwargs) -> Any: ...

    @classmethod
    def get_default_filetype(cls: Type[FigureCanvasBase]) -> Optional[Any]: ...

    @_api.deprecated(
        "3.4", alternative="manager.get_window_title or GUI-specific methods")
    def get_window_title(self: FigureCanvasBase) -> Any: ...

    @_api.deprecated(
        "3.4", alternative="manager.set_window_title or GUI-specific methods")
    def set_window_title(self: FigureCanvasBase,
                         title: Any) -> Optional[Any]: ...

    def get_default_filename(self: FigureCanvasBase) -> str: ...

    def switch_backends(self: FigureCanvasBase,
                        FigureCanvasClass: str) -> Any: ...

    def mpl_connect(self: FigureCanvasBase,
                    s: str,
                    func: Callable) -> Any: ...

    def mpl_disconnect(self: FigureCanvasBase,
                       cid: Any) -> Any: ...

    def new_timer(self: FigureCanvasBase,
                  interval: int = None,
                  callbacks: Union[Iterable, tuple] = None) -> TimerBase: ...

    def flush_events(self: FigureCanvasBase) -> None: ...

    def start_event_loop(self: FigureCanvasBase,
                         timeout: int = 0) -> None: ...

    def stop_event_loop(self: FigureCanvasBase) -> None: ...


class _Backend(object):
    @classmethod
    def new_figure_manager(cls: Type[_Backend],
                           num: Any,
                           *args,
                           **kwargs) -> FigureManagerBase: ...

    @classmethod
    def new_figure_manager_given_figure(cls: Type[_Backend],
                                        num: Any,
                                        figure: Any) -> FigureManagerBase: ...

    @classmethod
    def draw_if_interactive(cls: Type[_Backend]) -> None: ...

    @classmethod
    def show(cls: Type[_Backend],
             block: Any = None) -> None: ...

    @staticmethod
    def export(cls: {__module__}) -> {__module__}: ...


class ToolContainerBase(object):
    def __init__(self: ToolContainerBase,
                 toolmanager: {toolmanager_connect}) -> None: ...

    def _tool_toggled_cbk(self: ToolContainerBase,
                          event: {tool}) -> None: ...

    def add_tool(self: ToolContainerBase,
                 tool: Any,
                 group: str,
                 position: int = -1) -> None: ...

    def _get_image_filename(self: ToolContainerBase,
                            image: {__add__}) -> Union[None, {__add__}, str]: ...

    def trigger_tool(self: ToolContainerBase,
                     name: str) -> None: ...

    def add_toolitem(self: ToolContainerBase,
                     name: str,
                     group: str,
                     position: int,
                     image: str,
                     description: str,
                     toggle: bool) -> Any: ...

    def toggle_toolitem(self: ToolContainerBase,
                        name: str,
                        toggled: bool) -> Any: ...

    def remove_toolitem(self: ToolContainerBase,
                        name: str) -> Any: ...

    def set_message(self: ToolContainerBase,
                    s: str) -> Any: ...


class _Mode(str, Enum):
    def __str__(self: _Mode) -> str: ...

    @property
    def _navigate_mode(self: _Mode) -> Optional[Any]: ...


class LocationEvent(Event):
    def __init__(self: LocationEvent,
                 name: Any,
                 canvas: Any,
                 x: Any,
                 y: Any,
                 guiEvent: Any = None) -> None: ...

    def _update_enter_leave(self: LocationEvent) -> None: ...


class TimerBase(object):
    def __init__(self: TimerBase,
                 interval: int = None,
                 callbacks: Union[Iterable, tuple] = None) -> None: ...

    def __del__(self: TimerBase) -> None: ...

    def start(self: TimerBase,
              interval: Optional[int] = None) -> None: ...

    def stop(self: TimerBase) -> None: ...

    def _timer_start(self: TimerBase) -> None: ...

    def _timer_stop(self: TimerBase) -> None: ...

    @property
    def interval(self: TimerBase) -> int: ...

    @interval.setter
    def interval(self: TimerBase,
                 interval: Any) -> None: ...

    @property
    def single_shot(self: TimerBase) -> Any: ...

    @single_shot.setter
    def single_shot(self: TimerBase,
                    ss: Any) -> None: ...

    def add_callback(self: TimerBase,
                     func: Any,
                     *args,
                     **kwargs) -> Any: ...

    def remove_callback(self: TimerBase,
                        func: Any,
                        *args,
                        **kwargs) -> None: ...

    def _timer_set_interval(self: TimerBase) -> None: ...

    def _timer_set_single_shot(self: TimerBase) -> None: ...

    def _on_timer(self: TimerBase) -> None: ...


class NonGuiException(Exception):
    pass


class ResizeEvent(Event):
    def __init__(self: ResizeEvent,
                 name: Any,
                 canvas: {get_width_height}) -> None: ...


class MouseEvent(LocationEvent):
    def __init__(self: MouseEvent,
                 name: Any,
                 canvas: Any,
                 x: Any,
                 y: Any,
                 button: Any = None,
                 key: Any = None,
                 step: int = 0,
                 dblclick: bool = False,
                 guiEvent: Any = None) -> None: ...

    def __str__(self: MouseEvent) -> str: ...


class PickEvent(Event):
    def __init__(self: PickEvent,
                 name: Any,
                 canvas: Any,
                 mouseevent: Any,
                 artist: Any,
                 guiEvent: Any = None,
                 **kwargs) -> None: ...


class MouseButton(IntEnum):
    pass


class CloseEvent(Event):
    pass


class GraphicsContextBase(object):
    def __init__(self: GraphicsContextBase) -> None: ...

    def copy_properties(self: GraphicsContextBase,
                        gc: {get_linewidth}) -> None: ...

    def restore(self: GraphicsContextBase) -> None: ...

    def get_alpha(self: GraphicsContextBase) -> float: ...

    def get_antialiased(self: GraphicsContextBase) -> int: ...

    def get_capstyle(self: GraphicsContextBase) -> Any: ...

    def get_clip_rectangle(self: GraphicsContextBase) -> Any: ...

    def get_clip_path(self: GraphicsContextBase) -> Union[tuple[Any, Any], tuple[None, None]]: ...

    def get_dashes(self: GraphicsContextBase) -> tuple[int, None]: ...

    def get_forced_alpha(self: GraphicsContextBase) -> bool: ...

    def get_joinstyle(self: GraphicsContextBase) -> Any: ...

    def get_linewidth(self: GraphicsContextBase) -> int: ...

    def get_rgb(self: GraphicsContextBase) -> tuple[float, float, float, float]: ...

    def get_url(self: GraphicsContextBase) -> Any: ...

    def get_gid(self: GraphicsContextBase) -> Any: ...

    def get_snap(self: GraphicsContextBase) -> Any: ...

    def set_alpha(self: GraphicsContextBase,
                  alpha: Any) -> None: ...

    def set_antialiased(self: GraphicsContextBase,
                        b: Any) -> None: ...

    @docstring.interpd
    def set_capstyle(self: GraphicsContextBase,
                     cs: Any) -> Optional[Any]: ...

    def set_clip_rectangle(self: GraphicsContextBase,
                           rectangle: Any) -> None: ...

    def set_clip_path(self: GraphicsContextBase,
                      path: Any) -> None: ...

    def set_dashes(self: GraphicsContextBase,
                   dash_offset: Optional[float],
                   dash_list: Union[ndarray, Iterable, int, float, None]) -> Any: ...

    def set_foreground(self: GraphicsContextBase,
                       fg: Any,
                       isRGBA: bool = False) -> None: ...

    @docstring.interpd
    def set_joinstyle(self: GraphicsContextBase,
                      js: Any) -> Optional[Any]: ...

    def set_linewidth(self: GraphicsContextBase,
                      w: Union[float, None, int]) -> None: ...

    def set_url(self: GraphicsContextBase,
                url: Optional[Any]) -> None: ...

    def set_gid(self: GraphicsContextBase,
                id: Any) -> None: ...

    def set_snap(self: GraphicsContextBase,
                 snap: Any) -> None: ...

    def set_hatch(self: GraphicsContextBase,
                  hatch: Any) -> None: ...

    def get_hatch(self: GraphicsContextBase) -> Any: ...

    def get_hatch_path(self: GraphicsContextBase,
                       density: float = 6.0) -> Optional[Path]: ...

    def get_hatch_color(self: GraphicsContextBase) -> Union[Iterable, tuple]: ...

    def set_hatch_color(self: GraphicsContextBase,
                        hatch_color: Any) -> None: ...

    def get_hatch_linewidth(self: GraphicsContextBase) -> Optional[Any]: ...

    def get_sketch_params(self: GraphicsContextBase) -> Optional[tuple]: ...

    def set_sketch_params(self: GraphicsContextBase,
                          scale: Optional[float] = None,
                          length: float = None,
                          randomness: float = None) -> None: ...


class RendererBase(object):
    def __init__(self: RendererBase) -> None: ...

    def open_group(self: RendererBase,
                   s: Any,
                   gid: Any = None) -> None: ...

    def close_group(self: RendererBase,
                    s: Any) -> None: ...

    def draw_path(self: RendererBase,
                  gc: Union[GraphicsContextBase, {get_rgb, set_linewidth}],
                  path: Path,
                  transform: Affine2D,
                  rgbFace: Any = None) -> Any: ...

    def draw_markers(self: RendererBase,
                     gc: Any,
                     marker_path: Any,
                     marker_trans: Transform,
                     path: {iter_segments},
                     trans: Transform,
                     rgbFace: Any = None) -> None: ...

    def draw_path_collection(self: RendererBase,
                             gc: {get_linewidth},
                             master_transform: Any,
                             paths: {__len__, __getitem__},
                             all_transforms: {__len__},
                             offsets: {__len__},
                             offsetTrans: Any,
                             facecolors: {__len__},
                             edgecolors: {__len__},
                             linewidths: {__len__},
                             linestyles: {__len__},
                             antialiaseds: {__len__, __getitem__},
                             urls: {__len__},
                             offset_position: {__eq__}) -> None: ...

    def draw_quad_mesh(self: RendererBase,
                       gc: {get_linewidth, _alpha, _forced_alpha, _antialiased, _capstyle, _cliprect, _clippath,
                            _dashes, _joinstyle, _linestyle, _linewidth, _rgb, _hatch, _hatch_color, _hatch_linewidth,
                            _url, _gid, _snap, _sketch},
                       master_transform: Any,
                       meshWidth: {__mul__},
                       meshHeight: Any,
                       coordinates: Any,
                       offsets: {__len__},
                       offsetTrans: Any,
                       facecolors: {__len__},
                       antialiased: Any,
                       edgecolors: Optional[{__len__}]) -> None: ...

    def draw_gouraud_triangle(self: RendererBase,
                              gc: Any,
                              points: int,
                              colors: int,
                              transform: Transform) -> Any: ...

    def draw_gouraud_triangles(self: RendererBase,
                               gc: Any,
                               triangles_array: Any,
                               colors_array: Any,
                               transform: Transform) -> None: ...

    def _iter_collection_raw_paths(self: RendererBase,
                                   master_transform: Any,
                                   paths: list[Path],
                                   all_transforms: {__len__}) -> Generator[tuple[Path, Union[
        {input_dims, output_dims}, {output_dims,
                                    input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType]], Any, None]: ...

    def _iter_collection_uses_per_path(self: RendererBase,
                                       paths: {__len__},
                                       all_transforms: {__len__},
                                       offsets: {__len__},
                                       facecolors: {__len__},
                                       edgecolors: {__len__}) -> int: ...

    def _iter_collection(self: RendererBase,
                         gc: {_alpha, _forced_alpha, _antialiased, _capstyle, _cliprect, _clippath, _dashes, _joinstyle,
                              _linestyle, _linewidth, _rgb, _hatch, _hatch_color, _hatch_linewidth, _url, _gid, _snap,
                              _sketch},
                         master_transform: Any,
                         all_transforms: {__len__},
                         path_ids: {__len__, __getitem__},
                         offsets: {__len__},
                         offsetTrans: Any,
                         facecolors: {__len__},
                         edgecolors: {__len__},
                         linewidths: {__len__},
                         linestyles: {__len__},
                         antialiaseds: {__len__, __getitem__},
                         urls: {__len__},
                         offset_position: {__eq__}) -> Generator[
        tuple[int, int, Any, GraphicsContextBase, Optional[Any]], Any, None]: ...

    def get_image_magnification(self: RendererBase) -> float: ...

    def draw_image(self: RendererBase,
                   gc: Any,
                   x: Union[int, float, complex],
                   y: Union[int, float, complex],
                   im: int,
                   transform: Affine2DBase = None) -> Any: ...

    def option_image_nocomposite(self: RendererBase) -> bool: ...

    def option_scale_image(self: RendererBase) -> bool: ...

    @_api.delete_parameter("3.3", "ismath")
    def draw_tex(self: RendererBase,
                 gc: {get_rgb, set_linewidth},
                 x: Any,
                 y: Any,
                 s: Any,
                 prop: Any,
                 angle: Any,
                 ismath: str = 'TeX!',
                 mtext: Any = None) -> Optional[Any]: ...

    def draw_text(self: RendererBase,
                  gc: Any,
                  x: float,
                  y: float,
                  s: str,
                  prop: FontProperties,
                  angle: float,
                  ismath: bool = False,
                  mtext: Text = None) -> None: ...

    def _get_text_path_transform(self: RendererBase,
                                 x: Any,
                                 y: Any,
                                 s: str,
                                 prop: FontProperties,
                                 angle: Any,
                                 ismath: Any) -> tuple[Path, Affine2D]: ...

    def _draw_text_as_path(self: RendererBase,
                           gc: {get_rgb, set_linewidth},
                           x: Any,
                           y: Any,
                           s: str,
                           prop: FontProperties,
                           angle: Any,
                           ismath: Any) -> None: ...

    def get_text_width_height_descent(self: RendererBase,
                                      s: Any,
                                      prop: {get_size_in_points},
                                      ismath: {__eq__}) -> Union[tuple[Any, Any, Any], tuple[Any, Any, None]]: ...

    def flipy(self: RendererBase) -> bool: ...

    def get_canvas_width_height(self: RendererBase) -> tuple[int, int]: ...

    def get_texmanager(self: RendererBase) -> TexManager: ...

    def new_gc(self: RendererBase) -> GraphicsContextBase: ...

    def points_to_pixels(self: RendererBase,
                         points: Union[float, ndarray, Iterable, int]) -> Union[float, ndarray, Iterable, int]: ...

    def start_rasterizing(self: RendererBase) -> None: ...

    def stop_rasterizing(self: RendererBase) -> None: ...

    def start_filter(self: RendererBase) -> None: ...

    def stop_filter(self: RendererBase,
                    filter_func: Any) -> None: ...

    def _draw_disabled(self: RendererBase) -> Generator[Any, Any, None]: ...


class ShowBase(_Backend):
    def __call__(self: ShowBase,
                 block: Any = None) -> None: ...


class KeyEvent(LocationEvent):
    def __init__(self: KeyEvent,
                 name: Any,
                 canvas: Any,
                 key: Any,
                 x: int = 0,
                 y: int = 0,
                 guiEvent: Any = None) -> None: ...


class DrawEvent(Event):
    def __init__(self: DrawEvent,
                 name: Any,
                 canvas: {get_width_height},
                 renderer: Any) -> None: ...


class StatusbarBase(object):
    def __init__(self: StatusbarBase,
                 toolmanager: Any) -> None: ...

    def _message_cbk(self: StatusbarBase,
                     event: {message}) -> None: ...

    def set_message(self: StatusbarBase,
                    s: str) -> None: ...


class FigureManagerBase(object):
    def __init__(self: FigureManagerBase,
                 canvas: {manager, figure},
                 num: Any) -> None: ...

    def show(self: FigureManagerBase) -> None: ...

    def destroy(self: FigureManagerBase) -> None: ...

    def full_screen_toggle(self: FigureManagerBase) -> None: ...

    def resize(self: FigureManagerBase,
               w: Any,
               h: Any) -> None: ...

    @_api.deprecated(
        "3.4", alternative="self.canvas.callbacks.process(event.name, event)")
    def key_press(self: FigureManagerBase,
                  event: Any) -> Optional[Any]: ...

    @_api.deprecated(
        "3.4", alternative="self.canvas.callbacks.process(event.name, event)")
    def button_press(self: FigureManagerBase,
                     event: Any) -> Optional[Any]: ...

    def get_window_title(self: FigureManagerBase) -> str: ...

    def set_window_title(self: FigureManagerBase,
                         title: str) -> None: ...


def key_press_handler(event: KeyEvent,
                      canvas: FigureCanvasBase = None,
                      toolbar: NavigationToolbar2 = None) -> None: ...


def button_press_handler(event: Any,
                         canvas: Any = None,
                         toolbar: Any = None) -> None: ...


def get_registered_canvas_class(format: str) -> Optional[str]: ...


def _get_renderer(figure: Union[{draw}, Figure],
                  print_method: partial = None) -> Any: ...


def _safe_pyplot_import() -> pyplot.py: ...


def _check_savefig_extra_args(func: Any = None,
                              extra_kwargs: tuple = ()) -> Union[
    partial, (args: tuple[Any, ...], kwargs: dict[str, Any]) ->


def _no_output_draw(figure: {draw}) -> None: ...


def register_backend(format: str,
                     backend: Any,
                     description: str = None) -> None: ...


def _is_non_interactive_terminal_ipython(ip: {parent}) -> bool: ...