---
entity_id: "molecule.C04877"
entity_type: "small_molecule"
name: "UDP-N-acetylmuramoyl-L-alanyl-gamma-D-glutamyl-meso-2,6-diaminopimelate"
source_database: "KEGG"
source_id: "C04877"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "UDP-N-acetylmuramoyl-L-alanyl-gamma-D-glutamyl-meso-2,6-diaminopimelate"
  - "UDP-N-acetylmuramoyl-L-alanyl-gamma-D-glutamyl-meso-2,6-diaminoheptanedioate"
  - "UDP-N-acetyl-alpha-D-muramoyl-L-alanyl-gamma-D-glutamyl-meso-2,6-diaminoheptanedioate"
  - "UDP-N-acetylmuramoyl-L-alanyl-D-gamma-glutamyl-meso-2,6-diaminopimelate"
  - "UDP-N-acetylmuramoyl-L-alanyl-D-gamma-glutamyl-meso-2,6-diamino-heptanedioate"
---

# UDP-N-acetylmuramoyl-L-alanyl-gamma-D-glutamyl-meso-2,6-diaminopimelate

`molecule.C04877`

## Static

- Type: `small_molecule`
- Source: `KEGG:C04877`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: UDP-N-acetylmuramoyl-L-alanyl-gamma-D-glutamyl-meso-2,6-diaminopimelate; UDP-N-acetylmuramoyl-L-alanyl-gamma-D-glutamyl-meso-2,6-diaminoheptanedioate; UDP-N-acetyl-alpha-D-muramoyl-L-alanyl-gamma-D-glutamyl-meso-2,6-diaminoheptanedioate; UDP-N-acetylmuramoyl-L-alanyl-D-gamma-glutamyl-meso-2,6-diaminopimelate; UDP-N-acetylmuramoyl-L-alanyl-D-gamma-glutamyl-meso-2,6-diamino-heptanedioate EcoCyc common name: UDP-MurNAc-L-Ala-γ-D-Glu-meso-DAP.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 5 reaction(s).

## Enriched Pathways

- `eco00300` Lysine biosynthesis (KEGG)
- `eco00550` Peptidoglycan biosynthesis (KEGG)

## Annotation

KEGG compound: UDP-N-acetylmuramoyl-L-alanyl-gamma-D-glutamyl-meso-2,6-diaminopimelate; UDP-N-acetylmuramoyl-L-alanyl-gamma-D-glutamyl-meso-2,6-diaminoheptanedioate; UDP-N-acetyl-alpha-D-muramoyl-L-alanyl-gamma-D-glutamyl-meso-2,6-diaminoheptanedioate; UDP-N-acetylmuramoyl-L-alanyl-D-gamma-glutamyl-meso-2,6-diaminopimelate; UDP-N-acetylmuramoyl-L-alanyl-D-gamma-glutamyl-meso-2,6-diamino-heptanedioate

## Pathways

- `eco00300` Lysine biosynthesis (KEGG)
- `eco00550` Peptidoglycan biosynthesis (KEGG)

## Outgoing Edges (7)

- `is_product_of` --> [[reaction.R02788|reaction.R02788]] `KEGG` `database` - C00002 + C00692 + C00680 <=> C00008 + C00009 + C04877
- `is_product_of` --> [[reaction.R10901|reaction.R10901]] `KEGG` `database` - C00002 + C01050 + C20925 <=> C00008 + C00009 + C04877
- `is_product_of` --> [[reaction.ecocyc.RXN0-2061|reaction.ecocyc.RXN0-2061]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-2361|reaction.ecocyc.RXN0-2361]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.UDP-NACMURALGLDAPLIG-RXN|reaction.ecocyc.UDP-NACMURALGLDAPLIG-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.UDP-NACMURALGLDAPAALIG-RXN|reaction.ecocyc.UDP-NACMURALGLDAPAALIG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.UDP-NACMURALGLDAPLIG-RXN|reaction.ecocyc.UDP-NACMURALGLDAPLIG-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C04877`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
