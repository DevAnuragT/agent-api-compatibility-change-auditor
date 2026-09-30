# Decision and Reasoning

The change is compatible when prior fields remain with the same declared types; removed or changed fields are reported for version and migration review. The implementation returns structured findings so a reviewer can see how each result was derived.

# Inputs and Data Sources

The caller supplies previous and current endpoint-to-field-type maps, plus a declared semantic version change. The only data source is the caller-provided payload plus the checked-in rules and code; no network or private-file access is used.

# Known Limitations and Constraints

This compares structural field names and types only. It cannot infer behavioral compatibility, wire-level coercion, or every consumer dependency. The result is a bounded pre-review aid and must not be presented as professional certification or an official HiDevs result.
