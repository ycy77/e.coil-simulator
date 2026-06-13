---
entity_id: "molecule.C16675"
entity_type: "small_molecule"
name: "7-Aminomethyl-7-carbaguanine"
source_database: "KEGG"
source_id: "C16675"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "7-Aminomethyl-7-carbaguanine"
  - "7-Aminomethyl-7-deazaguanine"
  - "PreQ1"
---

# 7-Aminomethyl-7-carbaguanine

`molecule.C16675`

## Static

- Type: `small_molecule`
- Source: `KEGG:C16675`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 7-Aminomethyl-7-carbaguanine; 7-Aminomethyl-7-deazaguanine; PreQ1 EcoCyc common name: preQ1.

## Biological Role

Consumed as substrate in 3 reaction(s).

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)

## Annotation

KEGG compound: 7-Aminomethyl-7-carbaguanine; 7-Aminomethyl-7-deazaguanine; PreQ1

## Pathways

- `eco00790` Folate biosynthesis (KEGG)

## Outgoing Edges (3)

- `is_substrate_of` --> [[reaction.R10209|reaction.R10209]] `KEGG` `database` - C01977 + C16675 <=> C20446 + C00242
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-1321|reaction.ecocyc.RXN0-1321]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-4022|reaction.ecocyc.RXN0-4022]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C16675`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
