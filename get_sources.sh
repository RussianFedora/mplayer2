#!/bin/bash

ORIGNAME=mplayer2-build
VERSION=2.0
GIT_REVISION=b711624
NAME=${ORIGNAME}-${VERSION}.git

rm -rf ${ORIGNAME}
git clone git://git.mplayer2.org/${ORIGNAME}.git &>/dev/null
cd $ORIGNAME
./init --shallow
cd ..
mv ${ORIGNAME} ${NAME}
find ${NAME} -name ".git" -exec rm -rf {} \; 2>/dev/null

tar cfJ ${NAME}.tar.xz ${NAME}
rm -rf ${NAME}
