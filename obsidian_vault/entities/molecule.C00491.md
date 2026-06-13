---
entity_id: "molecule.C00491"
entity_type: "small_molecule"
name: "L-Cystine"
source_database: "KEGG"
source_id: "C00491"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Cystine"
  - "L-Dicysteine"
  - "L-alpha-Diamino-beta-dithiolactic acid"
---

# L-Cystine

`molecule.C00491`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00491`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Cystine; L-Dicysteine; L-alpha-Diamino-beta-dithiolactic acid

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: L-Cystine; L-Dicysteine; L-alpha-Diamino-beta-dithiolactic acid

## Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (8)

- `is_product_of` --> [[reaction.ecocyc.RXN0-6990|reaction.ecocyc.RXN0-6990]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-285|reaction.ecocyc.TRANS-RXN-285]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-593|reaction.ecocyc.TRANS-RXN0-593]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.1.8.4.4-RXN|reaction.ecocyc.1.8.4.4-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-285|reaction.ecocyc.TRANS-RXN-285]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-593|reaction.ecocyc.TRANS-RXN0-593]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.ASPARTATE-SEMIALDEHYDE-DEHYDROGENASE-RXN|reaction.ecocyc.ASPARTATE-SEMIALDEHYDE-DEHYDROGENASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.DIAMINOPIMDECARB-RXN|reaction.ecocyc.DIAMINOPIMDECARB-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (2)

- `transports` <-- [[complex.ecocyc.CPLX0-8152|complex.ecocyc.CPLX0-8152]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[protein.P77529|protein.P77529]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00491`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
