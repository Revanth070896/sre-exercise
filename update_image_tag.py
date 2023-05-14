import yaml
import argparse
from pathlib import Path


def update_image(filename, service, docker_image, image_tag):
    try:
        with open(filename, 'r') as f:
            data = yaml.safe_load(f)
            data['services'][service]['image'] = f"{docker_image}:{image_tag}"

        with open(filename, 'w') as f:
            yaml.dump(data, f)
    except Exception as e:
        print(f"Caught an exception while updating the image tag: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Update image tag in compose file')
    parser.add_argument("--path", required=True,
                        help="Output language")
    parser.add_argument("--service", required=True)
    parser.add_argument("--dockerimage", required=True)
    parser.add_argument("--dockertag", required=True)
    args = parser.parse_args()
    target_dir = Path(args.path)
    if not target_dir.exists():
        print("The target directory doesn't exist")
        raise SystemExit(1)

    update_image(target_dir, args.service, args.dockerimage, args.dockertag)