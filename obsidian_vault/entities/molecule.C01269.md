---
entity_id: "molecule.C01269"
entity_type: "small_molecule"
name: "5-O-(1-Carboxyvinyl)-3-phosphoshikimate"
source_database: "KEGG"
source_id: "C01269"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "5-O-(1-Carboxyvinyl)-3-phosphoshikimate"
  - "O5-(1-Carboxyvinyl)-3-phosphoshikimate"
---

# 5-O-(1-Carboxyvinyl)-3-phosphoshikimate

`molecule.C01269`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01269`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 5-O-(1-Carboxyvinyl)-3-phosphoshikimate; O5-(1-Carboxyvinyl)-3-phosphoshikimate EcoCyc common name: 5-enolpyruvoyl-shikimate 3-phosphate.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)

## Annotation

KEGG compound: 5-O-(1-Carboxyvinyl)-3-phosphoshikimate; O5-(1-Carboxyvinyl)-3-phosphoshikimate

## Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.2.5.1.19-RXN|reaction.ecocyc.2.5.1.19-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.CHORISMATE-SYNTHASE-RXN|reaction.ecocyc.CHORISMATE-SYNTHASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.2.5.1.19-RXN|reaction.ecocyc.2.5.1.19-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01269`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
