---
entity_id: "molecule.C04691"
entity_type: "small_molecule"
name: "2-Dehydro-3-deoxy-D-arabino-heptonate 7-phosphate"
source_database: "KEGG"
source_id: "C04691"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "2-Dehydro-3-deoxy-D-arabino-heptonate 7-phosphate"
  - "3-Deoxy-D-arabino-hept-2-ulosonate 7-phosphate"
  - "3-Deoxy-arabino-heptulonate 7-phosphate"
  - "3-Deoxy-D-arabino-heptulosonic acid 7-phosphate"
  - "DAHP"
  - "2-Dahp"
---

# 2-Dehydro-3-deoxy-D-arabino-heptonate 7-phosphate

`molecule.C04691`

## Static

- Type: `small_molecule`
- Source: `KEGG:C04691`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 2-Dehydro-3-deoxy-D-arabino-heptonate 7-phosphate; 3-Deoxy-D-arabino-hept-2-ulosonate 7-phosphate; 3-Deoxy-arabino-heptulonate 7-phosphate; 3-Deoxy-D-arabino-heptulosonic acid 7-phosphate; DAHP; 2-Dahp EcoCyc common name: 3-deoxy-D-arabino-heptulosonate 7-phosphate.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)

## Annotation

KEGG compound: 2-Dehydro-3-deoxy-D-arabino-heptonate 7-phosphate; 3-Deoxy-D-arabino-hept-2-ulosonate 7-phosphate; 3-Deoxy-arabino-heptulonate 7-phosphate; 3-Deoxy-D-arabino-heptulosonic acid 7-phosphate; DAHP; 2-Dahp

## Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.ecocyc.DAHPSYN-RXN|reaction.ecocyc.DAHPSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.3-DEHYDROQUINATE-SYNTHASE-RXN|reaction.ecocyc.3-DEHYDROQUINATE-SYNTHASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-20673|reaction.ecocyc.RXN-20673]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.3-DEHYDROQUINATE-SYNTHASE-RXN|reaction.ecocyc.3-DEHYDROQUINATE-SYNTHASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.DAHPSYN-RXN|reaction.ecocyc.DAHPSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C04691`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
