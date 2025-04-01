import roms_tools as rt
import pooch
from pathlib import Path

update_netcdf = True

dataset_dir = Path("roms_tools_datasets")

if not dataset_dir.exists():
    dataset_dir.mkdir(parents=True)
    pup_test_data = pooch.create(
        path=Path("roms_tools_datasets"),
        base_url="https://github.com/CWorthy-ocean/roms-tools-test-data/raw/main/",
        # The registry specifies the files that can be fetched                                                                                                                                                     
        registry={
            "GLORYS_NA_2012.nc": "b862add892f5d6e0d670c8f7fa698f4af5290ac87077ca812a6795e120d0ca8c",
            "ERA5_NA_2012.nc": "d07fa7450869dfd3aec54411777a5f7de3cb3ec21492eec36f4980e220c51757",
            "TPXO_global_test_data.nc": "457bfe87a7b247ec6e04e3c7d3e741ccf223020c41593f8ae33a14f2b5255e60",
            "CESM_BGC_2012.nc": "e374d5df3c1be742d564fd26fd861c2d40af73be50a432c51d258171d5638eb6",
            "CESM_BGC_SURFACE_2012.nc": "3c4d156adca97909d0fac36bf50b99583ab37d8020d7a3e8511e92abf2331b38",
        },
    )
    pup_test_data.fetch("GLORYS_NA_2012.nc")
    pup_test_data.fetch("TPXO_global_test_data.nc")
    pup_test_data.fetch("ERA5_NA_2012.nc")
    pup_test_data.fetch("CESM_BGC_2012.nc")
    pup_test_data.fetch("CESM_BGC_SURFACE_2012.nc")



Path("updated").mkdir(parents=True,exist_ok=True)

## Grid
roms_grd = rt.Grid.from_yaml("roms_grd.yaml")
roms_grd.to_yaml("updated/roms_grd.yaml")

## Tides
roms_tides = rt.TidalForcing.from_yaml("roms_tides.yaml")
roms_tides.to_yaml("updated/roms_tides.yaml")

## Initial Conditions
roms_ini = rt.InitialConditions.from_yaml("roms_ini.yaml")
roms_ini.to_yaml("updated/roms_ini.yaml")

## Surface Forcing
roms_frc = rt.SurfaceForcing.from_yaml("roms_frc.yaml")
roms_frc.to_yaml("updated/roms_frc.yaml")

## BGC Surface Forcing
roms_frc_bgc = rt.SurfaceForcing.from_yaml("roms_frc_bgc.yaml")
roms_frc_bgc.to_yaml("updated/roms_frc_bgc.yaml")

## Boundary Forcing
roms_bry = rt.BoundaryForcing.from_yaml("roms_bry.yaml")
roms_bry.to_yaml("updated/roms_bry.yaml")

## BGC Boundary Forcing
roms_bry_bgc = rt.BoundaryForcing.from_yaml("roms_bry_bgc.yaml")
roms_bry_bgc.to_yaml("updated/roms_bry_bgc.yaml")

## Update netcdf

netcdf_dir = Path("../input_datasets/ROMS/updated")
netcdf_dir.mkdir(parents=True, exist_ok=True)

if update_netcdf:
    roms_grd.save(netcdf_dir/"roms_grd")
    roms_tides.save(netcdf_dir/"roms_tides")
    roms_ini.save(netcdf_dir/"roms_ini")
    roms_frc.save(netcdf_dir/"roms_frc",group=False)
    roms_frc_bgc.save(netcdf_dir/"roms_frc_bgc",group=False)
    roms_bry.save(netcdf_dir/"roms_bry",group=False)
    roms_bry_bgc.save(netcdf_dir/"roms_bry_bgc",group=False)
