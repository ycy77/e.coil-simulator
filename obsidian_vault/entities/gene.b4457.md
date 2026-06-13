---
entity_id: "gene.b4457"
entity_type: "gene"
name: "csrC"
source_database: "NCBI RefSeq"
source_id: "gene-b4457"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4457"
  - "csrC"
---

# csrC

`gene.b4457`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4457`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

csrC (gene.b4457) is a gene entity. EcoCyc product frame: CSRC-RNA. EcoCyc synonyms: sraK, psrA21, ryiB, tpk2, IS198. Genomic coordinates: 4051036-4051281.

## Biological Role

Repressed by crp (protein.P0ACJ8). Activated by dksA (protein.P0ABS1), uvrY (protein.P0AED5).

## Enriched Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `activates` <-- [[protein.P0ABS1|protein.P0ABS1]] `RegulonDB` `S` - regulator=DksA; target=csrC; function=+
- `activates` <-- [[protein.P0AED5|protein.P0AED5]] `RegulonDB` `S` - regulator=UvrY; target=csrC; function=+
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=csrC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0047275,ECOCYC:G0-8874,GeneID:2847776`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:4051036-4051281:+; feature_type=gene
