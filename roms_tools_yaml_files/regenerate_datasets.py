""" This script regenerates all datasets from scratch,
rather than attempting to load prior yaml files. It can be used if the
previous yaml files are no longer compatible with roms-tools"""

# %% Setup
#
import datetime

start_time = datetime.datetime(2012,1,1,12,0,0)
end_time   = datetime.datetime(2012,1,1,12,10,0)

from pathlib import Path
# Output
yaml_path: Path | None = Path.cwd()
netcdf_path: Path | None = Path.cwd() / "../input_datasets/ROMS"


# Input
test_dataset_dir = Path("roms_tools_datasets")
full_dataset_dir = Path("~/Code/roms_tools_datasets").expanduser()
GLORYS_path = test_dataset_dir / "GLORYS_NA_2012.nc"
BGC_path = test_dataset_dir / "CESM_BGC_2012.nc"
BGC_frc_path = test_dataset_dir / "CESM_BGC_SURFACE_2012.nc"
ERA5_path = test_dataset_dir / "ERA5_NA_2012.nc"
tpxo_dict = {
    "grid": test_dataset_dir / "global_grid_tpxo10.v2.nc",
    "h": test_dataset_dir / "global_h_tpxo10.v2.nc",
    "u": test_dataset_dir / "global_u_tpxo10.v2.nc"
    # "grid": full_dataset_dir / "TPXO10.v2/grid_tpxo10v2.nc",
    # "h": full_dataset_dir / "TPXO10.v2/h_tpxo10.v2.nc",
    # "u": full_dataset_dir / "TPXO10.v2/u_tpxo10.v2.nc"
}

# %% Grid

from roms_tools import Grid

roms_grd = Grid(nx=8,ny=8,size_x=400,size_y=400,center_lat=60,center_lon=-5,rot=10,N=8)
if yaml_path:
    roms_grd.to_yaml(yaml_path / "roms_grd.yaml")
if netcdf_path:
    roms_grd.save(netcdf_path / "roms_grd.nc")
# %% Tides


from roms_tools import TidalForcing

roms_tides = TidalForcing(
    grid=roms_grd,
    ntides=1,
    source={"name": "TPXO", "path": tpxo_dict}
)
if yaml_path:
    roms_tides.to_yaml(yaml_path / "roms_tides.yaml")
if netcdf_path:
    roms_tides.save(netcdf_path / "roms_tides.nc")
# %% Surface Forcing

from roms_tools import SurfaceForcing

roms_frc = SurfaceForcing(
    grid=roms_grd,
    start_time=start_time,
    end_time=end_time,
    source={"name":"ERA5", "path":ERA5_path},
    type="physics",
    coarse_grid_mode="never"
)


if yaml_path:
    roms_frc.to_yaml(yaml_path / "roms_frc.yaml")
if netcdf_path:
    roms_frc.save(netcdf_path / "roms_frc.nc", group=False)

roms_frc_bgc = SurfaceForcing(
    grid=roms_grd,
    start_time=start_time,
    end_time=end_time,
    type="bgc",
    source={"climatology": False, "name": "CESM_REGRIDDED", "path": BGC_frc_path},
    coarse_grid_mode="never"
)

if yaml_path:
    roms_frc_bgc.to_yaml(yaml_path / "roms_frc_bgc.yaml")
if netcdf_path:
    roms_frc_bgc.save(netcdf_path / "roms_frc_bgc.nc", group=False)

# %% InitialConditions

from roms_tools import InitialConditions

roms_ini = InitialConditions(
    grid=roms_grd,
    ini_time=start_time,
    source={"name": "GLORYS", "path": GLORYS_path},
    bgc_source={"climatology": False, "name": "CESM_REGRIDDED", "path": BGC_path},
)

if yaml_path:
    roms_ini.to_yaml(yaml_path / "roms_ini.yaml")
if netcdf_path:
    roms_ini.save(netcdf_path / "roms_ini.nc")

# %% BoundaryConditions

from roms_tools import BoundaryForcing

roms_bry = BoundaryForcing(
    grid=roms_grd,
    start_time=start_time,
    end_time=end_time,
    source={"name": "GLORYS", "path": GLORYS_path},
    type="physics"
)
if yaml_path:
    roms_bry.to_yaml(yaml_path / "roms_bry.yaml")
if netcdf_path:
    roms_bry.save(netcdf_path / "roms_bry.nc", group=False)

roms_bry_bgc = BoundaryForcing(
    grid=roms_grd,
    start_time=start_time,
    end_time=end_time,
    source={"climatology": False, "name": "CESM_REGRIDDED", "path": BGC_path},
    type="bgc"
)
if yaml_path:
    roms_bry_bgc.to_yaml(yaml_path / "roms_bry_bgc.yaml")
if netcdf_path:
    roms_bry_bgc.save(netcdf_path / "roms_bry_bgc.nc", group=False)
