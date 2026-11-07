import logging

logging.basicConfig(
    filename="mindmate.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("MindMate application started.")

logging.warning("Task deadline is approaching.")

logging.error("Unable to load task records.")

print("Logging completed. Check mindmate.log")
