# Auto-generated at Mon, 15 Jun 2020 22:44:56 +0000 from pynefs/idl/rfc1813.x

import abc
from dataclasses import dataclass
import typing

from pynefs import rpchelp

TRUE = True
FALSE = False
NFS3_OK = 0
NFS3ERR_PERM = 1
NFS3ERR_NOENT = 2
NFS3ERR_IO = 5
NFS3ERR_NXIO = 6
NFS3ERR_ACCES = 13
NFS3ERR_EXIST = 17
NFS3ERR_XDEV = 18
NFS3ERR_NODEV = 19
NFS3ERR_NOTDIR = 20
NFS3ERR_ISDIR = 21
NFS3ERR_INVAL = 22
NFS3ERR_FBIG = 27
NFS3ERR_NOSPC = 28
NFS3ERR_ROFS = 30
NFS3ERR_MLINK = 31
NFS3ERR_NAMETOOLONG = 63
NFS3ERR_NOTEMPTY = 66
NFS3ERR_DQUOT = 69
NFS3ERR_STALE = 70
NFS3ERR_REMOTE = 71
NFS3ERR_BADHANDLE = 10001
NFS3ERR_NOT_SYNC = 10002
NFS3ERR_BAD_COOKIE = 10003
NFS3ERR_NOTSUPP = 10004
NFS3ERR_TOOSMALL = 10005
NFS3ERR_SERVERFAULT = 10006
NFS3ERR_BADTYPE = 10007
NFS3ERR_JUKEBOX = 10008
NF3REG = 1
NF3DIR = 2
NF3BLK = 3
NF3CHR = 4
NF3LNK = 5
NF3SOCK = 6
NF3FIFO = 7
DONT_CHANGE = 0
SET_TO_SERVER_TIME = 1
SET_TO_CLIENT_TIME = 2
UNSTABLE = 0
DATA_SYNC = 1
FILE_SYNC = 2
UNCHECKED = 0
GUARDED = 1
EXCLUSIVE = 2
MNT3_OK = 0
MNT3ERR_PERM = 1
MNT3ERR_NOENT = 2
MNT3ERR_IO = 5
MNT3ERR_ACCES = 13
MNT3ERR_NOTDIR = 20
MNT3ERR_INVAL = 22
MNT3ERR_NAMETOOLONG = 63
MNT3ERR_NOTSUPP = 10004
MNT3ERR_SERVERFAULT = 10006
NFS3_FHSIZE = 64
NFS3_COOKIEVERFSIZE = 8
NFS3_CREATEVERFSIZE = 8
NFS3_WRITEVERFSIZE = 8
uint64 = rpchelp.r_uhyper
int64 = rpchelp.r_hyper
uint32 = rpchelp.r_uint
int32 = rpchelp.r_int
filename3 = rpchelp.string(rpchelp.var, None)
nfspath3 = rpchelp.string(rpchelp.var, None)
fileid3 = uint64
cookie3 = uint64
cookieverf3 = rpchelp.opaque(rpchelp.fixed, NFS3_COOKIEVERFSIZE)
createverf3 = rpchelp.opaque(rpchelp.fixed, NFS3_CREATEVERFSIZE)
writeverf3 = rpchelp.opaque(rpchelp.fixed, NFS3_WRITEVERFSIZE)
uid3 = uint32
gid3 = uint32
size3 = uint64
offset3 = uint64
mode3 = uint32
count3 = uint32
nfsstat3 = rpchelp.r_int
ftype3 = rpchelp.r_int
specdata3 = rpchelp.struct('specdata3', [('specdata1', uint32), ('specdata2', uint32)])
nfs_fh3 = rpchelp.struct('nfs_fh3', [('data', rpchelp.opaque(rpchelp.var, NFS3_FHSIZE))])
nfstime3 = rpchelp.struct('nfstime3', [('seconds', uint32), ('nseconds', uint32)])
fattr3 = rpchelp.struct('fattr3', [('type', ftype3), ('mode', mode3), ('nlink', uint32), ('uid', uid3), ('gid', gid3), ('size', size3), ('used', size3), ('rdev', specdata3), ('fsid', uint64), ('fileid', fileid3), ('atime', nfstime3), ('mtime', nfstime3), ('ctime', nfstime3)])
post_op_attr = rpchelp.union('post_op_attr', rpchelp.r_bool, {TRUE: fattr3, FALSE: rpchelp.r_void})
wcc_attr = rpchelp.struct('wcc_attr', [('size', size3), ('mtime', nfstime3), ('ctime', nfstime3)])
pre_op_attr = rpchelp.union('pre_op_attr', rpchelp.r_bool, {TRUE: wcc_attr, FALSE: rpchelp.r_void})
wcc_data = rpchelp.struct('wcc_data', [('before', pre_op_attr), ('after', post_op_attr)])
post_op_fh3 = rpchelp.union('post_op_fh3', rpchelp.r_bool, {TRUE: nfs_fh3, FALSE: rpchelp.r_void})
time_how = rpchelp.r_int
set_mode3 = rpchelp.union('set_mode3', rpchelp.r_bool, {TRUE: mode3, None: rpchelp.r_void})
set_uid3 = rpchelp.union('set_uid3', rpchelp.r_bool, {TRUE: uid3, None: rpchelp.r_void})
set_gid3 = rpchelp.union('set_gid3', rpchelp.r_bool, {TRUE: gid3, None: rpchelp.r_void})
set_size3 = rpchelp.union('set_size3', rpchelp.r_bool, {TRUE: size3, None: rpchelp.r_void})
set_atime = rpchelp.union('set_atime', time_how, {SET_TO_CLIENT_TIME: nfstime3, None: rpchelp.r_void})
set_mtime = rpchelp.union('set_mtime', time_how, {SET_TO_CLIENT_TIME: nfstime3, None: rpchelp.r_void})
sattr3 = rpchelp.struct('sattr3', [('mode', set_mode3), ('uid', set_uid3), ('gid', set_gid3), ('size', set_size3), ('atime', set_atime), ('mtime', set_mtime)])
diropargs3 = rpchelp.struct('diropargs3', [('dir', nfs_fh3), ('name', filename3)])

