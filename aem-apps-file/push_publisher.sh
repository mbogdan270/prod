  #!/bin/bash

cd /usr/src/app/Archive
zip -r /usr/src/app/Archive/Archive.zip jcr_root META-INF
mv /usr/src/app/Archive/Archive.zip /usr/src/app/
cd /usr/src/app
curl -u admin:$2 -F file=@Archive.zip -F name="lala" -F force=true -F install=true $1
cd /tmp
