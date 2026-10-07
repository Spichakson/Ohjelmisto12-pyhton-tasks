from tqdm import tqdm
import time

for item in tqdm(range(100), desc="Завантаження"):
    time.sleep(0.02)