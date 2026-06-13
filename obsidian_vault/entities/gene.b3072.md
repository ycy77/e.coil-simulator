---
entity_id: "gene.b3072"
entity_type: "gene"
name: "aer"
source_database: "NCBI RefSeq"
source_id: "gene-b3072"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3072"
  - "aer"
---

# aer

`gene.b3072`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3072`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

aer (gene.b3072) is a gene entity. It encodes aer (protein.P50466). Encoded protein function: FUNCTION: Signal transducer for aerotaxis. The aerotactic response is the accumulation of cells around air bubbles. The nature of the sensory stimulus detected by this protein is the proton motive force or cellular redox state. It uses a FAD prosthetic group as a redox sensor to monitor oxygen levels. {ECO:0000269|PubMed:9190831, ECO:0000269|PubMed:9380671}. EcoCyc product frame: G7595-MONOMER. EcoCyc synonyms: yqjJ, air. Genomic coordinates: 3217556-3219076.

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by fnr (protein.P0A9E5), crp (protein.P0ACJ8), fliA (protein.P0AEM6).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P50466|protein.P50466]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=aer; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=aer; function=+
- `activates` <-- [[protein.P0AEM6|protein.P0AEM6]] `RegulonDB` `S` - sigma=sigma28; target=aer; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010087,ECOCYC:G7595,GeneID:945301`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3217556-3219076:-; feature_type=gene
