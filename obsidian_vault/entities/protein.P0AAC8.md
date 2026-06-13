---
entity_id: "protein.P0AAC8"
entity_type: "protein"
name: "iscA"
source_database: "UniProt"
source_id: "P0AAC8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "iscA yfhF b2528 JW2512"
---

# iscA

`protein.P0AAC8`

## Static

- Type: `protein`
- Source: `UniProt:P0AAC8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Is able to transfer iron-sulfur clusters to apo-ferredoxin. Multiple cycles of [2Fe2S] cluster formation and transfer are observed, suggesting that IscA acts catalytically. Recruits intracellular free iron so as to provide iron for the assembly of transient iron-sulfur cluster in IscU in the presence of IscS, L-cysteine and the thioredoxin reductase system TrxA/TrxB.

## Biological Role

Component of [Fe-S] cluster insertion protein IscA (complex.ecocyc.CPLX0-7908).

## Annotation

FUNCTION: Is able to transfer iron-sulfur clusters to apo-ferredoxin. Multiple cycles of [2Fe2S] cluster formation and transfer are observed, suggesting that IscA acts catalytically. Recruits intracellular free iron so as to provide iron for the assembly of transient iron-sulfur cluster in IscU in the presence of IscS, L-cysteine and the thioredoxin reductase system TrxA/TrxB.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7908|complex.ecocyc.CPLX0-7908]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b2528|gene.b2528]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AAC8`
- `KEGG:ecj:JW2512;eco:b2528;ecoc:C3026_14010;`
- `GeneID:86860654;93774608;946999;`
- `GO:GO:0005737; GO:0005829; GO:0008198; GO:0016226; GO:0034986; GO:0051537; GO:0051604; GO:1990230`

## Notes

Iron-binding protein IscA (Iron-sulfur cluster assembly protein)
