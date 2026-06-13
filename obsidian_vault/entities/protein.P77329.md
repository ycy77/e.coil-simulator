---
entity_id: "protein.P77329"
entity_type: "protein"
name: "hyfG"
source_database: "UniProt"
source_id: "P77329"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hyfG b2487 JW2472"
---

# hyfG

`protein.P77329`

## Static

- Type: `protein`
- Source: `UniProt:P77329`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Possible component of hydrogenase 4. {ECO:0000305|PubMed:9387241}. hyfABCDEFGHI encodes a predicted nine subunit Ni-Fe hydrogenase complex (hydrogenase 4). HyfG shows sequence similarity with the large subunit of hydrogenase 3 (HycE) and with the NuoD subunit of NADH oxidoreductase; the protein contains a predicted [Ni-Fe (CO)(CN)2] cluster

## Biological Role

Component of hydrogenase 4 (complex.ecocyc.CPLX0-250).

## Annotation

FUNCTION: Possible component of hydrogenase 4. {ECO:0000305|PubMed:9387241}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-250|complex.ecocyc.CPLX0-250]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2487|gene.b2487]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77329`
- `KEGG:ecj:JW2472;eco:b2487;ecoc:C3026_13800;`
- `GeneID:946964;`
- `GO:GO:0006007; GO:0008137; GO:0009061; GO:0009326; GO:0015944; GO:0016020; GO:0016151; GO:0016651; GO:0019645; GO:0048038; GO:0051287; GO:0051539; GO:0051540`
- `EC:1.-.-.-`

## Notes

Hydrogenase-4 component G (EC 1.-.-.-)
