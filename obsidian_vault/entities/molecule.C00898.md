---
entity_id: "molecule.C00898"
entity_type: "small_molecule"
name: "(R,R)-Tartaric acid"
source_database: "KEGG"
source_id: "C00898"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "(R,R)-Tartaric acid"
  - "(R,R)-Tartrate"
  - "L-Tartaric acid"
  - "Tartaric acid"
  - "Tartrate"
  - "2,3-Dihydroxybutanedioic acid"
  - "(2R,3R)-Tartaric acid"
  - "(+)-Tartaric acid"
---

# (R,R)-Tartaric acid

`molecule.C00898`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00898`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: (R,R)-Tartaric acid; (R,R)-Tartrate; L-Tartaric acid; Tartaric acid; Tartrate; 2,3-Dihydroxybutanedioic acid; (2R,3R)-Tartaric acid; (+)-Tartaric acid EcoCyc common name: L-tartrate. TARTRATE is widely distributed in higher plants, especially in fruits such as grapes.

## Biological Role

Consumed as substrate in 6 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)

## Annotation

KEGG compound: (R,R)-Tartaric acid; (R,R)-Tartrate; L-Tartaric acid; Tartaric acid; Tartrate; 2,3-Dihydroxybutanedioic acid; (2R,3R)-Tartaric acid; (+)-Tartaric acid

## Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)

## Outgoing Edges (11)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8048|complex.ecocyc.CPLX0-8048]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-127|reaction.ecocyc.TRANS-RXN-127]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00339|reaction.R00339]] `KEGG` `database` - C00898 <=> C00036 + C00001
- `is_substrate_of` --> [[reaction.R06180|reaction.R06180]] `KEGG` `database` - C00898 + C00003 <=> C03459 + C00004 + C00080
- `is_substrate_of` --> [[reaction.ecocyc.LTARTDEHYDRA-RXN|reaction.ecocyc.LTARTDEHYDRA-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6362|reaction.ecocyc.RXN0-6362]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TARTRATE-DEHYDROGENASE-RXN|reaction.ecocyc.TARTRATE-DEHYDROGENASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-127|reaction.ecocyc.TRANS-RXN-127]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.GLUCARDEHYDRA-RXN|reaction.ecocyc.GLUCARDEHYDRA-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-5462|reaction.ecocyc.RXN0-5462]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-703|reaction.ecocyc.RXN0-703]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `transports` <-- [[protein.P39414|protein.P39414]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00898`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
