---
entity_id: "protein.P76268"
entity_type: "protein"
name: "kdgR"
source_database: "UniProt"
source_id: "P76268"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "kdgR yebP b1827 JW1816"
---

# kdgR

`protein.P76268`

## Static

- Type: `protein`
- Source: `UniProt:P76268`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Transcriptional repressor that negatively regulates the expression of kdgT, kdgK and kdgA, which encode proteins involved in transport and catabolism of 2-keto-3-deoxygluconate (KDG) (PubMed:4359651). Also represses expression of eda, which encodes the Entner-Doudoroff aldolase, by binding to its P2 promoter region (PubMed:15659677). {ECO:0000269|PubMed:15659677, ECO:0000269|PubMed:4359651}. The "2-Keto-3-deoxygluconate repressor," KdgR, is a DNA-binding transcription factor that represses transcription of the operons involved in transport and catabolism of 2-keto-3-deoxy gluconate (KDG) . Synthesis of these genes is induced when E. coli is grown in the presence of KDG and under high-temperature conditions, between 32 and 35°C. Although little is known about the regulating mechanism of KdgR, it has been shown to act as a repressor that binds to a putative inverted repeat sequence . Comparative analysis of intergenic DNA sequences showed the consistent occurrence of KdgR possible binding sites upstream of the genes not related to the transport and catabolism of KDG . It appears that the kdgR gene undergoes adaptive mutations when E. coli invades a mammalian host...

## Annotation

FUNCTION: Transcriptional repressor that negatively regulates the expression of kdgT, kdgK and kdgA, which encode proteins involved in transport and catabolism of 2-keto-3-deoxygluconate (KDG) (PubMed:4359651). Also represses expression of eda, which encodes the Entner-Doudoroff aldolase, by binding to its P2 promoter region (PubMed:15659677). {ECO:0000269|PubMed:15659677, ECO:0000269|PubMed:4359651}.

## Outgoing Edges (1)

- `represses` --> [[gene.b1850|gene.b1850]] `RegulonDB` `S` - regulator=KdgR; target=eda; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b1827|gene.b1827]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76268`
- `KEGG:ecj:JW1816;eco:b1827;ecoc:C3026_10415;`
- `GeneID:946129;`
- `GO:GO:0003677; GO:0003700; GO:0005829; GO:0045892`

## Notes

HTH-type transcriptional regulator KdgR
