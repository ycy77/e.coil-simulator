---
entity_id: "gene.b0905"
entity_type: "gene"
name: "ycaO"
source_database: "NCBI RefSeq"
source_id: "gene-b0905"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0905"
  - "ycaO"
---

# ycaO

`gene.b0905`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0905`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ycaO (gene.b0905) is a gene entity. It encodes ycaO (protein.P75838). Encoded protein function: FUNCTION: Involved in beta-methylthiolation of ribosomal protein S12. {ECO:0000269|PubMed:21169565}. EcoCyc product frame: G6468-MONOMER. Genomic coordinates: 954872-956632. EcoCyc protein note: The YcaO protein is involved in the β-methylthiolation of EG10911-MONOMER. YcaO interacts directly with a ribonucleoprotein complex containing S12 . The molecular function of E. coli YcaO is unknown; however, the YcaO domain and its ATP binding motif define the YcaO superfamily which includes proteins that catalyze cyclodehydration, amidation and thioamidation reactions . Crystal structures of apo- and nucleotide-bound YcaO have been solved, showing a circularly symmetric homodimer. The protein consists of an N-terminal domain with a broadly conserved and previously unknown ATP-binding fold and a C-terminal dimerization domain. The purified protein hydrolyzes ATP to AMP and pyrophosphate in vitro . A ycaO deletion mutant contains significantly reduced levels of β-methylthiolated ribosomal protein S12 and has an altered transcriptional profile similar to that of a rimO deletion mutant . Review:

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75838|protein.P75838]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003081,ECOCYC:G6468,GeneID:945509`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:954872-956632:-; feature_type=gene
