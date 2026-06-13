---
entity_id: "protein.Q46866"
entity_type: "protein"
name: "ygiV"
source_database: "UniProt"
source_id: "Q46866"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ygiV b3023 JW5502"
---

# ygiV

`protein.Q46866`

## Static

- Type: `protein`
- Source: `UniProt:Q46866`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Represses expression of mcbR. {ECO:0000269|PubMed:18309357}. YgiV had been predicted as a transcriptional regulator . However, based on nickel enrichment DNA microarrays and additional gel shift assays, it was identified as a transcriptional repressor of mcbR, which regulates biofilm formation and mucoidity by repressing expression of mcbA (ybiM) . In the E. coli K-12-derived strain BW25113, a ygiV knockout mutant, only a slightly increase in biofilm formation was observed, in contrast to the large decrease observed with the same mutation in the pathogenic strain UPEC CFT073 . MqsR has a toxic effect on Escherichia coli bacterial growth, which is partially reduced by the ygiV mutation . Inhibition of ygiV expression by CRISPRi reduced cellular fitness under treatment with the antibiotics pyocyanin or novobiocin .

## Annotation

FUNCTION: Represses expression of mcbR. {ECO:0000269|PubMed:18309357}.

## Outgoing Edges (1)

- `represses` --> [[gene.b1450|gene.b1450]] `RegulonDB` `S` - regulator=YgiV; target=mcbR; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b3023|gene.b3023]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q46866`
- `KEGG:ecj:JW5502;eco:b3023;ecoc:C3026_16515;`
- `GeneID:945805;`
- `GO:GO:0045892`

## Notes

Probable transcriptional regulator YgiV
