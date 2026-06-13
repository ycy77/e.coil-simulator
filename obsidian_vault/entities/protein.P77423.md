---
entity_id: "protein.P77423"
entity_type: "protein"
name: "hyfH"
source_database: "UniProt"
source_id: "P77423"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hyfH b2488 JW2473"
---

# hyfH

`protein.P77423`

## Static

- Type: `protein`
- Source: `UniProt:P77423`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Probable electron transfer protein for hydrogenase 4. {ECO:0000305|PubMed:9387241}. hyfABCDEFGHI encodes a potential nine subunit [Ni-Fe]hydrogenase complex (hydrogenase 4). HyfH resembles the HycF subunit of hydrogenase 3 (44% sequence identity); the protein is predicted to contain three Fe-S redox sites (two [4Fe-4S] clusters and one mononuclear site) (see also ).

## Biological Role

Component of hydrogenase 4 (complex.ecocyc.CPLX0-250).

## Annotation

FUNCTION: Probable electron transfer protein for hydrogenase 4. {ECO:0000305|PubMed:9387241}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-250|complex.ecocyc.CPLX0-250]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2488|gene.b2488]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77423`
- `KEGG:ecj:JW2473;eco:b2488;ecoc:C3026_13805;`
- `GeneID:946965;`
- `GO:GO:0009060; GO:0016020; GO:0016651; GO:0046872; GO:0051539`

## Notes

Hydrogenase-4 component H
