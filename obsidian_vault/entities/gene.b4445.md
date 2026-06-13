---
entity_id: "gene.b4445"
entity_type: "gene"
name: "omrB"
source_database: "NCBI RefSeq"
source_id: "gene-b4445"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4445"
  - "omrB"
---

# omrB

`gene.b4445`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4445`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

omrB (gene.b4445) is a gene entity. EcoCyc product frame: RYGB-RNA. EcoCyc synonyms: PAIR2b, t59, rygB. Genomic coordinates: 2976304-2976385.

## Biological Role

Activated by ompR (protein.P0AA16).

## Enriched Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (12)

- `represses` --> [[gene.b0565|gene.b0565]] `RegulonDB` `S` - regulator=OmrB; target=ompT; function=-
- `represses` --> [[gene.b0584|gene.b0584]] `RegulonDB` `S` - regulator=OmrB; target=fepA; function=-
- `represses` --> [[gene.b1037|gene.b1037]] `RegulonDB` `S` - regulator=OmrB; target=csgG; function=-
- `represses` --> [[gene.b1038|gene.b1038]] `RegulonDB` `S` - regulator=OmrB; target=csgF; function=-
- `represses` --> [[gene.b1039|gene.b1039]] `RegulonDB` `S` - regulator=OmrB; target=csgE; function=-
- `represses` --> [[gene.b1040|gene.b1040]] `RegulonDB` `S` - regulator=OmrB; target=csgD; function=-
- `represses` --> [[gene.b1071|gene.b1071]] `RegulonDB` `S` - regulator=OmrB; target=flgM; function=-
- `represses` --> [[gene.b1341|gene.b1341]] `RegulonDB` `S` - regulator=OmrB; target=dgcM; function=-
- `represses` --> [[gene.b1891|gene.b1891]] `RegulonDB` `S` - regulator=OmrB; target=flhC; function=-
- `represses` --> [[gene.b1892|gene.b1892]] `RegulonDB` `S` - regulator=OmrB; target=flhD; function=-
- `represses` --> [[gene.b2155|gene.b2155]] `RegulonDB` `S` - regulator=OmrB; target=cirA; function=-
- `represses` --> [[gene.b3405|gene.b3405]] `RegulonDB` `S` - regulator=OmrB; target=ompR; function=-

## Incoming Edges (1)

- `activates` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `S` - regulator=OmpR; target=omrB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0047265,ECOCYC:G0-8882,GeneID:2847747`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:2976304-2976385:-; feature_type=gene
