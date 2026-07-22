# Changelog

## 1.1.0

Flattened the layout. The skill and commands moved to their standard Claude Code locations
(`.claude/skills/`, `.claude/commands/`) and the plugin manifests now point at them, replacing the
`product-analytics/` directory and the symlink. Gates are defined by exit conditions instead of
scripted lines.

## 1.0.0

First release. The analysis workflow as a Cowork/Claude Code plugin: a framing gate, a comparability
check that runs unprompted, and a validation gate before any conclusion. Two datasets included, both
synthetic.

Note: `product-analytics/.claude-plugin/plugin.json` pins an explicit version, so bump it whenever
you want installed copies to pick up changes. Pushing commits alone is not enough.
