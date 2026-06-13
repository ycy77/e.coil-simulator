---
entity_id: "gene.b1848"
entity_type: "gene"
name: "yebG"
source_database: "NCBI RefSeq"
source_id: "gene-b1848"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1848"
  - "yebG"
---

# yebG

`gene.b1848`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1848`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yebG (gene.b1848) is a gene entity. It encodes yebG (protein.P0ACY9). Encoded protein function: FUNCTION: May be involved in SOS response. {ECO:0000305|PubMed:10474193, ECO:0000305|PubMed:9368369}. EcoCyc product frame: EG11808-MONOMER. Genomic coordinates: 1930457-1930747. EcoCyc protein note: The yebG gene is a DNA damage-inducible gene of the SOS regulon . Overexpression of yebG increases the MIC of polyhexamethylene biguanide to between 5.25 and 6.75 mg/L . yebG is regulated by the LexA transcriptional repressor . Transcription of yebG is induced by mitomycin C , is induced upon entry into stationary phase, and requires cAMP and H-NS protein . Expression of yebG is induced 14-fold upon exposure of cells to the biocide polyhexamethylene biguanide . Expression of yebG also increases in dam and dam mutS mutants . Expression of yebG is induced 3.9-fold in the presence of autoinducer-2 (AI-2) . A yebG deletion mutant is 6-fold more sensitive to X-radiation than wild type .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACY9|protein.P0ACY9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006145,ECOCYC:EG11808,GeneID:946364`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1930457-1930747:-; feature_type=gene
