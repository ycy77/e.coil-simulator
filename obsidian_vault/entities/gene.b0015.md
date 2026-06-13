---
entity_id: "gene.b0015"
entity_type: "gene"
name: "dnaJ"
source_database: "NCBI RefSeq"
source_id: "gene-b0015"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0015"
  - "dnaJ"
---

# dnaJ

`gene.b0015`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0015`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dnaJ (gene.b0015) is a gene entity. It encodes dnaJ (protein.P08622). Encoded protein function: FUNCTION: Interacts with DnaK and GrpE to disassemble a protein complex at the origins of replication of phage lambda and several plasmids. Participates actively in the response to hyperosmotic and heat shock by preventing the aggregation of stress-denatured proteins and by disaggregating proteins, also in an autonomous, DnaK-independent fashion. Unfolded proteins bind initially to DnaJ; upon interaction with the DnaJ-bound protein, DnaK hydrolyzes its bound ATP, resulting in the formation of a stable complex. GrpE releases ADP from DnaK; ATP binding to DnaK triggers the release of the substrate protein, thus completing the reaction cycle. Several rounds of ATP-dependent interactions between DnaJ, DnaK and GrpE are required for fully efficient folding. {ECO:0000269|PubMed:15044009, ECO:0000269|PubMed:15302880, ECO:0000269|PubMed:15485812, ECO:0000269|PubMed:1826368}. EcoCyc product frame: EG10240-MONOMER. EcoCyc synonyms: groP, grpC. Genomic coordinates: 14168-15298.

## Biological Role

Activated by rpoH (protein.P0AGB3).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P08622|protein.P08622]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=dnaJ; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000054,ECOCYC:EG10240,GeneID:944753`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:14168-15298:+; feature_type=gene