GETATTR3args = rpchelp.struct('GETATTR3args', [('object', nfs_fh3)])
GETATTR3resok = rpchelp.struct('GETATTR3resok', [('obj_attributes', fattr3)])
GETATTR3res = rpchelp.union('GETATTR3res', nfsstat3, {NFS3_OK: GETATTR3resok, None: rpchelp.r_void})
sattrguard3 = rpchelp.union('sattrguard3', rpchelp.r_bool, {TRUE: nfstime3, FALSE: rpchelp.r_void})
SETATTR3args = rpchelp.struct('SETATTR3args', [('object', nfs_fh3), ('new_attributes', sattr3), ('guard', sattrguard3)])
SETATTR3resok = rpchelp.struct('SETATTR3resok', [('obj_wcc', wcc_data)])
SETATTR3resfail = rpchelp.struct('SETATTR3resfail', [('obj_wcc', wcc_data)])
SETATTR3res = rpchelp.union('SETATTR3res', nfsstat3, {NFS3_OK: SETATTR3resok, None: SETATTR3resfail})
LOOKUP3args = rpchelp.struct('LOOKUP3args', [('what', diropargs3)])
LOOKUP3resok = rpchelp.struct('LOOKUP3resok', [('object', nfs_fh3), ('obj_attributes', post_op_attr), ('dir_attributes', post_op_attr)])
LOOKUP3resfail = rpchelp.struct('LOOKUP3resfail', [('dir_attributes', post_op_attr)])
LOOKUP3res = rpchelp.union('LOOKUP3res', nfsstat3, {NFS3_OK: LOOKUP3resok, None: LOOKUP3resfail})
ACCESS3_READ = 0x0001
ACCESS3_LOOKUP = 0x0002
ACCESS3_MODIFY = 0x0004
ACCESS3_EXTEND = 0x0008
ACCESS3_DELETE = 0x0010
ACCESS3_EXECUTE = 0x0020
ACCESS3args = rpchelp.struct('ACCESS3args', [('object', nfs_fh3), ('access', uint32)])
ACCESS3resok = rpchelp.struct('ACCESS3resok', [('obj_attributes', post_op_attr), ('access', uint32)])
ACCESS3resfail = rpchelp.struct('ACCESS3resfail', [('obj_attributes', post_op_attr)])
ACCESS3res = rpchelp.union('ACCESS3res', nfsstat3, {NFS3_OK: ACCESS3resok, None: ACCESS3resfail})
READLINK3args = rpchelp.struct('READLINK3args', [('symlink', nfs_fh3)])
READLINK3resok = rpchelp.struct('READLINK3resok', [('symlink_attributes', post_op_attr), ('data', nfspath3)])
READLINK3resfail = rpchelp.struct('READLINK3resfail', [('symlink_attributes', post_op_attr)])
READLINK3res = rpchelp.union('READLINK3res', nfsstat3, {NFS3_OK: READLINK3resok, None: READLINK3resfail})
READ3args = rpchelp.struct('READ3args', [('file', nfs_fh3), ('offset', offset3), ('count', count3)])
READ3resok = rpchelp.struct('READ3resok', [('file_attributes', post_op_attr), ('count', count3), ('eof', rpchelp.r_bool), ('data', rpchelp.opaque(rpchelp.var, None))])
READ3resfail = rpchelp.struct('READ3resfail', [('file_attributes', post_op_attr)])
READ3res = rpchelp.union('READ3res', nfsstat3, {NFS3_OK: READ3resok, None: READ3resfail})
stable_how = rpchelp.r_int
WRITE3args = rpchelp.struct('WRITE3args', [('file', nfs_fh3), ('offset', offset3), ('count', count3), ('stable', stable_how), ('data', rpchelp.opaque(rpchelp.var, None))])
WRITE3resok = rpchelp.struct('WRITE3resok', [('file_wcc', wcc_data), ('count', count3), ('committed', stable_how), ('verf', writeverf3)])
WRITE3resfail = rpchelp.struct('WRITE3resfail', [('file_wcc', wcc_data)])
WRITE3res = rpchelp.union('WRITE3res', nfsstat3, {NFS3_OK: WRITE3resok, None: WRITE3resfail})
createmode3 = rpchelp.r_int
createhow3 = rpchelp.union('createhow3', createmode3, {UNCHECKED: sattr3, GUARDED: sattr3, EXCLUSIVE: createverf3})
CREATE3args = rpchelp.struct('CREATE3args', [('where', diropargs3), ('how', createhow3)])
CREATE3resok = rpchelp.struct('CREATE3resok', [('obj', post_op_fh3), ('obj_attributes', post_op_attr), ('dir_wcc', wcc_data)])
CREATE3resfail = rpchelp.struct('CREATE3resfail', [('dir_wcc', wcc_data)])
CREATE3res = rpchelp.union('CREATE3res', nfsstat3, {NFS3_OK: CREATE3resok, None: CREATE3resfail})
MKDIR3args = rpchelp.struct('MKDIR3args', [('where', diropargs3), ('attributes', sattr3)])
MKDIR3resok = rpchelp.struct('MKDIR3resok', [('obj', post_op_fh3), ('obj_attributes', post_op_attr), ('dir_wcc', wcc_data)])
MKDIR3resfail = rpchelp.struct('MKDIR3resfail', [('dir_wcc', wcc_data)])
MKDIR3res = rpchelp.union('MKDIR3res', nfsstat3, {NFS3_OK: MKDIR3resok, None: MKDIR3resfail})
symlinkdata3 = rpchelp.struct('symlinkdata3', [('symlink_attributes', sattr3), ('symlink_data', nfspath3)])
SYMLINK3args = rpchelp.struct('SYMLINK3args', [('where', diropargs3), ('symlink', symlinkdata3)])
SYMLINK3resok = rpchelp.struct('SYMLINK3resok', [('obj', post_op_fh3), ('obj_attributes', post_op_attr), ('dir_wcc', wcc_data)])
SYMLINK3resfail = rpchelp.struct('SYMLINK3resfail', [('dir_wcc', wcc_data)])
SYMLINK3res = rpchelp.union('SYMLINK3res', nfsstat3, {NFS3_OK: SYMLINK3resok, None: SYMLINK3resfail})
devicedata3 = rpchelp.struct('devicedata3', [('dev_attributes', sattr3), ('spec', specdata3)])
mknoddata3 = rpchelp.union('mknoddata3', ftype3, {NF3CHR: devicedata3, NF3BLK: devicedata3, NF3SOCK: sattr3, NF3FIFO: sattr3, None: rpchelp.r_void})
MKNOD3args = rpchelp.struct('MKNOD3args', [('where', diropargs3), ('what', mknoddata3)])
MKNOD3resok = rpchelp.struct('MKNOD3resok', [('obj', post_op_fh3), ('obj_attributes', post_op_attr), ('dir_wcc', wcc_data)])
MKNOD3resfail = rpchelp.struct('MKNOD3resfail', [('dir_wcc', wcc_data)])
MKNOD3res = rpchelp.union('MKNOD3res', nfsstat3, {NFS3_OK: MKNOD3resok, None: MKNOD3resfail})
REMOVE3args = rpchelp.struct('REMOVE3args', [('object', diropargs3)])
REMOVE3resok = rpchelp.struct('REMOVE3resok', [('dir_wcc', wcc_data)])
REMOVE3resfail = rpchelp.struct('REMOVE3resfail', [('dir_wcc', wcc_data)])
REMOVE3res = rpchelp.union('REMOVE3res', nfsstat3, {NFS3_OK: REMOVE3resok, None: REMOVE3resfail})
RMDIR3args = rpchelp.struct('RMDIR3args', [('object', diropargs3)])
RMDIR3resok = rpchelp.struct('RMDIR3resok', [('dir_wcc', wcc_data)])
RMDIR3resfail = rpchelp.struct('RMDIR3resfail', [('dir_wcc', wcc_data)])
RMDIR3res = rpchelp.union('RMDIR3res', nfsstat3, {NFS3_OK: RMDIR3resok, None: RMDIR3resfail})
RENAME3args = rpchelp.struct('RENAME3args', [('from_', diropargs3), ('to', diropargs3)])
RENAME3resok = rpchelp.struct('RENAME3resok', [('fromdir_wcc', wcc_data), ('todir_wcc', wcc_data)])
RENAME3resfail = rpchelp.struct('RENAME3resfail', [('fromdir_wcc', wcc_data), ('todir_wcc', wcc_data)])
RENAME3res = rpchelp.union('RENAME3res', nfsstat3, {NFS3_OK: RENAME3resok, None: RENAME3resfail})
LINK3args = rpchelp.struct('LINK3args', [('file', nfs_fh3), ('link', diropargs3)])
LINK3resok = rpchelp.struct('LINK3resok', [('file_attributes', post_op_attr), ('linkdir_wcc', wcc_data)])
LINK3resfail = rpchelp.struct('LINK3resfail', [('file_attributes', post_op_attr), ('linkdir_wcc', wcc_data)])
LINK3res = rpchelp.union('LINK3res', nfsstat3, {NFS3_OK: LINK3resok, None: LINK3resfail})
READDIR3args = rpchelp.struct('READDIR3args', [('dir', nfs_fh3), ('cookie', cookie3), ('cookieverf', cookieverf3), ('count', count3)])
entry3 = rpchelp.linked_list('entry3', [('fileid', fileid3), ('name', filename3), ('cookie', cookie3)])
dirlist3 = rpchelp.struct('dirlist3', [('entries', rpchelp.opt_data(entry3)), ('eof', rpchelp.r_bool)])
READDIR3resok = rpchelp.struct('READDIR3resok', [('dir_attributes', post_op_attr), ('cookieverf', cookieverf3), ('reply', dirlist3)])
READDIR3resfail = rpchelp.struct('READDIR3resfail', [('dir_attributes', post_op_attr)])
READDIR3res = rpchelp.union('READDIR3res', nfsstat3, {NFS3_OK: READDIR3resok, None: READDIR3resfail})
READDIRPLUS3args = rpchelp.struct('READDIRPLUS3args', [('dir', nfs_fh3), ('cookie', cookie3), ('cookieverf', cookieverf3), ('dircount', count3), ('maxcount', count3)])
entryplus3 = rpchelp.linked_list('entryplus3', [('fileid', fileid3), ('name', filename3), ('cookie', cookie3), ('name_attributes', post_op_attr), ('name_handle', post_op_fh3)])
dirlistplus3 = rpchelp.struct('dirlistplus3', [('entries', rpchelp.opt_data(entryplus3)), ('eof', rpchelp.r_bool)])
READDIRPLUS3resok = rpchelp.struct('READDIRPLUS3resok', [('dir_attributes', post_op_attr), ('cookieverf', cookieverf3), ('reply', dirlistplus3)])
READDIRPLUS3resfail = rpchelp.struct('READDIRPLUS3resfail', [('dir_attributes', post_op_attr)])
READDIRPLUS3res = rpchelp.union('READDIRPLUS3res', nfsstat3, {NFS3_OK: READDIRPLUS3resok, None: READDIRPLUS3resfail})
FSSTAT3args = rpchelp.struct('FSSTAT3args', [('fsroot', nfs_fh3)])
FSSTAT3resok = rpchelp.struct('FSSTAT3resok', [('obj_attributes', post_op_attr), ('tbytes', size3), ('fbytes', size3), ('abytes', size3), ('tfiles', size3), ('ffiles', size3), ('afiles', size3), ('invarsec', uint32)])
FSSTAT3resfail = rpchelp.struct('FSSTAT3resfail', [('obj_attributes', post_op_attr)])
FSSTAT3res = rpchelp.union('FSSTAT3res', nfsstat3, {NFS3_OK: FSSTAT3resok, None: FSSTAT3resfail})
FSF3_LINK = 0x0001
FSF3_SYMLINK = 0x0002
FSF3_HOMOGENEOUS = 0x0008
FSF3_CANSETTIME = 0x0010
FSINFO3args = rpchelp.struct('FSINFO3args', [('fsroot', nfs_fh3)])
FSINFO3resok = rpchelp.struct('FSINFO3resok', [('obj_attributes', post_op_attr), ('rtmax', uint32), ('rtpref', uint32), ('rtmult', uint32), ('wtmax', uint32), ('wtpref', uint32), ('wtmult', uint32), ('dtpref', uint32), ('maxfilesize', size3), ('time_delta', nfstime3), ('properties', uint32)])
FSINFO3resfail = rpchelp.struct('FSINFO3resfail', [('obj_attributes', post_op_attr)])
FSINFO3res = rpchelp.union('FSINFO3res', nfsstat3, {NFS3_OK: FSINFO3resok, None: FSINFO3resfail})
PATHCONF3args = rpchelp.struct('PATHCONF3args', [('object', nfs_fh3)])
PATHCONF3resok = rpchelp.struct('PATHCONF3resok', [('obj_attributes', post_op_attr), ('linkmax', uint32), ('name_max', uint32), ('no_trunc', rpchelp.r_bool), ('chown_restricted', rpchelp.r_bool), ('case_insensitive', rpchelp.r_bool), ('case_preserving', rpchelp.r_bool)])
PATHCONF3resfail = rpchelp.struct('PATHCONF3resfail', [('obj_attributes', post_op_attr)])
PATHCONF3res = rpchelp.union('PATHCONF3res', nfsstat3, {NFS3_OK: PATHCONF3resok, None: PATHCONF3resfail})
COMMIT3args = rpchelp.struct('COMMIT3args', [('file', nfs_fh3), ('offset', offset3), ('count', count3)])
COMMIT3resok = rpchelp.struct('COMMIT3resok', [('file_wcc', wcc_data), ('verf', writeverf3)])
COMMIT3resfail = rpchelp.struct('COMMIT3resfail', [('file_wcc', wcc_data)])
COMMIT3res = rpchelp.union('COMMIT3res', nfsstat3, {NFS3_OK: COMMIT3resok, None: COMMIT3resfail})
MNTPATHLEN = 1024
MNTNAMLEN = 255
FHSIZE3 = 64
fhandle3 = rpchelp.opaque(rpchelp.var, FHSIZE3)
dirpath = rpchelp.string(rpchelp.var, MNTPATHLEN)
name = rpchelp.string(rpchelp.var, MNTNAMLEN)
mountstat3 = rpchelp.r_int
mountres3_ok = rpchelp.struct('mountres3_ok', [('fhandle', fhandle3), ('auth_flavors', rpchelp.arr(rpchelp.r_int, rpchelp.var, None))])
mountres3 = rpchelp.union('mountres3', mountstat3, {MNT3_OK: mountres3_ok, None: rpchelp.r_void})
mountlist = rpchelp.linked_list('mountlist', [('hostname', name), ('directory', dirpath)])
grouplist = rpchelp.linked_list('grouplist', [('grname', name)])
exportlist = rpchelp.linked_list('exportlist', [('filesys', dirpath), ('groups', grouplist)])
@dataclass
class v_specdata3(rpchelp.struct_val_base):
	specdata1: int
	specdata2: int


