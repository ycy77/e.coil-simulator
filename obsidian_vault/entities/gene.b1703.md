---
entity_id: "gene.b1703"
entity_type: "gene"
name: "ppsR"
source_database: "NCBI RefSeq"
source_id: "gene-b1703"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1703"
  - "ppsR"
---

# ppsR

`gene.b1703`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1703`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ppsR (gene.b1703) is a gene entity. It encodes ppsR (protein.P0A8A4). Encoded protein function: FUNCTION: Bifunctional serine/threonine kinase and phosphorylase involved in the regulation of the phosphoenolpyruvate synthase (PEPS) by catalyzing its phosphorylation/dephosphorylation. {ECO:0000255|HAMAP-Rule:MF_01062, ECO:0000269|PubMed:20044937}. EcoCyc product frame: EG11132-MONOMER. EcoCyc synonyms: ydiA. Genomic coordinates: 1787445-1788278.

## Biological Role

Activated by DNA-binding transcriptional dual regulator Cra (complex.ecocyc.PC00061), pdhR (protein.P0ACL9).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8A4|protein.P0A8A4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[complex.ecocyc.PC00061|complex.ecocyc.PC00061]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0ACL9|protein.P0ACL9]] `RegulonDB|EcoCyc` `C` - regulator=PdhR; target=ppsR; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005682,ECOCYC:EG11132,GeneID:946207`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1787445-1788278:+; feature_type=gene
