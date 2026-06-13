---
entity_id: "protein.P23481"
entity_type: "protein"
name: "hyfA"
source_database: "UniProt"
source_id: "P23481"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hyfA yffE b2481 JW2466"
---

# hyfA

`protein.P23481`

## Static

- Type: `protein`
- Source: `UniProt:P23481`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Probable electron transfer protein for hydrogenase 4. {ECO:0000305|PubMed:9387241}. hyfABCDEFGHI encodes a potential nine subunit [Ni-Fe]hydrogenase complex (hydrogenase 4). HyfA resembles the HycB subunit of hydrogenase 3 (50% sequence identity); the protein is predicted to contain four [4Fe-4S] clusters and may function as an electron transferring subunit . HyfA may contain some β-structure elements

## Biological Role

Component of hydrogenase 4 (complex.ecocyc.CPLX0-250).

## Annotation

FUNCTION: Probable electron transfer protein for hydrogenase 4. {ECO:0000305|PubMed:9387241}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-250|complex.ecocyc.CPLX0-250]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2481|gene.b2481]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P23481`
- `KEGG:ecj:JW2466;eco:b2481;ecoc:C3026_13770;`
- `GeneID:946959;`
- `GO:GO:0016491; GO:0046872; GO:0051539`
- `EC:1.-.-.-`

## Notes

Hydrogenase-4 component A (EC 1.-.-.-)