specdata3.val_base_class = v_specdata3


@dataclass
class v_nfs_fh3(rpchelp.struct_val_base):
	data: bytes


nfs_fh3.val_base_class = v_nfs_fh3


@dataclass
class v_nfstime3(rpchelp.struct_val_base):
	seconds: int
	nseconds: int


nfstime3.val_base_class = v_nfstime3


@dataclass
class v_fattr3(rpchelp.struct_val_base):
	type: int
	mode: int
	nlink: int
	uid: int
	gid: int
	size: int
	used: int
	rdev: v_specdata3
	fsid: int
	fileid: int
	atime: v_nfstime3
	mtime: v_nfstime3
	ctime: v_nfstime3


fattr3.val_base_class = v_fattr3


@dataclass
class v_wcc_attr(rpchelp.struct_val_base):
	size: int
	mtime: v_nfstime3
	ctime: v_nfstime3


wcc_attr.val_base_class = v_wcc_attr


@dataclass
class v_wcc_data(rpchelp.struct_val_base):
	before: typing.Optional[v_wcc_attr]
	after: typing.Optional[v_fattr3]


wcc_data.val_base_class = v_wcc_data


@dataclass
class v_sattr3(rpchelp.struct_val_base):
	mode: typing.Tuple[bool, typing.Optional[int]]
	uid: typing.Tuple[bool, typing.Optional[int]]
	gid: typing.Tuple[bool, typing.Optional[int]]
	size: typing.Tuple[bool, typing.Optional[int]]
	atime: typing.Tuple[int, typing.Optional[v_nfstime3]]
	mtime: typing.Tuple[int, typing.Optional[v_nfstime3]]


