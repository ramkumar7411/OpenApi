import os
import logzero


cwd = os.path.dirname(__file__)

log_dir = os.path.join(cwd, "../", "logs")

if not os.path.exists(log_dir):
    os.mkdir(log_dir)

logger = logzero.setup_logger(__name__, logfile=os.path.join(log_dir, "api.log"))