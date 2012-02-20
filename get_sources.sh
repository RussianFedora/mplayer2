#!/bin/bash

ORIGNAME=mplayer2-build
VERSION=2.0
GIT_REVISION=fc6a9e4
NAME=${ORIGNAME}-${VERSION}.git

rm -rf ${ORIGNAME}
git clone git://git.mplayer2.org/mplayer2-build.git &>/dev/null
cd $ORIGNAME
./init --shallow
cd ..
mv ${ORIGNAME} ${NAME}

tar cfJ ${NAME}.tar.xz ${NAME}
rm -rf ${NAME}
