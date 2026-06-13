---
entity_id: "protein.P77416"
entity_type: "protein"
name: "hyfD"
source_database: "UniProt"
source_id: "P77416"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hyfD b2484 JW2469"
---

# hyfD

`protein.P77416`

## Static

- Type: `protein`
- Source: `UniProt:P77416`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: Possible component of hydrogenase 4. {ECO:0000305|PubMed:9387241}. hyfABCDEFGHI encodes a potential nine subunit [Ni-Fe]hydrogenase complex (hydrogenase 4). HyfD is predicted to be an integral membrane protein with 14 transmembrane domains

## Biological Role

Component of hydrogenase 4 (complex.ecocyc.CPLX0-250).

## Annotation

FUNCTION: Possible component of hydrogenase 4. {ECO:0000305|PubMed:9387241}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-250|complex.ecocyc.CPLX0-250]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2484|gene.b2484]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77416`
- `KEGG:ecj:JW2469;eco:b2484;ecoc:C3026_13785;`
- `GeneID:947290;`
- `GO:GO:0005886; GO:0006007; GO:0008137; GO:0009061; GO:0009326; GO:0015944; GO:0015990; GO:0016020; GO:0016491; GO:0019645; GO:0042773`
- `EC:1.-.-.-`

## Notes

Hydrogenase-4 component D (EC 1.-.-.-)
