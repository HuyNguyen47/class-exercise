import argparse
import logging
import sys
from pathlib import Path
import pandas as pd

from class6_7_netflix_utils import (
    clean_text,
    drop_missing_rows,
    remove_duplicates,
    remove_iqr_outliers,
    show_overview,
    )
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(
    description="Explore Netflix titles"
    )
    parser.add_argument(
    "--input",
    default="data/messy_netflix_titles.csv",
    help="Path to the Netflix CSV file"
    )
    parser.add_argument(
    "--verbose",
    action="store_true",
    help="Show debug messages"
    )

    args = parser.parse_args()

    logging.basicConfig(
    level=logging.DEBUG if args.verbose else logging.INFO,
    format="%(asctime)s %(levelname)-8s %(name)s — %(message)s",
    datefmt="%H:%M:%S"
    )
    # TODO 4:
    # Create a Path object from args.input.
    # Inside a try block, load that path using pd.read_csv().
    # Catch FileNotFoundError, log an ERROR message,
    # and exit with sys.exit(1).
    # Log an INFO message.
    # TODO 5:
    # Call show_overview().
    # Log an INFO message.
    # TODO 6:
    # Call remove_duplicates().
    # Call drop_missing_rows().
    # Log an INFO message after each step that
    # includes the number of rows removed.
    data_path = Path(args.input)
    try:
        df = pd.read_csv(data_path)
    except FileNotFoundError:
        logger.error("File Not Found")
        sys.exit(1)
    df_original = df.copy()
    logger.info(f"Dataset loaded: {args.input}")

    show_overview(df)
    logger.info(f"Overview displayed")
    before = len(df)

    df = remove_duplicates(df)
    logger.info("Duplicates removed")
    df = drop_missing_rows(df)
    logger.info("Removed missing rows")
    try:
        df = remove_iqr_outliers(df, "runtime_minutes", 1.5)
    except ValueError:
        sys.exit(1)
    logger.info("Removing outliers using iqr")
    print(df)
    for col in ["title", "type", "country"]:
        if col in df.columns:
            df[col].apply(clean_text)
            logger.info(f"Text Column {col} cleaned")
    report = {"rows_before": len(df_original), "rows_after": len(df), "rows_removed": len(df_original) - len(df), "columns": df.shape[1]}
    logger.info(f"Report: {report}")
    logger.info(f"{before-len(df)} rows have been removed")



if __name__ == "__main__":
    main()
