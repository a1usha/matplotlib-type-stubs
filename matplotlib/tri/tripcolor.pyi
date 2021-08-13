def tripcolor(*args,
              ax: {grid, update_datalim, autoscale_view, add_collection},
              alpha: float = 1.0,
              norm: Any = None,
              cmap: Any = None,
              vmin: Any = None,
              vmax: Any = None,
              shading: str = 'flat',
              facecolors: Any = None,
              **kwargs) -> Union[TriMesh, PolyCollection]: ...