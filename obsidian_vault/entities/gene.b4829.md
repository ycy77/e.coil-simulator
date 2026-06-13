---
entity_id: "gene.b4829"
entity_type: "gene"
name: "uhpU"
source_database: "NCBI RefSeq"
source_id: "gene-b4829"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4829"
  - "uhpU"
---

# uhpU

`gene.b4829`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4829`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

uhpU (gene.b4829) is a gene entity. EcoCyc product frame: RNA0-422. Genomic coordinates: 3845730-3845995.

## Biological Role

Activated by crp (protein.P0ACJ8), uvrY (protein.P0AED5), uhpA (protein.P0AGA6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `represses` --> [[gene.b2289|gene.b2289]] `RegulonDB` `S` - regulator=UhpU; target=lrhA; function=-

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=uhpU; function=+
- `activates` <-- [[protein.P0AED5|protein.P0AED5]] `RegulonDB` `S` - regulator=UvrY; target=uhpU; function=+
- `activates` <-- [[protein.P0AGA6|protein.P0AGA6]] `RegulonDB` `C` - regulator=UhpA; target=uhpU; function=+

## External IDs

- `Dbxref:ECOCYC:G0-17104,GeneID:71004574`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:3845730-3845995:-; feature_type=gene
