# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------
import os

import launch
from packaging import version
from modules import paths_internal


def install():  
    try:
        DML_UNET_MODEL_DIR = os.path.join(paths_internal.models_path, "Unet-dml")
        if not os.path.exists(DML_UNET_MODEL_DIR):
            os.makedirs(DML_UNET_MODEL_DIR)
    except:
        print("Error")

install()
