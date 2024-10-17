Usage
=====

This section will guide you through the process of using JSONMaestro to clean, process, and optimize JSON-like files.

There are two ways to use JSONMaestro:

1. As a command-line tool
2. As a Python library

Command-line tool
-----------------

The command-line tool is the simplest way to use JSONMaestro. It allows you to clean JSON files from the command line, providing a convenient way to process JSON data.

To use the command-line tool, follow these steps:

1. Install JSONMaestro using pip:

.. code-block:: bash

	pip install jsonmaestro

2. Locate the JSON file you want to clean. This can be a JSON file, JSONC file, or a VSCode settings.json file.

3. Run the following command, replacing ``<file_path>`` with the actual path to your JSON file:

.. code-block:: bash

	jsonmaestro -f <file_path>

.. note::
	You can also run this command without the ``-f`` flag, and it will prompt you to enter the path to your JSON file.

	.. code-block:: bash

		jsonmaestro

4. The tool will prompt you to select the operation you want to perform on the JSON file. You can choose to remove comments, sort keys, or sort keys in ascending or descending order.

5. The tool will then process the JSON file and save the cleaned data to a new file. The name of the new file will be the same as the original file, but with a ``_clean`` suffix.

6. You can now use the cleaned JSON file for further processing or analysis.