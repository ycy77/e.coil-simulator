---
entity_id: "molecule.C00644"
entity_type: "small_molecule"
name: "D-Mannitol 1-phosphate"
source_database: "KEGG"
source_id: "C00644"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Mannitol 1-phosphate"
---

# D-Mannitol 1-phosphate

`molecule.C00644`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00644`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Mannitol 1-phosphate Due to symmetry of the molecule, the phosphorylation of MANNITOL at either end produces the same molecule. When MANNITOL is transported by a PTS system, it is phosphorylated at the 6 position, but the resulting molecule is named MANNITOL-1P by conventional nomenclature rules.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

KEGG compound: D-Mannitol 1-phosphate

## Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-156|reaction.ecocyc.TRANS-RXN-156]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00758|reaction.R00758]] `KEGG` `database` - C00644 + C00003 <=> C00085 + C00004 + C00080
- `is_substrate_of` --> [[reaction.ecocyc.MANNITOL-1-PHOSPHATASE-RXN|reaction.ecocyc.MANNITOL-1-PHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.MANNPDEHYDROG-RXN|reaction.ecocyc.MANNPDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00644`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
