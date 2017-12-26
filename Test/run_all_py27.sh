#!/bin/bash

cd ..
cd Tasks

cd Audio.FlacToMp3
python -B -m pytest -v
cd ..

cd Calibre.Convert
python -B -m pytest -v
cd ..

cd DropPy.Common
python -B -m pytest -v
cd ..

cd FileSystem.CopyToDirectory
python -B -m pytest -v
cd ..

cd FileSystem.CopyToSourceDirectory
python -B -m pytest -v
cd ..

cd FileSystem.CreateTimestampDirectory
python -B -m pytest -v
cd ..

cd FileSystem.DeleteOriginals
python -B -m pytest -v
cd ..

cd FileSystem.ExitOnNoInput
python -B -m pytest -v
cd ..

cd FileSystem.PatternCopyToDirectory
python -B -m pytest -v
cd ..

cd FileSystem.Rename
python -B -m pytest -v
cd ..

cd FileSystem.ScpUpload
python -B -m pytest -v
cd ..

cd Filter.ByExtensions
python -B -m pytest -v
cd ..

cd Filter.ByUTIs
python -B -m pytest -v
cd ..

cd Filter.OnlyDirectories
python -B -m pytest -v
cd ..

cd Filter.OnlyFiles
python -B -m pytest -v
cd ..

cd Image.Convert
python -B -m pytest -v
cd ..

cd Image.Ocr
python -B -m pytest -v
cd ..

cd Image.RenameByExif
python -B -m pytest -v
cd ..

cd Image.Resize
python -B -m pytest -v
cd ..

cd Image.Rotate
python -B -m pytest -v
cd ..

cd MacOS.OpenFilesInApp
python -B -m pytest -v
cd ..

cd Markdown.AddToc
python -B -m pytest -v
cd ..

cd Markdown.FromHtml
python -B -m pytest -v
cd ..

cd Markdown.RemoveSection
python -B -m pytest -v
cd ..

cd Text.Append
python -B -m pytest -v
cd ..

cd Text.RemoveMultiNewlines
python -B -m pytest -v
cd ..

cd Video.Transcode
python -B -m pytest -v
cd ..

cd Web.ImgurUpload
python -B -m pytest -v
cd ..

cd Web.YouTubeDownload
python -B -m pytest -v
cd ..

cd ..
cd Test
