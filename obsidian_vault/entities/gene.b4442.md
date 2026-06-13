---
entity_id: "gene.b4442"
entity_type: "gene"
name: "micA"
source_database: "NCBI RefSeq"
source_id: "gene-b4442"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4442"
  - "micA"
---

# micA

`gene.b4442`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4442`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

micA (gene.b4442) is a gene entity. EcoCyc product frame: SRAD-RNA. EcoCyc synonyms: sraD, psrA10. Genomic coordinates: 2814802-2814874.

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (6)

- `represses` --> [[gene.b0411|gene.b0411]] `RegulonDB` `S` - regulator=MicA; target=tsx; function=-
- `represses` --> [[gene.b0814|gene.b0814]] `RegulonDB` `S` - regulator=MicA; target=ompX; function=-
- `represses` --> [[gene.b0957|gene.b0957]] `RegulonDB` `S` - regulator=MicA; target=ompA; function=-
- `represses` --> [[gene.b1129|gene.b1129]] `RegulonDB` `S` - regulator=MicA; target=phoQ; function=-
- `represses` --> [[gene.b1130|gene.b1130]] `RegulonDB` `S` - regulator=MicA; target=phoP; function=-
- `represses` --> [[gene.b4736|gene.b4736]] `RegulonDB` `S` - regulator=MicA; target=yliM; function=-

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=micA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0047262,ECOCYC:G0-8866,GeneID:2847697`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:2814802-2814874:+; feature_type=gene