sattr3.val_base_class = v_sattr3


@dataclass
class v_diropargs3(rpchelp.struct_val_base):
	dir: typing.Union[bytes, v_nfs_fh3]
	name: bytes


diropargs3.val_base_class = v_diropargs3


@dataclass
class v_GETATTR3args(rpchelp.struct_val_base):
	object: typing.Union[bytes, v_nfs_fh3]


GETATTR3args.val_base_class = v_GETATTR3args


@dataclass
class v_GETATTR3resok(rpchelp.struct_val_base):
	obj_attributes: v_fattr3


GETATTR3resok.val_base_class = v_GETATTR3resok


@dataclass
class v_SETATTR3args(rpchelp.struct_val_base):
	object: typing.Union[bytes, v_nfs_fh3]
	new_attributes: v_sattr3
	guard: typing.Optional[v_nfstime3]


SETATTR3args.val_base_class = v_SETATTR3args


@dataclass
class v_SETATTR3resok(rpchelp.struct_val_base):
	obj_wcc: v_wcc_data


SETATTR3resok.val_base_class = v_SETATTR3resok


@dataclass
class v_SETATTR3resfail(rpchelp.struct_val_base):
	obj_wcc: v_wcc_data


SETATTR3resfail.val_base_class = v_SETATTR3resfail


@dataclass
class v_LOOKUP3args(rpchelp.struct_val_base):
	what: v_diropargs3


LOOKUP3args.val_base_class = v_LOOKUP3args


@dataclass
class v_LOOKUP3resok(rpchelp.struct_val_base):
	object: typing.Union[bytes, v_nfs_fh3]
	obj_attributes: typing.Optional[v_fattr3]
	dir_attributes: typing.Optional[v_fattr3]


LOOKUP3resok.val_base_class = v_LOOKUP3resok


@dataclass
class v_LOOKUP3resfail(rpchelp.struct_val_base):
	dir_attributes: typing.Optional[v_fattr3]


LOOKUP3resfail.val_base_class = v_LOOKUP3resfail


@dataclass
class v_ACCESS3args(rpchelp.struct_val_base):
	object: typing.Union[bytes, v_nfs_fh3]
	access: int


ACCESS3args.val_base_class = v_ACCESS3args


@dataclass
class v_ACCESS3resok(rpchelp.struct_val_base):
	obj_attributes: typing.Optional[v_fattr3]
	access: int


ACCESS3resok.val_base_class = v_ACCESS3resok


@dataclass
class v_ACCESS3resfail(rpchelp.struct_val_base):
	obj_attributes: typing.Optional[v_fattr3]


ACCESS3resfail.val_base_class = v_ACCESS3resfail


@dataclass
class v_READLINK3args(rpchelp.struct_val_base):
	symlink: typing.Union[bytes, v_nfs_fh3]


READLINK3args.val_base_class = v_READLINK3args


@dataclass
class v_READLINK3resok(rpchelp.struct_val_base):
	symlink_attributes: typing.Optional[v_fattr3]
	data: bytes


READLINK3resok.val_base_class = v_READLINK3resok


@dataclass
class v_READLINK3resfail(rpchelp.struct_val_base):
	symlink_attributes: typing.Optional[v_fattr3]


READLINK3resfail.val_base_class = v_READLINK3resfail


@dataclass
class v_READ3args(rpchelp.struct_val_base):
	file: typing.Union[bytes, v_nfs_fh3]
	offset: int
	count: int


READ3args.val_base_class = v_READ3args


@dataclass
class v_READ3resok(rpchelp.struct_val_base):
	file_attributes: typing.Optional[v_fattr3]
	count: int
	eof: bool
	data: bytes


READ3resok.val_base_class = v_READ3resok


@dataclass
class v_READ3resfail(rpchelp.struct_val_base):
	file_attributes: typing.Optional[v_fattr3]


READ3resfail.val_base_class = v_READ3resfail


@dataclass
class v_WRITE3args(rpchelp.struct_val_base):
	file: typing.Union[bytes, v_nfs_fh3]
	offset: int
	count: int
	stable: int
	data: bytes


