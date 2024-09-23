"""
This script downloads data needed by roms-tools to create ROMS input files
"""

import pooch
from pathlib import Path

datadir=Path.cwd()/"roms_tools_datasets/"
datadir.mkdir(exist_ok=True)

pup_test_data = pooch.create(
    path=datadir,
    base_url="https://github.com/CWorthy-ocean/roms-tools-test-data/raw/main/",
    # The registry specifies the files that can be fetched
    registry={
        "GLORYS_NA_2012.nc": "b862add892f5d6e0d670c8f7fa698f4af5290ac87077ca812a6795e120d0ca8c",
        "ERA5_NA_2012.nc": "d07fa7450869dfd3aec54411777a5f7de3cb3ec21492eec36f4980e220c51757",
        "TPXO_global_test_data.nc": "457bfe87a7b247ec6e04e3c7d3e741ccf223020c41593f8ae33a14f2b5255e60",
        "CESM_BGC_2012.nc": "e374d5df3c1be742d564fd26fd861c2d40af73be50a432c51d258171d5638eb6",
        "CESM_BGC_SURFACE_2012.nc": "3c4d156adca97909d0fac36bf50b99583ab37d8020d7a3e8511e92abf2331b38"
    },
)
print("fetching data")
fname_glorys = pup_test_data.fetch("GLORYS_NA_2012.nc")
fname_tpxo = pup_test_data.fetch("TPXO_global_test_data.nc")
fname_era5 = pup_test_data.fetch("ERA5_NA_2012.nc")
fname_cesm_interior = pup_test_data.fetch("CESM_BGC_2012.nc")
fname_cesm_surface = pup_test_data.fetch("CESM_BGC_SURFACE_2012.nc")
