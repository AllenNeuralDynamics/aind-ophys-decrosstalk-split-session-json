from pathlib import Path
import json

INPUT_DIR = Path("/data/")
OUTPUT_DIR = Path("/results/")


def find_metadata(name):
    """Return the metadata file at or one level below the input root, or None."""
    for pattern in (name, f"*/{name}"):
        found = sorted(INPUT_DIR.glob(pattern))
        if found:
            return found[0]
    return None


def v2_pairs(acquisition):
    """Return (pair index, plane id, plane id) for each coupled pair of a v2 acquisition.

    v2 records each plane's partner as coupled_plane_index, so pairs are
    numbered in plane-index order, which is v1's coupled_fov_index.
    """
    planes = {}
    for data_stream in acquisition["data_streams"]:
        for config in data_stream.get("configurations") or []:
            for image in config.get("images") or []:
                for plane in image.get("planes") or []:
                    if plane.get("coupled_plane_index") is None:
                        continue
                    structure = plane["targeted_structure"]
                    if isinstance(structure, dict):
                        structure = structure["acronym"]
                    index = plane["plane_index"]
                    planes[index] = (plane["coupled_plane_index"], f"{structure}_{index}")
    pairs = []
    paired = set()
    for index in sorted(planes):
        if index in paired:
            continue
        partner, plane_id = planes[index]
        paired.update((index, partner))
        pairs.append((len(pairs), plane_id, planes[partner][1]))
    return pairs


if __name__ == "__main__":
    acquisition_fp = find_metadata("acquisition.json")
    if acquisition_fp is not None:
        with open(acquisition_fp, "r") as j:
            acquisition = json.load(j)
        for pair_index, first, second in v2_pairs(acquisition):
            with open(OUTPUT_DIR / f"pair{pair_index}.txt", "w") as f:
                f.write(f"{INPUT_DIR / first}\n{INPUT_DIR / second}\n")
    else:
        try:
            session_json_fp = next(INPUT_DIR.glob("session.json"))
        except StopIteration:
            session_json_fp = next(INPUT_DIR.glob("*/session.json"))

        with open(session_json_fp, "r") as j:
            session_data = json.load(j)
        pair_list = []
        for data_stream in session_data["data_streams"]:
            if data_stream["ophys_fovs"]:
                for fov in data_stream["ophys_fovs"]:
                    index = fov["index"]
                    coupled_fov_index = fov["coupled_fov_index"]
                    if coupled_fov_index in pair_list:
                        pair2_fp = INPUT_DIR / str(fov["targeted_structure"] + "_" + str(index))
                        pair_list = []
                        with open(OUTPUT_DIR / f"pair{coupled_fov_index}.txt", "w") as f:
                            f.write(f"{pair1_fp}\n{pair2_fp}\n")
                    else:
                        pair1_fp = INPUT_DIR /  str(fov["targeted_structure"] + "_" + str(index))
                        pair_list.append(coupled_fov_index)
