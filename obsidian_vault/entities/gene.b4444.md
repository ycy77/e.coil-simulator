---
entity_id: "gene.b4444"
entity_type: "gene"
name: "omrA"
source_database: "NCBI RefSeq"
source_id: "gene-b4444"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4444"
  - "omrA"
---

# omrA

`gene.b4444`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4444`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

omrA (gene.b4444) is a gene entity. EcoCyc product frame: SRAE-RNA. EcoCyc synonyms: psrA12, rygA, PAIR2a, t59, sraE. Genomic coordinates: 2976102-2976189.

## Biological Role

Activated by ompR (protein.P0AA16).

## Enriched Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (12)

- `represses` --> [[gene.b0565|gene.b0565]] `RegulonDB` `S` - regulator=OmrA; target=ompT; function=-
- `represses` --> [[gene.b0584|gene.b0584]] `RegulonDB` `S` - regulator=OmrA; target=fepA; function=-
- `represses` --> [[gene.b1037|gene.b1037]] `RegulonDB` `S` - regulator=OmrA; target=csgG; function=-
- `represses` --> [[gene.b1038|gene.b1038]] `RegulonDB` `S` - regulator=OmrA; target=csgF; function=-
- `represses` --> [[gene.b1039|gene.b1039]] `RegulonDB` `S` - regulator=OmrA; target=csgE; function=-
- `represses` --> [[gene.b1040|gene.b1040]] `RegulonDB` `S` - regulator=OmrA; target=csgD; function=-
- `represses` --> [[gene.b1071|gene.b1071]] `RegulonDB` `S` - regulator=OmrA; target=flgM; function=-
- `represses` --> [[gene.b1341|gene.b1341]] `RegulonDB` `S` - regulator=OmrA; target=dgcM; function=-
- `represses` --> [[gene.b1891|gene.b1891]] `RegulonDB` `S` - regulator=OmrA; target=flhC; function=-
- `represses` --> [[gene.b1892|gene.b1892]] `RegulonDB` `S` - regulator=OmrA; target=flhD; function=-
- `represses` --> [[gene.b2155|gene.b2155]] `RegulonDB` `S` - regulator=OmrA; target=cirA; function=-
- `represses` --> [[gene.b3405|gene.b3405]] `RegulonDB` `S` - regulator=OmrA; target=ompR; function=-

## Incoming Edges (1)

- `activates` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `S` - regulator=OmpR; target=omrA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0047264,ECOCYC:G0-8868,GeneID:2847746`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:2976102-2976189:-; feature_type=gene
