---
entity_id: "protein.P0AEW1"
entity_type: "protein"
name: "hyfE"
source_database: "UniProt"
source_id: "P0AEW1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:9278503}; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hyfE b2485 JW2470"
---

# hyfE

`protein.P0AEW1`

## Static

- Type: `protein`
- Source: `UniProt:P0AEW1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:9278503}; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Possible component of hydrogenase 4. {ECO:0000305|PubMed:9387241}. hyfABCDEFGHI encodes a potential nine subunit [Ni-Fe]hydrogenase complex (hydrogenase 4). HyfE is predicted to be an integral membrane protein with 7 transmembrane domains

## Biological Role

Component of hydrogenase 4 (complex.ecocyc.CPLX0-250).

## Annotation

FUNCTION: Possible component of hydrogenase 4. {ECO:0000305|PubMed:9387241}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-250|complex.ecocyc.CPLX0-250]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2485|gene.b2485]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEW1`
- `KEGG:ecj:JW2470;eco:b2485;ecoc:C3026_13790;`
- `GeneID:93774653;945298;`
- `GO:GO:0005886; GO:0006007; GO:0009061; GO:0009326; GO:0015944; GO:0016020; GO:0016491; GO:0019645`
- `EC:1.-.-.-`

## Notes

Hydrogenase-4 component E (EC 1.-.-.-)
