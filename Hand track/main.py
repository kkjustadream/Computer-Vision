import sys

site_packages_path = None
for path in sys.path:
    if 'site-packages' in path:
        site_packages_path = path
        break

print(site_packages_path)
