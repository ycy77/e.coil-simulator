---
entity_id: "gene.b1084"
entity_type: "gene"
name: "rne"
source_database: "NCBI RefSeq"
source_id: "gene-b1084"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1084"
  - "rne"
---

# rne

`gene.b1084`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1084`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rne (gene.b1084) is a gene entity. It encodes rne (protein.P21513). Encoded protein function: FUNCTION: Endoribonuclease that plays a central role in RNA processing and decay. Required for the maturation of 5S and 16S rRNAs and the majority of tRNAs. Also involved in the degradation of most mRNAs. Can also process other RNA species, such as RNAI, a molecule that controls the replication of ColE1 plasmid, and the cell division inhibitor DicF-RNA. It initiates the decay of RNAs by cutting them internally near their 5'-end. It is able to remove poly(A) tails by an endonucleolytic process. Required to initiate rRNA degradation during both starvation and quality control; acts after RNase PH (rph) exonucleolytically digests the 3'-end of the 16S rRNA (PubMed:27298395). Degradation of 16S rRNA leads to 23S rRNA degradation (PubMed:27298395). Processes the 3 tRNA(Pro) precursors immediately after the 3'-CCA to generate the mature ends (PubMed:27288443). {ECO:0000255|HAMAP-Rule:MF_00970, ECO:0000269|PubMed:10329633, ECO:0000269|PubMed:10762247, ECO:0000269|PubMed:11328869, ECO:0000269|PubMed:11871663, ECO:0000269|PubMed:16237448, ECO:0000269|PubMed:1691299, ECO:0000269|PubMed:1708438, ECO:0000269|PubMed:19889093, ECO:0000269|PubMed:27288443, ECO:0000269|PubMed:27298395, ECO:0000269|PubMed:6339234, ECO:0000269|PubMed:9732274}...

## Biological Role

Repressed by rne (protein.P21513). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco03018` RNA degradation (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P21513|protein.P21513]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rne; function=+
- `represses` <-- [[protein.P21513|protein.P21513]] `RegulonDB` `S` - regulator=ribonuclease E; target=rne; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003668,ECOCYC:EG10859,GeneID:945641`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1141182-1144367:-; feature_type=gene
