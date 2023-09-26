## MHL FILE SYNTAX

The given MHL_FILE must conform to the MHL format (draft 1.4), which can be found in the download section of mediahashlist.org. The syntax must adhere to the MHL XML schema, which can also be found in the download section of mediahashlist.org

## MHL FILE NAMING

- The MHL tool names the created MHL file as follows:
  `<foldername>_<date>_<time>-<qualifier>.mhl`
- where the placeholders are substituted with the following:

```xml
    <foldername> - name of the current directory, e.g. 'Movies'
    <date> - current date in format YYYY-MM-DD, e.g. '2013-05-10'
    <time> - current time in format HHMMSS, e.g. '111527'
    <qualifier>
```

- **complete** if the MHL file was created with the first synopsis form of `mhl seal`
- **partial** if the MHL file was created with any other synopsis form of `mhl seal`

## MHL FILE LOCATION

The MHL tool requires the MHL file to be placed along the path of the referenced file. This allows for an easy discovery when looking for an MHL file for a specific file.
For example, when creating a MHL file for the file
`/Example/Movies/Clip1.mov`

the MHL file can be put in the following locations:
   `/Example/Movies/`
   `/Example/`
   `/`
By default, the MHL file is located in the current directory you were in when calling the MHL tool (see section 'MHL file naming' above). You can manually specify the location of the MHL file, by passing the '--outputpath' option to the MHL tool.

***

## Verify

Verify folders and Media Hash List (MHL) files

#### SYNOPSIS

1. `mhl verify [-vv] -f MHL_FILE`

2. `mhl verify [-vv] -e -f MHL_FILE`

#### DESCRIPTION

In the first synopsis form `mhl verify` verifies the hashes stored in the MHL_FILE against the referenced files on disk.

In the second synopsis form `mhl verify` only checks if the files referenced by MHL_FILE are existent on disk.

#### EXAMPLES

Verifies the contents of a MHL file:

`$ mhl verify -f /path/to/file.mhl`

Verify the existence of all files references by a MHL file.

#### ARGUMENTS

- MHL_FILE

A path to a MHL file. The MHL file must adhere to the MHL format (see help topic 'mhl_format')

#### OPTIONS

- `-e, --existence`

Checks if the files referenced by MHL_FILE are existent on disk but does not compare hashes. Resealing is not possible if this option is passed.

- `-v, --verbose`

Prints status and result.

- `-vv, --very-verbose`

Same as -v, additionally prints progress.

#### DIAGNOSTICS

The `mhl verify` utility exits 0 on success, and >0 if an error occurs.

***

## Seal

`mhl-seal` -- Seal folders or files

#### SYNOPSIS

1. `mhl seal [-vv] FOLDER`
2. `mhl seal [-vv] [-#] FILEPATTERN`
3. `mhl seal [-vv] [-#] -o MHL_FOLDER FILEPATTERN`

#### DESCRIPTION

In the first synopsis form `mhl seal` takes a folder as an argument and creates an MHL file in that folder. This is the preferred way to seal folders.

In the second synopsis form `mhl seal` takes file(s) as arguments and creates an MHL file at the lowest common subfolder.

In the third synopsis form `mhl seal` takes file(s) as arguments and creates an MHL file in the MHL_FOLDER.

#### EXAMPLES

* Seal a folder:
  
  `mhl seal -v /path/to/folder`

* Create a MHL file for all 'mov' files within a folder:
  
  `mhl seal -v /path/to/folder/*.mov`

* Create a MHL file for all files in a subfolder recursively and create the MHL file in the containing folder:
  
  `mhl seal -v  -o /path/to/folder /path/to/folder/subfolder`

#### ARGUMENTS

- FOLDER
  Folder to seal. This will create an MHL file for all files in the folder, recursively. (e.g. dir for dir/file1 and dir/file2).
- FILEPATTERN
  Files to create MHL files for. Fileglobs (e.g. *.mov) can be given to specify multiple matching files.
  If the `-#` option is given, the FILEPATTERN is interpreted as a file sequence with the syntax described in help topic 'sequence_syntax'.
  Symbolic links are not followed. Sockets, FIFOs, etc. are ignored.
- MHL_FOLDER
  A path to a folder. The command 'mhl create' will store a MHL file in the given folder. This folder must to be located above all files.

#### OPTIONS

- `-o, --output-folder`
  Creates a MHL file in the given MHL\_FOLDER. Multiple --output-folder options can be given to create multiple MHL files. In this case, each MHL file only contains hashes for the files which are located in the corresponding MHL\_FOLDER or one of its subfolders. If relative paths are given which are located outside of all MHL_FOLDER(S), an error is thrown.
- `-#, --file-sequence`
  Looks for a file sequence as described in "FILE SEQUENCE FORMAT".
- `-v, --verbose`
  Prints status and result.
- `-vv, --very-verbose`
  Same as -v, additionally prints progress.

#### DIAGNOSTICS

The `mhl seal` command exits 0 on success, and >0 if an error occurs.

+++

## Hash

Creates and verifies files against hash values.

#### SYNOPSIS

