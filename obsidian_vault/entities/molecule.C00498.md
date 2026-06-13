---
entity_id: "molecule.C00498"
entity_type: "small_molecule"
name: "ADP-glucose"
source_database: "KEGG"
source_id: "C00498"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "ADP-glucose"
  - "ADP-alpha-D-glucose"
  - "Adenosine diphosphoglucose"
---

# ADP-glucose

`molecule.C00498`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00498`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: ADP-glucose; ADP-alpha-D-glucose; Adenosine diphosphoglucose EcoCyc common name: ADP-α-D-glucose.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)

## Annotation

KEGG compound: ADP-glucose; ADP-alpha-D-glucose; Adenosine diphosphoglucose

## Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)

## Outgoing Edges (9)

- `is_component_of` --> [[complex.ecocyc.CPLX0-11559|complex.ecocyc.CPLX0-11559]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.ecocyc.GLUC1PADENYLTRANS-RXN|reaction.ecocyc.GLUC1PADENYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-476|reaction.ecocyc.TRANS-RXN-476]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.GLYCOGENSYN-RXN|reaction.ecocyc.GLYCOGENSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7455|reaction.ecocyc.RXN0-7455]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-476|reaction.ecocyc.TRANS-RXN-476]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.5.1.3.20-RXN|reaction.ecocyc.5.1.3.20-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GLYCOPHOSPHORYL-RXN|reaction.ecocyc.GLYCOPHOSPHORYL-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.UDPSUGARHYDRO-RXN|reaction.ecocyc.UDPSUGARHYDRO-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00498`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
