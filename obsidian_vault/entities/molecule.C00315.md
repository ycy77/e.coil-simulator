---
entity_id: "molecule.C00315"
entity_type: "small_molecule"
name: "Spermidine"
source_database: "KEGG"
source_id: "C00315"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Spermidine"
  - "N-(3-Aminopropyl)-1,4-butane-diamine"
---

# Spermidine

`molecule.C00315`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00315`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Spermidine; N-(3-Aminopropyl)-1,4-butane-diamine

## Biological Role

Consumed as substrate in 6 reaction(s). Produced in 4 reaction(s).

## Enriched Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00480` Glutathione metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: Spermidine; N-(3-Aminopropyl)-1,4-butane-diamine

## Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00480` Glutathione metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (20)

- `activates` --> [[reaction.ecocyc.RXN-1381|reaction.ecocyc.RXN-1381]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.RXN0-6502|reaction.ecocyc.RXN0-6502]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Reactions
- `is_component_of` --> [[complex.ecocyc.CPLX0-9744|complex.ecocyc.CPLX0-9744]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.ecocyc.ABC-24-RXN|reaction.ecocyc.ABC-24-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GSPAMID-RXN|reaction.ecocyc.GSPAMID-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.SPERMIDINESYN-RXN|reaction.ecocyc.SPERMIDINESYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-266|reaction.ecocyc.TRANS-RXN0-266]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.ABC-24-RXN|reaction.ecocyc.ABC-24-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GSPSYN-RXN|reaction.ecocyc.GSPSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-24020|reaction.ecocyc.RXN-24020]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7165|reaction.ecocyc.RXN0-7165]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.SPERMACTRAN-RXN|reaction.ecocyc.SPERMACTRAN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-266|reaction.ecocyc.TRANS-RXN0-266]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.ARGDECARBOX-RXN|reaction.ecocyc.ARGDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.DIHYDROFOLATEREDUCT-RXN|reaction.ecocyc.DIHYDROFOLATEREDUCT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.LYSDECARBOX-RXN|reaction.ecocyc.LYSDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.ORNDECARBOX-RXN|reaction.ecocyc.ORNDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-2481|reaction.ecocyc.RXN0-2481]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.SAMDECARB-RXN|reaction.ecocyc.SAMDECARB-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.SPERMIDINESYN-RXN|reaction.ecocyc.SPERMIDINESYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (2)

- `transports` <-- [[complex.ecocyc.ABC-24-CPLX|complex.ecocyc.ABC-24-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[complex.ecocyc.YDGEF-CPLX|complex.ecocyc.YDGEF-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00315`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