1. `mhl hash [-vvm] [-#] [-t TYPES] FILEPATTERN`
2. `mhl hash [-vvm] -f FILE -h HASH`
3. `mhl hash [-vvm] -s`

#### DESCRIPTION

   In the first synopsis form 'mhl hash' creates and prints hash values from the given files. If no explicit hash format is given, creates md5 hashes. The results are printed to standard out.
   In the second synopsis form 'mhl hash' compares the hash value of the FILE with the given HASH.
   In the third synopsis form 'mhl hash' reads hash values as described in help topic 'hash_syntax' from stdin and compares them to the corresponding files.

#### EXAMPLES

- Create MD5 hashes for all movie files in a folder:
  
  ```$
      > MD5(/path/to/file3.mov)= ed7aa19a907a105af61f047db8d0b228
  ```

- Create MD5 hashes for a file sequence:
  
  ```$
      > MD5(/path/to/sequence012.dpx)= ed7aa19a907a105af61f047db8d0b228
      > MD5(/path/to/sequence013.dpx)= c95098251e22b102806ed17e0995f477
      > ...
  ```

- Verify single movie file with a given hash value:
  
  ```
  $ mhl hash -v -c /path/to/file.mov -h SHA1:a79302bfa825e1a57af2695177fe50c57984ec10
  > Summary: SUCCEEDED
  ```

#### ARGUMENTS

- FILEPATTERN
  
  Files to create MHL files for. Fileglobs (e.g. *.mov) can be given to specify multiple matching files.
  Also a leading directory name can be given to create an MHL file for all files in the directory, recursively. (e.g. dir for dir/file1 and dir/file2).
  If the '-#' option is given, the FILEPATTERN is interpreted as a file sequence with the syntax described in help topic 'sequence_syntax'.
  Symbolic links are not followed. Sockets, FIFOs, etc. are ignored.

- FILE
  
  A path to a file.

- HASH
  
  A hash string in either MD5, SHA1, xxHash, xxHash64 or xxHash64BE format.

- TYPES
  
  A list of hash types. Possible types are "md5", "sha1", "xxHash", "xxHash64" and "xxHash64BE".

#### OPTIONS

- `-s, --stdin`
  
  Causes 'mhl hash' to read hash values from stdin and compare them to the corresponding files. This is especially useful for comparing the hash values of file sequences

- `-f, --file`
  Scans the given FILE and compares its hash value with the given HASH. If no explicit hash format (md5, sha1, xxhash, xxhash64, xxhash64be) is given, mhlhash will automatically determine the hash format by the length of the HASH.

- `-v, --verbose`
  
  Prints status and result.

- `-vv, --very-verbose`
  
  Same as -v, additionally prints progress.

- `-#, --file-sequence`
  
   Looks for a file sequence as described in "FILE SEQUENCE FORMAT".

#### DIAGNOSTICS

The `mhl hash` command exits 0 on success, and >0 if an error occurs.

***

#### File

Create and parse Media Hash List (MHL) files

#### SYNOPSIS

1. `mhl file [-vv] -s [-o MHL_FOLDER]`

2. `mhl file [-vv] -f FILE [-o MHL_FOLDER]`

#### DESCRIPTION

In the first synopsis form `mhl file` takes input through stdin. The input syntax is described in help topic 'hash_syntax'

In the second synopsis form `mhl file` reads input from the FILE. The file must contain hash values as described in the help topic "hash_syntax", separated by newlines.

#### EXAMPLES

- Create a MHL file for media files in a folder with use of 'mhl hash':

```
$ mhl hash -c /path/to/folder/*.mov | mhl file -s -v -o /path/to/folder
> MHL file path(s):
> /path/to/folder/<folderName>_<date>_<time>.mhl
```

- Create a MHL file for media files in a folder with use of openssl:
  
  ```
  $ openssl dgst -md5 /path/to/files/ -name "*.mov" | mhl file -s -v -o /path/to/folder
  > MHL file path(s):
  > /path/to/folder/<folderName>_<date>_<time>.mhl
  ```

#### ARGUMENTS

- FILE

A path to a file. Symbolic links are not followed. Sockets, FIFOs, etc. are ignored.

- MHL_FOLDER
  
  A path to a folder. 'mhl file' will store the MHL file in the given folder. This folder has to be above all files that will be given as relative paths via stdin.

#### OPTIONS

- `-s, --stdin`
  
  Takes input from stdin

- `-f, --file`
  
  Takes input from the given FILE

- `-o, --output-folder`
  
  Creates a MHL file in the given MHL\_FOLDER. Multiple --output-folder options can be given to create multiple MHL files. In this case, each MHL file only contains hashes for the files which are located in the corresponding MHL\_FOLDER or one of its subfolders. If relative paths are given which are located outside of all MHL_FOLDER(S), an error is thrown.

- `-v, --verbose`
  
  Prints status and result

- `-vv, --very-verbose`
  
  Same as -v, additionally prints progress

##### DIAGNOSTICS

The 'mhl file' utility exits 0 on success, and >0 if an error occurs.
