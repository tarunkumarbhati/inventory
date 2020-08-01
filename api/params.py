import os

AVERAGE_AREA_ALLOWED = float(os.getenv('A1', 100))
AVERAGE_VOLUME_ALLOWED_CURRENT = float(os.getenv('V1', 1000))
WEEKLY_BOX_ALLOWED = int(os.getenv('L1', 100))
WEEKLY_BOX_ALLOWED_CURRENT = int(os.getenv('L2', 50))