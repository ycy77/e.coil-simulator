---
entity_id: "protein.P77626"
entity_type: "protein"
name: "sutR"
source_database: "UniProt"
source_id: "P77626"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "sutR ydcN b1434 JW1430"
---

# sutR

`protein.P77626`

## Static

- Type: `protein`
- Source: `UniProt:P77626`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Regulates the expression of 12-16 transcription units involved in various steps of sulfur utilization. Represses expression of pfkB, fliZ, cysE, ydcO and its own expression. Activates expression of ypfN. Acts by binding to SutR boxes. {ECO:0000269|PubMed:25406449}. SutR (formely YdcN) regulates a set of genes involved in the utilization of sulfur . SutR is a small transcription factor with a helix-turn-helix (HTH) motif and belongs to the Cro-C1-type superfamily . Based on genomic SELEX screen analysis, it was identified as a highly probable regulator for 12-16 operons involved in various steps of sulfur utilization, playing an important role in the coordination of expression of the genes involved in this metabolic pathway . Genes identified by SELEX analysis include the following: paoC, xseB, thiI, ydcO, sutR, ynfG, ydiY, pfkB, fliZ, ypfN, yfgM, yfiC, tdcF, cysE, and yjcS. Four peaks were located in type A spacers of divergent transcription units (TUs), and eight peaks were identified within type B spacers upstream of one TU but downstream of the preceding TUs . A direct repeat GCGT motif of the SutR box was found in the yfiC, ydcO, and sutR genes, which are associated with group A spacers, and the palindromic sequence of GCGT(Nn)ACGC was identified for yfiC, thiI, ydcO, and sutR genes...

## Annotation

FUNCTION: Regulates the expression of 12-16 transcription units involved in various steps of sulfur utilization. Represses expression of pfkB, fliZ, cysE, ydcO and its own expression. Activates expression of ypfN. Acts by binding to SutR boxes. {ECO:0000269|PubMed:25406449}.

## Outgoing Edges (9)

- `activates` --> [[gene.b1434|gene.b1434]] `RegulonDB` `S` - regulator=SutR; target=sutR; function=-+
- `activates` --> [[gene.b4547|gene.b4547]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b1433|gene.b1433]] `RegulonDB` `S` - regulator=SutR; target=ydcO; function=-
- `represses` --> [[gene.b1434|gene.b1434]] `RegulonDB` `S` - regulator=SutR; target=sutR; function=-+
- `represses` --> [[gene.b1723|gene.b1723]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b1920|gene.b1920]] `RegulonDB` `S` - regulator=SutR; target=tcyJ; function=-
- `represses` --> [[gene.b1921|gene.b1921]] `RegulonDB` `S` - regulator=SutR; target=fliZ; function=-
- `represses` --> [[gene.b1922|gene.b1922]] `RegulonDB` `S` - regulator=SutR; target=fliA; function=-
- `represses` --> [[gene.b3607|gene.b3607]] `RegulonDB` `S` - regulator=SutR; target=cysE; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b1434|gene.b1434]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77626`
- `KEGG:ecj:JW1430;eco:b1434;ecoc:C3026_08350;`
- `GeneID:75202355;946000;`
- `GO:GO:0003677; GO:0003700; GO:0006355; GO:0043565; GO:0045892; GO:0045893`

## Notes

HTH-type transcriptional regulator SutR (Sulfur utilization regulator)