WRITE3args.val_base_class = v_WRITE3args


@dataclass
class v_WRITE3resok(rpchelp.struct_val_base):
	file_wcc: v_wcc_data
	count: int
	committed: int
	verf: bytes


WRITE3resok.val_base_class = v_WRITE3resok


@dataclass
class v_WRITE3resfail(rpchelp.struct_val_base):
	file_wcc: v_wcc_data


WRITE3resfail.val_base_class = v_WRITE3resfail


@dataclass
class v_CREATE3args(rpchelp.struct_val_base):
	where: v_diropargs3
	how: typing.Tuple[int, typing.Union[v_sattr3, v_sattr3, bytes]]


CREATE3args.val_base_class = v_CREATE3args


@dataclass
class v_CREATE3resok(rpchelp.struct_val_base):
	obj: typing.Optional[typing.Union[bytes, v_nfs_fh3]]
	obj_attributes: typing.Optional[v_fattr3]
	dir_wcc: v_wcc_data


CREATE3resok.val_base_class = v_CREATE3resok


@dataclass
class v_CREATE3resfail(rpchelp.struct_val_base):
	dir_wcc: v_wcc_data


CREATE3resfail.val_base_class = v_CREATE3resfail


@dataclass
class v_MKDIR3args(rpchelp.struct_val_base):
	where: v_diropargs3
	attributes: v_sattr3


MKDIR3args.val_base_class = v_MKDIR3args


@dataclass
class v_MKDIR3resok(rpchelp.struct_val_base):
	obj: typing.Optional[typing.Union[bytes, v_nfs_fh3]]
	obj_attributes: typing.Optional[v_fattr3]
	dir_wcc: v_wcc_data


MKDIR3resok.val_base_class = v_MKDIR3resok


@dataclass
class v_MKDIR3resfail(rpchelp.struct_val_base):
	dir_wcc: v_wcc_data


MKDIR3resfail.val_base_class = v_MKDIR3resfail


@dataclass
class v_symlinkdata3(rpchelp.struct_val_base):
	symlink_attributes: v_sattr3
	symlink_data: bytes


symlinkdata3.val_base_class = v_symlinkdata3


@dataclass
class v_SYMLINK3args(rpchelp.struct_val_base):
	where: v_diropargs3
	symlink: v_symlinkdata3


SYMLINK3args.val_base_class = v_SYMLINK3args


@dataclass
class v_SYMLINK3resok(rpchelp.struct_val_base):
	obj: typing.Optional[typing.Union[bytes, v_nfs_fh3]]
	obj_attributes: typing.Optional[v_fattr3]
	dir_wcc: v_wcc_data


SYMLINK3resok.val_base_class = v_SYMLINK3resok


@dataclass
class v_SYMLINK3resfail(rpchelp.struct_val_base):
	dir_wcc: v_wcc_data


SYMLINK3resfail.val_base_class = v_SYMLINK3resfail


@dataclass
class v_devicedata3(rpchelp.struct_val_base):
	dev_attributes: v_sattr3
	spec: v_specdata3


devicedata3.val_base_class = v_devicedata3


@dataclass
class v_MKNOD3args(rpchelp.struct_val_base):
	where: v_diropargs3
	what: typing.Tuple[int, typing.Union[v_devicedata3, v_devicedata3, v_sattr3, v_sattr3, None]]


MKNOD3args.val_base_class = v_MKNOD3args


@dataclass
class v_MKNOD3resok(rpchelp.struct_val_base):
	obj: typing.Optional[typing.Union[bytes, v_nfs_fh3]]
	obj_attributes: typing.Optional[v_fattr3]
	dir_wcc: v_wcc_data


MKNOD3resok.val_base_class = v_MKNOD3resok


@dataclass
class v_MKNOD3resfail(rpchelp.struct_val_base):
	dir_wcc: v_wcc_data


MKNOD3resfail.val_base_class = v_MKNOD3resfail


@dataclass
class v_REMOVE3args(rpchelp.struct_val_base):
	object: v_diropargs3


REMOVE3args.val_base_class = v_REMOVE3args


@dataclass
class v_REMOVE3resok(rpchelp.struct_val_base):
	dir_wcc: v_wcc_data


REMOVE3resok.val_base_class = v_REMOVE3resok


@dataclass
class v_REMOVE3resfail(rpchelp.struct_val_base):
	dir_wcc: v_wcc_data


REMOVE3resfail.val_base_class = v_REMOVE3resfail


@dataclass
class v_RMDIR3args(rpchelp.struct_val_base):
	object: v_diropargs3


RMDIR3args.val_base_class = v_RMDIR3args


@dataclass
class v_RMDIR3resok(rpchelp.struct_val_base):
	dir_wcc: v_wcc_data


RMDIR3resok.val_base_class = v_RMDIR3resok


@dataclass
class v_RMDIR3resfail(rpchelp.struct_val_base):
	dir_wcc: v_wcc_data


RMDIR3resfail.val_base_class = v_RMDIR3resfail


@dataclass
class v_RENAME3args(rpchelp.struct_val_base):
	from_: v_diropargs3
	to: v_diropargs3


RENAME3args.val_base_class = v_RENAME3args


@dataclass
class v_RENAME3resok(rpchelp.struct_val_base):
	fromdir_wcc: v_wcc_data
	todir_wcc: v_wcc_data


RENAME3resok.val_base_class = v_RENAME3resok


@dataclass
class v_RENAME3resfail(rpchelp.struct_val_base):
	fromdir_wcc: v_wcc_data
	todir_wcc: v_wcc_data


RENAME3resfail.val_base_class = v_RENAME3resfail


@dataclass
class v_LINK3args(rpchelp.struct_val_base):
	file: typing.Union[bytes, v_nfs_fh3]
	link: v_diropargs3


LINK3args.val_base_class = v_LINK3args


@dataclass
class v_LINK3resok(rpchelp.struct_val_base):
	file_attributes: typing.Optional[v_fattr3]
	linkdir_wcc: v_wcc_data


LINK3resok.val_base_class = v_LINK3resok


@dataclass
class v_LINK3resfail(rpchelp.struct_val_base):
	file_attributes: typing.Optional[v_fattr3]
	linkdir_wcc: v_wcc_data


LINK3resfail.val_base_class = v_LINK3resfail


@dataclass
class v_READDIR3args(rpchelp.struct_val_base):
	dir: typing.Union[bytes, v_nfs_fh3]
	cookie: int
	cookieverf: bytes
	count: int


READDIR3args.val_base_class = v_READDIR3args


@dataclass
class v_entry3(rpchelp.struct_val_base):
	fileid: int
	name: bytes
	cookie: int


entry3.val_base_class = v_entry3


