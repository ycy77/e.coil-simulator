---
entity_id: "molecule.C01672"
entity_type: "small_molecule"
name: "Cadaverine"
source_database: "KEGG"
source_id: "C01672"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Cadaverine"
  - "1,5-Pentanediamine"
  - "1,5-Diaminopentane"
  - "Pentamethylenediamine"
---

# Cadaverine

`molecule.C01672`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01672`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Cadaverine; 1,5-Pentanediamine; 1,5-Diaminopentane; Pentamethylenediamine

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 4 reaction(s).

## Enriched Pathways

- `eco00310` Lysine degradation (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco00480` Glutathione metabolism (KEGG)

## Annotation

KEGG compound: Cadaverine; 1,5-Pentanediamine; 1,5-Diaminopentane; Pentamethylenediamine

## Pathways

- `eco00310` Lysine degradation (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco00480` Glutathione metabolism (KEGG)

## Outgoing Edges (12)

- `is_component_of` --> [[complex.ecocyc.CPLX0-9743|complex.ecocyc.CPLX0-9743]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.R00462|reaction.R00462]] `KEGG` `database` - C00047 <=> C01672 + C00011
- `is_product_of` --> [[reaction.ecocyc.LYSDECARBOX-RXN|reaction.ecocyc.LYSDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-68|reaction.ecocyc.TRANS-RXN-68]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-212|reaction.ecocyc.TRANS-RXN0-212]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5217|reaction.ecocyc.RXN0-5217]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7317|reaction.ecocyc.RXN0-7317]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-68|reaction.ecocyc.TRANS-RXN-68]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-212|reaction.ecocyc.TRANS-RXN0-212]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.DIHYDROFOLATEREDUCT-RXN|reaction.ecocyc.DIHYDROFOLATEREDUCT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.LYSINE--TRNA-LIGASE-RXN|reaction.ecocyc.LYSINE--TRNA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-2481|reaction.ecocyc.RXN0-2481]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `transports` <-- [[protein.P0AAE8|protein.P0AAE8]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C01672`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
