---
entity_id: "molecule.C03459"
entity_type: "small_molecule"
name: "2-Hydroxy-3-oxosuccinate"
source_database: "KEGG"
source_id: "C03459"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "2-Hydroxy-3-oxosuccinate"
  - "Oxaloglycolate"
---

# 2-Hydroxy-3-oxosuccinate

`molecule.C03459`

## Static

- Type: `small_molecule`
- Source: `KEGG:C03459`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 2-Hydroxy-3-oxosuccinate; Oxaloglycolate EcoCyc common name: (3R)-oxaloglycolate.

## Biological Role

Produced in 2 reaction(s).

## Enriched Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)

## Annotation

KEGG compound: 2-Hydroxy-3-oxosuccinate; Oxaloglycolate

## Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.R06180|reaction.R06180]] `KEGG` `database` - C00898 + C00003 <=> C03459 + C00004 + C00080
- `is_product_of` --> [[reaction.ecocyc.TARTRATE-DEHYDROGENASE-RXN|reaction.ecocyc.TARTRATE-DEHYDROGENASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C03459`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
