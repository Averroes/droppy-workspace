#!/bin/bash

cd ..
cd Tasks

cd Audio.FlacToMp3
python3 -B -m pytest -v
cd ..

cd Calibre.Convert
python3 -B -m pytest -v
cd ..

cd DropPy.Common
python3 -B -m pytest -v
cd ..

cd FileSystem.CopyToDirectory
python3 -B -m pytest -v
cd ..

cd FileSystem.CopyToSourceDirectory
python3 -B -m pytest -v
cd ..

cd FileSystem.CreateTimestampDirectory
python3 -B -m pytest -v
cd ..

cd FileSystem.DeleteOriginals
python3 -B -m pytest -v
cd ..

cd FileSystem.ExitOnNoInput
python3 -B -m pytest -v
cd ..

cd FileSystem.PatternCopyToDirectory
python3 -B -m pytest -v
cd ..

cd FileSystem.Rename
python3 -B -m pytest -v
cd ..

cd FileSystem.ScpUpload
python3 -B -m pytest -v
cd ..

cd Filter.ByExtensions
python3 -B -m pytest -v
cd ..

cd Filter.ByUTIs
python3 -B -m pytest -v
cd ..

cd Filter.OnlyDirectories
python3 -B -m pytest -v
cd ..

cd Filter.OnlyFiles
python3 -B -m pytest -v
cd ..

cd Image.Convert
python3 -B -m pytest -v
cd ..

cd Image.Ocr
python3 -B -m pytest -v
cd ..

cd Image.RenameByExif
python3 -B -m pytest -v
cd ..

cd Image.Resize
python3 -B -m pytest -v
cd ..

cd Image.Rotate
python3 -B -m pytest -v
cd ..

cd MacOS.OpenFilesInApp
python3 -B -m pytest -v
cd ..

cd Markdown.AddToc
python3 -B -m pytest -v
cd ..

cd Markdown.FromHtml
python3 -B -m pytest -v
cd ..

cd Markdown.RemoveSection
python3 -B -m pytest -v
cd ..

cd Text.Append
python3 -B -m pytest -v
cd ..

cd Text.RemoveMultiNewlines
python3 -B -m pytest -v
cd ..

cd Video.Transcode
python3 -B -m pytest -v
cd ..

cd Web.ImgurUpload
python3 -B -m pytest -v
cd ..

cd Web.YouTubeDownload
python3 -B -m pytest -v
cd ..

cd ..
cd Test
