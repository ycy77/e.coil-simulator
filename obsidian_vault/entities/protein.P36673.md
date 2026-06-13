---
entity_id: "protein.P36673"
entity_type: "protein"
name: "treR"
source_database: "UniProt"
source_id: "P36673"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "treR b4241 JW4200"
---

# treR

`protein.P36673`

## Static

- Type: `protein`
- Source: `UniProt:P36673`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Repressor of the treBC operon. It is able to bind trehalose-6-phosphate and trehalose. {ECO:0000269|PubMed:7608078, ECO:0000269|PubMed:9148912}.

## Biological Role

Component of DNA-binding transcriptional repressor TreR (complex.ecocyc.CPLX0-7854), TreR-D-trehalose 6-phosphate (complex.ecocyc.CPLX0-8056).

## Annotation

FUNCTION: Repressor of the treBC operon. It is able to bind trehalose-6-phosphate and trehalose. {ECO:0000269|PubMed:7608078, ECO:0000269|PubMed:9148912}.

## Outgoing Edges (4)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7854|complex.ecocyc.CPLX0-7854]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-8056|complex.ecocyc.CPLX0-8056]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b4239|gene.b4239]] `RegulonDB` `S` - regulator=TreR; target=treC; function=-
- `represses` --> [[gene.b4240|gene.b4240]] `RegulonDB` `S` - regulator=TreR; target=treB; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b4241|gene.b4241]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P36673`
- `KEGG:ecj:JW4200;eco:b4241;ecoc:C3026_22890;`
- `GeneID:948760;`
- `GO:GO:0000976; GO:0003700; GO:0005991; GO:0006355; GO:0045892`

## Notes

HTH-type transcriptional regulator TreR (Trehalose operon repressor)
