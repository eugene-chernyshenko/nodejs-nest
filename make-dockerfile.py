#!/usr/bin/env python

import yaml

node_version = '10.15.3'

package_manager = 'npm'

package_json = 'package.json'

package_lock = 'package-lock.json'

build_script = 'build'

start_script = 'start'

with open('Manifest') as f:
    manifest_str = f.read()

y = yaml.safe_load(manifest_str)
node = y.get('node')

if 'version' in node:
    node_version = node.get('version')
if 'packageManager' in node:
    package_manager = node.get('packageManager')
if 'packageJson' in node:
    package_json = node.get('packageJson')
if 'packageLock' in node:
    package_lock = node.get('packageLock')
if 'buildScript' in node:
    build_script = node.get('buildScript')
if 'startScript' in node:
    start_script = node.get('startScript')

dockerfile_str = f"""FROM node:{node_version}

WORKDIR /app

CMD ["{package_manager}", "run", "{start_script}"]

ADD {package_json} {package_lock} .

RUN {package_manager} install

ADD . .

RUN {package_manager} run {build_script}
"""

with open('Dockerfile', 'w') as f:
    f.write(dockerfile_str)
