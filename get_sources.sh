#!/bin/bash

ORIGNAME=mplayer2-build
VERSION=2.0
GIT_REVISION=c62dbb8
NAME=${ORIGNAME}-${VERSION}.git

rm -rf ${ORIGNAME}
git clone git://git.mplayer2.org/mplayer2-build.git &>/dev/null
cd $ORIGNAME
sed -i -e "s|#!/usr/bin/env python3|#!/usr/bin/env python|" "clean" ;
sed -i -e "s|#!/usr/bin/env python3|#!/usr/bin/env python|" "init" ;
sed -i -e "s|#!/usr/bin/env python3|#!/usr/bin/env python|" "script/libav-config" ;
sed -i -e "s|#!/usr/bin/env python3|#!/usr/bin/env python|" "script/update" ;
sed -i -e "s|#!/usr/bin/env python3|#!/usr/bin/env python|" "script/mplayer-config" ;
sed -i -e "s|#!/usr/bin/env python3|#!/usr/bin/env python|" "script/export" ;
./init --shallow
#sed -i -e "s|#!/usr/bin/env python3|#!/usr/bin/env python|" "mplayer/TOOLS/matroska.py" ;
#sed -i -e "s|#!/usr/bin/env python3|#!/usr/bin/env python|" "mplayer/TOOLS/file2string.py" ;
#sed -i -e "s|#!/usr/bin/env python3|#!/usr/bin/env python|" "mplayer/TOOLS/vdpau_functions.py" ;
cd ..
mv ${ORIGNAME} ${NAME}

tar cfJ ${NAME}.tar.xz ${NAME}
rm -rf ${NAME}
