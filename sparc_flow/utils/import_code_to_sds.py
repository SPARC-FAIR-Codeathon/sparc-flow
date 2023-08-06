import os
import shutil


def import_code_to_sds(source_code, sds_dir, action=0):
    """

    :param source_code: location of source code repository
    :type source_code: str
    :param sds_dir: path to the SDS folder
    :type sds_dir: str
    :param action: action can be 0 for copying, 1 for moving
    :type action: int
    :return:
    :rtype:
    """
    sds_code_dir = os.path.join(sds_dir, "code")

    if os.path.isdir(source_code):
        _import(source_code, sds_code_dir, action)
    pass


def _import(source_code, sds_code_dir, action):
    if action == 0:
        shutil.copytree(source_code, sds_code_dir, dirs_exist_ok=True)
    elif action == 1:
        shutil.move(source_code, sds_code_dir)
    else:
        pass

