import os
import pytest

from jsonmaestro import helpers, load_json, load_jsonc, save_json, remove_comments


`@pytest.mark.parametrize("file_name", [
    "jsonc.json", "commented.json", "commented_with_duplicate.json",
    "bc_symbols.json", "ds_symbols.json", "mixed_comment_symbols.json"
])
def test_remove_comments(file_name):
	if helpers.is_json(f"data/{file_name}"):
		loader = load_json
	else:
		loader = load_jsonc

	with open(f"data/{file_name}", "r") as file:
		print(remove_comments(file.read()))

	data = loader(f"data/{file_name}")
	save_json(data=data, file_path=f"data/{file_name}.cleaned.json")

	with open(f"data/{file_name}.cleaned.json", "r") as file:
		data = file.read()
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

	os.remove(f"data/{file_name}.cleaned.json")
