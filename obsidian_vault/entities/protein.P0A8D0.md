---
entity_id: "protein.P0A8D0"
entity_type: "protein"
name: "nrdR"
source_database: "UniProt"
source_id: "P0A8D0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nrdR ybaD b0413 JW0403"
---

# nrdR

`protein.P0A8D0`

## Static

- Type: `protein`
- Source: `UniProt:P0A8D0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Represses transcription of the class Ib RNR genes nrdHIEF but has much smaller effect on transcription of the class Ia RNR genes nrdAB and class III RNR genes nrdDG. By binding to nrdR boxes in the promoter regions to alter promoter activity, nrdR differentially regulates nrdAB, nrdHIEF and nrdD transcription in aerobic growth. {ECO:0000269|PubMed:17496099}.

## Biological Role

Component of NrdR transcriptional Repressor (complex.ecocyc.CPLX0-13264).

## Annotation

FUNCTION: Represses transcription of the class Ib RNR genes nrdHIEF but has much smaller effect on transcription of the class Ia RNR genes nrdAB and class III RNR genes nrdDG. By binding to nrdR boxes in the promoter regions to alter promoter activity, nrdR differentially regulates nrdAB, nrdHIEF and nrdD transcription in aerobic growth. {ECO:0000269|PubMed:17496099}.

## Outgoing Edges (10)

- `is_component_of` --> [[complex.ecocyc.CPLX0-13264|complex.ecocyc.CPLX0-13264]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4
- `represses` --> [[gene.b2234|gene.b2234]] `RegulonDB` `S` - regulator=NrdR; target=nrdA; function=-
- `represses` --> [[gene.b2235|gene.b2235]] `RegulonDB` `S` - regulator=NrdR; target=nrdB; function=-
- `represses` --> [[gene.b2236|gene.b2236]] `RegulonDB` `S` - regulator=NrdR; target=yfaE; function=-
- `represses` --> [[gene.b2673|gene.b2673]] `RegulonDB` `S` - regulator=NrdR; target=nrdH; function=-
- `represses` --> [[gene.b2674|gene.b2674]] `RegulonDB` `S` - regulator=NrdR; target=nrdI; function=-
- `represses` --> [[gene.b2675|gene.b2675]] `RegulonDB` `S` - regulator=NrdR; target=nrdE; function=-
- `represses` --> [[gene.b2676|gene.b2676]] `RegulonDB` `S` - regulator=NrdR; target=nrdF; function=-
- `represses` --> [[gene.b4237|gene.b4237]] `RegulonDB` `S` - regulator=NrdR; target=nrdG; function=-
- `represses` --> [[gene.b4238|gene.b4238]] `RegulonDB` `S` - regulator=NrdR; target=nrdD; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b0413|gene.b0413]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A8D0`
- `KEGG:ecj:JW0403;eco:b0413;ecoc:C3026_02015;`
- `GeneID:86862958;93777047;947437;`
- `GO:GO:0003690; GO:0005524; GO:0008270; GO:0045892`

## Notes

Transcriptional repressor NrdR
