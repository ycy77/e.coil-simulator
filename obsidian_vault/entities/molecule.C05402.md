---
entity_id: "molecule.C05402"
entity_type: "small_molecule"
name: "Melibiose"
source_database: "KEGG"
source_id: "C05402"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Melibiose"
  - "6-O-(alpha-D-Galactopyranosyl)-D-glucopyranose"
  - "D-Gal-alpha1->6D-Glucose"
---

# Melibiose

`molecule.C05402`

## Static

- Type: `small_molecule`
- Source: `KEGG:C05402`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Melibiose; 6-O-(alpha-D-Galactopyranosyl)-D-glucopyranose; D-Gal-alpha1->6D-Glucose

## Biological Role

Consumed as substrate in 5 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: Melibiose; 6-O-(alpha-D-Galactopyranosyl)-D-glucopyranose; D-Gal-alpha1->6D-Glucose

## Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (10)

- `is_component_of` --> [[complex.ecocyc.MONOMER0-161|complex.ecocyc.MONOMER0-161]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-94|reaction.ecocyc.TRANS-RXN-94]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-94A|reaction.ecocyc.TRANS-RXN-94A]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-94B|reaction.ecocyc.TRANS-RXN-94B]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.ALPHAGALACTOSID-RXN|reaction.ecocyc.ALPHAGALACTOSID-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-294|reaction.ecocyc.RXN0-294]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-94|reaction.ecocyc.TRANS-RXN-94]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-94A|reaction.ecocyc.TRANS-RXN-94A]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-94B|reaction.ecocyc.TRANS-RXN-94B]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.TRANS-RXN-82|reaction.ecocyc.TRANS-RXN-82]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (2)

- `transports` <-- [[protein.P02920|protein.P02920]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[protein.P02921|protein.P02921]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C05402`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
