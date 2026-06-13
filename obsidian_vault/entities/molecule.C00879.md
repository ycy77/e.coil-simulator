---
entity_id: "molecule.C00879"
entity_type: "small_molecule"
name: "D-Galactarate"
source_database: "KEGG"
source_id: "C00879"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Galactarate"
  - "D-Mucic acid"
  - "D-Galactaric acid"
  - "Galactaric acid"
  - "Galactarate"
  - "Mucic acid"
---

# D-Galactarate

`molecule.C00879`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00879`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Galactarate; D-Mucic acid; D-Galactaric acid; Galactaric acid; Galactarate; Mucic acid EcoCyc common name: galactarate. Galactarate is a symmetric (meso) compound, and thus no D- and L- forms exist.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00053` Ascorbate and aldarate metabolism (KEGG)

## Annotation

KEGG compound: D-Galactarate; D-Mucic acid; D-Galactaric acid; Galactaric acid; Galactarate; Mucic acid

## Pathways

- `eco00053` Ascorbate and aldarate metabolism (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-203|reaction.ecocyc.TRANS-RXN0-203]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.GALACTARDEHYDRA-RXN|reaction.ecocyc.GALACTARDEHYDRA-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-203|reaction.ecocyc.TRANS-RXN0-203]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.GLUCARDEHYDRA-RXN|reaction.ecocyc.GLUCARDEHYDRA-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.KDGALDOL-RXN|reaction.ecocyc.KDGALDOL-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `transports` <-- [[protein.Q46916|protein.Q46916]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00879`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
