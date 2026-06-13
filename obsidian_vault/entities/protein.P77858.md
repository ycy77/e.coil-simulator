---
entity_id: "protein.P77858"
entity_type: "protein"
name: "hyfC"
source_database: "UniProt"
source_id: "P77858"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:9278503}; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hyfC b2483 JW2468"
---

# hyfC

`protein.P77858`

## Static

- Type: `protein`
- Source: `UniProt:P77858`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:9278503}; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Possible component of hydrogenase 4. {ECO:0000305|PubMed:9387241}. hyfABCDEFGHI encodes a potential nine subunit [Ni-Fe]hydrogenase complex (hydrogenase 4). HyfC is predicted to be an integral membrane protein with 8 transmembrane domains; the protein has sequence similarity to the HycD subunit of hydrogenase 3

## Biological Role

Component of hydrogenase 4 (complex.ecocyc.CPLX0-250).

## Annotation

FUNCTION: Possible component of hydrogenase 4. {ECO:0000305|PubMed:9387241}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-250|complex.ecocyc.CPLX0-250]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2483|gene.b2483]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77858`
- `KEGG:ecj:JW2468;eco:b2483;ecoc:C3026_13780;`
- `GeneID:947492;`
- `GO:GO:0005886; GO:0006007; GO:0006974; GO:0009061; GO:0009326; GO:0015944; GO:0016020; GO:0016491; GO:0019645`
- `EC:1.-.-.-`

## Notes

Hydrogenase-4 component C (EC 1.-.-.-)
