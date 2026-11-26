import logging

logging.basicConfig(
    level=logging.DEBUG, 
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler("app_experiment14.log"),  
        logging.StreamHandler()                       
    ]
)

logging.debug("DEBUG: Detailed diagnostic information for debugging.")
logging.info("INFO: General confirmation that the program is working as expected.")
logging.warning("WARNING: An unexpected event occurred, or a problem may arise soon.")
logging.error("ERROR: A serious problem occurred; a function failed to execute.")
logging.critical("CRITICAL: A severe error occurred; the application may crash.")