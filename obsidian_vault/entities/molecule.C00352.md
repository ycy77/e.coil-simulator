---
entity_id: "molecule.C00352"
entity_type: "small_molecule"
name: "D-Glucosamine 6-phosphate"
source_database: "KEGG"
source_id: "C00352"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Glucosamine 6-phosphate"
  - "D-Glucosamine phosphate"
  - "α-D-glucosamine phosphate"
  - "α-α-D-glucosamine-6-P"
  - "α-D-glucosamine 6-phosphate"
---

# D-Glucosamine 6-phosphate

`molecule.C00352`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00352`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Glucosamine 6-phosphate; D-Glucosamine phosphate

## Biological Role

Consumed as substrate in 5 reaction(s). Produced in 6 reaction(s).

## Enriched Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

KEGG compound: D-Glucosamine 6-phosphate; D-Glucosamine phosphate

## Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (13)

- `is_product_of` --> [[reaction.R00768|reaction.R00768]] `KEGG` `database` - C00064 + C00085 <=> C00025 + C00352
- `is_product_of` --> [[reaction.ecocyc.GLUCOSAMINE-KINASE-RXN|reaction.ecocyc.GLUCOSAMINE-KINASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.L-GLN-FRUCT-6-P-AMINOTRANS-RXN|reaction.ecocyc.L-GLN-FRUCT-6-P-AMINOTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.NAG6PDEACET-RXN|reaction.ecocyc.NAG6PDEACET-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7392|reaction.ecocyc.RXN0-7392]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-167A|reaction.ecocyc.TRANS-RXN-167A]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00765|reaction.R00765]] `KEGG` `database` - C00352 + C00001 <=> C00085 + C00014
- `is_substrate_of` --> [[reaction.ecocyc.5.4.2.10-RXN|reaction.ecocyc.5.4.2.10-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GLUCOSAMINE-6-P-DEAMIN-RXN|reaction.ecocyc.GLUCOSAMINE-6-P-DEAMIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-16424|reaction.ecocyc.RXN-16424]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17745|reaction.ecocyc.RXN-17745]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.GLUTAMINESYN-RXN|reaction.ecocyc.GLUTAMINESYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.NAG6PDEACET-RXN|reaction.ecocyc.NAG6PDEACET-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00352`
- `EcoCyc:CPD-13469`
- `ZINC:ZINC000004097103`
- `REACTOME-CPD:449701`
- `SEED:cpd23898`
- `HMDB:HMDB01254`
- `METANETX:MNXM162238`
- `REFMET:Glucosamine-6-phosphate`
- `CHEBI:75989`
- `DRUGBANK:DB02657`
- `PUBCHEM:25244770`
- `canonicalized_from:molecule.ecocyc.CPD-13469`

## Notes

Included because it appears in at least one E. coli KEGG pathway. | molecule.ecocyc.CPD-13469: EcoCyc:CPD-13469
