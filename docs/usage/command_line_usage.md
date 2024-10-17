# Command Line Usage

## Interactive Mode

To run the tool in interactive mode, simply run the following command:

```bash
jsonmaestro
```

This will prompt you to enter the path to the JSON, JSONC, or VSCode settings.json file you want to clean. It will then ask you if you want to sort the keys and remove comments.

## Non-Interactive Mode

To run the tool in non-interactive mode, you can use the following command:

```bash
jsonmaestro -f <file_path> [-s <sort>] [-i]
```

This will clean the specified file and save the cleaned data to a new file. The `-f` option specifies the path to the file you want to clean, and the `-s` option specifies the sort order (ascending or descending) for the keys. The `-i` option runs the tool in interactive mode, which will prompt you to confirm the cleaning process.

> Note
>
> You can Use multiple `-f` options to clean multiple files at once.

### Sort Order

The sort order can be specified as either `a` for ascending or `d` for descending. The default sort order is ascending.

### Interactive Mode

The interactive mode allows you to specify the path to the file you want to clean, and whether you want to sort the keys and remove comments. It will then prompt you to confirm the cleaning process.
