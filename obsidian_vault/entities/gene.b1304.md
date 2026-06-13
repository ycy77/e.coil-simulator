---
entity_id: "gene.b1304"
entity_type: "gene"
name: "pspA"
source_database: "NCBI RefSeq"
source_id: "gene-b1304"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1304"
  - "pspA"
---

# pspA

`gene.b1304`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1304`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pspA (gene.b1304) is a gene entity. It encodes pspA (protein.P0AFM6). Encoded protein function: FUNCTION: The phage shock protein (psp) operon (pspABCDE) may play a significant role in the competition for survival under nutrient- or energy-limited conditions. PspA negatively regulates expression of the pspABCDE promoter and of pspG through negative regulation of the psp-specific transcriptional activator PspF. Is also required for membrane integrity, efficient translocation and maintenance of the proton motive force. {ECO:0000269|PubMed:10629175, ECO:0000269|PubMed:15485810, ECO:0000269|PubMed:1712397, ECO:0000269|PubMed:19804784, ECO:0000269|PubMed:8598199}. EcoCyc product frame: EG10776-MONOMER. EcoCyc synonyms: cog. Genomic coordinates: 1368079-1368747. EcoCyc protein note: PspA is a bifunctional protein, protecting membrane integrity under stress conditions and regulating EG12344-MONOMER PspF transcription factor activity. PspA was first identified as a highly expressed protein upon infection of E. coli with the filamentous phage f1. PspA is a bacterial member of the conserved ESCRT-III family of proteins which are involved in membrane remodelling and repair across all domains of life . Based on its heptad repeat motif, PspA was predicted to form a coiled-coil structure...

## Biological Role

Activated by pspF (protein.P37344).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFM6|protein.P0AFM6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P37344|protein.P37344]] `RegulonDB` `S` - regulator=PspF; target=pspA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0004387,ECOCYC:EG10776,GeneID:945887`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1368079-1368747:+; feature_type=gene
