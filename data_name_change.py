import os

# 🔧 바꿀 파일들이 있는 디렉토리 경로를 지정하세요
target_dir = "/home/airo/act/data/aloha_dataset/converted/data"  # 예: "/home/user/data"

# 디렉토리 내 파일 목록 중 .hdf5만 필터링
files = [f for f in os.listdir(target_dir) if f.endswith(".hdf5")]

# 순서대로 이름 변경
for i, old_name in enumerate(files):
    old_path = os.path.join(target_dir, old_name)
    new_name = f"episode_{i}.hdf5"
    new_path = os.path.join(target_dir, new_name)

    os.rename(old_path, new_path)
    print(f"Renamed: {old_name} -> {new_name}")