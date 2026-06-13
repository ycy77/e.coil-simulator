---
entity_id: "molecule.C03506"
entity_type: "small_molecule"
name: "Indoleglycerol phosphate"
source_database: "KEGG"
source_id: "C03506"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Indoleglycerol phosphate"
  - "1-C-(Indol-3-yl)glycerol 3-phosphate"
  - "(3-Indolyl)-glycerol phosphate"
  - "C1-(3-Indolyl)-glycerol 3-phosphate"
  - "(1S,2R)-1-C-(Indol-3-yl)glycerol 3-phosphate"
  - "Indole-3-glycerol phosphate"
---

# Indoleglycerol phosphate

`molecule.C03506`

## Static

- Type: `small_molecule`
- Source: `KEGG:C03506`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Indoleglycerol phosphate; 1-C-(Indol-3-yl)glycerol 3-phosphate; (3-Indolyl)-glycerol phosphate; C1-(3-Indolyl)-glycerol 3-phosphate; (1S,2R)-1-C-(Indol-3-yl)glycerol 3-phosphate; Indole-3-glycerol phosphate EcoCyc common name: (1S,2R)-1-C-(indol-3-yl)glycerol 3-phosphate.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco00999` Biosynthesis of various plant secondary metabolites (KEGG)

## Annotation

KEGG compound: Indoleglycerol phosphate; 1-C-(Indol-3-yl)glycerol 3-phosphate; (3-Indolyl)-glycerol phosphate; C1-(3-Indolyl)-glycerol 3-phosphate; (1S,2R)-1-C-(Indol-3-yl)glycerol 3-phosphate; Indole-3-glycerol phosphate

## Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco00999` Biosynthesis of various plant secondary metabolites (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.ecocyc.IGPSYN-RXN|reaction.ecocyc.IGPSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R02340|reaction.R02340]] `KEGG` `database` - C03506 <=> C00463 + C00118
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-2381|reaction.ecocyc.RXN0-2381]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRYPSYN-RXN|reaction.ecocyc.TRYPSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C03506`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
