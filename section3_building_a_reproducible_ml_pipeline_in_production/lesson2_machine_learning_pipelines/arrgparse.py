#!/usr/bin/env python
import argparse
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):
    # Your code here
    # For example:
    logger.info("This is a message")
    logger.warning("This is a warning")
    logger.error("This is an error")

    logger.info(f"This is {args.artifact_name}")

    logger.info(f"This is {args.optional_arg}")


if __name__ == "__main__":
    # This block is executed only if this file is being
    # executed as a script. It is NOT executed if the file
    # is imported as a module
    parser = argparse.ArgumentParser(
        description="This is a tutorial on argparse"
    )

    parser.add_argument(
        "--artifact_name", type=str, help="Name and version of W&B artifact", required=True
    )

    parser.add_argument(
        "--optional_arg", type=float, help="An optional argument", required=False,
        default=2.3
    )

    args = parser.parse_args()

    go(args)