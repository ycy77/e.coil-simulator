---
entity_id: "molecule.C05840"
entity_type: "small_molecule"
name: "Iminoaspartate"
source_database: "KEGG"
source_id: "C05840"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Iminoaspartate"
  - "Iminoaspartic acid"
  - "Iminosuccinate"
  - "2-Iminosuccinate"
  - "2-Iminobutanedioic acid"
---

# Iminoaspartate

`molecule.C05840`

## Static

- Type: `small_molecule`
- Source: `KEGG:C05840`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Iminoaspartate; Iminoaspartic acid; Iminosuccinate; 2-Iminosuccinate; 2-Iminobutanedioic acid EcoCyc common name: 2-iminosuccinate. kr96-7-17: this is an enzyme-bound intermediate.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)

## Annotation

KEGG compound: Iminoaspartate; Iminoaspartic acid; Iminosuccinate; 2-Iminosuccinate; 2-Iminobutanedioic acid

## Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)

## Outgoing Edges (6)

- `is_product_of` --> [[reaction.R00481|reaction.R00481]] `KEGG` `database` - C00049 + C00007 <=> C05840 + C00027
- `is_product_of` --> [[reaction.ecocyc.L-ASPARTATE-OXID-RXN|reaction.ecocyc.L-ASPARTATE-OXID-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-9772|reaction.ecocyc.RXN-9772]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.QUINOLINATE-SYNTHA-RXN|reaction.ecocyc.QUINOLINATE-SYNTHA-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-9771|reaction.ecocyc.RXN-9771]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.L-ASPARTATE-OXID-RXN|reaction.ecocyc.L-ASPARTATE-OXID-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C05840`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
