---
entity_id: "gene.b0315"
entity_type: "gene"
name: "pdeL"
source_database: "NCBI RefSeq"
source_id: "gene-b0315"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0315"
  - "pdeL"
---

# pdeL

`gene.b0315`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0315`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pdeL (gene.b0315) is a gene entity. It encodes pdeL (protein.P21514). Encoded protein function: FUNCTION: Acts both as an enzyme and as a c-di-GMP sensor to couple transcriptional activity to the c-di-GMP status of the cell (PubMed:26553851). Phosphodiesterase (PDE) that catalyzes the hydrolysis of cyclic-di-GMP (c-di-GMP) to 5'-pGpG (PubMed:15995192, PubMed:24451384, PubMed:26553851). Also acts as a transcription factor to control its own expression (PubMed:26553851). {ECO:0000269|PubMed:15995192, ECO:0000269|PubMed:24451384, ECO:0000269|PubMed:26553851}. EcoCyc product frame: EG11236-MONOMER. EcoCyc synonyms: yahA. Genomic coordinates: 332371-333459.

## Biological Role

Repressed by hns (protein.P0ACF8), cra (protein.P0ACP1), nac (protein.Q47005). Activated by pdeL (protein.P21514).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P21514|protein.P21514]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P21514|protein.P21514]] `RegulonDB` `C` - regulator=PdeL; target=pdeL; function=+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=pdeL; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=pdeL; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001086,ECOCYC:EG11236,GeneID:947459`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:332371-333459:+; feature_type=gene
