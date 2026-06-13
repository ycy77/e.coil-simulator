---
entity_id: "gene.b1708"
entity_type: "gene"
name: "nlpC"
source_database: "NCBI RefSeq"
source_id: "gene-b1708"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1708"
  - "nlpC"
---

# nlpC

`gene.b1708`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1708`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nlpC (gene.b1708) is a gene entity. It encodes nlpC (protein.P23898). Encoded protein function: Probable endopeptidase NlpC (EC 3.4.-.-) (ORF-17) (Probable lipoprotein NlpC) EcoCyc product frame: EG11133-MONOMER. Genomic coordinates: 1792267-1792731. EcoCyc protein note: The NlpC lipoprotein of Escherichia coli exhibits high sequence similarity to the p60 proteins of Listeria species and to the cell wall hydrolase, LytE (CwlF) of Bacillus subtilis .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P23898|protein.P23898]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005704,ECOCYC:EG11133,GeneID:946220`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1792267-1792731:-; feature_type=gene
