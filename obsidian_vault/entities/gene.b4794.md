---
entity_id: "gene.b4794"
entity_type: "gene"
name: "baxL"
source_database: "NCBI RefSeq"
source_id: "gene-b4794"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4794"
  - "baxL"
---

# baxL

`gene.b4794`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4794`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

baxL (gene.b4794) is a gene entity. It encodes baxL (protein.P0DSH2). Encoded protein function: FUNCTION: May serve a regulatory role in expression of downstream gene baxA; in a baxL-baxA-lacZ fusion mutation of the start codon to a stop codon in baxL increases expression of beta-galactosidase. {ECO:0000269|PubMed:30837344}. EcoCyc product frame: MONOMER0-4506. Genomic coordinates: 3737177-3737203. EcoCyc protein note: BaxL was identified as a previously unannotated small protein; its expression is higher during exponential phase than during stationary phase in rich media. Introduction of a stop codon into the baxL ORF leads to increased expression of the downstream baxA gene, suggesting a regulatory role of BaxL .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0DSH2|protein.P0DSH2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ECOCYC:G0-17040,GeneID:63925657`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3737177-3737203:-; feature_type=gene
