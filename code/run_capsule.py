from pathlib import Path
import json

INPUT_DIR = Path("/data/")
OUTPUT_DIR = Path("/results/")

if __name__ == "__main__":
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