@dataclass
class v_dirlist3(rpchelp.struct_val_base):
	entries: typing.List[v_entry3]
	eof: bool


dirlist3.val_base_class = v_dirlist3


@dataclass
class v_READDIR3resok(rpchelp.struct_val_base):
	dir_attributes: typing.Optional[v_fattr3]
	cookieverf: bytes
	reply: v_dirlist3


READDIR3resok.val_base_class = v_READDIR3resok


@dataclass
class v_READDIR3resfail(rpchelp.struct_val_base):
	dir_attributes: typing.Optional[v_fattr3]


READDIR3resfail.val_base_class = v_READDIR3resfail


@dataclass
class v_READDIRPLUS3args(rpchelp.struct_val_base):
	dir: typing.Union[bytes, v_nfs_fh3]
	cookie: int
	cookieverf: bytes
	dircount: int
	maxcount: int


READDIRPLUS3args.val_base_class = v_READDIRPLUS3args


@dataclass
class v_entryplus3(rpchelp.struct_val_base):
	fileid: int
	name: bytes
	cookie: int
	name_attributes: typing.Optional[v_fattr3]
	name_handle: typing.Optional[typing.Union[bytes, v_nfs_fh3]]


entryplus3.val_base_class = v_entryplus3


@dataclass
class v_dirlistplus3(rpchelp.struct_val_base):
	entries: typing.List[v_entryplus3]
	eof: bool


dirlistplus3.val_base_class = v_dirlistplus3


@dataclass
class v_READDIRPLUS3resok(rpchelp.struct_val_base):
	dir_attributes: typing.Optional[v_fattr3]
	cookieverf: bytes
	reply: v_dirlistplus3


READDIRPLUS3resok.val_base_class = v_READDIRPLUS3resok


@dataclass
class v_READDIRPLUS3resfail(rpchelp.struct_val_base):
	dir_attributes: typing.Optional[v_fattr3]


READDIRPLUS3resfail.val_base_class = v_READDIRPLUS3resfail


@dataclass
class v_FSSTAT3args(rpchelp.struct_val_base):
	fsroot: typing.Union[bytes, v_nfs_fh3]


FSSTAT3args.val_base_class = v_FSSTAT3args


@dataclass
class v_FSSTAT3resok(rpchelp.struct_val_base):
	obj_attributes: typing.Optional[v_fattr3]
	tbytes: int
	fbytes: int
	abytes: int
	tfiles: int
	ffiles: int
	afiles: int
	invarsec: int


FSSTAT3resok.val_base_class = v_FSSTAT3resok


@dataclass
class v_FSSTAT3resfail(rpchelp.struct_val_base):
	obj_attributes: typing.Optional[v_fattr3]


FSSTAT3resfail.val_base_class = v_FSSTAT3resfail


@dataclass
class v_FSINFO3args(rpchelp.struct_val_base):
	fsroot: typing.Union[bytes, v_nfs_fh3]


FSINFO3args.val_base_class = v_FSINFO3args


@dataclass
class v_FSINFO3resok(rpchelp.struct_val_base):
	obj_attributes: typing.Optional[v_fattr3]
	rtmax: int
	rtpref: int
	rtmult: int
	wtmax: int
	wtpref: int
	wtmult: int
	dtpref: int
	maxfilesize: int
	time_delta: v_nfstime3
	properties: int


FSINFO3resok.val_base_class = v_FSINFO3resok


@dataclass
class v_FSINFO3resfail(rpchelp.struct_val_base):
	obj_attributes: typing.Optional[v_fattr3]


FSINFO3resfail.val_base_class = v_FSINFO3resfail


@dataclass
class v_PATHCONF3args(rpchelp.struct_val_base):
	object: typing.Union[bytes, v_nfs_fh3]


PATHCONF3args.val_base_class = v_PATHCONF3args


@dataclass
class v_PATHCONF3resok(rpchelp.struct_val_base):
	obj_attributes: typing.Optional[v_fattr3]
	linkmax: int
	name_max: int
	no_trunc: bool
	chown_restricted: bool
	case_insensitive: bool
	case_preserving: bool


PATHCONF3resok.val_base_class = v_PATHCONF3resok


@dataclass
class v_PATHCONF3resfail(rpchelp.struct_val_base):
	obj_attributes: typing.Optional[v_fattr3]


PATHCONF3resfail.val_base_class = v_PATHCONF3resfail


@dataclass
class v_COMMIT3args(rpchelp.struct_val_base):
	file: typing.Union[bytes, v_nfs_fh3]
	offset: int
	count: int


COMMIT3args.val_base_class = v_COMMIT3args


@dataclass
class v_COMMIT3resok(rpchelp.struct_val_base):
	file_wcc: v_wcc_data
	verf: bytes


COMMIT3resok.val_base_class = v_COMMIT3resok


@dataclass
class v_COMMIT3resfail(rpchelp.struct_val_base):
	file_wcc: v_wcc_data


COMMIT3resfail.val_base_class = v_COMMIT3resfail


@dataclass
class v_mountres3_ok(rpchelp.struct_val_base):
	fhandle: bytes
	auth_flavors: typing.List[int]


mountres3_ok.val_base_class = v_mountres3_ok


@dataclass
class v_mountlist(rpchelp.struct_val_base):
	hostname: bytes
	directory: bytes


mountlist.val_base_class = v_mountlist


@dataclass
class v_grouplist(rpchelp.struct_val_base):
	grname: bytes


grouplist.val_base_class = v_grouplist


@dataclass
class v_exportlist(rpchelp.struct_val_base):
	filesys: bytes
	groups: typing.List[typing.Union[bytes, v_grouplist]]


exportlist.val_base_class = v_exportlist





