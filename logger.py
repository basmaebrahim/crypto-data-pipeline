import logging
import sys

# إعادة تعريف stdout ليكون UTF-8 عشان الإيموجي يشتغل على Windows
sys.stdout.reconfigure(encoding='utf-8')

def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        stream=sys.stdout,
    )