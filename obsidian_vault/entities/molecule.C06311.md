---
entity_id: "molecule.C06311"
entity_type: "small_molecule"
name: "Galactitol 1-phosphate"
source_database: "KEGG"
source_id: "C06311"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Galactitol 1-phosphate"
  - "L-Galactitol 1-phosphate"
  - "D-Galactitol 6-phosphate"
---

# Galactitol 1-phosphate

`molecule.C06311`

## Static

- Type: `small_molecule`
- Source: `KEGG:C06311`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Galactitol 1-phosphate; L-Galactitol 1-phosphate; D-Galactitol 6-phosphate Due to symmetry of the molecule, the phosphorylation of GALACTITOL at either end produces the same molecule. When GALACTITOL is transported by a PTS system, it is phosphorylated at the 6 position, but the resulting molecule is named GALACTITOL-1-PHOSPHATE by conventional nomenclature rules.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

KEGG compound: Galactitol 1-phosphate; L-Galactitol 1-phosphate; D-Galactitol 6-phosphate

## Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-161|reaction.ecocyc.TRANS-RXN-161]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.1.1.1.251-RXN|reaction.ecocyc.1.1.1.251-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C06311`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
