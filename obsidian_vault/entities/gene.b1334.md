---
entity_id: "gene.b1334"
entity_type: "gene"
name: "fnr"
source_database: "NCBI RefSeq"
source_id: "gene-b1334"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1334"
  - "fnr"
---

# fnr

`gene.b1334`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1334`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fnr (gene.b1334) is a gene entity. It encodes fnr (protein.P0A9E5). Encoded protein function: FUNCTION: Global transcription factor that controls the expression of over 100 target genes in response to anoxia. It facilitates the adaptation to anaerobic growth conditions by regulating the expression of gene products that are involved in anaerobic energy metabolism. When the terminal electron acceptor, O(2), is no longer available, it represses the synthesis of enzymes involved in aerobic respiration and increases the synthesis of enzymes required for anaerobic respiration. EcoCyc product frame: PD00197. EcoCyc synonyms: nirA, nirR, ossA, oxrA. Genomic coordinates: 1398774-1399526.

## Biological Role

Repressed by fnr (protein.P0A9E5). Activated by DNA-binding transcriptional dual regulator FNR (complex.ecocyc.CPLX0-7797), fnr (protein.P0A9E5).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9E5|protein.P0A9E5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[complex.ecocyc.CPLX0-7797|complex.ecocyc.CPLX0-7797]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=fnr; function=-+
- `represses` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=fnr; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0004475,ECOCYC:EG10325,GeneID:945908`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1398774-1399526:-; feature_type=gene