class NFS_PROGRAM_3(rpchelp.Server):
	prog = 100003
	vers = 3
	procs = {
		0: rpchelp.Proc('NULL', rpchelp.r_void, [rpchelp.r_void]),
		1: rpchelp.Proc('GETATTR', GETATTR3res, [GETATTR3args]),
		2: rpchelp.Proc('SETATTR', SETATTR3res, [SETATTR3args]),
		3: rpchelp.Proc('LOOKUP', LOOKUP3res, [LOOKUP3args]),
		4: rpchelp.Proc('ACCESS', ACCESS3res, [ACCESS3args]),
		5: rpchelp.Proc('READLINK', READLINK3res, [READLINK3args]),
		6: rpchelp.Proc('READ', READ3res, [READ3args]),
		7: rpchelp.Proc('WRITE', WRITE3res, [WRITE3args]),
		8: rpchelp.Proc('CREATE', CREATE3res, [CREATE3args]),
		9: rpchelp.Proc('MKDIR', MKDIR3res, [MKDIR3args]),
		10: rpchelp.Proc('SYMLINK', SYMLINK3res, [SYMLINK3args]),
		11: rpchelp.Proc('MKNOD', MKNOD3res, [MKNOD3args]),
		12: rpchelp.Proc('REMOVE', REMOVE3res, [REMOVE3args]),
		13: rpchelp.Proc('RMDIR', RMDIR3res, [RMDIR3args]),
		14: rpchelp.Proc('RENAME', RENAME3res, [RENAME3args]),
		15: rpchelp.Proc('LINK', LINK3res, [LINK3args]),
		16: rpchelp.Proc('READDIR', READDIR3res, [READDIR3args]),
		17: rpchelp.Proc('READDIRPLUS', READDIRPLUS3res, [READDIRPLUS3args]),
		18: rpchelp.Proc('FSSTAT', FSSTAT3res, [FSSTAT3args]),
		19: rpchelp.Proc('FSINFO', FSINFO3res, [FSINFO3args]),
		20: rpchelp.Proc('PATHCONF', PATHCONF3res, [PATHCONF3args]),
		21: rpchelp.Proc('COMMIT', COMMIT3res, [COMMIT3args]),
	}

	@abc.abstractmethod
	def NULL(self, arg_0: None) -> None:
		pass

	@abc.abstractmethod
	def GETATTR(self, arg_0: typing.Union[typing.Union[bytes, v_nfs_fh3], v_GETATTR3args]) -> typing.Tuple[int, typing.Optional[typing.Union[v_fattr3, v_GETATTR3resok]]]:
		pass

	@abc.abstractmethod
	def SETATTR(self, arg_0: v_SETATTR3args) -> typing.Tuple[int, typing.Union[typing.Union[v_wcc_data, v_SETATTR3resok], typing.Union[v_wcc_data, v_SETATTR3resfail]]]:
		pass

	@abc.abstractmethod
	def LOOKUP(self, arg_0: typing.Union[v_diropargs3, v_LOOKUP3args]) -> typing.Tuple[int, typing.Union[v_LOOKUP3resok, typing.Union[typing.Optional[v_fattr3], v_LOOKUP3resfail]]]:
		pass

	@abc.abstractmethod
	def ACCESS(self, arg_0: v_ACCESS3args) -> typing.Tuple[int, typing.Union[v_ACCESS3resok, typing.Union[typing.Optional[v_fattr3], v_ACCESS3resfail]]]:
		pass

	@abc.abstractmethod
	def READLINK(self, arg_0: typing.Union[typing.Union[bytes, v_nfs_fh3], v_READLINK3args]) -> typing.Tuple[int, typing.Union[v_READLINK3resok, typing.Union[typing.Optional[v_fattr3], v_READLINK3resfail]]]:
		pass

	@abc.abstractmethod
	def READ(self, arg_0: v_READ3args) -> typing.Tuple[int, typing.Union[v_READ3resok, typing.Union[typing.Optional[v_fattr3], v_READ3resfail]]]:
		pass

	@abc.abstractmethod
	def WRITE(self, arg_0: v_WRITE3args) -> typing.Tuple[int, typing.Union[v_WRITE3resok, typing.Union[v_wcc_data, v_WRITE3resfail]]]:
		pass

	@abc.abstractmethod
	def CREATE(self, arg_0: v_CREATE3args) -> typing.Tuple[int, typing.Union[v_CREATE3resok, typing.Union[v_wcc_data, v_CREATE3resfail]]]:
		pass

	@abc.abstractmethod
	def MKDIR(self, arg_0: v_MKDIR3args) -> typing.Tuple[int, typing.Union[v_MKDIR3resok, typing.Union[v_wcc_data, v_MKDIR3resfail]]]:
		pass

	@abc.abstractmethod
	def SYMLINK(self, arg_0: v_SYMLINK3args) -> typing.Tuple[int, typing.Union[v_SYMLINK3resok, typing.Union[v_wcc_data, v_SYMLINK3resfail]]]:
		pass

	@abc.abstractmethod
	def MKNOD(self, arg_0: v_MKNOD3args) -> typing.Tuple[int, typing.Union[v_MKNOD3resok, typing.Union[v_wcc_data, v_MKNOD3resfail]]]:
		pass

	@abc.abstractmethod
	def REMOVE(self, arg_0: typing.Union[v_diropargs3, v_REMOVE3args]) -> typing.Tuple[int, typing.Union[typing.Union[v_wcc_data, v_REMOVE3resok], typing.Union[v_wcc_data, v_REMOVE3resfail]]]:
		pass

	@abc.abstractmethod
	def RMDIR(self, arg_0: typing.Union[v_diropargs3, v_RMDIR3args]) -> typing.Tuple[int, typing.Union[typing.Union[v_wcc_data, v_RMDIR3resok], typing.Union[v_wcc_data, v_RMDIR3resfail]]]:
		pass

	@abc.abstractmethod
	def RENAME(self, arg_0: v_RENAME3args) -> typing.Tuple[int, typing.Union[v_RENAME3resok, v_RENAME3resfail]]:
		pass

	@abc.abstractmethod
	def LINK(self, arg_0: v_LINK3args) -> typing.Tuple[int, typing.Union[v_LINK3resok, v_LINK3resfail]]:
		pass

	@abc.abstractmethod
	def READDIR(self, arg_0: v_READDIR3args) -> typing.Tuple[int, typing.Union[v_READDIR3resok, typing.Union[typing.Optional[v_fattr3], v_READDIR3resfail]]]:
		pass

	@abc.abstractmethod
	def READDIRPLUS(self, arg_0: v_READDIRPLUS3args) -> typing.Tuple[int, typing.Union[v_READDIRPLUS3resok, typing.Union[typing.Optional[v_fattr3], v_READDIRPLUS3resfail]]]:
		pass

	@abc.abstractmethod
	def FSSTAT(self, arg_0: typing.Union[typing.Union[bytes, v_nfs_fh3], v_FSSTAT3args]) -> typing.Tuple[int, typing.Union[v_FSSTAT3resok, typing.Union[typing.Optional[v_fattr3], v_FSSTAT3resfail]]]:
		pass

	@abc.abstractmethod
	def FSINFO(self, arg_0: typing.Union[typing.Union[bytes, v_nfs_fh3], v_FSINFO3args]) -> typing.Tuple[int, typing.Union[v_FSINFO3resok, typing.Union[typing.Optional[v_fattr3], v_FSINFO3resfail]]]:
		pass

	@abc.abstractmethod
	def PATHCONF(self, arg_0: typing.Union[typing.Union[bytes, v_nfs_fh3], v_PATHCONF3args]) -> typing.Tuple[int, typing.Union[v_PATHCONF3resok, typing.Union[typing.Optional[v_fattr3], v_PATHCONF3resfail]]]:
		pass

	@abc.abstractmethod
	def COMMIT(self, arg_0: v_COMMIT3args) -> typing.Tuple[int, typing.Union[v_COMMIT3resok, typing.Union[v_wcc_data, v_COMMIT3resfail]]]:
		pass


