#!/usr/local/autopkg/python
#
# Copyright 2020 Anver Housseini
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""See docstring for AircallURLProvider class"""

import json

from autopkglib import URLGetter

__all__ = ["DruvaInsyncURLProvider"]


class DruvaInsyncURLProvider(URLGetter):
    """Provides the URL for the latest Druva Insync Downlaod."""

    description = __doc__
    input_variables = {
        "url": {"required": False, "description": "URL to Druva Insync Download API"}
    }

    output_variables = {"url": {"description": ("URL of the latest Druva Insync release.")}}

    def main(self):
        """Grab version from appcast"""

        url = "https://downloads.druva.com/insync/js/data.json"

        appcast = self.download(url)

        data = json.loads(appcast.decode("utf-8"))
        for i in data:
          if i['title'] == 'macOS':
            latestVersion = max(i["installerDetails"], key=lambda x:x['version'])

        self.env["url"] = latestVersion['downloadURL']
        self.output("Found url %s" % self.env["url"])


if __name__ == "__main__":
    processor = DruvaInsyncURLProvider()
    processor.execute_shell()