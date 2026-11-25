import re 
from pathlib import Path

Notes_dir =(Path(__file__).parent / "notes").resolve()

print(f"Notes directory: {Notes_dir}")


relative_path = [str(p.relative_to(Notes_dir)) for p in Notes_dir.rglob("*.md")]
print(f"Relative paths: {relative_path}")


pattern = "connection pool"
rx = re.compile(pattern, re.IGNORECASE)
print(rx)


r = rx.search("This is a test string with Connection Pool inside.")
if r:
    print(f"Match found: {r.group()}") 
r = rx.search("This is a test string does not contain the pattern.")
if not r:
    print("No match found.")


filename = Notes_dir / "textdata.md"
text= filename.read_text()
lines = text.splitlines()
one_file_hits = []

for i, line in enumerate(lines, start=1):
    if rx.search(line):
        rel = filename.relative_to(Notes_dir)
        one_file_hits.append((rel, i, line.strip()))


print(f"Hits found: {one_file_hits}")


def grep (pattern: str, max_results: int = 10):
    rx= re.compile(pattern, re.IGNORECASE)
    hits = []
    for filename in sorted(Notes_dir.rglob("*.md")):
        text = filename.read_text()
        lines = text.splitlines()
        for i, line in enumerate(lines, start=1):
            if rx.search(line):
                rel = filename.relative_to(Notes_dir)
                hits.append((rel, i, line.strip()))
                if len(hits) >= max_results:
                    return hits
    return hits

print(grep("connection pool", max_results=5))


requested = "textdata.md"
target_file= (Notes_dir / requested).resolve()
def read_file(path : str) -> str:
    file_path = (Notes_dir / path).resolve()
    if not file_path.is_file():
        raise FileNotFoundError(f"File not found: {file_path}")
    return file_path.read_text()
