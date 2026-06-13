---
entity_id: "molecule.C00127"
entity_type: "small_molecule"
name: "Glutathione disulfide"
source_database: "KEGG"
source_id: "C00127"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Glutathione disulfide"
  - "GSSG"
  - "Oxiglutatione"
  - "Oxidized glutathione"
---

# Glutathione disulfide

`molecule.C00127`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00127`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Glutathione disulfide; GSSG; Oxiglutatione; Oxidized glutathione

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 17 reaction(s).

## Enriched Pathways

- `eco00480` Glutathione metabolism (KEGG)

## Annotation

KEGG compound: Glutathione disulfide; GSSG; Oxiglutatione; Oxidized glutathione

## Pathways

- `eco00480` Glutathione metabolism (KEGG)

## Outgoing Edges (20)

- `is_product_of` --> [[reaction.R00094|reaction.R00094]] `KEGG` `database` - 2 C00051 + C00003 <=> C00127 + C00004 + C00080
- `is_product_of` --> [[reaction.R00115|reaction.R00115]] `KEGG` `database` - 2 C00051 + C00006 <=> C00127 + C00005 + C00080
- `is_product_of` --> [[reaction.R00274|reaction.R00274]] `KEGG` `database` - C00027 + 2 C00051 <=> C00127 + 2 C00001
- `is_product_of` --> [[reaction.ecocyc.1.8.4.4-RXN|reaction.ecocyc.1.8.4.4-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GLUTATHIONE-PEROXIDASE-RXN|reaction.ecocyc.GLUTATHIONE-PEROXIDASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GLUTATHIONE-REDUCT-NADPH-RXN|reaction.ecocyc.GLUTATHIONE-REDUCT-NADPH-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PRODISULFREDUCT-A-RXN|reaction.ecocyc.PRODISULFREDUCT-A-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PRODISULFREDUCT-RXN|reaction.ecocyc.PRODISULFREDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-12864|reaction.ecocyc.RXN-12864]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-14497|reaction.ecocyc.RXN-14497]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-15348|reaction.ecocyc.RXN-15348]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-17886|reaction.ecocyc.RXN-17886]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-19629|reaction.ecocyc.RXN-19629]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6256|reaction.ecocyc.RXN0-6256]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7010|reaction.ecocyc.RXN0-7010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.THIOSULFATE--THIOL-SULFURTRANSFERASE-RXN|reaction.ecocyc.THIOSULFATE--THIOL-SULFURTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-637|reaction.ecocyc.TRANS-RXN0-637]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-637|reaction.ecocyc.TRANS-RXN0-637]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.GLUTATHIONE-REDUCT-NADPH-RXN|reaction.ecocyc.GLUTATHIONE-REDUCT-NADPH-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GLUTATHIONE-SYN-RXN|reaction.ecocyc.GLUTATHIONE-SYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `transports` <-- [[complex.ecocyc.ABC-49-CPLX|complex.ecocyc.ABC-49-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00127`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
