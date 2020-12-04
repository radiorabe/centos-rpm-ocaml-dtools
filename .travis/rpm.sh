#!/bin/bash
#
# RPM build wrapper for ocaml-dtools, runs inside the build container on travis-ci

set -xe

curl -o /etc/yum.repos.d/ocaml.repo "https://download.opensuse.org/repositories/home:/radiorabe:/liquidsoap:/ocaml/CentOS_8/home:radiorabe:liquidsoap:ocaml.repo"

chown root:root ocaml-dtools.spec

build-rpm-package.sh ocaml-dtools.spec
