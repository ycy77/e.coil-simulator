---
entity_id: "molecule.C00668"
entity_type: "small_molecule"
name: "alpha-D-Glucose 6-phosphate"
source_database: "KEGG"
source_id: "C00668"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "alpha-D-Glucose 6-phosphate"
---

# alpha-D-Glucose 6-phosphate

`molecule.C00668`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00668`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: alpha-D-Glucose 6-phosphate EcoCyc common name: α-D-glucose 6-phosphate.

## Biological Role

Consumed as substrate in 3 reaction(s).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00052` Galactose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)

## Annotation

KEGG compound: alpha-D-Glucose 6-phosphate

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00052` Galactose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)

## Outgoing Edges (3)

- `is_substrate_of` --> [[reaction.ecocyc.GLUCOSE-6-PHOSPHATE-1-EPIMERASE-RXN|reaction.ecocyc.GLUCOSE-6-PHOSPHATE-1-EPIMERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PGLUCISOM-RXN|reaction.ecocyc.PGLUCISOM-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-15312|reaction.ecocyc.RXN-15312]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00668`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
