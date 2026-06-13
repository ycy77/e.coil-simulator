---
entity_id: "gene.b4417"
entity_type: "gene"
name: "rybB"
source_database: "NCBI RefSeq"
source_id: "gene-b4417"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4417"
  - "rybB"
---

# rybB

`gene.b4417`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4417`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rybB (gene.b4417) is a gene entity. EcoCyc product frame: RYBB-RNA. EcoCyc synonyms: p25. Genomic coordinates: 887979-888057.

## Biological Role

Activated by dksA (protein.P0ABS1), rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (9)

- `represses` --> [[gene.b0721|gene.b0721]] `RegulonDB` `S` - regulator=RybB; target=sdhC; function=-
- `represses` --> [[gene.b0805|gene.b0805]] `RegulonDB` `S` - regulator=RybB; target=fiu; function=-
- `represses` --> [[gene.b0929|gene.b0929]] `RegulonDB` `S` - regulator=RybB; target=ompF; function=-
- `represses` --> [[gene.b1037|gene.b1037]] `RegulonDB` `S` - regulator=RybB; target=csgG; function=-
- `represses` --> [[gene.b1038|gene.b1038]] `RegulonDB` `S` - regulator=RybB; target=csgF; function=-
- `represses` --> [[gene.b1039|gene.b1039]] `RegulonDB` `S` - regulator=RybB; target=csgE; function=-
- `represses` --> [[gene.b1040|gene.b1040]] `RegulonDB` `S` - regulator=RybB; target=csgD; function=-
- `represses` --> [[gene.b2594|gene.b2594]] `RegulonDB` `S` - regulator=RybB; target=rluD; function=-
- `represses` --> [[gene.b3751|gene.b3751]] `RegulonDB` `S` - regulator=RybB; target=rbsB; function=-

## Incoming Edges (2)

- `activates` <-- [[protein.P0ABS1|protein.P0ABS1]] `RegulonDB` `S` - regulator=DksA; target=rybB; function=+
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=rybB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0047241,ECOCYC:G0-8880,GeneID:2847774`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:887979-888057:-; feature_type=gene