class MOUNT_PROGRAM_3(rpchelp.Server):
	prog = 100005
	vers = 3
	procs = {
		0: rpchelp.Proc('NULL', rpchelp.r_void, [rpchelp.r_void]),
		1: rpchelp.Proc('MNT', mountres3, [dirpath]),
		2: rpchelp.Proc('DUMP', mountlist, [rpchelp.r_void]),
		3: rpchelp.Proc('UMNT', rpchelp.r_void, [dirpath]),
		4: rpchelp.Proc('UMNTALL', rpchelp.r_void, [rpchelp.r_void]),
		5: rpchelp.Proc('EXPORT', exportlist, [rpchelp.r_void]),
	}

	@abc.abstractmethod
	def NULL(self, arg_0: None) -> None:
		pass

	@abc.abstractmethod
	def MNT(self, arg_0: bytes) -> typing.Tuple[int, typing.Optional[v_mountres3_ok]]:
		pass

	@abc.abstractmethod
	def DUMP(self, arg_0: None) -> typing.List[v_mountlist]:
		pass

	@abc.abstractmethod
	def UMNT(self, arg_0: bytes) -> None:
		pass

	@abc.abstractmethod
	def UMNTALL(self, arg_0: None) -> None:
		pass

	@abc.abstractmethod
	def EXPORT(self, arg_0: None) -> typing.List[v_exportlist]:
		pass


__all__ = ['v_specdata3', 'v_nfs_fh3', 'v_nfstime3', 'v_fattr3', 'v_wcc_attr', 'v_wcc_data', 'v_sattr3', 'v_diropargs3', 'v_GETATTR3args', 'v_GETATTR3resok', 'v_SETATTR3args', 'v_SETATTR3resok', 'v_SETATTR3resfail', 'v_LOOKUP3args', 'v_LOOKUP3resok', 'v_LOOKUP3resfail', 'v_ACCESS3args', 'v_ACCESS3resok', 'v_ACCESS3resfail', 'v_READLINK3args', 'v_READLINK3resok', 'v_READLINK3resfail', 'v_READ3args', 'v_READ3resok', 'v_READ3resfail', 'v_WRITE3args', 'v_WRITE3resok', 'v_WRITE3resfail', 'v_CREATE3args', 'v_CREATE3resok', 'v_CREATE3resfail', 'v_MKDIR3args', 'v_MKDIR3resok', 'v_MKDIR3resfail', 'v_symlinkdata3', 'v_SYMLINK3args', 'v_SYMLINK3resok', 'v_SYMLINK3resfail', 'v_devicedata3', 'v_MKNOD3args', 'v_MKNOD3resok', 'v_MKNOD3resfail', 'v_REMOVE3args', 'v_REMOVE3resok', 'v_REMOVE3resfail', 'v_RMDIR3args', 'v_RMDIR3resok', 'v_RMDIR3resfail', 'v_RENAME3args', 'v_RENAME3resok', 'v_RENAME3resfail', 'v_LINK3args', 'v_LINK3resok', 'v_LINK3resfail', 'v_READDIR3args', 'v_entry3', 'v_dirlist3', 'v_READDIR3resok', 'v_READDIR3resfail', 'v_READDIRPLUS3args', 'v_entryplus3', 'v_dirlistplus3', 'v_READDIRPLUS3resok', 'v_READDIRPLUS3resfail', 'v_FSSTAT3args', 'v_FSSTAT3resok', 'v_FSSTAT3resfail', 'v_FSINFO3args', 'v_FSINFO3resok', 'v_FSINFO3resfail', 'v_PATHCONF3args', 'v_PATHCONF3resok', 'v_PATHCONF3resfail', 'v_COMMIT3args', 'v_COMMIT3resok', 'v_COMMIT3resfail', 'v_mountres3_ok', 'v_mountlist', 'v_grouplist', 'v_exportlist', 'NFS_PROGRAM_3', 'MOUNT_PROGRAM_3', 'TRUE', 'FALSE', 'NFS3_OK', 'NFS3ERR_PERM', 'NFS3ERR_NOENT', 'NFS3ERR_IO', 'NFS3ERR_NXIO', 'NFS3ERR_ACCES', 'NFS3ERR_EXIST', 'NFS3ERR_XDEV', 'NFS3ERR_NODEV', 'NFS3ERR_NOTDIR', 'NFS3ERR_ISDIR', 'NFS3ERR_INVAL', 'NFS3ERR_FBIG', 'NFS3ERR_NOSPC', 'NFS3ERR_ROFS', 'NFS3ERR_MLINK', 'NFS3ERR_NAMETOOLONG', 'NFS3ERR_NOTEMPTY', 'NFS3ERR_DQUOT', 'NFS3ERR_STALE', 'NFS3ERR_REMOTE', 'NFS3ERR_BADHANDLE', 'NFS3ERR_NOT_SYNC', 'NFS3ERR_BAD_COOKIE', 'NFS3ERR_NOTSUPP', 'NFS3ERR_TOOSMALL', 'NFS3ERR_SERVERFAULT', 'NFS3ERR_BADTYPE', 'NFS3ERR_JUKEBOX', 'NF3REG', 'NF3DIR', 'NF3BLK', 'NF3CHR', 'NF3LNK', 'NF3SOCK', 'NF3FIFO', 'DONT_CHANGE', 'SET_TO_SERVER_TIME', 'SET_TO_CLIENT_TIME', 'UNSTABLE', 'DATA_SYNC', 'FILE_SYNC', 'UNCHECKED', 'GUARDED', 'EXCLUSIVE', 'MNT3_OK', 'MNT3ERR_PERM', 'MNT3ERR_NOENT', 'MNT3ERR_IO', 'MNT3ERR_ACCES', 'MNT3ERR_NOTDIR', 'MNT3ERR_INVAL', 'MNT3ERR_NAMETOOLONG', 'MNT3ERR_NOTSUPP', 'MNT3ERR_SERVERFAULT', 'NFS3_FHSIZE', 'NFS3_COOKIEVERFSIZE', 'NFS3_CREATEVERFSIZE', 'NFS3_WRITEVERFSIZE', 'ACCESS3_READ', 'ACCESS3_LOOKUP', 'ACCESS3_MODIFY', 'ACCESS3_EXTEND', 'ACCESS3_DELETE', 'ACCESS3_EXECUTE', 'FSF3_LINK', 'FSF3_SYMLINK', 'FSF3_HOMOGENEOUS', 'FSF3_CANSETTIME', 'MNTPATHLEN', 'MNTNAMLEN', 'FHSIZE3']
