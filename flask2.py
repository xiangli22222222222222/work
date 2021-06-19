import os
const char* fileName= "C:/Readme.txt";
char drive[100];//磁盘名
char dir[100];//路径
char fname[100];//文件名（无后缀）
char ext[100]; //后缀
_splitpath(fileName, drive, dir, fname, ext);
char dstpath[100]; //合成后路径
_makepath(dstpath, drive, dir, fname, ".b");