---
entity_id: "molecule.C00245"
entity_type: "small_molecule"
name: "Taurine"
source_database: "KEGG"
source_id: "C00245"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Taurine"
  - "2-Aminoethanesulfonic acid"
  - "Aminoethylsulfonic acid"
---

# Taurine

`molecule.C00245`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00245`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Taurine; 2-Aminoethanesulfonic acid; Aminoethylsulfonic acid Taurine is an amino sulfonic acid. The name comes from Taurus (Latin for bull), as it was first isolated from ox bile. It is found in high abundance in the tissues of many animals (especially sea animals) and, in lesser abundance, in plants, fungi, and some bacterial species. Taurine plays several important roles in mammals and is essential to newborns of many species. The main functions of taurine in mammals include bile acid conjugation, detoxification, osmoregulation, membrane stabilization, and regulation of intracellular Ca2+ homeostasis.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00430` Taurine and hypotaurine metabolism (KEGG)
- `eco00920` Sulfur metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: Taurine; 2-Aminoethanesulfonic acid; Aminoethylsulfonic acid

## Pathways

- `eco00430` Taurine and hypotaurine metabolism (KEGG)
- `eco00920` Sulfur metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.ecocyc.ABC-64-RXN|reaction.ecocyc.ABC-64-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R05320|reaction.R05320]] `KEGG` `database` - C00245 + C00026 + C00007 <=> C00094 + C06735 + C00042 + C00011
- `is_substrate_of` --> [[reaction.ecocyc.ABC-64-RXN|reaction.ecocyc.ABC-64-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-299|reaction.ecocyc.RXN0-299]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[complex.ecocyc.ABC-64-CPLX|complex.ecocyc.ABC-64-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00245`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
