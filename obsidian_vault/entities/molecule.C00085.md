---
entity_id: "molecule.C00085"
entity_type: "small_molecule"
name: "D-Fructose 6-phosphate"
source_database: "KEGG"
source_id: "C00085"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Fructose 6-phosphate"
  - "D-Fructose 6-phosphoric acid"
  - "Neuberg ester"
---

# D-Fructose 6-phosphate

`molecule.C00085`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00085`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Fructose 6-phosphate; D-Fructose 6-phosphoric acid; Neuberg ester EcoCyc common name: D-fructofuranose 6-phosphate.

## Biological Role

Consumed as substrate in 6 reaction(s). Produced in 7 reaction(s).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00052` Galactose metabolism (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)

## Annotation

KEGG compound: D-Fructose 6-phosphate; D-Fructose 6-phosphoric acid; Neuberg ester

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00052` Galactose metabolism (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)

## Outgoing Edges (13)

- `is_product_of` --> [[reaction.R00758|reaction.R00758]] `KEGG` `database` - C00644 + C00003 <=> C00085 + C00004 + C00080
- `is_product_of` --> [[reaction.R00760|reaction.R00760]] `KEGG` `database` - C00002 + C00095 <=> C00008 + C00085
- `is_product_of` --> [[reaction.R00762|reaction.R00762]] `KEGG` `database` - C00354 + C00001 <=> C00085 + C00009
- `is_product_of` --> [[reaction.R00765|reaction.R00765]] `KEGG` `database` - C00352 + C00001 <=> C00085 + C00014
- `is_product_of` --> [[reaction.R00771|reaction.R00771]] `KEGG` `database` - C00092 <=> C00085
- `is_product_of` --> [[reaction.R00772|reaction.R00772]] `KEGG` `database` - C00275 <=> C00085
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-501|reaction.ecocyc.TRANS-RXN0-501]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00756|reaction.R00756]] `KEGG` `database` - C00002 + C00085 <=> C00008 + C00354
- `is_substrate_of` --> [[reaction.R00767|reaction.R00767]] `KEGG` `database` - C00063 + C00085 <=> C00112 + C00354
- `is_substrate_of` --> [[reaction.R00768|reaction.R00768]] `KEGG` `database` - C00064 + C00085 <=> C00025 + C00352
- `is_substrate_of` --> [[reaction.R00769|reaction.R00769]] `KEGG` `database` - C00075 + C00085 <=> C00015 + C00354
- `is_substrate_of` --> [[reaction.R00770|reaction.R00770]] `KEGG` `database` - C00081 + C00085 <=> C00104 + C00354
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-501|reaction.ecocyc.TRANS-RXN0-501]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[protein.P0AGC0|protein.P0AGC0]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00085`
- `EcoCyc:CPD-24813`
- `canonicalized_from:molecule.ecocyc.CPD-24813`

## Notes

Included because it appears in at least one E. coli KEGG pathway. | molecule.ecocyc.CPD-24813: EcoCyc:CPD-24813
