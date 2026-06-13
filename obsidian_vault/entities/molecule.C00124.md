---
entity_id: "molecule.C00124"
entity_type: "small_molecule"
name: "D-Galactose"
source_database: "KEGG"
source_id: "C00124"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Galactose"
  - "D-Galactopyranose"
  - "D-Gal"
---

# D-Galactose

`molecule.C00124`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00124`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Galactose; D-Galactopyranose EcoCyc common name: D-galactopyranose. This compound stands for a mixture of ALPHA-D-GALACTOSE and GALACTOSE. In most cases, each of these compounds mutarotates quickly to form a mixture of the two, and thus it is the general rule to use this non-specific form in reactions unless it is specifically known that an enzyme can accept only one of the forms.

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 9 reaction(s).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

KEGG compound: D-Galactose; D-Galactopyranose

## Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (17)

- `is_component_of` --> [[complex.ecocyc.MONOMER-52|complex.ecocyc.MONOMER-52]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.MONOMER-53|complex.ecocyc.MONOMER-53]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.R01329|reaction.R01329]] `KEGG` `database` - C05400 + C00001 <=> C00159 + C00124
- `is_product_of` --> [[reaction.R07807|reaction.R07807]] `KEGG` `database` - G01977 + C00001 <=> G13073 + C00124
- `is_product_of` --> [[reaction.ecocyc.ABC-18-RXN|reaction.ecocyc.ABC-18-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.ALPHAGALACTOSID-RXN|reaction.ecocyc.ALPHAGALACTOSID-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-14409|reaction.ecocyc.RXN-14409]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-24169|reaction.ecocyc.RXN-24169]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-25312|reaction.ecocyc.RXN-25312]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7219|reaction.ecocyc.RXN0-7219]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-21|reaction.ecocyc.TRANS-RXN-21]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.ABC-18-RXN|reaction.ecocyc.ABC-18-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.R138-RXN|reaction.ecocyc.R138-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.R139-RXN|reaction.ecocyc.R139-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-21|reaction.ecocyc.TRANS-RXN-21]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.RXN-14722|reaction.ecocyc.RXN-14722]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN-24169|reaction.ecocyc.RXN-24169]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (2)

- `transports` <-- [[complex.ecocyc.ABC-18-CPLX|complex.ecocyc.ABC-18-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[protein.P0AEP1|protein.P0AEP1]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00124`
- `EcoCyc:D-Galactose`
- `CHEMSPIDER:2301265`
- `CHEBI:12936`
- `canonicalized_from:molecule.ecocyc.D-Galactose`

## Notes

Included because it appears in at least one E. coli KEGG pathway. | molecule.ecocyc.D-Galactose: EcoCyc:D-Galactose
