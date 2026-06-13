---
entity_id: "molecule.C00842"
entity_type: "small_molecule"
name: "dTDP-glucose"
source_database: "KEGG"
source_id: "C00842"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "dTDP-glucose"
  - "dTDP-D-glucose"
  - "dTDP-alpha-D-glucose"
---

# dTDP-glucose

`molecule.C00842`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00842`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: dTDP-glucose; dTDP-D-glucose; dTDP-alpha-D-glucose EcoCyc common name: dTDP-α-D-glucose.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00521` Streptomycin biosynthesis (KEGG)
- `eco00523` Polyketide sugar unit biosynthesis (KEGG)
- `eco00525` Acarbose and validamycin biosynthesis (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)

## Annotation

KEGG compound: dTDP-glucose; dTDP-D-glucose; dTDP-alpha-D-glucose

## Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00521` Streptomycin biosynthesis (KEGG)
- `eco00523` Polyketide sugar unit biosynthesis (KEGG)
- `eco00525` Acarbose and validamycin biosynthesis (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.R02328|reaction.R02328]] `KEGG` `database` - C00459 + C00103 <=> C00013 + C00842
- `is_product_of` --> [[reaction.ecocyc.DTDPGLUCOSEPP-RXN|reaction.ecocyc.DTDPGLUCOSEPP-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.DTDPGLUCDEHYDRAT-RXN|reaction.ecocyc.DTDPGLUCDEHYDRAT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.DTDPGLUCOSEPP-RXN|reaction.ecocyc.DTDPGLUCOSEPP-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GLYCOPHOSPHORYL-RXN|reaction.ecocyc.GLYCOPHOSPHORYL-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00842`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
