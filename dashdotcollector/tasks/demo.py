IMAGEMANIFESTVULN = r"""{
    "apiVersion": "v1",
    "items": [
        {
            "apiVersion": "secscan.quay.redhat.com/v1alpha1",
            "kind": "ImageManifestVuln",
            "metadata": {
                "creationTimestamp": "2020-05-20T14:24:56Z",
                "generation": 42,
                "labels": {
                    "cso/sleep-6f84df5847-4bn9p": "true",
                    "cso/sleep-6f84df5847-bctxz": "true",
                    "cso/sleep-6f84df5847-dh9l8": "true"
                },
                "name": "sha256.9e0c275e0bcb495773b10a18e499985d782810e47b4fce076422acb4bc3da3dd",
                "namespace": "cso",
                "resourceVersion": "935794",
                "selfLink": "/apis/secscan.quay.redhat.com/v1alpha1/namespaces/cso/imagemanifestvulns/sha256.9e0c275e0bcb495773b10a18e499985d782810e47b4fce076422acb4bc3da3dd",
                "uid": "fff9e72d-531f-45ac-94c9-acbf6d85a062"
            },
            "spec": {
                "features": [
                    {
                        "name": "platform-python-pip",
                        "namespaceName": "centos:8",
                        "version": "9.0.3-15.el8",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "pip is a package management system used to install and manage software packages written in Python. Many packages can be found in the Python Package Index (PyPI). pip is a recursive acronym that can stand for either \"Pip Installs Packages\" or \"Pip Installs Python\".  Security Fix(es): * python-urllib3: Cross-host redirect does not remove Authorization header allow for credential exposure (CVE-2018-20060) * python-urllib3: CRLF injection due to not encoding the '\\r\\n' sequence leading to possible attack on internal service (CVE-2019-11236) * python-urllib3: Certification mishandle when error should be thrown (CVE-2019-11324) * python-requests: Redirect from HTTPS to HTTP does not remove Authorization header (CVE-2018-18074) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 8.2 Release Notes linked from the References section.",
                                "fixedby": "0:9.0.3-16.el8",
                                "link": "https://access.redhat.com/errata/RHSA-2020:1916",
                                "metadata": "null",
                                "name": "RHSA-2020:1916",
                                "namespaceName": "centos:8",
                                "severity": "Medium"
                            }
                        ]
                    },
                    {
                        "name": "libstdc++",
                        "namespaceName": "centos:8",
                        "version": "8.3.1-4.5.el8",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "The gcc packages provide compilers for C, C++, Java, Fortran, Objective C, and Ada 95 GNU, as well as related support libraries. Security Fix(es): * gcc: POWER9 \"DARN\" RNG intrinsic produces repeated output (CVE-2019-15847) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 8.2 Release Notes linked from the References section.",
                                "fixedby": "0:8.3.1-5.el8",
                                "link": "https://access.redhat.com/errata/RHSA-2020:1864",
                                "metadata": "null",
                                "name": "RHSA-2020:1864",
                                "namespaceName": "centos:8",
                                "severity": "Medium"
                            }
                        ]
                    },
                    {
                        "name": "sqlite-libs",
                        "namespaceName": "centos:8",
                        "version": "3.26.0-3.el8",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "SQLite is a C library that implements an SQL database engine. A large subset of SQL92 is supported. A complete database is stored in a single disk file. The API is designed for convenience and ease of use. Applications that link against SQLite can enjoy the power and flexibility of an SQL database without the administrative hassles of supporting a separate database server. Security Fix(es): * sqlite: fts3: improve shadow table corruption detection (CVE-2019-13734) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section.",
                                "fixedby": "0:3.26.0-4.el8_1",
                                "link": "https://access.redhat.com/errata/RHSA-2020:0273",
                                "metadata": "null",
                                "name": "RHSA-2020:0273",
                                "namespaceName": "centos:8",
                                "severity": "High"
                            },
                            {
                                "description": "SQLite is a C library that implements an SQL database engine. A large subset of SQL92 is supported. A complete database is stored in a single disk file. The API is designed for convenience and ease of use. Applications that link against SQLite can enjoy the power and flexibility of an SQL database without the administrative hassles of supporting a separate database server. Security Fix(es): * sqlite: heap out-of-bound read in function rtreenode() (CVE-2019-8457) * sqlite: fts3: improve shadow table corruption detection (CVE-2019-13752) * sqlite: fts3: incorrectly removed corruption check (CVE-2019-13753) * sqlite: mishandling of certain uses of SELECT DISTINCT involving a LEFT JOIN in flattenSubquery in select.c leads to a NULL pointer dereference (CVE-2019-19923) * sqlite: incorrect sqlite3WindowRewrite() error handling leads to mishandling certain parser-tree rewriting (CVE-2019-19924) * sqlite: zipfileUpdate in ext/misc/zipfile.c mishandles a NULL pathname during an update of a ZIP archive (CVE-2019-19925) * sqlite: mishandles certain uses of INSERT INTO in situations involving embedded '\\0' characters in filenames (CVE-2019-19959) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 8.2 Release Notes linked from the References section.",
                                "fixedby": "0:3.26.0-6.el8",
                                "link": "https://access.redhat.com/errata/RHSA-2020:1810",
                                "metadata": "null",
                                "name": "RHSA-2020:1810",
                                "namespaceName": "centos:8",
                                "severity": "Medium"
                            },
                            {
                                "description": "SQLite is a C library that implements an SQL database engine. A large subset of SQL92 is supported. A complete database is stored in a single disk file. The API is designed for convenience and ease of use. Applications that link against SQLite can enjoy the power and flexibility of an SQL database without the administrative hassles of supporting a separate database server. Security Fix(es): * sqlite: fts3: improve shadow table corruption detection (CVE-2019-13734) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section.",
                                "fixedby": "0:3.26.0-4.el8_0",
                                "link": "https://access.redhat.com/errata/RHSA-2020:0229",
                                "metadata": "null",
                                "name": "RHSA-2020:0229",
                                "namespaceName": "centos:8",
                                "severity": "High"
                            }
                        ]
                    },
                    {
                        "name": "python3-libs",
                        "namespaceName": "centos:8",
                        "version": "3.6.8-15.1.el8",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "Python is an interpreted, interactive, object-oriented programming language, which includes modules, classes, exceptions, very high level dynamic data types and dynamic typing. Python supports interfaces to many system calls and libraries, as well as to various windowing systems.  Security Fix(es): * python: Cookie domain check returns incorrect results (CVE-2018-20852) * python: email.utils.parseaddr wrongly parses email addresses (CVE-2019-16056) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 8.2 Release Notes linked from the References section.",
                                "fixedby": "0:3.6.8-23.el8",
                                "link": "https://access.redhat.com/errata/RHSA-2020:1764",
                                "metadata": "null",
                                "name": "RHSA-2020:1764",
                                "namespaceName": "centos:8",
                                "severity": "Medium"
                            }
                        ]
                    },
                    {
                        "name": "libcom_err",
                        "namespaceName": "centos:8",
                        "version": "1.44.6-3.el8",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "The e2fsprogs packages provide a number of utilities for creating, checking, modifying, and correcting the ext2, ext3, and ext4 file systems. The following packages have been upgraded to a later upstream version: e2fsprogs (1.45.4). (BZ#1783777) Security Fix(es): * e2fsprogs: crafted ext4 partition leads to out-of-bounds write (CVE-2019-5094) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 8.2 Release Notes linked from the References section.",
                                "fixedby": "0:1.45.4-3.el8",
                                "link": "https://access.redhat.com/errata/RHSA-2020:1913",
                                "metadata": "null",
                                "name": "RHSA-2020:1913",
                                "namespaceName": "centos:8",
                                "severity": "Medium"
                            }
                        ]
                    },
                    {
                        "name": "systemd-udev",
                        "namespaceName": "centos:8",
                        "version": "239-18.el8_1.1",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "The systemd packages contain systemd, a system and service manager for Linux, compatible with the SysV and LSB init scripts. It provides aggressive parallelism capabilities, uses socket and D-Bus activation for starting services, offers on-demand starting of daemons, and keeps track of processes using Linux cgroups. In addition, it supports snapshotting and restoring of the system state, maintains mount and automount points, and implements an elaborate transactional dependency-based service control logic. It can also work as a drop-in replacement for sysvinit. Security Fix(es): * systemd: services with DynamicUser can create SUID/SGID binaries (CVE-2019-3843) * systemd: services with DynamicUser can get new privileges and create SGID binaries (CVE-2019-3844) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 8.2 Release Notes linked from the References section.",
                                "fixedby": "0:239-29.el8",
                                "link": "https://access.redhat.com/errata/RHSA-2020:1794",
                                "metadata": "null",
                                "name": "RHSA-2020:1794",
                                "namespaceName": "centos:8",
                                "severity": "Medium"
                            },
                            {
                                "description": "The systemd packages contain systemd, a system and service manager for Linux, compatible with the SysV and LSB init scripts. It provides aggressive parallelism capabilities, uses socket and D-Bus activation for starting services, offers on-demand starting of daemons, and keeps track of processes using Linux cgroups. In addition, it supports snapshotting and restoring of the system state, maintains mount and automount points, and implements an elaborate transactional dependency-based service control logic. It can also work as a drop-in replacement for sysvinit. Security Fix(es): * systemd: use-after-free when asynchronous polkit queries are performed (CVE-2020-1712) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Bug Fix(es): * systemd: systemctl reload command breaks ordering dependencies between units (BZ#1781712)",
                                "fixedby": "0:239-18.el8_1.4",
                                "link": "https://access.redhat.com/errata/RHSA-2020:0575",
                                "metadata": "null",
                                "name": "RHSA-2020:0575",
                                "namespaceName": "centos:8",
                                "severity": "High"
                            }
                        ]
                    },
                    {
                        "name": "curl",
                        "namespaceName": "centos:8",
                        "version": "7.61.1-11.el8",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "The curl packages provide the libcurl library and the curl utility for downloading files from servers using various protocols, including HTTP, FTP, and LDAP. Security Fix(es): * curl: double free due to subsequent call of realloc() (CVE-2019-5481) * curl: heap buffer overflow in function tftp_receive_packet() (CVE-2019-5482) * curl: TFTP receive heap buffer overflow in tftp_receive_packet() function (CVE-2019-5436) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 8.2 Release Notes linked from the References section.",
                                "fixedby": "0:7.61.1-12.el8",
                                "link": "https://access.redhat.com/errata/RHSA-2020:1792",
                                "metadata": "null",
                                "name": "RHSA-2020:1792",
                                "namespaceName": "centos:8",
                                "severity": "Medium"
                            }
                        ]
                    },
                    {
                        "name": "glibc-minimal-langpack",
                        "namespaceName": "centos:8",
                        "version": "2.28-72.el8",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "The glibc packages provide the standard C libraries (libc), POSIX thread libraries (libpthread), standard math libraries (libm), and the name service cache daemon (nscd) used by multiple programs on the system. Without these libraries, the Linux system cannot function correctly. Security Fix(es): * glibc: LD_PREFER_MAP_32BIT_EXEC not ignored in setuid binaries (CVE-2019-19126) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 8.2 Release Notes linked from the References section.",
                                "fixedby": "0:2.28-101.el8",
                                "link": "https://access.redhat.com/errata/RHSA-2020:1828",
                                "metadata": "null",
                                "name": "RHSA-2020:1828",
                                "namespaceName": "centos:8",
                                "severity": "Low"
                            }
                        ]
                    },
                    {
                        "name": "python3-pip-wheel",
                        "namespaceName": "centos:8",
                        "version": "9.0.3-15.el8",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "pip is a package management system used to install and manage software packages written in Python. Many packages can be found in the Python Package Index (PyPI). pip is a recursive acronym that can stand for either \"Pip Installs Packages\" or \"Pip Installs Python\".  Security Fix(es): * python-urllib3: Cross-host redirect does not remove Authorization header allow for credential exposure (CVE-2018-20060) * python-urllib3: CRLF injection due to not encoding the '\\r\\n' sequence leading to possible attack on internal service (CVE-2019-11236) * python-urllib3: Certification mishandle when error should be thrown (CVE-2019-11324) * python-requests: Redirect from HTTPS to HTTP does not remove Authorization header (CVE-2018-18074) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 8.2 Release Notes linked from the References section.",
                                "fixedby": "0:9.0.3-16.el8",
                                "link": "https://access.redhat.com/errata/RHSA-2020:1916",
                                "metadata": "null",
                                "name": "RHSA-2020:1916",
                                "namespaceName": "centos:8",
                                "severity": "Medium"
                            }
                        ]
                    },
                    {
                        "name": "binutils",
                        "namespaceName": "centos:8",
                        "version": "2.30-58.el8.0.1",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "The binutils packages provide a collection of binary utilities for the manipulation of object code in various object file formats. It includes the ar, as, gprof, ld, nm, objcopy, objdump, ranlib, readelf, size, strings, strip, and addr2line utilities. Security Fix(es): * binutils: integer overflow leading to a SEGV in _bfd_dwarf2_find_nearest_line in dwarf2.c (CVE-2019-17451) * binutils: Improper Input Validation, Signed/Unsigned Comparison, Out-of-bounds Read in gold/fileread.cc and elfcpp/elfcpp_file.h leads to denial of service (CVE-2019-1010204) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 8.2 Release Notes linked from the References section.",
                                "fixedby": "0:2.30-73.el8",
                                "link": "https://access.redhat.com/errata/RHSA-2020:1797",
                                "metadata": "null",
                                "name": "RHSA-2020:1797",
                                "namespaceName": "centos:8",
                                "severity": "Low"
                            }
                        ]
                    },
                    {
                        "name": "systemd-libs",
                        "namespaceName": "centos:8",
                        "version": "239-18.el8_1.1",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "The systemd packages contain systemd, a system and service manager for Linux, compatible with the SysV and LSB init scripts. It provides aggressive parallelism capabilities, uses socket and D-Bus activation for starting services, offers on-demand starting of daemons, and keeps track of processes using Linux cgroups. In addition, it supports snapshotting and restoring of the system state, maintains mount and automount points, and implements an elaborate transactional dependency-based service control logic. It can also work as a drop-in replacement for sysvinit. Security Fix(es): * systemd: services with DynamicUser can create SUID/SGID binaries (CVE-2019-3843) * systemd: services with DynamicUser can get new privileges and create SGID binaries (CVE-2019-3844) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 8.2 Release Notes linked from the References section.",
                                "fixedby": "0:239-29.el8",
                                "link": "https://access.redhat.com/errata/RHSA-2020:1794",
                                "metadata": "null",
                                "name": "RHSA-2020:1794",
                                "namespaceName": "centos:8",
                                "severity": "Medium"
                            },
                            {
                                "description": "The systemd packages contain systemd, a system and service manager for Linux, compatible with the SysV and LSB init scripts. It provides aggressive parallelism capabilities, uses socket and D-Bus activation for starting services, offers on-demand starting of daemons, and keeps track of processes using Linux cgroups. In addition, it supports snapshotting and restoring of the system state, maintains mount and automount points, and implements an elaborate transactional dependency-based service control logic. It can also work as a drop-in replacement for sysvinit. Security Fix(es): * systemd: use-after-free when asynchronous polkit queries are performed (CVE-2020-1712) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Bug Fix(es): * systemd: systemctl reload command breaks ordering dependencies between units (BZ#1781712)",
                                "fixedby": "0:239-18.el8_1.4",
                                "link": "https://access.redhat.com/errata/RHSA-2020:0575",
                                "metadata": "null",
                                "name": "RHSA-2020:0575",
                                "namespaceName": "centos:8",
                                "severity": "High"
                            }
                        ]
                    },
                    {
                        "name": "systemd",
                        "namespaceName": "centos:8",
                        "version": "239-18.el8_1.1",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "The systemd packages contain systemd, a system and service manager for Linux, compatible with the SysV and LSB init scripts. It provides aggressive parallelism capabilities, uses socket and D-Bus activation for starting services, offers on-demand starting of daemons, and keeps track of processes using Linux cgroups. In addition, it supports snapshotting and restoring of the system state, maintains mount and automount points, and implements an elaborate transactional dependency-based service control logic. It can also work as a drop-in replacement for sysvinit. Security Fix(es): * systemd: services with DynamicUser can create SUID/SGID binaries (CVE-2019-3843) * systemd: services with DynamicUser can get new privileges and create SGID binaries (CVE-2019-3844) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 8.2 Release Notes linked from the References section.",
                                "fixedby": "0:239-29.el8",
                                "link": "https://access.redhat.com/errata/RHSA-2020:1794",
                                "metadata": "null",
                                "name": "RHSA-2020:1794",
                                "namespaceName": "centos:8",
                                "severity": "Medium"
                            },
                            {
                                "description": "The systemd packages contain systemd, a system and service manager for Linux, compatible with the SysV and LSB init scripts. It provides aggressive parallelism capabilities, uses socket and D-Bus activation for starting services, offers on-demand starting of daemons, and keeps track of processes using Linux cgroups. In addition, it supports snapshotting and restoring of the system state, maintains mount and automount points, and implements an elaborate transactional dependency-based service control logic. It can also work as a drop-in replacement for sysvinit. Security Fix(es): * systemd: use-after-free when asynchronous polkit queries are performed (CVE-2020-1712) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Bug Fix(es): * systemd: systemctl reload command breaks ordering dependencies between units (BZ#1781712)",
                                "fixedby": "0:239-18.el8_1.4",
                                "link": "https://access.redhat.com/errata/RHSA-2020:0575",
                                "metadata": "null",
                                "name": "RHSA-2020:0575",
                                "namespaceName": "centos:8",
                                "severity": "High"
                            }
                        ]
                    },
                    {
                        "name": "gnutls",
                        "namespaceName": "centos:8",
                        "version": "3.6.8-8.el8",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "The gnutls packages provide the GNU Transport Layer Security (GnuTLS) library, which implements cryptographic algorithms and protocols such as SSL, TLS, and DTLS. Security Fix(es): * gnutls: DTLS client hello contains a random value of all zeroes (CVE-2020-11501) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section.",
                                "fixedby": "0:3.6.8-10.el8_2",
                                "link": "https://access.redhat.com/errata/RHSA-2020:1998",
                                "metadata": "null",
                                "name": "RHSA-2020:1998",
                                "namespaceName": "centos:8",
                                "severity": "Medium"
                            }
                        ]
                    },
                    {
                        "name": "glib2",
                        "namespaceName": "centos:8",
                        "version": "2.56.4-7.el8",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "GLib provides the core application building blocks for libraries and applications written in C. It provides the core object system used in GNOME, the main loop implementation, and a large set of utility functions for strings and common data structures. The Intelligent Input Bus (IBus) is an input method framework for multilingual input in Unix-like operating systems. Security Fix(es): * ibus: missing authorization allows local attacker to access the input bus of another user (CVE-2019-14822) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 8.2 Release Notes linked from the References section.",
                                "fixedby": "0:2.56.4-8.el8",
                                "link": "https://access.redhat.com/errata/RHSA-2020:1880",
                                "metadata": "null",
                                "name": "RHSA-2020:1880",
                                "namespaceName": "centos:8",
                                "severity": "Medium"
                            }
                        ]
                    },
                    {
                        "name": "libarchive",
                        "namespaceName": "centos:8",
                        "version": "3.3.2-7.el8",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "The libarchive programming library can create and read several different streaming archive formats, including GNU tar, cpio, and ISO 9660 CD-ROM images. Libarchive is used notably in the bsdtar utility, scripting language bindings such as python-libarchive, and several popular desktop file managers. Security Fix(es): * libarchive: use-after-free in archive_read_format_rar_read_data when there is an error in the decompression of an archive entry (CVE-2019-18408) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section.",
                                "fixedby": "0:3.3.2-8.el8_1",
                                "link": "https://access.redhat.com/errata/RHSA-2020:0271",
                                "metadata": "null",
                                "name": "RHSA-2020:0271",
                                "namespaceName": "centos:8",
                                "severity": "High"
                            }
                        ]
                    },
                    {
                        "name": "glibc",
                        "namespaceName": "centos:8",
                        "version": "2.28-72.el8",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "The glibc packages provide the standard C libraries (libc), POSIX thread libraries (libpthread), standard math libraries (libm), and the name service cache daemon (nscd) used by multiple programs on the system. Without these libraries, the Linux system cannot function correctly. Security Fix(es): * glibc: LD_PREFER_MAP_32BIT_EXEC not ignored in setuid binaries (CVE-2019-19126) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 8.2 Release Notes linked from the References section.",
                                "fixedby": "0:2.28-101.el8",
                                "link": "https://access.redhat.com/errata/RHSA-2020:1828",
                                "metadata": "null",
                                "name": "RHSA-2020:1828",
                                "namespaceName": "centos:8",
                                "severity": "Low"
                            }
                        ]
                    },
                    {
                        "name": "platform-python",
                        "namespaceName": "centos:8",
                        "version": "3.6.8-15.1.el8",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "Python is an interpreted, interactive, object-oriented programming language, which includes modules, classes, exceptions, very high level dynamic data types and dynamic typing. Python supports interfaces to many system calls and libraries, as well as to various windowing systems.  Security Fix(es): * python: Cookie domain check returns incorrect results (CVE-2018-20852) * python: email.utils.parseaddr wrongly parses email addresses (CVE-2019-16056) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 8.2 Release Notes linked from the References section.",
                                "fixedby": "0:3.6.8-23.el8",
                                "link": "https://access.redhat.com/errata/RHSA-2020:1764",
                                "metadata": "null",
                                "name": "RHSA-2020:1764",
                                "namespaceName": "centos:8",
                                "severity": "Medium"
                            }
                        ]
                    },
                    {
                        "name": "bind-export-libs",
                        "namespaceName": "centos:8",
                        "version": "32:9.11.4-26.P2.el8",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "The Berkeley Internet Name Domain (BIND) is an implementation of the Domain Name System (DNS) protocols. BIND includes a DNS server (named); a resolver library (routines for applications to use when interfacing with DNS); and tools for verifying that the DNS server is operating correctly. The following packages have been upgraded to a later upstream version: bind (9.11.13). (BZ#1704328) Security Fix(es): * bind: TCP Pipelining doesn't limit TCP clients on a single connection (CVE-2019-6477) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 8.2 Release Notes linked from the References section.",
                                "fixedby": "32:9.11.13-3.el8",
                                "link": "https://access.redhat.com/errata/RHSA-2020:1845",
                                "metadata": "null",
                                "name": "RHSA-2020:1845",
                                "namespaceName": "centos:8",
                                "severity": "Medium"
                            }
                        ]
                    },
                    {
                        "name": "glibc-common",
                        "namespaceName": "centos:8",
                        "version": "2.28-72.el8",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "The glibc packages provide the standard C libraries (libc), POSIX thread libraries (libpthread), standard math libraries (libm), and the name service cache daemon (nscd) used by multiple programs on the system. Without these libraries, the Linux system cannot function correctly. Security Fix(es): * glibc: LD_PREFER_MAP_32BIT_EXEC not ignored in setuid binaries (CVE-2019-19126) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 8.2 Release Notes linked from the References section.",
                                "fixedby": "0:2.28-101.el8",
                                "link": "https://access.redhat.com/errata/RHSA-2020:1828",
                                "metadata": "null",
                                "name": "RHSA-2020:1828",
                                "namespaceName": "centos:8",
                                "severity": "Low"
                            }
                        ]
                    },
                    {
                        "name": "systemd-pam",
                        "namespaceName": "centos:8",
                        "version": "239-18.el8_1.1",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "The systemd packages contain systemd, a system and service manager for Linux, compatible with the SysV and LSB init scripts. It provides aggressive parallelism capabilities, uses socket and D-Bus activation for starting services, offers on-demand starting of daemons, and keeps track of processes using Linux cgroups. In addition, it supports snapshotting and restoring of the system state, maintains mount and automount points, and implements an elaborate transactional dependency-based service control logic. It can also work as a drop-in replacement for sysvinit. Security Fix(es): * systemd: services with DynamicUser can create SUID/SGID binaries (CVE-2019-3843) * systemd: services with DynamicUser can get new privileges and create SGID binaries (CVE-2019-3844) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 8.2 Release Notes linked from the References section.",
                                "fixedby": "0:239-29.el8",
                                "link": "https://access.redhat.com/errata/RHSA-2020:1794",
                                "metadata": "null",
                                "name": "RHSA-2020:1794",
                                "namespaceName": "centos:8",
                                "severity": "Medium"
                            },
                            {
                                "description": "The systemd packages contain systemd, a system and service manager for Linux, compatible with the SysV and LSB init scripts. It provides aggressive parallelism capabilities, uses socket and D-Bus activation for starting services, offers on-demand starting of daemons, and keeps track of processes using Linux cgroups. In addition, it supports snapshotting and restoring of the system state, maintains mount and automount points, and implements an elaborate transactional dependency-based service control logic. It can also work as a drop-in replacement for sysvinit. Security Fix(es): * systemd: use-after-free when asynchronous polkit queries are performed (CVE-2020-1712) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Bug Fix(es): * systemd: systemctl reload command breaks ordering dependencies between units (BZ#1781712)",
                                "fixedby": "0:239-18.el8_1.4",
                                "link": "https://access.redhat.com/errata/RHSA-2020:0575",
                                "metadata": "null",
                                "name": "RHSA-2020:0575",
                                "namespaceName": "centos:8",
                                "severity": "High"
                            }
                        ]
                    },
                    {
                        "name": "openssl-libs",
                        "namespaceName": "centos:8",
                        "version": "1:1.1.1c-2.el8",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "OpenSSL is a toolkit that implements the Secure Sockets Layer (SSL) and Transport Layer Security (TLS) protocols, as well as a full-strength general-purpose cryptography library. Security Fix(es): * openssl: side-channel weak encryption vulnerability (CVE-2019-1547) * openssl: information disclosure in fork() (CVE-2019-1549) * openssl: information disclosure in PKCS7_dataDecode and CMS_decrypt_set1_pkey (CVE-2019-1563) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 8.2 Release Notes linked from the References section.",
                                "fixedby": "1:1.1.1c-15.el8",
                                "link": "https://access.redhat.com/errata/RHSA-2020:1840",
                                "metadata": "null",
                                "name": "RHSA-2020:1840",
                                "namespaceName": "centos:8",
                                "severity": "Medium"
                            }
                        ]
                    },
                    {
                        "name": "libxml2",
                        "namespaceName": "centos:8",
                        "version": "2.9.7-5.el8",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "The libxml2 library is a development toolbox providing the implementation of various XML standards. Security Fix(es): * libxml2: NULL pointer dereference in xmlXPathCompOpEval() function in xpath.c (CVE-2018-14404) * libxml2: infinite loop in xz_decomp function in xzlib.c (CVE-2018-9251) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 8.2 Release Notes linked from the References section.",
                                "fixedby": "0:2.9.7-7.el8",
                                "link": "https://access.redhat.com/errata/RHSA-2020:1827",
                                "metadata": "null",
                                "name": "RHSA-2020:1827",
                                "namespaceName": "centos:8",
                                "severity": "Medium"
                            }
                        ]
                    },
                    {
                        "name": "libcurl-minimal",
                        "namespaceName": "centos:8",
                        "version": "7.61.1-11.el8",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "The curl packages provide the libcurl library and the curl utility for downloading files from servers using various protocols, including HTTP, FTP, and LDAP. Security Fix(es): * curl: double free due to subsequent call of realloc() (CVE-2019-5481) * curl: heap buffer overflow in function tftp_receive_packet() (CVE-2019-5482) * curl: TFTP receive heap buffer overflow in tftp_receive_packet() function (CVE-2019-5436) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 8.2 Release Notes linked from the References section.",
                                "fixedby": "0:7.61.1-12.el8",
                                "link": "https://access.redhat.com/errata/RHSA-2020:1792",
                                "metadata": "null",
                                "name": "RHSA-2020:1792",
                                "namespaceName": "centos:8",
                                "severity": "Medium"
                            }
                        ]
                    },
                    {
                        "name": "libgcc",
                        "namespaceName": "centos:8",
                        "version": "8.3.1-4.5.el8",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "The gcc packages provide compilers for C, C++, Java, Fortran, Objective C, and Ada 95 GNU, as well as related support libraries. Security Fix(es): * gcc: POWER9 \"DARN\" RNG intrinsic produces repeated output (CVE-2019-15847) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 8.2 Release Notes linked from the References section.",
                                "fixedby": "0:8.3.1-5.el8",
                                "link": "https://access.redhat.com/errata/RHSA-2020:1864",
                                "metadata": "null",
                                "name": "RHSA-2020:1864",
                                "namespaceName": "centos:8",
                                "severity": "Medium"
                            }
                        ]
                    }
                ],
                "image": "quay.io/app-sre/centos",
                "manifest": "sha256:9e0c275e0bcb495773b10a18e499985d782810e47b4fce076422acb4bc3da3dd"
            },
            "status": {
                "affectedPods": {
                    "cso/sleep-6f84df5847-4bn9p": [
                        "cri-o://930f7f496a479adfbc626f2008d242dda1aae4141cbb7b474449bc3833511acf",
                        "cri-o://9082983cb6ef4830013d1e2acd3b5299a1d282d893e3ce65111655f562b37535"
                    ],
                    "cso/sleep-6f84df5847-bctxz": [
                        "cri-o://fdee7a36879063dbf7230f95ef62cbc2ab7757995455011bc822958192fb63c2",
                        "cri-o://95c7afc839f6ec0c8e12dc869837fc04ddca473913d214b3b097a33503f51a6f"
                    ],
                    "cso/sleep-6f84df5847-dh9l8": [
                        "cri-o://9f9ffae372345e7f41289579383253a8175ce57ff9e52e13ee5f19f764bf5cb5",
                        "cri-o://4083bcd52a9254d8ee5751e0b0b5929f7a22a0fc607eb4f05d905ed6a0770d02"
                    ]
                },
                "fixableCount": 30,
                "highCount": 7,
                "highestSeverity": "High",
                "lastUpdate": "2020-05-22 16:01:50.344204207 +0000 UTC",
                "lowCount": 4,
                "mediumCount": 19
            }
        },
        {
            "apiVersion": "secscan.quay.redhat.com/v1alpha1",
            "kind": "ImageManifestVuln",
            "metadata": {
                "creationTimestamp": "2020-05-20T14:42:03Z",
                "generation": 40,
                "labels": {
                    "cso/sleep2-65844c6b58-2q2s5": "true",
                    "cso/sleep2-65844c6b58-qlng8": "true"
                },
                "name": "sha256.a42f741b046c974973052d2453ecbb672b62d4c45ead2eda69b3c43d3763abf9",
                "namespace": "cso",
                "resourceVersion": "928985",
                "selfLink": "/apis/secscan.quay.redhat.com/v1alpha1/namespaces/cso/imagemanifestvulns/sha256.a42f741b046c974973052d2453ecbb672b62d4c45ead2eda69b3c43d3763abf9",
                "uid": "b5b86eff-6ea7-4029-9f01-87a8cf205650"
            },
            "spec": {
                "features": [
                    {
                        "name": "util-linux",
                        "namespaceName": "centos:7",
                        "version": "2.23.2-33.el7",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "The util-linux packages contain a large variety of low-level system utilities that are necessary for a Linux system to function. Among others, these include the fdisk configuration tool and the login program. Security Fix(es): * A race condition was found in the way su handled the management of child processes. A local authenticated attacker could use this flaw to kill other processes with root privileges under specific conditions. (CVE-2017-2616) Red Hat would like to thank Tobias Stöckmann for reporting this issue. Bug Fix(es): * The \"findmnt --target \u003cpath\u003e\" command prints all file systems where the mount point directory is \u003cpath\u003e. Previously, when used in the chroot environment, \"findmnt --target \u003cpath\u003e\" incorrectly displayed all mount points. The command has been fixed so that it now checks the mount point path and returns information only for the relevant mount point. (BZ#1414481)",
                                "fixedby": "0:2.23.2-33.el7_3.2",
                                "link": "https://access.redhat.com/errata/RHSA-2017:0907",
                                "metadata": "null",
                                "name": "RHSA-2017:0907",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            }
                        ]
                    },
                    {
                        "name": "glib2",
                        "namespaceName": "centos:7",
                        "version": "2.46.2-4.el7",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "GNOME is the default desktop environment of Red Hat Enterprise Linux. For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.7 Release Notes linked from the References section. Users of gnome are advised to upgrade to these updated packages.",
                                "fixedby": "0:2.56.1-5.el7",
                                "link": "https://access.redhat.com/errata/RHBA-2019:2044",
                                "metadata": "null",
                                "name": "RHBA-2019:2044",
                                "namespaceName": "centos:7",
                                "severity": "Unknown"
                            },
                            {
                                "description": "GNOME is the default desktop environment of Red Hat Enterprise Linux. Security Fix(es): * libsoup: Crash in soup_cookie_jar.c:get_cookies() on empty hostnames (CVE-2018-12910) * poppler: Infinite recursion in fofi/FoFiType1C.cc:FoFiType1C::cvtGlyph() function allows denial of service (CVE-2017-18267) * libgxps: heap based buffer over read in ft_font_face_hash function of gxps-fonts.c (CVE-2018-10733) * libgxps: Stack-based buffer overflow in calling glib in gxps_images_guess_content_type of gcontenttype.c (CVE-2018-10767) * poppler: NULL pointer dereference in Annot.h:AnnotPath::getCoordsLength() allows for denial of service via crafted PDF (CVE-2018-10768) * poppler: out of bounds read in pdfunite (CVE-2018-13988) For more details about the security issue(s), including the impact, a CVSS score, and other related information, refer to the CVE page(s) listed in the References section. Red Hat would like to thank chenyuan (NESA Lab) for reporting CVE-2018-10733 and CVE-2018-10767 and Hosein Askari for reporting CVE-2018-13988. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.6 Release Notes linked from the References section.",
                                "fixedby": "0:2.56.1-2.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2018:3140",
                                "metadata": "null",
                                "name": "RHSA-2018:3140",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            }
                        ]
                    },
                    {
                        "name": "libxml2",
                        "namespaceName": "centos:7",
                        "version": "2.9.1-6.el7_2.3",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "The libxml2 library is a development toolbox providing the implementation of various XML standards. Security Fix(es): * libxml2: Use after free triggered by XPointer paths beginning with range-to (CVE-2016-5131) * libxml2: Use after free in xmlXPathCompOpEvalPositionalPredicate() function in xpath.c (CVE-2017-15412) * libxml2: DoS caused by incorrect error detection during XZ decompression (CVE-2015-8035) * libxml2: NULL pointer dereference in xmlXPathCompOpEval() function in xpath.c (CVE-2018-14404) * libxml2: Unrestricted memory usage in xz_head() function in xzlib.c (CVE-2017-18258) * libxml2: Infinite loop caused by incorrect error detection during LZMA decompression (CVE-2018-14567) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.8 Release Notes linked from the References section.",
                                "fixedby": "0:2.9.1-6.el7.4",
                                "link": "https://access.redhat.com/errata/RHSA-2020:1190",
                                "metadata": "null",
                                "name": "RHSA-2020:1190",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            }
                        ]
                    },
                    {
                        "name": "libgcc",
                        "namespaceName": "centos:7",
                        "version": "4.8.5-11.el7",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "The gcc packages provide compilers for C, C++, Java, Fortran, Objective C, and Ada 95 GNU, as well as related support libraries. Security Fix(es): * gcc: GCC generates incorrect code for RDRAND/RDSEED intrinsics (CVE-2017-11671) For more details about the security issue(s), including the impact, a CVSS score, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.5 Release Notes linked from the References section.",
                                "fixedby": "0:4.8.5-28.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2018:0849",
                                "metadata": "null",
                                "name": "RHSA-2018:0849",
                                "namespaceName": "centos:7",
                                "severity": "Low"
                            }
                        ]
                    },
                    {
                        "name": "procps-ng",
                        "namespaceName": "centos:7",
                        "version": "3.3.10-10.el7",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "The procps-ng packages contain a set of system utilities that provide system information, including ps, free, skill, pkill, pgrep, snice, tload, top, uptime, vmstat, w, watch, and pwdx. Security Fix(es): * procps-ng, procps: Integer overflows leading to heap overflow in file2strvec (CVE-2018-1124) * procps-ng, procps: incorrect integer size in proc/alloc.* leading to truncation / integer overflow issues (CVE-2018-1126) For more details about the security issue(s), including the impact, a CVSS score, and other related information, refer to the CVE page(s) listed in the References section. Red Hat would like to thank Qualys Research Labs for reporting these issues.",
                                "fixedby": "0:3.3.10-17.el7_5.2",
                                "link": "https://access.redhat.com/errata/RHSA-2018:1700",
                                "metadata": "null",
                                "name": "RHSA-2018:1700",
                                "namespaceName": "centos:7",
                                "severity": "High"
                            },
                            {
                                "description": "The procps-ng packages contain a set of system utilities that provide system information, including ps, free, skill, pkill, pgrep, snice, tload, top, uptime, vmstat, w, watch, and pwdx. Security Fix(es): * procps-ng, procps: Local privilege escalation in top (CVE-2018-1122) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.7 Release Notes linked from the References section.",
                                "fixedby": "0:3.3.10-26.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2019:2189",
                                "metadata": "null",
                                "name": "RHSA-2019:2189",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            }
                        ]
                    },
                    {
                        "name": "systemd-libs",
                        "namespaceName": "centos:7",
                        "version": "219-30.el7_3.6",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "The systemd packages contain systemd, a system and service manager for Linux, compatible with the SysV and LSB init scripts. It provides aggressive parallelism capabilities, uses socket and D-Bus activation for starting services, offers on-demand starting of daemons, and keeps track of processes using Linux cgroups. In addition, it supports snapshotting and restoring of the system state, maintains mount and automount points, and implements an elaborate transactional dependency-based service control logic. It can also work as a drop-in replacement for sysvinit. Security Fix(es): * A race condition was found in systemd. This could result in automount requests not being serviced and processes using them could hang, causing denial of service. (CVE-2018-1049)",
                                "fixedby": "0:219-42.el7_4.7",
                                "link": "https://access.redhat.com/errata/RHSA-2018:0260",
                                "metadata": "null",
                                "name": "RHSA-2018:0260",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            },
                            {
                                "description": "The systemd packages contain systemd, a system and service manager for Linux, compatible with the SysV and LSB init scripts. It provides aggressive parallelism capabilities, uses socket and D-Bus activation for starting services, offers on-demand starting of daemons, and keeps track of processes using Linux cgroups. In addition, it supports snapshotting and restoring of the system state, maintains mount and automount points, and implements an elaborate transactional dependency-based service control logic. It can also work as a drop-in replacement for sysvinit. Security Fix(es): * systemd: Insufficient input validation in bus_process_object() resulting in PID 1 crash (CVE-2019-6454) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section.",
                                "fixedby": "0:219-62.el7_6.5",
                                "link": "https://access.redhat.com/errata/RHSA-2019:0368",
                                "metadata": "null",
                                "name": "RHSA-2019:0368",
                                "namespaceName": "centos:7",
                                "severity": "High"
                            },
                            {
                                "description": "The systemd packages contain systemd, a system and service manager for Linux, compatible with the SysV and LSB init scripts. It provides aggressive parallelism capabilities, uses socket and D-Bus activation for starting services, offers on-demand starting of daemons, and keeps track of processes using Linux cgroups. In addition, it supports snapshotting and restoring of the system state, maintains mount and automount points, and implements an elaborate transactional dependency-based service control logic. It can also work as a drop-in replacement for sysvinit. Security Fix(es): * systemd: Out-of-bounds heap write in systemd-networkd dhcpv6 option handling (CVE-2018-15688) * systemd: stack overflow when calling syslog from a command with long cmdline (CVE-2018-16864) * systemd: stack overflow when receiving many journald entries (CVE-2018-16865) For more details about the security issue(s), including the impact, a CVSS score, and other related information, refer to the CVE page(s) listed in the References section. Red Hat would like to thank Ubuntu Security Team for reporting CVE-2018-15688 and Qualys Research Labs for reporting CVE-2018-16864 and CVE-2018-16865. Upstream acknowledges Felix Wilhelm (Google) as the original reporter of CVE-2018-15688.",
                                "fixedby": "0:219-62.el7_6.2",
                                "link": "https://access.redhat.com/errata/RHSA-2019:0049",
                                "metadata": "null",
                                "name": "RHSA-2019:0049",
                                "namespaceName": "centos:7",
                                "severity": "High"
                            },
                            {
                                "description": "The systemd packages contain systemd, a system and service manager for Linux, compatible with the SysV and LSB init scripts. It provides aggressive parallelism capabilities, uses socket and D-Bus activation for starting services, offers on-demand starting of daemons, and keeps track of processes using Linux cgroups. In addition, it supports snapshotting and restoring of the system state, maintains mount and automount points, and implements an elaborate transactional dependency-based service control logic. It can also work as a drop-in replacement for sysvinit. Security Fix(es): * systemd: memory leak in journald-server.c introduced by fix for CVE-2018-16864 (CVE-2019-3815) For more details about the security issue(s), including the impact, a CVSS score, and other related information, refer to the CVE page(s) listed in the References section.",
                                "fixedby": "0:219-62.el7_6.3",
                                "link": "https://access.redhat.com/errata/RHSA-2019:0201",
                                "metadata": "null",
                                "name": "RHSA-2019:0201",
                                "namespaceName": "centos:7",
                                "severity": "Low"
                            },
                            {
                                "description": "The systemd packages contain systemd, a system and service manager for Linux, compatible with the SysV and LSB init scripts. It provides aggressive parallelism capabilities, uses socket and D-Bus activation for starting services, offers on-demand starting of daemons, and keeps track of processes using Linux cgroups. In addition, it supports snapshotting and restoring of the system state, maintains mount and automount points, and implements an elaborate transactional dependency-based service control logic. It can also work as a drop-in replacement for sysvinit. Security Fix(es): * systemd: line splitting via fgets() allows for state injection during daemon-reexec (CVE-2018-15686) * systemd: out-of-bounds read when parsing a crafted syslog message (CVE-2018-16866) * systemd: kills privileged process if unprivileged PIDFile was tampered (CVE-2018-16888) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.7 Release Notes linked from the References section.",
                                "fixedby": "0:219-67.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2019:2091",
                                "metadata": "null",
                                "name": "RHSA-2019:2091",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            }
                        ]
                    },
                    {
                        "name": "curl",
                        "namespaceName": "centos:7",
                        "version": "7.29.0-35.el7.centos",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "The curl packages provide the libcurl library and the curl utility for downloading files from servers using various protocols, including HTTP, FTP, and LDAP. Security Fix(es): * A buffer overrun flaw was found in the IMAP handler of libcurl. By tricking an unsuspecting user into connecting to a malicious IMAP server, an attacker could exploit this flaw to potentially cause information disclosure or crash the application. (CVE-2017-1000257) Red Hat would like to thank the Curl project for reporting this issue. Upstream acknowledges Brian Carpenter and the OSS-Fuzz project as the original reporters.",
                                "fixedby": "0:7.29.0-42.el7_4.1",
                                "link": "https://access.redhat.com/errata/RHSA-2017:3263",
                                "metadata": "null",
                                "name": "RHSA-2017:3263",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            },
                            {
                                "description": "The curl packages provide the libcurl library and the curl utility for downloading files from servers using various protocols, including HTTP, FTP, and LDAP. Security Fix(es): * curl: NTLM password overflow via integer overflow (CVE-2018-14618) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Bug Fix(es): * baseurl with file:// hangs and then timeout in yum repo (BZ#1709474) * curl crashes on http links with rate-limit (BZ#1711914)",
                                "fixedby": "0:7.29.0-51.el7_6.3",
                                "link": "https://access.redhat.com/errata/RHSA-2019:1880",
                                "metadata": "null",
                                "name": "RHSA-2019:1880",
                                "namespaceName": "centos:7",
                                "severity": "Low"
                            },
                            {
                                "description": "The curl packages provide the libcurl library and the curl utility for downloading files from servers using various protocols, including HTTP, FTP, and LDAP. Security Fix(es): * curl: Heap-based buffer over-read in the curl tool warning formatting (CVE-2018-16842) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.7 Release Notes linked from the References section.",
                                "fixedby": "0:7.29.0-54.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2019:2181",
                                "metadata": "null",
                                "name": "RHSA-2019:2181",
                                "namespaceName": "centos:7",
                                "severity": "Low"
                            },
                            {
                                "description": "The curl packages provide the libcurl library and the curl utility for downloading files from servers using various protocols, including HTTP, FTP, and LDAP. Security Fix(es): * curl: TFTP receive heap buffer overflow in tftp_receive_packet() function (CVE-2019-5436) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.8 Release Notes linked from the References section.",
                                "fixedby": "0:7.29.0-57.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2020:1020",
                                "metadata": "null",
                                "name": "RHSA-2020:1020",
                                "namespaceName": "centos:7",
                                "severity": "Low"
                            },
                            {
                                "description": "The curl packages provide the libcurl library and the curl utility for downloading files from servers using various protocols, including HTTP, FTP, and LDAP. Security Fix(es): * Multiple integer overflow flaws leading to heap-based buffer overflows were found in the way curl handled escaping and unescaping of data. An attacker could potentially use these flaws to crash an application using libcurl by sending a specially crafted input to the affected libcurl functions. (CVE-2016-7167) Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.4 Release Notes linked from the References section.",
                                "fixedby": "0:7.29.0-42.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2017:2016",
                                "metadata": "null",
                                "name": "RHSA-2017:2016",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            },
                            {
                                "description": "The curl packages provide the libcurl library and the curl utility for downloading files from servers using various protocols, including HTTP, FTP, and LDAP. The nss-pem package provides the PEM file reader for Network Security Services (NSS) implemented as a PKCS#11 module. Security Fix(es): * curl: HTTP authentication leak in redirects (CVE-2018-1000007) * curl: FTP path trickery leads to NIL byte out of bounds write (CVE-2018-1000120) * curl: RTSP RTP buffer over-read (CVE-2018-1000122) * curl: Out-of-bounds heap read when missing RTSP headers allows information leak of denial of service (CVE-2018-1000301) * curl: LDAP NULL pointer dereference (CVE-2018-1000121) For more details about the security issue(s), including the impact, a CVSS score, and other related information, refer to the CVE page(s) listed in the References section. Red Hat would like to thank the Curl project for reporting these issues. Upstream acknowledges Craig de Stigter as the original reporter of CVE-2018-1000007; Duy Phan Thanh as the original reporter of CVE-2018-1000120; Max Dymond as the original reporter of CVE-2018-1000122; the OSS-fuzz project as the original reporter of CVE-2018-1000301; and Dario Weisser as the original reporter of CVE-2018-1000121. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.6 Release Notes linked from the References section.",
                                "fixedby": "0:7.29.0-51.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2018:3157",
                                "metadata": "null",
                                "name": "RHSA-2018:3157",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            }
                        ]
                    },
                    {
                        "name": "gnupg2",
                        "namespaceName": "centos:7",
                        "version": "2.0.22-4.el7",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "The GNU Privacy Guard (GnuPG or GPG) is a tool for encrypting data and creating digital signatures, compliant with OpenPGP and S/MIME standards. Security Fix(es): * gnupg2: Improper sanitization of filenames allows for the display of fake status messages and the bypass of signature verification (CVE-2018-12020) For more details about the security issue(s), including the impact, a CVSS score, and other related information, refer to the CVE page(s) listed in the References section.",
                                "fixedby": "0:2.0.22-5.el7_5",
                                "link": "https://access.redhat.com/errata/RHSA-2018:2181",
                                "metadata": "null",
                                "name": "RHSA-2018:2181",
                                "namespaceName": "centos:7",
                                "severity": "High"
                            }
                        ]
                    },
                    {
                        "name": "libcurl",
                        "namespaceName": "centos:7",
                        "version": "7.29.0-35.el7.centos",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "The curl packages provide the libcurl library and the curl utility for downloading files from servers using various protocols, including HTTP, FTP, and LDAP. Security Fix(es): * A buffer overrun flaw was found in the IMAP handler of libcurl. By tricking an unsuspecting user into connecting to a malicious IMAP server, an attacker could exploit this flaw to potentially cause information disclosure or crash the application. (CVE-2017-1000257) Red Hat would like to thank the Curl project for reporting this issue. Upstream acknowledges Brian Carpenter and the OSS-Fuzz project as the original reporters.",
                                "fixedby": "0:7.29.0-42.el7_4.1",
                                "link": "https://access.redhat.com/errata/RHSA-2017:3263",
                                "metadata": "null",
                                "name": "RHSA-2017:3263",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            },
                            {
                                "description": "The curl packages provide the libcurl library and the curl utility for downloading files from servers using various protocols, including HTTP, FTP, and LDAP. Security Fix(es): * curl: NTLM password overflow via integer overflow (CVE-2018-14618) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Bug Fix(es): * baseurl with file:// hangs and then timeout in yum repo (BZ#1709474) * curl crashes on http links with rate-limit (BZ#1711914)",
                                "fixedby": "0:7.29.0-51.el7_6.3",
                                "link": "https://access.redhat.com/errata/RHSA-2019:1880",
                                "metadata": "null",
                                "name": "RHSA-2019:1880",
                                "namespaceName": "centos:7",
                                "severity": "Low"
                            },
                            {
                                "description": "The curl packages provide the libcurl library and the curl utility for downloading files from servers using various protocols, including HTTP, FTP, and LDAP. Security Fix(es): * curl: Heap-based buffer over-read in the curl tool warning formatting (CVE-2018-16842) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.7 Release Notes linked from the References section.",
                                "fixedby": "0:7.29.0-54.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2019:2181",
                                "metadata": "null",
                                "name": "RHSA-2019:2181",
                                "namespaceName": "centos:7",
                                "severity": "Low"
                            },
                            {
                                "description": "The curl packages provide the libcurl library and the curl utility for downloading files from servers using various protocols, including HTTP, FTP, and LDAP. Security Fix(es): * curl: TFTP receive heap buffer overflow in tftp_receive_packet() function (CVE-2019-5436) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.8 Release Notes linked from the References section.",
                                "fixedby": "0:7.29.0-57.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2020:1020",
                                "metadata": "null",
                                "name": "RHSA-2020:1020",
                                "namespaceName": "centos:7",
                                "severity": "Low"
                            },
                            {
                                "description": "The curl packages provide the libcurl library and the curl utility for downloading files from servers using various protocols, including HTTP, FTP, and LDAP. Security Fix(es): * Multiple integer overflow flaws leading to heap-based buffer overflows were found in the way curl handled escaping and unescaping of data. An attacker could potentially use these flaws to crash an application using libcurl by sending a specially crafted input to the affected libcurl functions. (CVE-2016-7167) Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.4 Release Notes linked from the References section.",
                                "fixedby": "0:7.29.0-42.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2017:2016",
                                "metadata": "null",
                                "name": "RHSA-2017:2016",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            },
                            {
                                "description": "The curl packages provide the libcurl library and the curl utility for downloading files from servers using various protocols, including HTTP, FTP, and LDAP. The nss-pem package provides the PEM file reader for Network Security Services (NSS) implemented as a PKCS#11 module. Security Fix(es): * curl: HTTP authentication leak in redirects (CVE-2018-1000007) * curl: FTP path trickery leads to NIL byte out of bounds write (CVE-2018-1000120) * curl: RTSP RTP buffer over-read (CVE-2018-1000122) * curl: Out-of-bounds heap read when missing RTSP headers allows information leak of denial of service (CVE-2018-1000301) * curl: LDAP NULL pointer dereference (CVE-2018-1000121) For more details about the security issue(s), including the impact, a CVSS score, and other related information, refer to the CVE page(s) listed in the References section. Red Hat would like to thank the Curl project for reporting these issues. Upstream acknowledges Craig de Stigter as the original reporter of CVE-2018-1000007; Duy Phan Thanh as the original reporter of CVE-2018-1000120; Max Dymond as the original reporter of CVE-2018-1000122; the OSS-fuzz project as the original reporter of CVE-2018-1000301; and Dario Weisser as the original reporter of CVE-2018-1000121. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.6 Release Notes linked from the References section.",
                                "fixedby": "0:7.29.0-51.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2018:3157",
                                "metadata": "null",
                                "name": "RHSA-2018:3157",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            }
                        ]
                    },
                    {
                        "name": "nspr",
                        "namespaceName": "centos:7",
                        "version": "4.11.0-1.el7_2",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "Network Security Services (NSS) is a set of libraries designed to support the cross-platform development of security-enabled client and server applications. Netscape Portable Runtime (NSPR) provides platform independence for non-GUI operating system facilities. The following packages have been upgraded to a later upstream version: nss (3.44.0), nss-softokn (3.44.0), nss-util (3.44.0), nspr (4.21.0). (BZ#1645231, BZ#1692269, BZ#1692271, BZ#1692274) Security Fix(es): * ROHNP: Key Extraction Side Channel in Multiple Crypto Libraries (CVE-2018-0495) * nss: Cache side-channel variant of the Bleichenbacher attack (CVE-2018-12404) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.7 Release Notes linked from the References section.",
                                "fixedby": "0:4.21.0-1.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2019:2237",
                                "metadata": "null",
                                "name": "RHSA-2019:2237",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            }
                        ]
                    },
                    {
                        "name": "systemd",
                        "namespaceName": "centos:7",
                        "version": "219-30.el7_3.6",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "The systemd packages contain systemd, a system and service manager for Linux, compatible with the SysV and LSB init scripts. It provides aggressive parallelism capabilities, uses socket and D-Bus activation for starting services, offers on-demand starting of daemons, and keeps track of processes using Linux cgroups. In addition, it supports snapshotting and restoring of the system state, maintains mount and automount points, and implements an elaborate transactional dependency-based service control logic. It can also work as a drop-in replacement for sysvinit. Security Fix(es): * A race condition was found in systemd. This could result in automount requests not being serviced and processes using them could hang, causing denial of service. (CVE-2018-1049)",
                                "fixedby": "0:219-42.el7_4.7",
                                "link": "https://access.redhat.com/errata/RHSA-2018:0260",
                                "metadata": "null",
                                "name": "RHSA-2018:0260",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            },
                            {
                                "description": "The systemd packages contain systemd, a system and service manager for Linux, compatible with the SysV and LSB init scripts. It provides aggressive parallelism capabilities, uses socket and D-Bus activation for starting services, offers on-demand starting of daemons, and keeps track of processes using Linux cgroups. In addition, it supports snapshotting and restoring of the system state, maintains mount and automount points, and implements an elaborate transactional dependency-based service control logic. It can also work as a drop-in replacement for sysvinit. Security Fix(es): * systemd: Insufficient input validation in bus_process_object() resulting in PID 1 crash (CVE-2019-6454) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section.",
                                "fixedby": "0:219-62.el7_6.5",
                                "link": "https://access.redhat.com/errata/RHSA-2019:0368",
                                "metadata": "null",
                                "name": "RHSA-2019:0368",
                                "namespaceName": "centos:7",
                                "severity": "High"
                            },
                            {
                                "description": "The systemd packages contain systemd, a system and service manager for Linux, compatible with the SysV and LSB init scripts. It provides aggressive parallelism capabilities, uses socket and D-Bus activation for starting services, offers on-demand starting of daemons, and keeps track of processes using Linux cgroups. In addition, it supports snapshotting and restoring of the system state, maintains mount and automount points, and implements an elaborate transactional dependency-based service control logic. It can also work as a drop-in replacement for sysvinit. Security Fix(es): * systemd: Out-of-bounds heap write in systemd-networkd dhcpv6 option handling (CVE-2018-15688) * systemd: stack overflow when calling syslog from a command with long cmdline (CVE-2018-16864) * systemd: stack overflow when receiving many journald entries (CVE-2018-16865) For more details about the security issue(s), including the impact, a CVSS score, and other related information, refer to the CVE page(s) listed in the References section. Red Hat would like to thank Ubuntu Security Team for reporting CVE-2018-15688 and Qualys Research Labs for reporting CVE-2018-16864 and CVE-2018-16865. Upstream acknowledges Felix Wilhelm (Google) as the original reporter of CVE-2018-15688.",
                                "fixedby": "0:219-62.el7_6.2",
                                "link": "https://access.redhat.com/errata/RHSA-2019:0049",
                                "metadata": "null",
                                "name": "RHSA-2019:0049",
                                "namespaceName": "centos:7",
                                "severity": "High"
                            },
                            {
                                "description": "The systemd packages contain systemd, a system and service manager for Linux, compatible with the SysV and LSB init scripts. It provides aggressive parallelism capabilities, uses socket and D-Bus activation for starting services, offers on-demand starting of daemons, and keeps track of processes using Linux cgroups. In addition, it supports snapshotting and restoring of the system state, maintains mount and automount points, and implements an elaborate transactional dependency-based service control logic. It can also work as a drop-in replacement for sysvinit. Security Fix(es): * systemd: memory leak in journald-server.c introduced by fix for CVE-2018-16864 (CVE-2019-3815) For more details about the security issue(s), including the impact, a CVSS score, and other related information, refer to the CVE page(s) listed in the References section.",
                                "fixedby": "0:219-62.el7_6.3",
                                "link": "https://access.redhat.com/errata/RHSA-2019:0201",
                                "metadata": "null",
                                "name": "RHSA-2019:0201",
                                "namespaceName": "centos:7",
                                "severity": "Low"
                            },
                            {
                                "description": "The systemd packages contain systemd, a system and service manager for Linux, compatible with the SysV and LSB init scripts. It provides aggressive parallelism capabilities, uses socket and D-Bus activation for starting services, offers on-demand starting of daemons, and keeps track of processes using Linux cgroups. In addition, it supports snapshotting and restoring of the system state, maintains mount and automount points, and implements an elaborate transactional dependency-based service control logic. It can also work as a drop-in replacement for sysvinit. Security Fix(es): * systemd: line splitting via fgets() allows for state injection during daemon-reexec (CVE-2018-15686) * systemd: out-of-bounds read when parsing a crafted syslog message (CVE-2018-16866) * systemd: kills privileged process if unprivileged PIDFile was tampered (CVE-2018-16888) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.7 Release Notes linked from the References section.",
                                "fixedby": "0:219-67.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2019:2091",
                                "metadata": "null",
                                "name": "RHSA-2019:2091",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            }
                        ]
                    },
                    {
                        "name": "yum-plugin-fastestmirror",
                        "namespaceName": "centos:7",
                        "version": "1.1.31-40.el7",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "The yum-utils packages provide a collection of utilities and examples for the yum package manager to make yum easier and more powerful to use. Security Fix(es): * yum-utils: reposync: improper path validation may lead to directory traversal (CVE-2018-10897) For more details about the security issue(s), including the impact, a CVSS score, and other related information, refer to the CVE page(s) listed in the References section. Red Hat would like to thank Jay Grizzard (Clover Network) and Aaron Levy (Clover Network) for reporting this issue.",
                                "fixedby": "0:1.1.31-46.el7_5",
                                "link": "https://access.redhat.com/errata/RHSA-2018:2285",
                                "metadata": "null",
                                "name": "RHSA-2018:2285",
                                "namespaceName": "centos:7",
                                "severity": "High"
                            }
                        ]
                    },
                    {
                        "name": "nss",
                        "namespaceName": "centos:7",
                        "version": "3.21.3-2.el7_3",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "Network Security Services (NSS) is a set of libraries designed to support the cross-platform development of security-enabled client and server applications. The nss-util packages provide utilities for use with the Network Security Services (NSS) libraries. The following packages have been upgraded to a newer upstream version: nss (3.28.4), nss-util (3.28.4). Security Fix(es): * An out-of-bounds write flaw was found in the way NSS performed certain Base64-decoding operations. An attacker could use this flaw to create a specially crafted certificate which, when parsed by NSS, could cause it to crash or execute arbitrary code, using the permissions of the user running an application compiled against the NSS library. (CVE-2017-5461) Red Hat would like to thank the Mozilla project for reporting this issue. Upstream acknowledges Ronald Crane as the original reporter.",
                                "fixedby": "0:3.28.4-1.0.el7_3",
                                "link": "https://access.redhat.com/errata/RHSA-2017:1100",
                                "metadata": "null",
                                "name": "RHSA-2017:1100",
                                "namespaceName": "centos:7",
                                "severity": "Critical"
                            },
                            {
                                "description": "Network Security Services (NSS) is a set of libraries designed to support the cross-platform development of security-enabled client and server applications. Security Fix(es): * A null pointer dereference flaw was found in the way NSS handled empty SSLv2 messages. An attacker could use this flaw to crash a server application compiled against the NSS library. (CVE-2017-7502) Bug Fix(es): * The Network Security Services (NSS) code and Certificate Authority (CA) list have been updated to meet the recommendations as published with the latest Mozilla Firefox Extended Support Release (ESR). The updated CA list improves compatibility with the certificates that are used in the Internet Public Key Infrastructure (PKI). To avoid certificate validation refusals, Red Hat recommends installing the updated CA list on June 12, 2017. (BZ#1451421)",
                                "fixedby": "0:3.28.4-1.2.el7_3",
                                "link": "https://access.redhat.com/errata/RHSA-2017:1365",
                                "metadata": "null",
                                "name": "RHSA-2017:1365",
                                "namespaceName": "centos:7",
                                "severity": "High"
                            },
                            {
                                "description": "Network Security Services (NSS) is a set of libraries designed to support the cross-platform development of security-enabled client and server applications. Security Fix(es): * A use-after-free flaw was found in the TLS 1.2 implementation in the NSS library when client authentication was used. A malicious client could use this flaw to cause an application compiled against NSS to crash or, potentially, execute arbitrary code with the permission of the user running the application. (CVE-2017-7805) Red Hat would like to thank the Mozilla project for reporting this issue. Upstream acknowledges Martin Thomson as the original reporter.",
                                "fixedby": "0:3.28.4-12.el7_4",
                                "link": "https://access.redhat.com/errata/RHSA-2017:2832",
                                "metadata": "null",
                                "name": "RHSA-2017:2832",
                                "namespaceName": "centos:7",
                                "severity": "High"
                            },
                            {
                                "description": "Network Security Services (NSS) is a set of libraries designed to support the cross-platform development of security-enabled client and server applications. Security Fix(es): * nss: ServerHello.random is all zeros when handling a v2-compatible ClientHello (CVE-2018-12384) For more details about the security issue(s), including the impact, a CVSS score, and other related information, refer to the CVE page(s) listed in the References section. Red Hat would like to thank the Mozilla project for reporting this issue.",
                                "fixedby": "0:3.36.0-7.el7_5",
                                "link": "https://access.redhat.com/errata/RHSA-2018:2768",
                                "metadata": "null",
                                "name": "RHSA-2018:2768",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            },
                            {
                                "description": "Network Security Services (NSS) is a set of libraries designed to support the cross-platform development of security-enabled client and server applications. Netscape Portable Runtime (NSPR) provides platform independence for non-GUI operating system facilities. The following packages have been upgraded to a later upstream version: nss (3.44.0), nss-softokn (3.44.0), nss-util (3.44.0), nspr (4.21.0). (BZ#1645231, BZ#1692269, BZ#1692271, BZ#1692274) Security Fix(es): * ROHNP: Key Extraction Side Channel in Multiple Crypto Libraries (CVE-2018-0495) * nss: Cache side-channel variant of the Bleichenbacher attack (CVE-2018-12404) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.7 Release Notes linked from the References section.",
                                "fixedby": "0:3.44.0-4.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2019:2237",
                                "metadata": "null",
                                "name": "RHSA-2019:2237",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            },
                            {
                                "description": "Network Security Services (NSS) is a set of libraries designed to support the cross-platform development of security-enabled client and server applications. The nss-softokn package provides the Network Security Services Softoken Cryptographic Module. The nss-util packages provide utilities for use with the Network Security Services (NSS) libraries. Security Fix(es): * nss: Out-of-bounds write when passing an output buffer smaller than the block size to NSC_EncryptUpdate (CVE-2019-11745) * nss: Empty or malformed p256-ECDH public keys may trigger a segmentation fault (CVE-2019-11729) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section.",
                                "fixedby": "0:3.44.0-7.el7_7",
                                "link": "https://access.redhat.com/errata/RHSA-2019:4190",
                                "metadata": "null",
                                "name": "RHSA-2019:4190",
                                "namespaceName": "centos:7",
                                "severity": "High"
                            }
                        ]
                    },
                    {
                        "name": "nss-tools",
                        "namespaceName": "centos:7",
                        "version": "3.21.3-2.el7_3",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "Network Security Services (NSS) is a set of libraries designed to support the cross-platform development of security-enabled client and server applications. The nss-util packages provide utilities for use with the Network Security Services (NSS) libraries. The following packages have been upgraded to a newer upstream version: nss (3.28.4), nss-util (3.28.4). Security Fix(es): * An out-of-bounds write flaw was found in the way NSS performed certain Base64-decoding operations. An attacker could use this flaw to create a specially crafted certificate which, when parsed by NSS, could cause it to crash or execute arbitrary code, using the permissions of the user running an application compiled against the NSS library. (CVE-2017-5461) Red Hat would like to thank the Mozilla project for reporting this issue. Upstream acknowledges Ronald Crane as the original reporter.",
                                "fixedby": "0:3.28.4-1.0.el7_3",
                                "link": "https://access.redhat.com/errata/RHSA-2017:1100",
                                "metadata": "null",
                                "name": "RHSA-2017:1100",
                                "namespaceName": "centos:7",
                                "severity": "Critical"
                            },
                            {
                                "description": "Network Security Services (NSS) is a set of libraries designed to support the cross-platform development of security-enabled client and server applications. Security Fix(es): * A null pointer dereference flaw was found in the way NSS handled empty SSLv2 messages. An attacker could use this flaw to crash a server application compiled against the NSS library. (CVE-2017-7502) Bug Fix(es): * The Network Security Services (NSS) code and Certificate Authority (CA) list have been updated to meet the recommendations as published with the latest Mozilla Firefox Extended Support Release (ESR). The updated CA list improves compatibility with the certificates that are used in the Internet Public Key Infrastructure (PKI). To avoid certificate validation refusals, Red Hat recommends installing the updated CA list on June 12, 2017. (BZ#1451421)",
                                "fixedby": "0:3.28.4-1.2.el7_3",
                                "link": "https://access.redhat.com/errata/RHSA-2017:1365",
                                "metadata": "null",
                                "name": "RHSA-2017:1365",
                                "namespaceName": "centos:7",
                                "severity": "High"
                            },
                            {
                                "description": "Network Security Services (NSS) is a set of libraries designed to support the cross-platform development of security-enabled client and server applications. Security Fix(es): * A use-after-free flaw was found in the TLS 1.2 implementation in the NSS library when client authentication was used. A malicious client could use this flaw to cause an application compiled against NSS to crash or, potentially, execute arbitrary code with the permission of the user running the application. (CVE-2017-7805) Red Hat would like to thank the Mozilla project for reporting this issue. Upstream acknowledges Martin Thomson as the original reporter.",
                                "fixedby": "0:3.28.4-12.el7_4",
                                "link": "https://access.redhat.com/errata/RHSA-2017:2832",
                                "metadata": "null",
                                "name": "RHSA-2017:2832",
                                "namespaceName": "centos:7",
                                "severity": "High"
                            },
                            {
                                "description": "Network Security Services (NSS) is a set of libraries designed to support the cross-platform development of security-enabled client and server applications. Security Fix(es): * nss: ServerHello.random is all zeros when handling a v2-compatible ClientHello (CVE-2018-12384) For more details about the security issue(s), including the impact, a CVSS score, and other related information, refer to the CVE page(s) listed in the References section. Red Hat would like to thank the Mozilla project for reporting this issue.",
                                "fixedby": "0:3.36.0-7.el7_5",
                                "link": "https://access.redhat.com/errata/RHSA-2018:2768",
                                "metadata": "null",
                                "name": "RHSA-2018:2768",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            },
                            {
                                "description": "Network Security Services (NSS) is a set of libraries designed to support the cross-platform development of security-enabled client and server applications. Netscape Portable Runtime (NSPR) provides platform independence for non-GUI operating system facilities. The following packages have been upgraded to a later upstream version: nss (3.44.0), nss-softokn (3.44.0), nss-util (3.44.0), nspr (4.21.0). (BZ#1645231, BZ#1692269, BZ#1692271, BZ#1692274) Security Fix(es): * ROHNP: Key Extraction Side Channel in Multiple Crypto Libraries (CVE-2018-0495) * nss: Cache side-channel variant of the Bleichenbacher attack (CVE-2018-12404) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.7 Release Notes linked from the References section.",
                                "fixedby": "0:3.44.0-4.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2019:2237",
                                "metadata": "null",
                                "name": "RHSA-2019:2237",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            },
                            {
                                "description": "Network Security Services (NSS) is a set of libraries designed to support the cross-platform development of security-enabled client and server applications. The nss-softokn package provides the Network Security Services Softoken Cryptographic Module. The nss-util packages provide utilities for use with the Network Security Services (NSS) libraries. Security Fix(es): * nss: Out-of-bounds write when passing an output buffer smaller than the block size to NSC_EncryptUpdate (CVE-2019-11745) * nss: Empty or malformed p256-ECDH public keys may trigger a segmentation fault (CVE-2019-11729) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section.",
                                "fixedby": "0:3.44.0-7.el7_7",
                                "link": "https://access.redhat.com/errata/RHSA-2019:4190",
                                "metadata": "null",
                                "name": "RHSA-2019:4190",
                                "namespaceName": "centos:7",
                                "severity": "High"
                            }
                        ]
                    },
                    {
                        "name": "openssl-libs",
                        "namespaceName": "centos:7",
                        "version": "1:1.0.1e-60.el7",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "OpenSSL is a toolkit that implements the Secure Sockets Layer (SSL) and Transport Layer Security (TLS) protocols, as well as a full-strength general-purpose cryptography library. Security Fix(es): * openssl: bn_sqrx8x_internal carry bug on x86_64 (CVE-2017-3736) * openssl: Read/write after SSL object in error state (CVE-2017-3737) * openssl: rsaz_1024_mul_avx2 overflow bug on x86_64 (CVE-2017-3738) For more details about the security issue(s), including the impact, a CVSS score, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.5 Release Notes linked from the References section.",
                                "fixedby": "1:1.0.2k-12.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2018:0998",
                                "metadata": "null",
                                "name": "RHSA-2018:0998",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            },
                            {
                                "description": "OpenSSL is a toolkit that implements the Secure Sockets Layer (SSL) and Transport Layer Security (TLS) protocols, as well as a full-strength general-purpose cryptography library. Security Fix(es): * openssl: ROHNP - Key Extraction Side Channel in Multiple Crypto Libraries (CVE-2018-0495) * openssl: Malicious server can send large prime to client during DH(E) TLS handshake causing the client to hang (CVE-2018-0732) * openssl: Handling of crafted recursive ASN.1 structures can cause a stack overflow and resulting denial of service (CVE-2018-0739) * openssl: Malformed X.509 IPAdressFamily could cause OOB read (CVE-2017-3735) * openssl: RSA key generation cache timing vulnerability in crypto/rsa/rsa_gen.c allows attackers to recover private keys (CVE-2018-0737) For more details about the security issue(s), including the impact, a CVSS score, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.6 Release Notes linked from the References section.",
                                "fixedby": "1:1.0.2k-16.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2018:3221",
                                "metadata": "null",
                                "name": "RHSA-2018:3221",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            },
                            {
                                "description": "OpenSSL is a toolkit that implements the Secure Sockets Layer (SSL) and Transport Layer Security (TLS) protocols, as well as a full-strength general-purpose cryptography library. Security Fix(es): * openssl: Side-channel vulnerability on SMT/Hyper-Threading architectures (PortSmash) (CVE-2018-5407) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Bug Fix(es): * Perform the RSA signature self-tests with SHA-256 (BZ#1673914)",
                                "fixedby": "1:1.0.2k-16.el7_6.1",
                                "link": "https://access.redhat.com/errata/RHSA-2019:0483",
                                "metadata": "null",
                                "name": "RHSA-2019:0483",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            },
                            {
                                "description": "OpenSSL is a toolkit that implements the Secure Sockets Layer (SSL) and Transport Layer Security (TLS) protocols, as well as a full-strength general-purpose cryptography library. Security Fix(es): * openssl: 0-byte record padding oracle (CVE-2019-1559) * openssl: timing side channel attack in the DSA signature algorithm (CVE-2018-0734) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.7 Release Notes linked from the References section.",
                                "fixedby": "1:1.0.2k-19.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2019:2304",
                                "metadata": "null",
                                "name": "RHSA-2019:2304",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            },
                            {
                                "description": "OpenSSL is a toolkit that implements the Secure Sockets Layer (SSL) and Transport Layer Security (TLS) protocols, as well as a full-strength general-purpose cryptography library. Security Fix(es): * An integer underflow leading to an out of bounds read flaw was found in OpenSSL. A remote attacker could possibly use this flaw to crash a 32-bit TLS/SSL server or client using OpenSSL if it used the RC4-MD5 cipher suite. (CVE-2017-3731) * A denial of service flaw was found in the way the TLS/SSL protocol defined processing of ALERT packets during a connection handshake. A remote attacker could use this flaw to make a TLS/SSL server consume an excessive amount of CPU and fail to accept connections form other clients. (CVE-2016-8610)",
                                "fixedby": "1:1.0.1e-60.el7_3.1",
                                "link": "https://access.redhat.com/errata/RHSA-2017:0286",
                                "metadata": "null",
                                "name": "RHSA-2017:0286",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            },
                            {
                                "description": "OpenSSL is a toolkit that implements the Secure Sockets Layer (SSL) and Transport Layer Security (TLS) protocols, as well as a full-strength general-purpose cryptography library. For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.4 Release Notes linked from the References section. Users of openssl are advised to upgrade to these updated packages.",
                                "fixedby": "1:1.0.2k-8.el7",
                                "link": "https://access.redhat.com/errata/RHBA-2017:1929",
                                "metadata": "null",
                                "name": "RHBA-2017:1929",
                                "namespaceName": "centos:7",
                                "severity": "Unknown"
                            }
                        ]
                    },
                    {
                        "name": "dracut",
                        "namespaceName": "centos:7",
                        "version": "033-463.el7",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "The dracut packages contain an event-driven initial RAM file system (initramfs) generator infrastructure based on the udev device manager. The virtual file system, initramfs, is loaded together with the kernel at boot time and initializes the system, so it can read and boot from the root partition. This update fixes the following bug: * Microcode on AMD family 16h processors was not updated early in the boot process. With this bug fix, the issue is addressed. (BZ#1526943) Users of dracut are advised to upgrade to these updated packages, which fix this bug.",
                                "fixedby": "0:033-502.el7_4.1",
                                "link": "https://access.redhat.com/errata/RHBA-2018:0042",
                                "metadata": "null",
                                "name": "RHBA-2018:0042",
                                "namespaceName": "centos:7",
                                "severity": "Unknown"
                            }
                        ]
                    },
                    {
                        "name": "nss-sysinit",
                        "namespaceName": "centos:7",
                        "version": "3.21.3-2.el7_3",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "Network Security Services (NSS) is a set of libraries designed to support the cross-platform development of security-enabled client and server applications. The nss-util packages provide utilities for use with the Network Security Services (NSS) libraries. The following packages have been upgraded to a newer upstream version: nss (3.28.4), nss-util (3.28.4). Security Fix(es): * An out-of-bounds write flaw was found in the way NSS performed certain Base64-decoding operations. An attacker could use this flaw to create a specially crafted certificate which, when parsed by NSS, could cause it to crash or execute arbitrary code, using the permissions of the user running an application compiled against the NSS library. (CVE-2017-5461) Red Hat would like to thank the Mozilla project for reporting this issue. Upstream acknowledges Ronald Crane as the original reporter.",
                                "fixedby": "0:3.28.4-1.0.el7_3",
                                "link": "https://access.redhat.com/errata/RHSA-2017:1100",
                                "metadata": "null",
                                "name": "RHSA-2017:1100",
                                "namespaceName": "centos:7",
                                "severity": "Critical"
                            },
                            {
                                "description": "Network Security Services (NSS) is a set of libraries designed to support the cross-platform development of security-enabled client and server applications. Security Fix(es): * A null pointer dereference flaw was found in the way NSS handled empty SSLv2 messages. An attacker could use this flaw to crash a server application compiled against the NSS library. (CVE-2017-7502) Bug Fix(es): * The Network Security Services (NSS) code and Certificate Authority (CA) list have been updated to meet the recommendations as published with the latest Mozilla Firefox Extended Support Release (ESR). The updated CA list improves compatibility with the certificates that are used in the Internet Public Key Infrastructure (PKI). To avoid certificate validation refusals, Red Hat recommends installing the updated CA list on June 12, 2017. (BZ#1451421)",
                                "fixedby": "0:3.28.4-1.2.el7_3",
                                "link": "https://access.redhat.com/errata/RHSA-2017:1365",
                                "metadata": "null",
                                "name": "RHSA-2017:1365",
                                "namespaceName": "centos:7",
                                "severity": "High"
                            },
                            {
                                "description": "Network Security Services (NSS) is a set of libraries designed to support the cross-platform development of security-enabled client and server applications. Security Fix(es): * A use-after-free flaw was found in the TLS 1.2 implementation in the NSS library when client authentication was used. A malicious client could use this flaw to cause an application compiled against NSS to crash or, potentially, execute arbitrary code with the permission of the user running the application. (CVE-2017-7805) Red Hat would like to thank the Mozilla project for reporting this issue. Upstream acknowledges Martin Thomson as the original reporter.",
                                "fixedby": "0:3.28.4-12.el7_4",
                                "link": "https://access.redhat.com/errata/RHSA-2017:2832",
                                "metadata": "null",
                                "name": "RHSA-2017:2832",
                                "namespaceName": "centos:7",
                                "severity": "High"
                            },
                            {
                                "description": "Network Security Services (NSS) is a set of libraries designed to support the cross-platform development of security-enabled client and server applications. Security Fix(es): * nss: ServerHello.random is all zeros when handling a v2-compatible ClientHello (CVE-2018-12384) For more details about the security issue(s), including the impact, a CVSS score, and other related information, refer to the CVE page(s) listed in the References section. Red Hat would like to thank the Mozilla project for reporting this issue.",
                                "fixedby": "0:3.36.0-7.el7_5",
                                "link": "https://access.redhat.com/errata/RHSA-2018:2768",
                                "metadata": "null",
                                "name": "RHSA-2018:2768",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            },
                            {
                                "description": "Network Security Services (NSS) is a set of libraries designed to support the cross-platform development of security-enabled client and server applications. Netscape Portable Runtime (NSPR) provides platform independence for non-GUI operating system facilities. The following packages have been upgraded to a later upstream version: nss (3.44.0), nss-softokn (3.44.0), nss-util (3.44.0), nspr (4.21.0). (BZ#1645231, BZ#1692269, BZ#1692271, BZ#1692274) Security Fix(es): * ROHNP: Key Extraction Side Channel in Multiple Crypto Libraries (CVE-2018-0495) * nss: Cache side-channel variant of the Bleichenbacher attack (CVE-2018-12404) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.7 Release Notes linked from the References section.",
                                "fixedby": "0:3.44.0-4.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2019:2237",
                                "metadata": "null",
                                "name": "RHSA-2019:2237",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            },
                            {
                                "description": "Network Security Services (NSS) is a set of libraries designed to support the cross-platform development of security-enabled client and server applications. The nss-softokn package provides the Network Security Services Softoken Cryptographic Module. The nss-util packages provide utilities for use with the Network Security Services (NSS) libraries. Security Fix(es): * nss: Out-of-bounds write when passing an output buffer smaller than the block size to NSC_EncryptUpdate (CVE-2019-11745) * nss: Empty or malformed p256-ECDH public keys may trigger a segmentation fault (CVE-2019-11729) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section.",
                                "fixedby": "0:3.44.0-7.el7_7",
                                "link": "https://access.redhat.com/errata/RHSA-2019:4190",
                                "metadata": "null",
                                "name": "RHSA-2019:4190",
                                "namespaceName": "centos:7",
                                "severity": "High"
                            }
                        ]
                    },
                    {
                        "name": "gobject-introspection",
                        "namespaceName": "centos:7",
                        "version": "1.42.0-1.el7",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "GNOME is the default desktop environment of Red Hat Enterprise Linux. Security Fix(es): * libsoup: Crash in soup_cookie_jar.c:get_cookies() on empty hostnames (CVE-2018-12910) * poppler: Infinite recursion in fofi/FoFiType1C.cc:FoFiType1C::cvtGlyph() function allows denial of service (CVE-2017-18267) * libgxps: heap based buffer over read in ft_font_face_hash function of gxps-fonts.c (CVE-2018-10733) * libgxps: Stack-based buffer overflow in calling glib in gxps_images_guess_content_type of gcontenttype.c (CVE-2018-10767) * poppler: NULL pointer dereference in Annot.h:AnnotPath::getCoordsLength() allows for denial of service via crafted PDF (CVE-2018-10768) * poppler: out of bounds read in pdfunite (CVE-2018-13988) For more details about the security issue(s), including the impact, a CVSS score, and other related information, refer to the CVE page(s) listed in the References section. Red Hat would like to thank chenyuan (NESA Lab) for reporting CVE-2018-10733 and CVE-2018-10767 and Hosein Askari for reporting CVE-2018-13988. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.6 Release Notes linked from the References section.",
                                "fixedby": "0:1.56.1-1.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2018:3140",
                                "metadata": "null",
                                "name": "RHSA-2018:3140",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            }
                        ]
                    },
                    {
                        "name": "openldap",
                        "namespaceName": "centos:7",
                        "version": "2.4.40-13.el7",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "OpenLDAP is an open-source suite of Lightweight Directory Access Protocol (LDAP) applications and development tools. LDAP is a set of protocols used to access and maintain distributed directory information services over an IP network. The openldap packages contain configuration files, libraries, and documentation for OpenLDAP. The following packages have been upgraded to a later upstream version: openldap (2.4.44). (BZ#1386365) Security Fix(es): * A double-free flaw was found in the way OpenLDAP's slapd server using the MDB backend handled LDAP searches. A remote attacker with access to search the directory could potentially use this flaw to crash slapd by issuing a specially crafted LDAP search query. (CVE-2017-9287) Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.4 Release Notes linked from the References section.",
                                "fixedby": "0:2.4.44-5.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2017:1852",
                                "metadata": "null",
                                "name": "RHSA-2017:1852",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            }
                        ]
                    },
                    {
                        "name": "libtasn1",
                        "namespaceName": "centos:7",
                        "version": "3.8-3.el7",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "Libtasn1 is a library that provides Abstract Syntax Notation One (ASN.1, as specified by the X.680 ITU-T recommendation) parsing and structures management, and Distinguished Encoding Rules (DER, as per X.690) encoding and decoding functions. The following packages have been upgraded to a later upstream version: libtasn1 (4.10). (BZ#1360639) Security Fix(es): * A heap-based buffer overflow flaw was found in the way the libtasn1 library decoded certain DER-encoded inputs. A specially crafted DER-encoded input could cause an application using libtasn1 to perform an invalid read, causing the application to crash. (CVE-2015-3622) * A stack-based buffer overflow was found in the way libtasn1 decoded certain DER encoded data. An attacker could use this flaw to crash an application using the libtasn1 library. (CVE-2015-2806) Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.4 Release Notes linked from the References section.",
                                "fixedby": "0:4.10-1.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2017:1860",
                                "metadata": "null",
                                "name": "RHSA-2017:1860",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            }
                        ]
                    },
                    {
                        "name": "glibc-common",
                        "namespaceName": "centos:7",
                        "version": "2.17-157.el7_3.1",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "The glibc packages provide the standard C libraries (libc), POSIX thread libraries (libpthread), standard math libraries (libm), and the name service cache daemon (nscd) used by multiple programs on the system. Without these libraries, the Linux system cannot function correctly. Security Fix(es): * A flaw was found in the way memory was being allocated on the stack for user space binaries. If heap (or different memory region) and stack memory regions were adjacent to each other, an attacker could use this flaw to jump over the stack guard gap, cause controlled memory corruption on process stack or the adjacent memory region, and thus increase their privileges on the system. This is glibc-side mitigation which blocks processing of LD_LIBRARY_PATH for programs running in secure-execution mode and reduces the number of allocations performed by the processing of LD_AUDIT, LD_PRELOAD, and LD_HWCAP_MASK, making successful exploitation of this issue more difficult. (CVE-2017-1000366) Red Hat would like to thank Qualys Research Labs for reporting this issue.",
                                "fixedby": "0:2.17-157.el7_3.4",
                                "link": "https://access.redhat.com/errata/RHSA-2017:1481",
                                "metadata": "null",
                                "name": "RHSA-2017:1481",
                                "namespaceName": "centos:7",
                                "severity": "High"
                            },
                            {
                                "description": "The glibc packages provide the standard C libraries (libc), POSIX thread libraries (libpthread), standard math libraries (libm), and the name service cache daemon (nscd) used by multiple programs on the system. Without these libraries, the Linux system cannot function correctly. Security Fix(es): * glibc: realpath() buffer underflow when getcwd() returns relative path allows privilege escalation (CVE-2018-1000001) * glibc: Buffer overflow in glob with GLOB_TILDE (CVE-2017-15670) * glibc: Buffer overflow during unescaping of user names with the ~ operator (CVE-2017-15804) * glibc: denial of service in getnetbyname function (CVE-2014-9402) * glibc: DNS resolver NULL pointer dereference with crafted record type (CVE-2015-5180) * glibc: Fragmentation attacks possible when EDNS0 is enabled (CVE-2017-12132) For more details about the security issue(s), including the impact, a CVSS score, and other related information, refer to the CVE page(s) listed in the References section. Red Hat would like to thank halfdog for reporting CVE-2018-1000001. The CVE-2015-5180 issue was discovered by Florian Weimer (Red Hat Product Security). Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.5 Release Notes linked from the References section.",
                                "fixedby": "0:2.17-222.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2018:0805",
                                "metadata": "null",
                                "name": "RHSA-2018:0805",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            },
                            {
                                "description": "The glibc packages provide the standard C libraries (libc), POSIX thread libraries (libpthread), standard math libraries (libm), and the name service cache daemon (nscd) used by multiple programs on the system. Without these libraries, the Linux system cannot function correctly. Security Fix(es): * glibc: Incorrect handling of RPATH in elf/dl-load.c can be used to execute code loaded from arbitrary libraries (CVE-2017-16997) * glibc: Integer overflow in posix_memalign in memalign functions (CVE-2018-6485) * glibc: Integer overflow in stdlib/canonicalize.c on 32-bit architectures leading to stack-based buffer overflow (CVE-2018-11236) * glibc: Buffer overflow in __mempcpy_avx512_no_vzeroupper (CVE-2018-11237) For more details about the security issue(s), including the impact, a CVSS score, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.6 Release Notes linked from the References section.",
                                "fixedby": "0:2.17-260.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2018:3092",
                                "metadata": "null",
                                "name": "RHSA-2018:3092",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            },
                            {
                                "description": "The glibc packages provide the standard C libraries (libc), POSIX thread libraries (libpthread), standard math libraries (libm), and the name service cache daemon (nscd) used by multiple programs on the system. Without these libraries, the Linux system cannot function correctly. Security Fix(es): * glibc: getaddrinfo should reject IP addresses with trailing characters (CVE-2016-10739) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.7 Release Notes linked from the References section.",
                                "fixedby": "0:2.17-292.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2019:2118",
                                "metadata": "null",
                                "name": "RHSA-2019:2118",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            },
                            {
                                "description": "The glibc packages provide the standard C libraries (libc), POSIX thread libraries (libpthread), standard math libraries (libm), and the name service cache daemon (nscd) used by multiple programs on the system. Without these libraries, the Linux system cannot function correctly. Security Fix(es): * A stack overflow vulnerability was found in nan* functions that could cause applications, which process long strings with the nan function, to crash or, potentially, execute arbitrary code. (CVE-2014-9761) * It was found that out-of-range time values passed to the strftime() function could result in an out-of-bounds memory access. This could lead to application crash or, potentially, information disclosure. (CVE-2015-8776) * An integer overflow vulnerability was found in hcreate() and hcreate_r() functions which could result in an out-of-bounds memory access. This could lead to application crash or, potentially, arbitrary code execution. (CVE-2015-8778) * A stack based buffer overflow vulnerability was found in the catopen() function. An excessively long string passed to the function could cause it to crash or, potentially, execute arbitrary code. (CVE-2015-8779) * It was found that the dynamic loader did not sanitize the LD_POINTER_GUARD environment variable. An attacker could use this flaw to bypass the pointer guarding protection on set-user-ID or set-group-ID programs to execute arbitrary code with the permissions of the user running the application. (CVE-2015-8777) Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.4 Release Notes linked from the References section.",
                                "fixedby": "0:2.17-196.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2017:1916",
                                "metadata": "null",
                                "name": "RHSA-2017:1916",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            }
                        ]
                    },
                    {
                        "name": "libxml2-python",
                        "namespaceName": "centos:7",
                        "version": "2.9.1-6.el7_2.3",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "The libxml2 library is a development toolbox providing the implementation of various XML standards. Security Fix(es): * libxml2: Use after free triggered by XPointer paths beginning with range-to (CVE-2016-5131) * libxml2: Use after free in xmlXPathCompOpEvalPositionalPredicate() function in xpath.c (CVE-2017-15412) * libxml2: DoS caused by incorrect error detection during XZ decompression (CVE-2015-8035) * libxml2: NULL pointer dereference in xmlXPathCompOpEval() function in xpath.c (CVE-2018-14404) * libxml2: Unrestricted memory usage in xz_head() function in xzlib.c (CVE-2017-18258) * libxml2: Infinite loop caused by incorrect error detection during LZMA decompression (CVE-2018-14567) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.8 Release Notes linked from the References section.",
                                "fixedby": "0:2.9.1-6.el7.4",
                                "link": "https://access.redhat.com/errata/RHSA-2020:1190",
                                "metadata": "null",
                                "name": "RHSA-2020:1190",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            }
                        ]
                    },
                    {
                        "name": "glibc",
                        "namespaceName": "centos:7",
                        "version": "2.17-157.el7_3.1",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "The glibc packages provide the standard C libraries (libc), POSIX thread libraries (libpthread), standard math libraries (libm), and the name service cache daemon (nscd) used by multiple programs on the system. Without these libraries, the Linux system cannot function correctly. Security Fix(es): * A flaw was found in the way memory was being allocated on the stack for user space binaries. If heap (or different memory region) and stack memory regions were adjacent to each other, an attacker could use this flaw to jump over the stack guard gap, cause controlled memory corruption on process stack or the adjacent memory region, and thus increase their privileges on the system. This is glibc-side mitigation which blocks processing of LD_LIBRARY_PATH for programs running in secure-execution mode and reduces the number of allocations performed by the processing of LD_AUDIT, LD_PRELOAD, and LD_HWCAP_MASK, making successful exploitation of this issue more difficult. (CVE-2017-1000366) Red Hat would like to thank Qualys Research Labs for reporting this issue.",
                                "fixedby": "0:2.17-157.el7_3.4",
                                "link": "https://access.redhat.com/errata/RHSA-2017:1481",
                                "metadata": "null",
                                "name": "RHSA-2017:1481",
                                "namespaceName": "centos:7",
                                "severity": "High"
                            },
                            {
                                "description": "The glibc packages provide the standard C libraries (libc), POSIX thread libraries (libpthread), standard math libraries (libm), and the name service cache daemon (nscd) used by multiple programs on the system. Without these libraries, the Linux system cannot function correctly. Security Fix(es): * glibc: realpath() buffer underflow when getcwd() returns relative path allows privilege escalation (CVE-2018-1000001) * glibc: Buffer overflow in glob with GLOB_TILDE (CVE-2017-15670) * glibc: Buffer overflow during unescaping of user names with the ~ operator (CVE-2017-15804) * glibc: denial of service in getnetbyname function (CVE-2014-9402) * glibc: DNS resolver NULL pointer dereference with crafted record type (CVE-2015-5180) * glibc: Fragmentation attacks possible when EDNS0 is enabled (CVE-2017-12132) For more details about the security issue(s), including the impact, a CVSS score, and other related information, refer to the CVE page(s) listed in the References section. Red Hat would like to thank halfdog for reporting CVE-2018-1000001. The CVE-2015-5180 issue was discovered by Florian Weimer (Red Hat Product Security). Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.5 Release Notes linked from the References section.",
                                "fixedby": "0:2.17-222.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2018:0805",
                                "metadata": "null",
                                "name": "RHSA-2018:0805",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            },
                            {
                                "description": "The glibc packages provide the standard C libraries (libc), POSIX thread libraries (libpthread), standard math libraries (libm), and the name service cache daemon (nscd) used by multiple programs on the system. Without these libraries, the Linux system cannot function correctly. Security Fix(es): * glibc: Incorrect handling of RPATH in elf/dl-load.c can be used to execute code loaded from arbitrary libraries (CVE-2017-16997) * glibc: Integer overflow in posix_memalign in memalign functions (CVE-2018-6485) * glibc: Integer overflow in stdlib/canonicalize.c on 32-bit architectures leading to stack-based buffer overflow (CVE-2018-11236) * glibc: Buffer overflow in __mempcpy_avx512_no_vzeroupper (CVE-2018-11237) For more details about the security issue(s), including the impact, a CVSS score, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.6 Release Notes linked from the References section.",
                                "fixedby": "0:2.17-260.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2018:3092",
                                "metadata": "null",
                                "name": "RHSA-2018:3092",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            },
                            {
                                "description": "The glibc packages provide the standard C libraries (libc), POSIX thread libraries (libpthread), standard math libraries (libm), and the name service cache daemon (nscd) used by multiple programs on the system. Without these libraries, the Linux system cannot function correctly. Security Fix(es): * glibc: getaddrinfo should reject IP addresses with trailing characters (CVE-2016-10739) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.7 Release Notes linked from the References section.",
                                "fixedby": "0:2.17-292.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2019:2118",
                                "metadata": "null",
                                "name": "RHSA-2019:2118",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            },
                            {
                                "description": "The glibc packages provide the standard C libraries (libc), POSIX thread libraries (libpthread), standard math libraries (libm), and the name service cache daemon (nscd) used by multiple programs on the system. Without these libraries, the Linux system cannot function correctly. Security Fix(es): * A stack overflow vulnerability was found in nan* functions that could cause applications, which process long strings with the nan function, to crash or, potentially, execute arbitrary code. (CVE-2014-9761) * It was found that out-of-range time values passed to the strftime() function could result in an out-of-bounds memory access. This could lead to application crash or, potentially, information disclosure. (CVE-2015-8776) * An integer overflow vulnerability was found in hcreate() and hcreate_r() functions which could result in an out-of-bounds memory access. This could lead to application crash or, potentially, arbitrary code execution. (CVE-2015-8778) * A stack based buffer overflow vulnerability was found in the catopen() function. An excessively long string passed to the function could cause it to crash or, potentially, execute arbitrary code. (CVE-2015-8779) * It was found that the dynamic loader did not sanitize the LD_POINTER_GUARD environment variable. An attacker could use this flaw to bypass the pointer guarding protection on set-user-ID or set-group-ID programs to execute arbitrary code with the permissions of the user running the application. (CVE-2015-8777) Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.4 Release Notes linked from the References section.",
                                "fixedby": "0:2.17-196.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2017:1916",
                                "metadata": "null",
                                "name": "RHSA-2017:1916",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            }
                        ]
                    },
                    {
                        "name": "yum-utils",
                        "namespaceName": "centos:7",
                        "version": "1.1.31-40.el7",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "The yum-utils packages provide a collection of utilities and examples for the yum package manager to make yum easier and more powerful to use. Security Fix(es): * yum-utils: reposync: improper path validation may lead to directory traversal (CVE-2018-10897) For more details about the security issue(s), including the impact, a CVSS score, and other related information, refer to the CVE page(s) listed in the References section. Red Hat would like to thank Jay Grizzard (Clover Network) and Aaron Levy (Clover Network) for reporting this issue.",
                                "fixedby": "0:1.1.31-46.el7_5",
                                "link": "https://access.redhat.com/errata/RHSA-2018:2285",
                                "metadata": "null",
                                "name": "RHSA-2018:2285",
                                "namespaceName": "centos:7",
                                "severity": "High"
                            }
                        ]
                    },
                    {
                        "name": "python",
                        "namespaceName": "centos:7",
                        "version": "2.7.5-48.el7",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "Python is an interpreted, interactive, object-oriented programming language, which includes modules, classes, exceptions, very high level dynamic data types and dynamic typing. Python supports interfaces to many system calls and libraries, as well as to various windowing systems. Security Fix(es): * A flaw was found in the way the DES/3DES cipher was used as part of the TLS/SSL protocol. A man-in-the-middle attacker could use this flaw to recover some plaintext data by capturing large amounts of encrypted traffic between TLS/SSL server and client if the communication used a DES/3DES based ciphersuite. (CVE-2016-2183) Note: This update modifies the Python ssl module to disable 3DES cipher suites by default. Red Hat would like to thank OpenVPN for reporting this issue. Upstream acknowledges Karthikeyan Bhargavan (Inria) and Gaëtan Leurent (Inria) as the original reporters.",
                                "fixedby": "0:2.7.5-69.el7_5",
                                "link": "https://access.redhat.com/errata/RHSA-2018:2123",
                                "metadata": "null",
                                "name": "RHSA-2018:2123",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            },
                            {
                                "description": "Python is an interpreted, interactive, object-oriented programming language, which includes modules, classes, exceptions, very high level dynamic data types and dynamic typing. Python supports interfaces to many system calls and libraries, as well as to various windowing systems. Security Fix(es): * python: DOS via regular expression backtracking in difflib.IS_LINE_JUNK method in difflib (CVE-2018-1061) * python: DOS via regular expression catastrophic backtracking in apop() method in pop3lib (CVE-2018-1060) For more details about the security issue(s), including the impact, a CVSS score, and other related information, refer to the CVE page(s) listed in the References section. Red Hat would like to thank the Python security response team for reporting these issues. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.6 Release Notes linked from the References section.",
                                "fixedby": "0:2.7.5-76.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2018:3041",
                                "metadata": "null",
                                "name": "RHSA-2018:3041",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            },
                            {
                                "description": "Python is an interpreted, interactive, object-oriented programming language, which includes modules, classes, exceptions, very high level dynamic data types and dynamic typing. Python supports interfaces to many system calls and libraries, as well as to various windowing systems. Security Fix(es): * python: Information Disclosure due to urlsplit improper NFKC normalization (CVE-2019-9636) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section.",
                                "fixedby": "0:2.7.5-77.el7_6",
                                "link": "https://access.redhat.com/errata/RHSA-2019:0710",
                                "metadata": "null",
                                "name": "RHSA-2019:0710",
                                "namespaceName": "centos:7",
                                "severity": "High"
                            },
                            {
                                "description": "Python is an interpreted, interactive, object-oriented programming language, which includes modules, classes, exceptions, very high level dynamic data types and dynamic typing. Python supports interfaces to many system calls and libraries, as well as to various windowing systems. Security Fix(es): * python: regression of CVE-2019-9636 due to functional fix to allow port numbers in netloc (CVE-2019-10160) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section.",
                                "fixedby": "0:2.7.5-80.el7_6",
                                "link": "https://access.redhat.com/errata/RHSA-2019:1587",
                                "metadata": "null",
                                "name": "RHSA-2019:1587",
                                "namespaceName": "centos:7",
                                "severity": "High"
                            },
                            {
                                "description": "Python is an interpreted, interactive, object-oriented programming language, which includes modules, classes, exceptions, very high level dynamic data types and dynamic typing. Python supports interfaces to many system calls and libraries, as well as to various windowing systems. Security Fix(es): * python: Missing salt initialization in _elementtree.c module (CVE-2018-14647) * python: NULL pointer dereference using a specially crafted X509 certificate (CVE-2019-5010) * python: CRLF injection via the query part of the url passed to urlopen() (CVE-2019-9740) * python: CRLF injection via the path part of the url passed to urlopen() (CVE-2019-9947) * python: Undocumented local_file protocol allows remote attackers to bypass protection mechanisms (CVE-2019-9948) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.7 Release Notes linked from the References section.",
                                "fixedby": "0:2.7.5-86.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2019:2030",
                                "metadata": "null",
                                "name": "RHSA-2019:2030",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            },
                            {
                                "description": "Python is an interpreted, interactive, object-oriented programming language, which includes modules, classes, exceptions, very high level dynamic data types and dynamic typing. Python supports interfaces to many system calls and libraries, as well as to various windowing systems. Security Fix(es): * python: Cookie domain check returns incorrect results (CVE-2018-20852) * python: email.utils.parseaddr wrongly parses email addresses (CVE-2019-16056) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.8 Release Notes linked from the References section.",
                                "fixedby": "0:2.7.5-88.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2020:1131",
                                "metadata": "null",
                                "name": "RHSA-2020:1131",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            },
                            {
                                "description": "Python is an interpreted, interactive, object-oriented programming language, which includes modules, classes, exceptions, very high level dynamic data types and dynamic typing. Python supports interfaces to many system calls and libraries, as well as to various windowing systems. Security Fix(es): * The Python standard library HTTP client modules (such as httplib or urllib) did not perform verification of TLS/SSL certificates when connecting to HTTPS servers. A man-in-the-middle attacker could use this flaw to hijack connections and eavesdrop or modify transferred data. (CVE-2014-9365) Note: The Python standard library was updated to enable certificate verification by default. Refer to the Knowledgebase article 2039753 linked to in the References section for further details about this change. (BZ#1219110) Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.4 Release Notes linked from the References section.",
                                "fixedby": "0:2.7.5-58.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2017:1868",
                                "metadata": "null",
                                "name": "RHSA-2017:1868",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            }
                        ]
                    },
                    {
                        "name": "binutils",
                        "namespaceName": "centos:7",
                        "version": "2.25.1-22.base.el7",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "The binutils packages provide a collection of binary utilities for the manipulation of object code in various object file formats. It includes the ar, as, gprof, ld, nm, objcopy, objdump, ranlib, readelf, size, strings, strip, and addr2line utilities. Security Fix(es): * binutils: integer overflow leads to heap-based buffer overflow in objdump (CVE-2018-1000876) * binutils: Stack Exhaustion in the demangling functions provided by libiberty (CVE-2018-12641) * binutils: NULL pointer dereference in work_stuff_copy_to_from in cplus-dem.c. (CVE-2018-12697) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.7 Release Notes linked from the References section.",
                                "fixedby": "0:2.27-41.base.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2019:2075",
                                "metadata": "null",
                                "name": "RHSA-2019:2075",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            },
                            {
                                "description": "The binutils packages provide a collection of binary utilities for the manipulation of object code in various object file formats. It includes the ar, as, gprof, ld, nm, objcopy, objdump, ranlib, readelf, size, strings, strip, and addr2line utilities. Security Fix(es): * binutils: Improper bounds check in coffgen.c:coff_pointerize_aux() allows for denial of service when parsing a crafted COFF file (CVE-2018-7208) * binutils: integer overflow via an ELF file with corrupt dwarf1 debug information in libbfd library (CVE-2018-7568) * binutils: integer underflow or overflow via an ELF file with a corrupt DWARF FORM block in libbfd library (CVE-2018-7569) * binutils: NULL pointer dereference in swap_std_reloc_in function in aoutx.h resulting in crash (CVE-2018-7642) * binutils: Integer overflow in the display_debug_ranges function resulting in crash (CVE-2018-7643) * binutils: Crash in elf.c:bfd_section_from_shdr() with crafted executable (CVE-2018-8945) * binutils: Heap-base buffer over-read in dwarf.c:process_cu_tu_index() allows for denial of service via crafted file (CVE-2018-10372) * binutils: NULL pointer dereference in dwarf2.c:concat_filename() allows for denial of service via crafted file (CVE-2018-10373) * binutils: out of bounds memory write in peXXigen.c files (CVE-2018-10534) * binutils: NULL pointer dereference in elf.c (CVE-2018-10535) * binutils: Uncontrolled Resource Consumption in execution of nm (CVE-2018-13033) For more details about the security issue(s), including the impact, a CVSS score, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.6 Release Notes linked from the References section.",
                                "fixedby": "0:2.27-34.base.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2018:3032",
                                "metadata": "null",
                                "name": "RHSA-2018:3032",
                                "namespaceName": "centos:7",
                                "severity": "Low"
                            }
                        ]
                    },
                    {
                        "name": "libstdc++",
                        "namespaceName": "centos:7",
                        "version": "4.8.5-11.el7",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "The gcc packages provide compilers for C, C++, Java, Fortran, Objective C, and Ada 95 GNU, as well as related support libraries. Security Fix(es): * gcc: GCC generates incorrect code for RDRAND/RDSEED intrinsics (CVE-2017-11671) For more details about the security issue(s), including the impact, a CVSS score, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.5 Release Notes linked from the References section.",
                                "fixedby": "0:4.8.5-28.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2018:0849",
                                "metadata": "null",
                                "name": "RHSA-2018:0849",
                                "namespaceName": "centos:7",
                                "severity": "Low"
                            }
                        ]
                    },
                    {
                        "name": "yum-plugin-ovl",
                        "namespaceName": "centos:7",
                        "version": "1.1.31-40.el7",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "The yum-utils packages provide a collection of utilities and examples for the yum package manager to make yum easier and more powerful to use. Security Fix(es): * yum-utils: reposync: improper path validation may lead to directory traversal (CVE-2018-10897) For more details about the security issue(s), including the impact, a CVSS score, and other related information, refer to the CVE page(s) listed in the References section. Red Hat would like to thank Jay Grizzard (Clover Network) and Aaron Levy (Clover Network) for reporting this issue.",
                                "fixedby": "0:1.1.31-46.el7_5",
                                "link": "https://access.redhat.com/errata/RHSA-2018:2285",
                                "metadata": "null",
                                "name": "RHSA-2018:2285",
                                "namespaceName": "centos:7",
                                "severity": "High"
                            }
                        ]
                    },
                    {
                        "name": "nss-softokn-freebl",
                        "namespaceName": "centos:7",
                        "version": "3.16.2.3-14.4.el7",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "Network Security Services (NSS) is a set of libraries designed to support the cross-platform development of security-enabled client and server applications. Netscape Portable Runtime (NSPR) provides platform independence for non-GUI operating system facilities. The following packages have been upgraded to a later upstream version: nss (3.44.0), nss-softokn (3.44.0), nss-util (3.44.0), nspr (4.21.0). (BZ#1645231, BZ#1692269, BZ#1692271, BZ#1692274) Security Fix(es): * ROHNP: Key Extraction Side Channel in Multiple Crypto Libraries (CVE-2018-0495) * nss: Cache side-channel variant of the Bleichenbacher attack (CVE-2018-12404) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.7 Release Notes linked from the References section.",
                                "fixedby": "0:3.44.0-5.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2019:2237",
                                "metadata": "null",
                                "name": "RHSA-2019:2237",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            },
                            {
                                "description": "Network Security Services (NSS) is a set of libraries designed to support the cross-platform development of security-enabled client and server applications. The nss-softokn package provides the Network Security Services Softoken Cryptographic Module. The nss-util packages provide utilities for use with the Network Security Services (NSS) libraries. Security Fix(es): * nss: Out-of-bounds write when passing an output buffer smaller than the block size to NSC_EncryptUpdate (CVE-2019-11745) * nss: Empty or malformed p256-ECDH public keys may trigger a segmentation fault (CVE-2019-11729) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section.",
                                "fixedby": "0:3.44.0-8.el7_7",
                                "link": "https://access.redhat.com/errata/RHSA-2019:4190",
                                "metadata": "null",
                                "name": "RHSA-2019:4190",
                                "namespaceName": "centos:7",
                                "severity": "High"
                            }
                        ]
                    },
                    {
                        "name": "nss-util",
                        "namespaceName": "centos:7",
                        "version": "3.21.3-1.1.el7_3",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "Network Security Services (NSS) is a set of libraries designed to support the cross-platform development of security-enabled client and server applications. The nss-util packages provide utilities for use with the Network Security Services (NSS) libraries. The following packages have been upgraded to a newer upstream version: nss (3.28.4), nss-util (3.28.4). Security Fix(es): * An out-of-bounds write flaw was found in the way NSS performed certain Base64-decoding operations. An attacker could use this flaw to create a specially crafted certificate which, when parsed by NSS, could cause it to crash or execute arbitrary code, using the permissions of the user running an application compiled against the NSS library. (CVE-2017-5461) Red Hat would like to thank the Mozilla project for reporting this issue. Upstream acknowledges Ronald Crane as the original reporter.",
                                "fixedby": "0:3.28.4-1.0.el7_3",
                                "link": "https://access.redhat.com/errata/RHSA-2017:1100",
                                "metadata": "null",
                                "name": "RHSA-2017:1100",
                                "namespaceName": "centos:7",
                                "severity": "Critical"
                            },
                            {
                                "description": "Network Security Services (NSS) is a set of libraries designed to support the cross-platform development of security-enabled client and server applications. Netscape Portable Runtime (NSPR) provides platform independence for non-GUI operating system facilities. The following packages have been upgraded to a later upstream version: nss (3.44.0), nss-softokn (3.44.0), nss-util (3.44.0), nspr (4.21.0). (BZ#1645231, BZ#1692269, BZ#1692271, BZ#1692274) Security Fix(es): * ROHNP: Key Extraction Side Channel in Multiple Crypto Libraries (CVE-2018-0495) * nss: Cache side-channel variant of the Bleichenbacher attack (CVE-2018-12404) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.7 Release Notes linked from the References section.",
                                "fixedby": "0:3.44.0-3.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2019:2237",
                                "metadata": "null",
                                "name": "RHSA-2019:2237",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            },
                            {
                                "description": "Network Security Services (NSS) is a set of libraries designed to support the cross-platform development of security-enabled client and server applications. The nss-softokn package provides the Network Security Services Softoken Cryptographic Module. The nss-util packages provide utilities for use with the Network Security Services (NSS) libraries. Security Fix(es): * nss: Out-of-bounds write when passing an output buffer smaller than the block size to NSC_EncryptUpdate (CVE-2019-11745) * nss: Empty or malformed p256-ECDH public keys may trigger a segmentation fault (CVE-2019-11729) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section.",
                                "fixedby": "0:3.44.0-4.el7_7",
                                "link": "https://access.redhat.com/errata/RHSA-2019:4190",
                                "metadata": "null",
                                "name": "RHSA-2019:4190",
                                "namespaceName": "centos:7",
                                "severity": "High"
                            }
                        ]
                    },
                    {
                        "name": "vim-minimal",
                        "namespaceName": "centos:7",
                        "version": "2:7.4.160-1.el7",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "Vim (Vi IMproved) is an updated and improved version of the vi editor. Security Fix(es): * vim/neovim: ':source!' command allows arbitrary command execution via modelines (CVE-2019-12735) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section.",
                                "fixedby": "2:7.4.160-6.el7_6",
                                "link": "https://access.redhat.com/errata/RHSA-2019:1619",
                                "metadata": "null",
                                "name": "RHSA-2019:1619",
                                "namespaceName": "centos:7",
                                "severity": "High"
                            },
                            {
                                "description": "Vim (Vi IMproved) is an updated and improved version of the vi editor. Security Fix(es): * A vulnerability was found in vim in how certain modeline options were treated. An attacker could craft a file that, when opened in vim with modelines enabled, could execute arbitrary commands with privileges of the user running vim. (CVE-2016-1248)",
                                "fixedby": "2:7.4.160-1.el7_3.1",
                                "link": "https://access.redhat.com/errata/RHSA-2016:2972",
                                "metadata": "null",
                                "name": "RHSA-2016:2972",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            }
                        ]
                    },
                    {
                        "name": "expat",
                        "namespaceName": "centos:7",
                        "version": "2.1.0-10.el7_3",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "Expat is a C library for parsing XML documents. Security Fix(es): * expat: Integer overflow leading to buffer overflow in XML_GetBuffer() (CVE-2015-2716) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.8 Release Notes linked from the References section.",
                                "fixedby": "0:2.1.0-11.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2020:1011",
                                "metadata": "null",
                                "name": "RHSA-2020:1011",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            }
                        ]
                    },
                    {
                        "name": "libssh2",
                        "namespaceName": "centos:7",
                        "version": "1.4.3-10.el7_2.1",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "The libssh2 packages provide a library that implements the SSH2 protocol. Security Fix(es): * libssh2: Integer overflow in transport read resulting in out of bounds write (CVE-2019-3855) * libssh2: Integer overflow in keyboard interactive handling resulting in out of bounds write (CVE-2019-3856) * libssh2: Integer overflow in SSH packet processing channel resulting in out of bounds write (CVE-2019-3857) * libssh2: Integer overflow in user authenticate keyboard interactive allows out-of-bounds writes (CVE-2019-3863) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section.",
                                "fixedby": "0:1.4.3-12.el7_6.2",
                                "link": "https://access.redhat.com/errata/RHSA-2019:0679",
                                "metadata": "null",
                                "name": "RHSA-2019:0679",
                                "namespaceName": "centos:7",
                                "severity": "High"
                            },
                            {
                                "description": "The libssh2 packages provide a library that implements the SSH2 protocol. Security Fix(es): * libssh2: Out-of-bounds memory comparison with specially crafted message channel request (CVE-2019-3862) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section.",
                                "fixedby": "0:1.4.3-12.el7_6.3",
                                "link": "https://access.redhat.com/errata/RHSA-2019:1884",
                                "metadata": "null",
                                "name": "RHSA-2019:1884",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            },
                            {
                                "description": "The libssh2 packages provide a library that implements the SSH2 protocol. The following packages have been upgraded to a later upstream version: libssh2 (1.8.0). (BZ#1592784) Security Fix(es): * libssh2: Zero-byte allocation with a specially crafted SFTP packed leading to an out-of-bounds read (CVE-2019-3858) * libssh2: Out-of-bounds reads with specially crafted SSH packets (CVE-2019-3861) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.7 Release Notes linked from the References section.",
                                "fixedby": "0:1.8.0-3.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2019:2136",
                                "metadata": "null",
                                "name": "RHSA-2019:2136",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            }
                        ]
                    },
                    {
                        "name": "python-libs",
                        "namespaceName": "centos:7",
                        "version": "2.7.5-48.el7",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "Python is an interpreted, interactive, object-oriented programming language, which includes modules, classes, exceptions, very high level dynamic data types and dynamic typing. Python supports interfaces to many system calls and libraries, as well as to various windowing systems. Security Fix(es): * A flaw was found in the way the DES/3DES cipher was used as part of the TLS/SSL protocol. A man-in-the-middle attacker could use this flaw to recover some plaintext data by capturing large amounts of encrypted traffic between TLS/SSL server and client if the communication used a DES/3DES based ciphersuite. (CVE-2016-2183) Note: This update modifies the Python ssl module to disable 3DES cipher suites by default. Red Hat would like to thank OpenVPN for reporting this issue. Upstream acknowledges Karthikeyan Bhargavan (Inria) and Gaëtan Leurent (Inria) as the original reporters.",
                                "fixedby": "0:2.7.5-69.el7_5",
                                "link": "https://access.redhat.com/errata/RHSA-2018:2123",
                                "metadata": "null",
                                "name": "RHSA-2018:2123",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            },
                            {
                                "description": "Python is an interpreted, interactive, object-oriented programming language, which includes modules, classes, exceptions, very high level dynamic data types and dynamic typing. Python supports interfaces to many system calls and libraries, as well as to various windowing systems. Security Fix(es): * python: DOS via regular expression backtracking in difflib.IS_LINE_JUNK method in difflib (CVE-2018-1061) * python: DOS via regular expression catastrophic backtracking in apop() method in pop3lib (CVE-2018-1060) For more details about the security issue(s), including the impact, a CVSS score, and other related information, refer to the CVE page(s) listed in the References section. Red Hat would like to thank the Python security response team for reporting these issues. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.6 Release Notes linked from the References section.",
                                "fixedby": "0:2.7.5-76.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2018:3041",
                                "metadata": "null",
                                "name": "RHSA-2018:3041",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            },
                            {
                                "description": "Python is an interpreted, interactive, object-oriented programming language, which includes modules, classes, exceptions, very high level dynamic data types and dynamic typing. Python supports interfaces to many system calls and libraries, as well as to various windowing systems. Security Fix(es): * python: Information Disclosure due to urlsplit improper NFKC normalization (CVE-2019-9636) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section.",
                                "fixedby": "0:2.7.5-77.el7_6",
                                "link": "https://access.redhat.com/errata/RHSA-2019:0710",
                                "metadata": "null",
                                "name": "RHSA-2019:0710",
                                "namespaceName": "centos:7",
                                "severity": "High"
                            },
                            {
                                "description": "Python is an interpreted, interactive, object-oriented programming language, which includes modules, classes, exceptions, very high level dynamic data types and dynamic typing. Python supports interfaces to many system calls and libraries, as well as to various windowing systems. Security Fix(es): * python: regression of CVE-2019-9636 due to functional fix to allow port numbers in netloc (CVE-2019-10160) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section.",
                                "fixedby": "0:2.7.5-80.el7_6",
                                "link": "https://access.redhat.com/errata/RHSA-2019:1587",
                                "metadata": "null",
                                "name": "RHSA-2019:1587",
                                "namespaceName": "centos:7",
                                "severity": "High"
                            },
                            {
                                "description": "Python is an interpreted, interactive, object-oriented programming language, which includes modules, classes, exceptions, very high level dynamic data types and dynamic typing. Python supports interfaces to many system calls and libraries, as well as to various windowing systems. Security Fix(es): * python: Missing salt initialization in _elementtree.c module (CVE-2018-14647) * python: NULL pointer dereference using a specially crafted X509 certificate (CVE-2019-5010) * python: CRLF injection via the query part of the url passed to urlopen() (CVE-2019-9740) * python: CRLF injection via the path part of the url passed to urlopen() (CVE-2019-9947) * python: Undocumented local_file protocol allows remote attackers to bypass protection mechanisms (CVE-2019-9948) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.7 Release Notes linked from the References section.",
                                "fixedby": "0:2.7.5-86.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2019:2030",
                                "metadata": "null",
                                "name": "RHSA-2019:2030",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            },
                            {
                                "description": "Python is an interpreted, interactive, object-oriented programming language, which includes modules, classes, exceptions, very high level dynamic data types and dynamic typing. Python supports interfaces to many system calls and libraries, as well as to various windowing systems. Security Fix(es): * python: Cookie domain check returns incorrect results (CVE-2018-20852) * python: email.utils.parseaddr wrongly parses email addresses (CVE-2019-16056) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.8 Release Notes linked from the References section.",
                                "fixedby": "0:2.7.5-88.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2020:1131",
                                "metadata": "null",
                                "name": "RHSA-2020:1131",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            },
                            {
                                "description": "Python is an interpreted, interactive, object-oriented programming language, which includes modules, classes, exceptions, very high level dynamic data types and dynamic typing. Python supports interfaces to many system calls and libraries, as well as to various windowing systems. Security Fix(es): * The Python standard library HTTP client modules (such as httplib or urllib) did not perform verification of TLS/SSL certificates when connecting to HTTPS servers. A man-in-the-middle attacker could use this flaw to hijack connections and eavesdrop or modify transferred data. (CVE-2014-9365) Note: The Python standard library was updated to enable certificate verification by default. Refer to the Knowledgebase article 2039753 linked to in the References section for further details about this change. (BZ#1219110) Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.4 Release Notes linked from the References section.",
                                "fixedby": "0:2.7.5-58.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2017:1868",
                                "metadata": "null",
                                "name": "RHSA-2017:1868",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            }
                        ]
                    },
                    {
                        "name": "libblkid",
                        "namespaceName": "centos:7",
                        "version": "2.23.2-33.el7",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "The util-linux packages contain a large variety of low-level system utilities that are necessary for a Linux system to function. Among others, these include the fdisk configuration tool and the login program. Security Fix(es): * A race condition was found in the way su handled the management of child processes. A local authenticated attacker could use this flaw to kill other processes with root privileges under specific conditions. (CVE-2017-2616) Red Hat would like to thank Tobias Stöckmann for reporting this issue. Bug Fix(es): * The \"findmnt --target \u003cpath\u003e\" command prints all file systems where the mount point directory is \u003cpath\u003e. Previously, when used in the chroot environment, \"findmnt --target \u003cpath\u003e\" incorrectly displayed all mount points. The command has been fixed so that it now checks the mount point path and returns information only for the relevant mount point. (BZ#1414481)",
                                "fixedby": "0:2.23.2-33.el7_3.2",
                                "link": "https://access.redhat.com/errata/RHSA-2017:0907",
                                "metadata": "null",
                                "name": "RHSA-2017:0907",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            }
                        ]
                    },
                    {
                        "name": "libuuid",
                        "namespaceName": "centos:7",
                        "version": "2.23.2-33.el7",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "The util-linux packages contain a large variety of low-level system utilities that are necessary for a Linux system to function. Among others, these include the fdisk configuration tool and the login program. Security Fix(es): * A race condition was found in the way su handled the management of child processes. A local authenticated attacker could use this flaw to kill other processes with root privileges under specific conditions. (CVE-2017-2616) Red Hat would like to thank Tobias Stöckmann for reporting this issue. Bug Fix(es): * The \"findmnt --target \u003cpath\u003e\" command prints all file systems where the mount point directory is \u003cpath\u003e. Previously, when used in the chroot environment, \"findmnt --target \u003cpath\u003e\" incorrectly displayed all mount points. The command has been fixed so that it now checks the mount point path and returns information only for the relevant mount point. (BZ#1414481)",
                                "fixedby": "0:2.23.2-33.el7_3.2",
                                "link": "https://access.redhat.com/errata/RHSA-2017:0907",
                                "metadata": "null",
                                "name": "RHSA-2017:0907",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            }
                        ]
                    },
                    {
                        "name": "krb5-libs",
                        "namespaceName": "centos:7",
                        "version": "1.14.1-27.el7_3",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "Kerberos is a network authentication system, which can improve the security of your network by eliminating the insecure practice of sending passwords over the network in unencrypted form. It allows clients and servers to authenticate to each other with the help of a trusted third party, the Kerberos key distribution center (KDC). Security Fix(es): * krb5: Authentication bypass by improper validation of certificate EKU and SAN (CVE-2017-7562) * krb5: Invalid S4U2Self or S4U2Proxy request causes assertion failure (CVE-2017-11368) For more details about the security issue(s), including the impact, a CVSS score, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.5 Release Notes linked from the References section.",
                                "fixedby": "0:1.15.1-18.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2018:0666",
                                "metadata": "null",
                                "name": "RHSA-2018:0666",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            },
                            {
                                "description": "Kerberos is a network authentication system, which can improve the security of your network by eliminating the insecure practice of sending passwords over the network in unencrypted form. It allows clients and servers to authenticate to each other with the help of a trusted third party, the Kerberos key distribution center (KDC). Security Fix(es): * krb5: null dereference in kadmind or DN container check bypass by supplying special crafted data (CVE-2018-5729) * krb5: DN container check bypass by supplying special crafted data (CVE-2018-5730) For more details about the security issue(s), including the impact, a CVSS score, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.6 Release Notes linked from the References section.",
                                "fixedby": "0:1.15.1-34.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2018:3071",
                                "metadata": "null",
                                "name": "RHSA-2018:3071",
                                "namespaceName": "centos:7",
                                "severity": "Low"
                            },
                            {
                                "description": "Kerberos is a network authentication system, which can improve the security of your network by eliminating the insecure practice of sending passwords over the network in unencrypted form. It allows clients and servers to authenticate to each other with the help of a trusted third party, the Kerberos key distribution center (KDC). This update fixes the following bug: * KDC and keytab can disagree on kvno after update (BZ#1732743)",
                                "fixedby": "0:1.15.1-37.el7_7.2",
                                "link": "https://access.redhat.com/errata/RHBA-2019:2599",
                                "metadata": "null",
                                "name": "RHBA-2019:2599",
                                "namespaceName": "centos:7",
                                "severity": "Unknown"
                            }
                        ]
                    },
                    {
                        "name": "shared-mime-info",
                        "namespaceName": "centos:7",
                        "version": "1.1-9.el7",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "GNOME is the default desktop environment of Red Hat Enterprise Linux. Security Fix(es): * gnome-shell: partial lock screen bypass (CVE-2019-3820) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.8 Release Notes linked from the References section.",
                                "fixedby": "0:1.8-5.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2020:1021",
                                "metadata": "null",
                                "name": "RHSA-2020:1021",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            }
                        ]
                    },
                    {
                        "name": "bash",
                        "namespaceName": "centos:7",
                        "version": "4.2.46-21.el7_3",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "The bash packages provide Bash (Bourne-again shell), which is the default shell for Red Hat Enterprise Linux. Security Fix(es): * bash: BASH_CMD is writable in restricted bash shells (CVE-2019-9924) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.8 Release Notes linked from the References section.",
                                "fixedby": "0:4.2.46-34.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2020:1113",
                                "metadata": "null",
                                "name": "RHSA-2020:1113",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            },
                            {
                                "description": "The bash packages provide Bash (Bourne-again shell), which is the default shell for Red Hat Enterprise Linux. Security Fix(es): * An arbitrary command injection flaw was found in the way bash processed the hostname value. A malicious DHCP server could use this flaw to execute arbitrary commands on the DHCP client machines running bash under specific circumstances. (CVE-2016-0634) * An arbitrary command injection flaw was found in the way bash processed the SHELLOPTS and PS4 environment variables. A local, authenticated attacker could use this flaw to exploit poorly written setuid programs to elevate their privileges under certain circumstances. (CVE-2016-7543) * A denial of service flaw was found in the way bash handled popd commands. A poorly written shell script could cause bash to crash resulting in a local denial of service limited to a specific bash session. (CVE-2016-9401) Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.4 Release Notes linked from the References section.",
                                "fixedby": "0:4.2.46-28.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2017:1931",
                                "metadata": "null",
                                "name": "RHSA-2017:1931",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            }
                        ]
                    },
                    {
                        "name": "elfutils-libs",
                        "namespaceName": "centos:7",
                        "version": "0.166-2.el7",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "The elfutils packages contain a number of utility programs and libraries related to the creation and maintenance of executable code. The following packages have been upgraded to a later upstream version: elfutils (0.176). (BZ#1676504) Security Fix(es): * elfutils: Heap-based buffer over-read in libdw/dwarf_getaranges.c:dwarf_getaranges() via crafted file (CVE-2018-16062) * elfutils: Double-free due to double decompression of sections in crafted ELF causes crash (CVE-2018-16402) * elfutils: Heap-based buffer over-read in libdw/dwarf_getabbrev.c and libwd/dwarf_hasattr.c causes crash (CVE-2018-16403) * elfutils: invalid memory address dereference was discovered in dwfl_segment_report_module.c in libdwfl (CVE-2018-18310) * elfutils: eu-size cannot handle recursive ar files (CVE-2018-18520) * elfutils: Divide-by-zero in arlib_add_symbols function in arlib.c (CVE-2018-18521) * elfutils: heap-based buffer over-read in read_srclines in dwarf_getsrclines.c in libdw (CVE-2019-7149) * elfutils: segmentation fault in elf64_xlatetom in libelf/elf32_xlatetom.c (CVE-2019-7150) * elfutils: Out of bound write in elf_cvt_note in libelf/note_xlate.h (CVE-2019-7664) * elfutils: heap-based buffer over-read in function elf32_xlatetom in elf32_xlatetom.c (CVE-2019-7665) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.7 Release Notes linked from the References section.",
                                "fixedby": "0:0.176-2.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2019:2197",
                                "metadata": "null",
                                "name": "RHSA-2019:2197",
                                "namespaceName": "centos:7",
                                "severity": "Low"
                            }
                        ]
                    },
                    {
                        "name": "elfutils-libelf",
                        "namespaceName": "centos:7",
                        "version": "0.166-2.el7",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "The elfutils packages contain a number of utility programs and libraries related to the creation and maintenance of executable code. The following packages have been upgraded to a later upstream version: elfutils (0.176). (BZ#1676504) Security Fix(es): * elfutils: Heap-based buffer over-read in libdw/dwarf_getaranges.c:dwarf_getaranges() via crafted file (CVE-2018-16062) * elfutils: Double-free due to double decompression of sections in crafted ELF causes crash (CVE-2018-16402) * elfutils: Heap-based buffer over-read in libdw/dwarf_getabbrev.c and libwd/dwarf_hasattr.c causes crash (CVE-2018-16403) * elfutils: invalid memory address dereference was discovered in dwfl_segment_report_module.c in libdwfl (CVE-2018-18310) * elfutils: eu-size cannot handle recursive ar files (CVE-2018-18520) * elfutils: Divide-by-zero in arlib_add_symbols function in arlib.c (CVE-2018-18521) * elfutils: heap-based buffer over-read in read_srclines in dwarf_getsrclines.c in libdw (CVE-2019-7149) * elfutils: segmentation fault in elf64_xlatetom in libelf/elf32_xlatetom.c (CVE-2019-7150) * elfutils: Out of bound write in elf_cvt_note in libelf/note_xlate.h (CVE-2019-7664) * elfutils: heap-based buffer over-read in function elf32_xlatetom in elf32_xlatetom.c (CVE-2019-7665) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.7 Release Notes linked from the References section.",
                                "fixedby": "0:0.176-2.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2019:2197",
                                "metadata": "null",
                                "name": "RHSA-2019:2197",
                                "namespaceName": "centos:7",
                                "severity": "Low"
                            }
                        ]
                    },
                    {
                        "name": "bind-license",
                        "namespaceName": "centos:7",
                        "version": "32:9.9.4-38.el7_3",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "The Berkeley Internet Name Domain (BIND) is an implementation of the Domain Name System (DNS) protocols. BIND includes a DNS server (named); a resolver library (routines for applications to use when interfacing with DNS); and tools for verifying that the DNS server is operating correctly. Security Fix(es): * A denial of service flaw was found in the way BIND handled a query response containing CNAME or DNAME resource records in an unusual order. A remote attacker could use this flaw to make named exit unexpectedly with an assertion failure via a specially crafted DNS response. (CVE-2017-3137) * A denial of service flaw was found in the way BIND handled query requests when using DNS64 with \"break-dnssec yes\" option. A remote attacker could use this flaw to make named exit unexpectedly with an assertion failure via a specially crafted DNS request. (CVE-2017-3136) Red Hat would like to thank ISC for reporting these issues. Upstream acknowledges Oleg Gorokhov (Yandex) as the original reporter of CVE-2017-3136.",
                                "fixedby": "32:9.9.4-38.el7_3.3",
                                "link": "https://access.redhat.com/errata/RHSA-2017:1095",
                                "metadata": "null",
                                "name": "RHSA-2017:1095",
                                "namespaceName": "centos:7",
                                "severity": "High"
                            },
                            {
                                "description": "The Berkeley Internet Name Domain (BIND) is an implementation of the Domain Name System (DNS) protocols. BIND includes a DNS server (named); a resolver library (routines for applications to use when interfacing with DNS); and tools for verifying that the DNS server is operating correctly. Security Fix(es): * A flaw was found in the way BIND handled TSIG authentication for dynamic updates. A remote attacker able to communicate with an authoritative BIND server could use this flaw to manipulate the contents of a zone, by forging a valid TSIG or SIG(0) signature for a dynamic update request. (CVE-2017-3143) * A flaw was found in the way BIND handled TSIG authentication of AXFR requests. A remote attacker, able to communicate with an authoritative BIND server, could use this flaw to view the entire contents of a zone by sending a specially constructed request packet. (CVE-2017-3142) Red Hat would like to thank Internet Systems Consortium for reporting these issues. Upstream acknowledges Clement Berthaux (Synacktiv) as the original reporter of these issues. Bug Fix(es): * ICANN is planning to perform a Root Zone DNSSEC Key Signing Key (KSK) rollover during October 2017. Maintaining an up-to-date KSK, by adding the new root zone KSK, is essential for ensuring that validating DNS resolvers continue to function following the rollover. (BZ#1459649)",
                                "fixedby": "32:9.9.4-50.el7_3.1",
                                "link": "https://access.redhat.com/errata/RHSA-2017:1680",
                                "metadata": "null",
                                "name": "RHSA-2017:1680",
                                "namespaceName": "centos:7",
                                "severity": "High"
                            },
                            {
                                "description": "The Berkeley Internet Name Domain (BIND) is an implementation of the Domain Name System (DNS) protocols. BIND includes a DNS server (named); a resolver library (routines for applications to use when interfacing with DNS); and tools for verifying that the DNS server is operating correctly. Security Fix(es): * A use-after-free flaw leading to denial of service was found in the way BIND internally handled cleanup operations on upstream recursion fetch contexts. A remote attacker could potentially use this flaw to make named, acting as a DNSSEC validating resolver, exit unexpectedly with an assertion failure via a specially crafted DNS request. (CVE-2017-3145) Red Hat would like to thank ISC for reporting this issue. Upstream acknowledges Jayachandran Palanisamy (Cygate AB) as the original reporter.",
                                "fixedby": "32:9.9.4-51.el7_4.2",
                                "link": "https://access.redhat.com/errata/RHSA-2018:0102",
                                "metadata": "null",
                                "name": "RHSA-2018:0102",
                                "namespaceName": "centos:7",
                                "severity": "High"
                            },
                            {
                                "description": "The Berkeley Internet Name Domain (BIND) is an implementation of the Domain Name System (DNS) protocols. BIND includes a DNS server (named); a resolver library (routines for applications to use when interfacing with DNS); and tools for verifying that the DNS server is operating correctly. Security Fix(es): * bind: processing of certain records when \"deny-answer-aliases\" is in use may trigger an assert leading to a denial of service (CVE-2018-5740) For more details about the security issue(s), including the impact, a CVSS score, and other related information, refer to the CVE page(s) listed in the References section. Red Hat would like to thank ISC for reporting this issue. Upstream acknowledges Tony Finch (University of Cambridge) as the original reporter.",
                                "fixedby": "32:9.9.4-61.el7_5.1",
                                "link": "https://access.redhat.com/errata/RHSA-2018:2570",
                                "metadata": "null",
                                "name": "RHSA-2018:2570",
                                "namespaceName": "centos:7",
                                "severity": "High"
                            },
                            {
                                "description": "The Berkeley Internet Name Domain (BIND) is an implementation of the Domain Name System (DNS) protocols. BIND includes a DNS server (named); a resolver library (routines for applications to use when interfacing with DNS); and tools for verifying that the DNS server is operating correctly. Security Fix(es): * bind: Crash from assertion error when debug log level is 10 and log entries meet buffer boundary (CVE-2018-5742) For more details about the security issue(s), including the impact, a CVSS score, and other related information, refer to the CVE page(s) listed in the References section.",
                                "fixedby": "32:9.9.4-73.el7_6",
                                "link": "https://access.redhat.com/errata/RHSA-2019:0194",
                                "metadata": "null",
                                "name": "RHSA-2019:0194",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            },
                            {
                                "description": "The Berkeley Internet Name Domain (BIND) is an implementation of the Domain Name System (DNS) protocols. BIND includes a DNS server (named); a resolver library (routines for applications to use when interfacing with DNS); and tools for verifying that the DNS server is operating correctly. Security Fix(es): * bind: Limiting simultaneous TCP clients is ineffective (CVE-2018-5743) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section.",
                                "fixedby": "32:9.9.4-74.el7_6.1",
                                "link": "https://access.redhat.com/errata/RHSA-2019:1294",
                                "metadata": "null",
                                "name": "RHSA-2019:1294",
                                "namespaceName": "centos:7",
                                "severity": "High"
                            },
                            {
                                "description": "The Berkeley Internet Name Domain (BIND) is an implementation of the Domain Name System (DNS) protocols. BIND includes a DNS server (named); a resolver library (routines for applications to use when interfacing with DNS); and tools for verifying that the DNS server is operating correctly. The following packages have been upgraded to a later upstream version: bind (9.11.4). (BZ#1640561) Security Fix(es): * bind: Incorrect documentation of krb5-subdomain and ms-subdomain update policies (CVE-2018-5741) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.7 Release Notes linked from the References section.",
                                "fixedby": "32:9.11.4-9.P2.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2019:2057",
                                "metadata": "null",
                                "name": "RHSA-2019:2057",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            },
                            {
                                "description": "The Berkeley Internet Name Domain (BIND) is an implementation of the Domain Name System (DNS) protocols. BIND includes a DNS server (named); a resolver library (routines for applications to use when interfacing with DNS); and tools for verifying that the DNS server is operating correctly. Security Fix(es): * bind: TCP Pipelining doesn't limit TCP clients on a single connection (CVE-2019-6477) * bind: An assertion failure if a trust anchor rolls over to an unsupported key algorithm when using managed-keys (CVE-2018-5745) * bind: Controls for zone transfers may not be properly applied to DLZs if the zones are writable (CVE-2019-6465) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.8 Release Notes linked from the References section.",
                                "fixedby": "32:9.11.4-16.P2.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2020:1061",
                                "metadata": "null",
                                "name": "RHSA-2020:1061",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            },
                            {
                                "description": "The Berkeley Internet Name Domain (BIND) is an implementation of the Domain Name System (DNS) protocols. BIND includes a DNS server (named); a resolver library (routines for applications to use when interfacing with DNS); and tools for verifying that the DNS server is operating correctly. Security Fix(es): * A denial of service flaw was found in the way BIND handled query responses when both DNS64 and RPZ were used. A remote attacker could use this flaw to make named exit unexpectedly with an assertion failure or a null pointer dereference via a specially crafted DNS response. (CVE-2017-3135) Red Hat would like to thank ISC for reporting this issue. Upstream acknowledges Ramesh Damodaran (Infoblox) and Aliaksandr Shubnik (Infoblox) as the original reporter.",
                                "fixedby": "32:9.9.4-38.el7_3.2",
                                "link": "https://access.redhat.com/errata/RHSA-2017:0276",
                                "metadata": "null",
                                "name": "RHSA-2017:0276",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            },
                            {
                                "description": "The Berkeley Internet Name Domain (BIND) is an implementation of the Domain Name System (DNS) protocols. BIND includes a DNS server (named); a resolver library (routines for applications to use when interfacing with DNS); and tools for verifying that the DNS server is operating correctly. Security Fix(es): * A denial of service flaw was found in the way BIND processed a response to an ANY query. A remote attacker could use this flaw to make named exit unexpectedly with an assertion failure via a specially crafted DNS response. (CVE-2016-9131) * A denial of service flaw was found in the way BIND handled a query response containing inconsistent DNSSEC information. A remote attacker could use this flaw to make named exit unexpectedly with an assertion failure via a specially crafted DNS response. (CVE-2016-9147) * A denial of service flaw was found in the way BIND handled an unusually-formed DS record response. A remote attacker could use this flaw to make named exit unexpectedly with an assertion failure via a specially crafted DNS response. (CVE-2016-9444) Red Hat would like to thank ISC for reporting these issues.",
                                "fixedby": "32:9.9.4-38.el7_3.1",
                                "link": "https://access.redhat.com/errata/RHSA-2017:0062",
                                "metadata": "null",
                                "name": "RHSA-2017:0062",
                                "namespaceName": "centos:7",
                                "severity": "High"
                            },
                            {
                                "description": "The Berkeley Internet Name Domain (BIND) is an implementation of the Domain Name System (DNS) protocols. BIND includes a DNS server (named); a resolver library (routines for applications to use when interfacing with DNS); and tools for verifying that the DNS server is operating correctly. For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.4 Release Notes linked from the References section. Users of bind are advised to upgrade to these updated packages.",
                                "fixedby": "32:9.9.4-50.el7",
                                "link": "https://access.redhat.com/errata/RHBA-2017:1767",
                                "metadata": "null",
                                "name": "RHBA-2017:1767",
                                "namespaceName": "centos:7",
                                "severity": "Unknown"
                            }
                        ]
                    },
                    {
                        "name": "nss-softokn",
                        "namespaceName": "centos:7",
                        "version": "3.16.2.3-14.4.el7",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "Network Security Services (NSS) is a set of libraries designed to support the cross-platform development of security-enabled client and server applications. Netscape Portable Runtime (NSPR) provides platform independence for non-GUI operating system facilities. The following packages have been upgraded to a later upstream version: nss (3.44.0), nss-softokn (3.44.0), nss-util (3.44.0), nspr (4.21.0). (BZ#1645231, BZ#1692269, BZ#1692271, BZ#1692274) Security Fix(es): * ROHNP: Key Extraction Side Channel in Multiple Crypto Libraries (CVE-2018-0495) * nss: Cache side-channel variant of the Bleichenbacher attack (CVE-2018-12404) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.7 Release Notes linked from the References section.",
                                "fixedby": "0:3.44.0-5.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2019:2237",
                                "metadata": "null",
                                "name": "RHSA-2019:2237",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            },
                            {
                                "description": "Network Security Services (NSS) is a set of libraries designed to support the cross-platform development of security-enabled client and server applications. The nss-softokn package provides the Network Security Services Softoken Cryptographic Module. The nss-util packages provide utilities for use with the Network Security Services (NSS) libraries. Security Fix(es): * nss: Out-of-bounds write when passing an output buffer smaller than the block size to NSC_EncryptUpdate (CVE-2019-11745) * nss: Empty or malformed p256-ECDH public keys may trigger a segmentation fault (CVE-2019-11729) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section.",
                                "fixedby": "0:3.44.0-8.el7_7",
                                "link": "https://access.redhat.com/errata/RHSA-2019:4190",
                                "metadata": "null",
                                "name": "RHSA-2019:4190",
                                "namespaceName": "centos:7",
                                "severity": "High"
                            }
                        ]
                    },
                    {
                        "name": "setup",
                        "namespaceName": "centos:7",
                        "version": "2.8.71-7.el7",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "The setup package contains a set of important default system configuration and setup files. Examples include /etc/passwd, /etc/group, and /etc/profile. Other examples are the default lists of reserved user IDs, reserved ports, reserved protocols, allowed shells, allowed secure terminals. Security Fix(es): * setup: nologin listed in /etc/shells violates security expectations (CVE-2018-1113) For more details about the security issue(s), including the impact, a CVSS score, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.6 Release Notes linked from the References section.",
                                "fixedby": "0:2.8.71-10.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2018:3249",
                                "metadata": "null",
                                "name": "RHSA-2018:3249",
                                "namespaceName": "centos:7",
                                "severity": "Low"
                            }
                        ]
                    },
                    {
                        "name": "sqlite",
                        "namespaceName": "centos:7",
                        "version": "3.7.17-8.el7",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "SQLite is a C library that implements an SQL database engine. A large subset of SQL92 is supported. A complete database is stored in a single disk file. The API is designed for convenience and ease of use. Applications that link against SQLite can enjoy the power and flexibility of an SQL database without the administrative hassles of supporting a separate database server. Security Fix(es): * sqlite: fts3: improve shadow table corruption detection (CVE-2019-13734) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section.",
                                "fixedby": "0:3.7.17-8.el7_7.1",
                                "link": "https://access.redhat.com/errata/RHSA-2020:0227",
                                "metadata": "null",
                                "name": "RHSA-2020:0227",
                                "namespaceName": "centos:7",
                                "severity": "High"
                            }
                        ]
                    },
                    {
                        "name": "libmount",
                        "namespaceName": "centos:7",
                        "version": "2.23.2-33.el7",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "The util-linux packages contain a large variety of low-level system utilities that are necessary for a Linux system to function. Among others, these include the fdisk configuration tool and the login program. Security Fix(es): * A race condition was found in the way su handled the management of child processes. A local authenticated attacker could use this flaw to kill other processes with root privileges under specific conditions. (CVE-2017-2616) Red Hat would like to thank Tobias Stöckmann for reporting this issue. Bug Fix(es): * The \"findmnt --target \u003cpath\u003e\" command prints all file systems where the mount point directory is \u003cpath\u003e. Previously, when used in the chroot environment, \"findmnt --target \u003cpath\u003e\" incorrectly displayed all mount points. The command has been fixed so that it now checks the mount point path and returns information only for the relevant mount point. (BZ#1414481)",
                                "fixedby": "0:2.23.2-33.el7_3.2",
                                "link": "https://access.redhat.com/errata/RHSA-2017:0907",
                                "metadata": "null",
                                "name": "RHSA-2017:0907",
                                "namespaceName": "centos:7",
                                "severity": "Medium"
                            }
                        ]
                    },
                    {
                        "name": "file-libs",
                        "namespaceName": "centos:7",
                        "version": "5.11-33.el7",
                        "versionformat": "rpm",
                        "vulnerabilities": [
                            {
                                "description": "The file command is used to identify a particular file according to the type of data the file contains. It can identify many different file types, including Executable and Linkable Format (ELF) binary files, system libraries, RPM packages, and different graphics formats. Security Fix(es): * file: out-of-bounds read via a crafted ELF file (CVE-2018-10360) For more details about the security issue(s), including the impact, a CVSS score, acknowledgments, and other related information, refer to the CVE page(s) listed in the References section. Additional Changes: For detailed information on changes in this release, see the Red Hat Enterprise Linux 7.8 Release Notes linked from the References section.",
                                "fixedby": "0:5.11-36.el7",
                                "link": "https://access.redhat.com/errata/RHSA-2020:1022",
                                "metadata": "null",
                                "name": "RHSA-2020:1022",
                                "namespaceName": "centos:7",
                                "severity": "Low"
                            }
                        ]
                    }
                ],
                "image": "quay.io/app-sre/centos",
                "manifest": "sha256:a42f741b046c974973052d2453ecbb672b62d4c45ead2eda69b3c43d3763abf9"
            },
            "status": {
                "affectedPods": {
                    "cso/sleep2-65844c6b58-2q2s5": [
                        "cri-o://9e3df8f21b8f5d0879a90fae4667f8f19757f691a4ec2b338913b3db91d39bee",
                        "cri-o://088f351ef35c98498353882dcb83aecd42d5f1c09e71b78c6c8e3b9dff8a0a7b"
                    ],
                    "cso/sleep2-65844c6b58-qlng8": [
                        "cri-o://4ddf5f548a1f7236135b91f6ba25507d3fa7f2859f713bfe36f6ab3631ff81a6",
                        "cri-o://90d0f3cfad21752f8f3006b571c5b4cad181c650201683ca686d45a095c10ec8"
                    ]
                },
                "criticalCount": 4,
                "fixableCount": 128,
                "highCount": 36,
                "highestSeverity": "Critical",
                "lastUpdate": "2020-05-22 15:32:43.176797137 +0000 UTC",
                "lowCount": 16,
                "mediumCount": 67,
                "unknownCount": 5
            }
        }
    ],
    "kind": "List",
    "metadata": {
        "resourceVersion": "",
        "selfLink": ""
    }
}
"""
