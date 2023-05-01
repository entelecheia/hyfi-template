"""Command line interface for hyfi_template"""

# Importing the libraries
import sys

from hyfi import hydra_main


def main() -> None:
    """Main function for the CLI"""
    sys.argv.append("--config-path=pkg://hyfi_template.conf")
    print(sys.argv)
    hydra_main()


if __name__ == "__main__":
    main()
