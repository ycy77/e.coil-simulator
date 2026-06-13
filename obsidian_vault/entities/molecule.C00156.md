---
entity_id: "molecule.C00156"
entity_type: "small_molecule"
name: "4-Hydroxybenzoate"
source_database: "KEGG"
source_id: "C00156"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "4-Hydroxybenzoate"
  - "Hydroxybenzoic acid"
  - "4-Hydroxybenzoic acid"
  - "Hydroxybenzenecarboxylic acid"
---

# 4-Hydroxybenzoate

`molecule.C00156`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00156`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 4-Hydroxybenzoate; Hydroxybenzoic acid; 4-Hydroxybenzoic acid; Hydroxybenzenecarboxylic acid

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00623` Toluene degradation (KEGG)
- `eco00627` Aminobenzoate degradation (KEGG)
- `eco00790` Folate biosynthesis (KEGG)

## Annotation

KEGG compound: 4-Hydroxybenzoate; Hydroxybenzoic acid; 4-Hydroxybenzoic acid; Hydroxybenzenecarboxylic acid

## Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00623` Toluene degradation (KEGG)
- `eco00627` Aminobenzoate degradation (KEGG)
- `eco00790` Folate biosynthesis (KEGG)

## Outgoing Edges (6)

- `is_product_of` --> [[reaction.ecocyc.CHORPYRLY-RXN|reaction.ecocyc.CHORPYRLY-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-233|reaction.ecocyc.TRANS-RXN0-233]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R07273|reaction.R07273]] `KEGG` `database` - C04145 + C00156 <=> C00013 + C03885
- `is_substrate_of` --> [[reaction.ecocyc.4OHBENZOATE-OCTAPRENYLTRANSFER-RXN|reaction.ecocyc.4OHBENZOATE-OCTAPRENYLTRANSFER-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-233|reaction.ecocyc.TRANS-RXN0-233]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.CHORPYRLY-RXN|reaction.ecocyc.CHORPYRLY-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `transports` <-- [[complex.ecocyc.CPLX0-4|complex.ecocyc.CPLX0-4]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00156`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
