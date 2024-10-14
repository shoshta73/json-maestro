import os
import pytest

from jsonmaestro import remove_comments


@pytest.mark.parametrize("file_name", [
    "jsonc.json", "commented.json", "commented_with_duplicate.json",
    "bc_symbols.json", "ds_symbols.json", "mixed_comment_symbols.json"
])
def test_remove_comments(file_name):
	with open(f"data/{file_name}", "r") as file:
		data = remove_comments(file.read())
		print(data)

		if not file_name in [
		    "bc_symbols.json", "ds_symbols.json", "mixed_comment_symbols.json"
		]:
			assert "//" not in data
			assert "/*" not in data
			assert "*/" not in data
		else:
			assert "//" in data
			assert "/*" in data
			assert "*/" in data
