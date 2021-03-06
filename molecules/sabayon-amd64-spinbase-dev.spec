# Use abs path, otherwise daily builds automagic won't work
%env %import ${SABAYON_MOLECULE_HOME:-/sabayon}/molecules/spinbase.common
%env %import ${SABAYON_MOLECULE_HOME:-/sabayon}/molecules/amd64.common

%env destination_chroot: ${SABAYON_MOLECULE_HOME:-/sabayon}/chroots/limbo
%env inner_chroot_script: ${SABAYON_MOLECULE_HOME:-/sabayon}/scripts/inner_chroot_script.sh sabayon-limbo
%env destination_livecd_root: ${SABAYON_MOLECULE_HOME:-/sabayon}/chroots/limbo

# Release Version
# Keep this here, otherwise daily builds automagic won't work
%env release_version: ${SABAYON_RELEASE:-LATEST}

# Release Version string description
release_desc: amd64 SpinBase Development

# Source chroot directory, where files are pulled from
%env source_chroot: ${SABAYON_MOLECULE_HOME:-/sabayon}/sources/amd64-docker-spinbase

# Destination ISO image name, call whatever you want.iso, not mandatory
# Keep this here and set, otherwise daily builds automagic won't work
%env destination_iso_image_name: Sabayon_Linux_${SABAYON_RELEASE:-LATEST}_amd64_SpinBase-dev.iso
