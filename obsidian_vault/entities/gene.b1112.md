---
entity_id: "gene.b1112"
entity_type: "gene"
name: "bhsA"
source_database: "NCBI RefSeq"
source_id: "gene-b1112"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1112"
  - "bhsA"
---

# bhsA

`gene.b1112`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1112`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

bhsA (gene.b1112) is a gene entity. It encodes bhsA (protein.P0AB40). Encoded protein function: FUNCTION: Reduces the permeability of the outer membrane to copper. Seems to be involved in the regulation of biofilm formation. May decrease biofilm formation by repressing cell-cell interaction and cell surface interaction. {ECO:0000269|PubMed:17293424, ECO:0000269|PubMed:22089859}. EcoCyc product frame: G6570-MONOMER. EcoCyc synonyms: ycfR, comC. Genomic coordinates: 1169073-1169330. EcoCyc protein note: BhsA/ComC is a small outer membrane protein , involved in biofilm formation and response to stress . Its presence appears to reduce the permeability of the outer membrane to copper . Transcription of bhsA is induced upon biofilm formation compared to planktonic growth in exponential phase and under various cellular stress conditions . Induction of expression was found to be independent of the presence of the F plasmid . Expression of comC is induced 30-fold in the presence of 3mM copper in E. coli wild-type but is induced approximately 270-fold in a comR negative strain indicating that ComR represses comC expression in the wild type . A comC knockout strain is more sensitive to copper than the wild type...

## Biological Role

Repressed by crp (protein.P0ACJ8), comR (protein.P75952). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AB40|protein.P0AB40]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=bhsA; function=+
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=bhsA; function=-
- `represses` <-- [[protein.P75952|protein.P75952]] `RegulonDB` `S` - regulator=ComR; target=bhsA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003758,ECOCYC:G6570,GeneID:945492`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1169073-1169330:+; feature_type=gene
