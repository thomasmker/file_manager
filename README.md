on
# File Manager
A personal use file manager to rename files removing prefix and suffix in batch

## Introduction
After download a batch of anime episodes I would always rename from the original name to a more user friendly name.

For example:

__From:__ [GST] JoJo no Kimyou na Bouken Part 6 Stone Ocean - 01 [1080p].mkv

__To:__ 01.mkv

I use this project as an opportunity to use the python unittest and pytest for the first time

## Scope of functionalities 
- From the terminal only the remove prefix and suffix functionality is available
In order to make the tests there are also:
- Check if the directory exists
- Create directory
- Delete directory and its contents
- Create empty files
- Add prefix to files
- Add suffix to files

## Examples of use
On terminal:
```bash
python main.py --path="C:\Users\MyUser\Videos\anime name" --prefix="[GST] JoJo no Kimyou na Bouken Part 6 Stone Ocean - " --suffix=" [1080p]"
```

You can see the full list with:
```bash
python main.py -h
```

## Technologies
- Python 3.9.1
- Pytest 6.2.5
