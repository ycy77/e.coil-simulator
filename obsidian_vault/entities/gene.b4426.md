---
entity_id: "gene.b4426"
entity_type: "gene"
name: "mcaS"
source_database: "NCBI RefSeq"
source_id: "gene-b4426"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4426"
  - "mcaS"
---

# mcaS

`gene.b4426`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4426`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mcaS (gene.b4426) is a gene entity. EcoCyc product frame: IS061-RNA. EcoCyc synonyms: IS061, isrA. Genomic coordinates: 1405658-1405751.

## Biological Role

Repressed by ArgR-L-arginine DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-228), argR (protein.P0A6D0). Activated by crp (protein.P0ACJ8).

## Enriched Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (6)

- `activates` --> [[gene.b1891|gene.b1891]] `RegulonDB` `S` - regulator=McaS; target=flhC; function=+
- `activates` --> [[gene.b1892|gene.b1892]] `RegulonDB` `S` - regulator=McaS; target=flhD; function=+
- `represses` --> [[gene.b1037|gene.b1037]] `RegulonDB` `S` - regulator=McaS; target=csgG; function=-
- `represses` --> [[gene.b1038|gene.b1038]] `RegulonDB` `S` - regulator=McaS; target=csgF; function=-
- `represses` --> [[gene.b1039|gene.b1039]] `RegulonDB` `S` - regulator=McaS; target=csgE; function=-
- `represses` --> [[gene.b1040|gene.b1040]] `RegulonDB` `S` - regulator=McaS; target=csgD; function=-

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=mcaS; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-228|complex.ecocyc.CPLX0-228]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `S` - regulator=ArgR; target=mcaS; function=-

## External IDs

- `Dbxref:ASAP:ABE-0047247,ECOCYC:G0-8899,GeneID:2847751`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:1405658-1405751:-; feature_type=gene
