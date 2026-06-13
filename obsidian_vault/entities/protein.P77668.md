---
entity_id: "protein.P77668"
entity_type: "protein"
name: "hyfI"
source_database: "UniProt"
source_id: "P77668"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hyfI b2489 JW5805"
---

# hyfI

`protein.P77668`

## Static

- Type: `protein`
- Source: `UniProt:P77668`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Possible component of hydrogenase 4. {ECO:0000305|PubMed:9387241}. hyfABCDEFGHI encodes a predicted nine subunit Ni-Fe hydrogenase complex (hydrogenase 4). HyfI resembles the small subunit (HycG) of hydrogenase 3 (63% sequence identity) and the NuoB subunit of NADH oxidoreductase (27% sequence identity); the protein contains a predicted [4Fe-4S] cluster (see also ).

## Biological Role

Component of hydrogenase 4 (complex.ecocyc.CPLX0-250).

## Annotation

FUNCTION: Possible component of hydrogenase 4. {ECO:0000305|PubMed:9387241}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-250|complex.ecocyc.CPLX0-250]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2489|gene.b2489]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77668`
- `KEGG:ecj:JW5805;eco:b2489;ecoc:C3026_13810;`
- `GeneID:946966;`
- `GO:GO:0008137; GO:0009326; GO:0015944; GO:0016491; GO:0019645; GO:0046872; GO:0048038; GO:0051539`
- `EC:1.-.-.-`

## Notes

Hydrogenase-4 component I (EC 1.-.-.-)
