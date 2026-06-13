---
entity_id: "gene.b4827"
entity_type: "gene"
name: "fliX"
source_database: "NCBI RefSeq"
source_id: "gene-b4827"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4827"
  - "fliX"
---

# fliX

`gene.b4827`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4827`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fliX (gene.b4827) is a gene entity. EcoCyc product frame: RNA0-420. Genomic coordinates: 2001912-2002106.

## Biological Role

Repressed by ecpR (protein.P71301). Activated by fliA (protein.P0AEM6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (11)

- `represses` --> [[gene.b3311|gene.b3311]] `RegulonDB` `S` - regulator=FliX; target=rpsQ; function=-
- `represses` --> [[gene.b3312|gene.b3312]] `RegulonDB` `S` - regulator=FliX; target=rpmC; function=-
- `represses` --> [[gene.b3313|gene.b3313]] `RegulonDB` `S` - regulator=FliX; target=rplP; function=-
- `represses` --> [[gene.b3314|gene.b3314]] `RegulonDB` `S` - regulator=FliX; target=rpsC; function=-
- `represses` --> [[gene.b3315|gene.b3315]] `RegulonDB` `S` - regulator=FliX; target=rplV; function=-
- `represses` --> [[gene.b3316|gene.b3316]] `RegulonDB` `S` - regulator=FliX; target=rpsS; function=-
- `represses` --> [[gene.b3317|gene.b3317]] `RegulonDB` `S` - regulator=FliX; target=rplB; function=-
- `represses` --> [[gene.b3318|gene.b3318]] `RegulonDB` `S` - regulator=FliX; target=rplW; function=-
- `represses` --> [[gene.b3319|gene.b3319]] `RegulonDB` `S` - regulator=FliX; target=rplD; function=-
- `represses` --> [[gene.b3320|gene.b3320]] `RegulonDB` `S` - regulator=FliX; target=rplC; function=-
- `represses` --> [[gene.b3321|gene.b3321]] `RegulonDB` `S` - regulator=FliX; target=rpsJ; function=-

## Incoming Edges (2)

- `activates` <-- [[protein.P0AEM6|protein.P0AEM6]] `RegulonDB` `S` - sigma=sigma28; target=fliX; function=+
- `represses` <-- [[protein.P71301|protein.P71301]] `RegulonDB` `S` - regulator=MatA; target=fliX; function=-

## External IDs

- `Dbxref:ECOCYC:G0-17102,GeneID:71004566`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:2001912-2002106:-; feature_type=gene
