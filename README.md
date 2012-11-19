# Snapshot Link

## Overview

``cass_snapshot_link`` is a script that creates [symbolic links](http://en.wikipedia.org/wiki/Symbolic_links) to join together a snapshot created by Cassandra 1.1.

In Cassandra 1.1 the on disk layout for files was changed to make it easier to use SSD storage for select Column Families. The change put the files for each Column Family into it's own directory, snapshots are created in the Column Family directory.

## Installation

*Note:* The code uses [argparse](http://docs.python.org/2/library/argparse.html), which is part of the standard library in Python 2.7 and 3.2. The installer tries to install the package for previous Python versions, let me know if I got it wrong. 

### Installation from source
 
Download the package and either install using [pip](http://www.pip-installer.org/):

`pip install cass_snapshot_link/`

Or using the default python package management:

`python setup.py install`

Or you can just use it as a uninstalled script.

## Usage

It's all on the command line. 

```
usage: cass_snapshot_link [-h] [--data-dir DATA_DIR] [--link-dir LINK_DIR]
                          [--keyspace [KEYSPACE [KEYSPACE ...]]] [--all]
                          [--replace-existing] [--dry-run] [--no-logging]
                          [--log-level {FATAL,CRITICAL,ERROR,WARN,INFO,DEBUG}]
                          [--log-file LOG_FILE]
                          [snapshot_name]

Sym link Cassandra 1.1 snapshots.

positional arguments:
  snapshot_name         Name of the snapshot to link, optional if --all is
                        used.

optional arguments:
  -h, --help            show this help message and exit
  --data-dir DATA_DIR   Path to the cassandra data directory (default
                        /var/lib/cassandra/data).
  --link-dir LINK_DIR   Directory to create the snapshot links in (default
                        /var/lib/cassandra/data).
  --keyspace [KEYSPACE [KEYSPACE ...]]
                        Name of the keyspaces to link from, if not specified
                        links all.
  --all                 Link all found snapshots.
  --replace-existing    Replace existing links, otherwise do not link.
  --dry-run             Do not change anything.
  --no-logging          Disable logging.
  --log-level {FATAL,CRITICAL,ERROR,WARN,INFO,DEBUG}
                        Logging level default (INFO).
  --log-file LOG_FILE   Logging file (default ./cass_snapshot_link.log).

Creates a directory of sym links for one or all snapshots 
    for names or all keyspaces. 

    In Cassandra 1.1 the files for a Column Family are located in their own 
    data directory, and the snapshots are located within those.

    This script creates links as follows:

    snapshots/<snapshot_name>/<keyspace_name>/<cf_name>

    For example in the directory /var/lib/cassandra/data/snapshots/foo/system:

    LocationInfo -> /var/lib/cassandra/data/system/LocationInfo/snapshots/foo
    Versions -> /var/lib/cassandra/data/system/Versions/snapshots/foo
```

For example:

Link the ``foo`` snapshot:

```
$ ./cass_snapshot_link foo
Linked:
Linked /var/lib/cassandra/data/snapshots/foo/system/LocationInfo to /var/lib/cassandra/data/system/LocationInfo/snapshots/foo
Linked /var/lib/cassandra/data/snapshots/foo/system/Versions to /var/lib/cassandra/data/system/Versions/snapshots/foo
```

Results in:

```
$ cd /var/lib/cassandra/data/snapshots/foo/system
$ ls -lah
total 16
drwxr-xr-x  4 aaron  wheel   136B 19 Nov 16:07 .
drwxr-xr-x  3 aaron  wheel   102B 19 Nov 16:07 ..
lrwxr-xr-x  1 aaron  wheel    57B 19 Nov 16:07 LocationInfo -> /var/lib/cassandra/data/system/LocationInfo/snapshots/foo
lrwxr-xr-x  1 aaron  wheel    53B 19 Nov 16:07 Versions -> /var/lib/cassandra/data/system/Versions/snapshots/foo
```

Link the ``super-test1`` snapshot for ``Keyspace1``:

```
$ ./cass_snapshot_link  super-test --keyspace Keyspace1
Linked:
Linked /var/lib/cassandra/data/snapshots/super-test/Keyspace1/Standard1 to /var/lib/cassandra/data/Keyspace1/Standard1/snapshots/super-test
```

Results in:

```
$ cd /var/lib/cassandra/data/snapshots/super-test/Keyspace1
$ ls -lah 
total 8
drwxr-xr-x  3 aaron  wheel   102B 19 Nov 16:11 .
drwxr-xr-x  3 aaron  wheel   102B 19 Nov 16:11 ..
lrwxr-xr-x  1 aaron  wheel    64B 19 Nov 16:11 Standard1 -> /var/lib/cassandra/data/Keyspace1/Standard1/snapshots/super-test
```

Link all snapshots, in all Keyspaces and replace any existing links:

```
$ ./cass_snapshot_link --all --replace-existing
Linked:
Replaced /var/lib/cassandra/data/snapshots/super-test/Keyspace1/Standard1 with link to /var/lib/cassandra/data/Keyspace1/Standard1/snapshots/super-test
Linked /var/lib/cassandra/data/snapshots/foo/cassandra/data to /var/lib/cassandra/data/snapshots/foo
Linked /var/lib/cassandra/data/snapshots/super-test/cassandra/data to /var/lib/cassandra/data/snapshots/super-test
Replaced /var/lib/cassandra/data/snapshots/foo/system/LocationInfo with link to /var/lib/cassandra/data/system/LocationInfo/snapshots/foo
Linked /var/lib/cassandra/data/snapshots/super-test/system/LocationInfo to /var/lib/cassandra/data/system/LocationInfo/snapshots/super-test
Linked /var/lib/cassandra/data/snapshots/super-test/system/schema_columnfamilies to /var/lib/cassandra/data/system/schema_columnfamilies/snapshots/super-test
Linked /var/lib/cassandra/data/snapshots/super-test/system/schema_keyspaces to /var/lib/cassandra/data/system/schema_keyspaces/snapshots/super-test
Replaced /var/lib/cassandra/data/snapshots/foo/system/Versions with link to /var/lib/cassandra/data/system/Versions/snapshots/foo
Linked /var/lib/cassandra/data/snapshots/super-test/system/Versions to /var/lib/cassandra/data/system/Versions/snapshots/super-test
```

Results in:

```
$ cd /var/lib/cassandra/data/snapshots/foo/system
$ ls -lah 
total 16
drwxr-xr-x  4 aaron  wheel   136B 19 Nov 16:15 .
drwxr-xr-x  4 aaron  wheel   136B 19 Nov 16:15 ..
lrwxr-xr-x  1 aaron  wheel    57B 19 Nov 16:15 LocationInfo -> /var/lib/cassandra/data/system/LocationInfo/snapshots/foo
lrwxr-xr-x  1 aaron  wheel    53B 19 Nov 16:15 Versions -> /var/lib/cassandra/data/system/Versions/snapshots/foo

$ cd /var/lib/cassandra/data/snapshots/super-test/Keyspace1
$ ls -lah 
total 8
drwxr-xr-x  3 aaron  wheel   102B 19 Nov 16:15 .
drwxr-xr-x  5 aaron  wheel   170B 19 Nov 16:15 ..
lrwxr-xr-x  1 aaron  wheel    64B 19 Nov 16:15 Standard1 -> /var/lib/cassandra/data/Keyspace1/Standard1/snapshots/super-test
```

Questions, Comments, and Help
-----------------------------

* Raise an issue on [github project](XX)
* IRC `#cassandra-ops` on `irc.freenode.net`
* Email the Cassandra [User List](http://cassandra.apache.org/)
