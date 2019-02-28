  #!/bin/bash

cd /usr/src/app/Archive
zip -r /usr/src/app/Archive/Archive.zip jcr_root META-INF
mv /usr/src/app/Archive/Archive.zip /usr/src/app/
cd /usr/src/app
curl -u admin:xvfT9T4FRCWV=W@v?=+Q}GHL -F file=@Archive.zip -F name="lala" -F force=true -F install=true http://35.183.247.189:4503/crx/packmgr/service.jsp
