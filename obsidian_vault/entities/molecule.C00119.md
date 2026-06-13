---
entity_id: "molecule.C00119"
entity_type: "small_molecule"
name: "5-Phospho-alpha-D-ribose 1-diphosphate"
source_database: "KEGG"
source_id: "C00119"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "5-Phospho-alpha-D-ribose 1-diphosphate"
  - "5-Phosphoribosyl diphosphate"
  - "5-Phosphoribosyl 1-pyrophosphate"
  - "PRPP"
---

# 5-Phospho-alpha-D-ribose 1-diphosphate

`molecule.C00119`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00119`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 5-Phospho-alpha-D-ribose 1-diphosphate; 5-Phosphoribosyl diphosphate; 5-Phosphoribosyl 1-pyrophosphate; PRPP EcoCyc common name: 5-phospho-α-D-ribose 1-diphosphate.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 15 reaction(s).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00340` Histidine metabolism (KEGG)
- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco00790` Folate biosynthesis (KEGG)

## Annotation

KEGG compound: 5-Phospho-alpha-D-ribose 1-diphosphate; 5-Phosphoribosyl diphosphate; 5-Phosphoribosyl 1-pyrophosphate; PRPP

## Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00340` Histidine metabolism (KEGG)
- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco00790` Folate biosynthesis (KEGG)

## Outgoing Edges (17)

- `is_product_of` --> [[reaction.R00190|reaction.R00190]] `KEGG` `database` - C00020 + C00013 <=> C00147 + C00119
- `is_product_of` --> [[reaction.R01724|reaction.R01724]] `KEGG` `database` - C01185 + C00013 + C00008 + C00009 <=> C00253 + C00119 + C00002 + C00001 + C00080
- `is_product_of` --> [[reaction.R02142|reaction.R02142]] `KEGG` `database` - C00655 + C00013 <=> C00385 + C00119
- `is_product_of` --> [[reaction.ecocyc.ADENPRIBOSYLTRAN-RXN|reaction.ecocyc.ADENPRIBOSYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.ATPPHOSPHORIBOSYLTRANS-RXN|reaction.ecocyc.ATPPHOSPHORIBOSYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GUANPRIBOSYLTRAN-RXN|reaction.ecocyc.GUANPRIBOSYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.HYPOXANPRIBOSYLTRAN-RXN|reaction.ecocyc.HYPOXANPRIBOSYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.OROPRIBTRANS-RXN|reaction.ecocyc.OROPRIBTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PRPPAMIDOTRANS-RXN|reaction.ecocyc.PRPPAMIDOTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PRPPSYN-RXN|reaction.ecocyc.PRPPSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PRTRANS-RXN|reaction.ecocyc.PRTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.QUINOPRIBOTRANS-RXN|reaction.ecocyc.QUINOPRIBOTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-1401|reaction.ecocyc.RXN0-1401]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.URACIL-PRIBOSYLTRANS-RXN|reaction.ecocyc.URACIL-PRIBOSYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.XANPRIBOSYLTRAN-RXN|reaction.ecocyc.XANPRIBOSYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.NICOTINATEPRIBOSYLTRANS-RXN|reaction.ecocyc.NICOTINATEPRIBOSYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7170|reaction.ecocyc.RXN0-7170]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00119`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
