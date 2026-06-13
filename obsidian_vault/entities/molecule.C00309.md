---
entity_id: "molecule.C00309"
entity_type: "small_molecule"
name: "D-Ribulose"
source_database: "KEGG"
source_id: "C00309"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Ribulose"
  - "D-erythro-2-Pentulose"
  - "D-Arabinoketose"
  - "D-Arabinulose"
  - "D-Riboketose"
  - "D-erythro-pentulose"
  - "D-erythropentulose"
  - "erythropentulose"
---

# D-Ribulose

`molecule.C00309`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00309`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Ribulose; D-erythro-2-Pentulose; D-Arabinoketose; D-Arabinulose; D-Riboketose

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)

## Annotation

KEGG compound: D-Ribulose; D-erythro-2-Pentulose; D-Arabinoketose; D-Arabinulose; D-Riboketose

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.ecocyc.DARABISOM-RXN|reaction.ecocyc.DARABISOM-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RIBITOL-2-DEHYDROGENASE-RXN|reaction.ecocyc.RIBITOL-2-DEHYDROGENASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R01526|reaction.R01526]] `KEGG` `database` - C00002 + C00309 <=> C00008 + C00199
- `is_substrate_of` --> [[reaction.ecocyc.D-RIBULOKIN-RXN|reaction.ecocyc.D-RIBULOKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.DARABKIN-RXN|reaction.ecocyc.DARABKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00309`
- `EcoCyc:D-RIBULOSE`
- `LIGAND-CPD:C05052`
- `CHEBI:17173`
- `SEED:cpd00258`
- `METANETX:MNXM41271`
- `REFMET:D-Ribulose`
- `METABOLIGHTS:MTBLC17173`
- `HMDB:HMDB00621`
- `CHEMSPIDER:133316`
- `PUBCHEM:151261`
- `CAS:5556-48-9`
- `canonicalized_from:molecule.ecocyc.D-RIBULOSE`

## Notes

Included because it appears in at least one E. coli KEGG pathway. | molecule.ecocyc.D-RIBULOSE: EcoCyc:D-RIBULOSE
