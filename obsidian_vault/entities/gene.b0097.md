---
entity_id: "gene.b0097"
entity_type: "gene"
name: "secM"
source_database: "NCBI RefSeq"
source_id: "gene-b0097"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0097"
  - "secM"
---

# secM

`gene.b0097`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0097`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

secM (gene.b0097) is a gene entity. It encodes secM (protein.P62395). Encoded protein function: FUNCTION: Regulates secA expression by translational coupling of the secM secA operon. Ribosomes translating the C-terminal region of secM can disrupt an RNA repressor helix that normally blocks secA translation initiation, derepressing the expression of secA. Translational pausing of secM at Pro-166 under secretion-limiting conditions increases the duration of the disruption and thus increases secA expression. This is controlled by interaction of the secM signal peptide with secA and the translocon, possibly by secA pulling the paused secM out of the ribosome. The arrest sequence (150-FXXXXWIXXXXGIRAGP-166) is sufficient to cause arrest of unrelated proteins (PubMed:11893334). Elongation arrest can be alleviated by mutations in the 23S rRNA or in ribosomal protein L22. Elongation arrest can be alleviated by YheS in vitro (PubMed:38661232). {ECO:0000269|PubMed:11893334, ECO:0000269|PubMed:38661232}. EcoCyc product frame: EG11087-MONOMER. EcoCyc synonyms: srrA, yacA. Genomic coordinates: 107705-108217. EcoCyc protein note: secM encodes a presecretory protein that regulates production of the protein translocation ATPase CPLX0-8089 SecA via translation arrest...

## Enriched Pathways

- `eco03060` Protein export (KEGG)
- `eco03070` Bacterial secretion system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P62395|protein.P62395]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000340,ECOCYC:EG11087,GeneID:944831`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:107705-108217:+; feature_type=gene
