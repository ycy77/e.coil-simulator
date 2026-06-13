---
entity_id: "protein.P23482"
entity_type: "protein"
name: "hyfB"
source_database: "UniProt"
source_id: "P23482"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hyfB yffF b2482 JW2467"
---

# hyfB

`protein.P23482`

## Static

- Type: `protein`
- Source: `UniProt:P23482`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: Possible component of hydrogenase 4. {ECO:0000305|PubMed:9387241}. hyfABCDEFGHI encodes a potential nine subunit [Ni-Fe]hydrogenase complex (hydrogenase 4). HyfB is predicted to be an integral membrane protein with 16 transmembrane domains; the protein has sequence similarity to the HycC subunit of hydrogenase 3

## Biological Role

Component of hydrogenase 4 (complex.ecocyc.CPLX0-250).

## Annotation

FUNCTION: Possible component of hydrogenase 4. {ECO:0000305|PubMed:9387241}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-250|complex.ecocyc.CPLX0-250]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2482|gene.b2482]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P23482`
- `KEGG:ecj:JW2467;eco:b2482;ecoc:C3026_13775;`
- `GeneID:946961;`
- `GO:GO:0005886; GO:0006007; GO:0008137; GO:0009061; GO:0009326; GO:0015944; GO:0016020; GO:0016491; GO:0019645; GO:0042773`
- `EC:1.-.-.-`

## Notes

Hydrogenase-4 component B (EC 1.-.-.-)
