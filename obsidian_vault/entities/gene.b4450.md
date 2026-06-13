---
entity_id: "gene.b4450"
entity_type: "gene"
name: "arcZ"
source_database: "NCBI RefSeq"
source_id: "gene-b4450"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4450"
  - "arcZ"
---

# arcZ

`gene.b4450`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4450`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

arcZ (gene.b4450) is a gene entity. EcoCyc product frame: SRAH-RNA. EcoCyc synonyms: psrA16, sraH, ryhA. Genomic coordinates: 3350577-3350697.

## Enriched Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (5)

- `activates` --> [[gene.b2741|gene.b2741]] `RegulonDB` `S` - regulator=ArcZ; target=rpoS; function=+
- `represses` --> [[gene.b1891|gene.b1891]] `RegulonDB` `S` - regulator=ArcZ; target=flhC; function=-
- `represses` --> [[gene.b1892|gene.b1892]] `RegulonDB` `S` - regulator=ArcZ; target=flhD; function=-
- `represses` --> [[gene.b2733|gene.b2733]] `RegulonDB` `S` - regulator=ArcZ; target=mutS; function=-
- `represses` --> [[gene.b3546|gene.b3546]] `RegulonDB` `S` - regulator=ArcZ; target=eptB; function=-

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0047270,ECOCYC:G0-8871,GeneID:2847690`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:3350577-3350697:+; feature_type=gene
