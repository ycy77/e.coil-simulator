---
entity_id: "molecule.C00905"
entity_type: "small_molecule"
name: "D-Fructuronate"
source_database: "KEGG"
source_id: "C00905"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Fructuronate"
  - "D-Fructuronic acid"
  - "β-D-fructuronic acid"
  - "β-D-fructuronate"
---

# D-Fructuronate

`molecule.C00905`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00905`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Fructuronate; D-Fructuronic acid

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)

## Annotation

KEGG compound: D-Fructuronate; D-Fructuronic acid

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)

## Outgoing Edges (7)

- `is_component_of` --> [[complex.ecocyc.MONOMER0-2101|complex.ecocyc.MONOMER0-2101]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.ecocyc.GLUCUROISOM-RXN|reaction.ecocyc.GLUCUROISOM-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.MANNONOXIDOREDUCT-RXN|reaction.ecocyc.MANNONOXIDOREDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-81|reaction.ecocyc.TRANS-RXN-81]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-4161|reaction.ecocyc.RXN0-4161]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-81|reaction.ecocyc.TRANS-RXN-81]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.ALTRO-OXIDOREDUCT-RXN|reaction.ecocyc.ALTRO-OXIDOREDUCT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `transports` <-- [[protein.P0AC94|protein.P0AC94]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00905`
- `EcoCyc:CPD-12537`
- `ZINC:ZINC000004095492`
- `SEED:cpd23467`
- `METANETX:MNXM491856`
- `CHEBI:59883`
- `PUBCHEM:46878577`
- `canonicalized_from:molecule.ecocyc.CPD-12537`

## Notes

Included because it appears in at least one E. coli KEGG pathway. | molecule.ecocyc.CPD-12537: EcoCyc:CPD-12537
