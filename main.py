import os
import sys
import time
from src.tools.email_fetchers.main_poller import EmailPoller

# 添加项目根目录到Python路径
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from src.utils.logger import getLogger

logger = getLogger(__name__)

def main():
    poller = EmailPoller(config_path="src/config/email_config.json")
    poller.start()

    try:
        while True:
            # Keep main thread alive until Ctrl+C
            # Check if any poller threads are still alive
            if not any(t.is_alive() for t in poller.threads if t is not None):
                logger.info("All poller threads have unexpectedly stopped.")
                break
            time.sleep(5) 
    except KeyboardInterrupt:
        logger.info("Ctrl+C received, shutting down...")
    finally:
        poller.stop()

if __name__ == "__main__":
    sys.exit(main()) 