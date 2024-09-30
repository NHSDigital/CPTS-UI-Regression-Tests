import argparse
import subprocess

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # commandline arguments
    parser.add_argument(
        "--product",
        required=True,
        help="The product under test",
    )
    parser.add_argument(
        "--tags",
        required=False,
        help="Tags to include or exclude. use ~tag_name to exclude tags",
    )
    argument = parser.parse_args()

    # Convert to behave commandline args
    product_tag = argument.product.lower().replace("-", "_")
    if argument.tags:
        tags = f" --tags {product_tag} --tags {argument.tags} "
    else:
        tags = f" --tags {product_tag}"
    PRODUCT = f" -D product={argument.product}"

    # complete command
    command = f"pytest features/{product_tag}"

    print(f"Running subprocess with command: '{command}'")
    subprocess.run(command, shell=True, check=True)
