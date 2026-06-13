---
entity_id: "protein.P0ABF1"
entity_type: "protein"
name: "pcnB"
source_database: "UniProt"
source_id: "P0ABF1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:15737627}. Cell inner membrane {ECO:0000269|PubMed:15737627}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pcnB b0143 JW5808"
---

# pcnB

`protein.P0ABF1`

## Static

- Type: `protein`
- Source: `UniProt:P0ABF1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:15737627}. Cell inner membrane {ECO:0000269|PubMed:15737627}.

## Enriched Summary

FUNCTION: Adds poly(A) tail to the 3' end of many RNAs, which usually targets these RNAs for decay. Plays a significant role in the global control of gene expression, through influencing the rate of transcript degradation, and in the general RNA quality control. Rho-independent transcription terminators may serve as polyadenylation signals. Seems to be involved in plasmid copy number control. {ECO:0000255|HAMAP-Rule:MF_00957, ECO:0000269|PubMed:10594833, ECO:0000269|PubMed:1438224, ECO:0000269|PubMed:17040898}. Poly(A) polymerase I (PAP I) is responsible for the polyadenylation of 3' ends of RNA molecules. PAP I polyadenylates the vast majority of mRNA transcripts . Unlike in eukaryotes, increased polyadenylation of mRNAs leads to decreased mRNA half-life . Rho-independent transcription terminators appear to serve as targeting signals for polyadenylation . The Hfq protein appears to be involved in the recognition of 3' termini of RNA by poly(A) polymerase I . Polyadenylation of tRNA fragment has been demonstrated during tRNA processing of Glu2, Ile1 and Ala1B tRNAs. The breakdown of the 3' ends of the tRNA by other 3' → 5' exonucleases appears to be dependent on the polyadenylation by PAP I . Intracellular levels of PAP I as well as the level of pcnB transcription vary inversely with growth rate . Overexpression of PAP I is toxic and leads to slowed growth...

## Biological Role

Catalyzes ATP:polynucleotide adenylyltransferase; (reaction.R00435), POLYNUCLEOTIDE-ADENYLYLTRANSFERASE-RXN (reaction.ecocyc.POLYNUCLEOTIDE-ADENYLYLTRANSFERASE-RXN), polyadenylation of an RNA fragment (reaction.ecocyc.RXN0-7462).

## Enriched Pathways

- `eco03018` RNA degradation (KEGG)

## Annotation

FUNCTION: Adds poly(A) tail to the 3' end of many RNAs, which usually targets these RNAs for decay. Plays a significant role in the global control of gene expression, through influencing the rate of transcript degradation, and in the general RNA quality control. Rho-independent transcription terminators may serve as polyadenylation signals. Seems to be involved in plasmid copy number control. {ECO:0000255|HAMAP-Rule:MF_00957, ECO:0000269|PubMed:10594833, ECO:0000269|PubMed:1438224, ECO:0000269|PubMed:17040898}.

## Pathways

- `eco03018` RNA degradation (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00435|reaction.R00435]] `KEGG` `database` - via EC:2.7.7.19
- `catalyzes` --> [[reaction.ecocyc.POLYNUCLEOTIDE-ADENYLYLTRANSFERASE-RXN|reaction.ecocyc.POLYNUCLEOTIDE-ADENYLYLTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7462|reaction.ecocyc.RXN0-7462]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0143|gene.b0143]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABF1`
- `KEGG:ecj:JW5808;eco:b0143;`
- `GeneID:93777284;947318;`
- `GO:GO:0003723; GO:0005524; GO:0005737; GO:0005829; GO:0005886; GO:0006276; GO:0006397; GO:0009451; GO:0042780; GO:0043633; GO:0071047; GO:1990817`
- `EC:2.7.7.19`

## Notes

Poly(A) polymerase I (PAP I) (EC 2.7.7.19) (Plasmid copy number protein)
