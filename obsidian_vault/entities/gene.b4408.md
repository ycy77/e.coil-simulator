---
entity_id: "gene.b4408"
entity_type: "gene"
name: "csrB"
source_database: "NCBI RefSeq"
source_id: "gene-b4408"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4408"
  - "csrB"
---

# csrB

`gene.b4408`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4408`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

csrB (gene.b4408) is a gene entity. EcoCyc product frame: CSRB-RNA. Genomic coordinates: 2924156-2924524.

## Biological Role

Activated by rpoD (protein.P00579), dksA (protein.P0ABS1), uvrY (protein.P0AED5).

## Enriched Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=csrB; function=+
- `activates` <-- [[protein.P0ABS1|protein.P0ABS1]] `RegulonDB` `S` - regulator=DksA; target=csrB; function=+
- `activates` <-- [[protein.P0AED5|protein.P0AED5]] `RegulonDB` `S` - regulator=UvrY; target=csrB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0047213,ECOCYC:G0-8785,GeneID:2847719`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:2924156-2924524:-; feature_type=gene
