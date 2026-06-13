---
entity_id: "gene.b4718"
entity_type: "gene"
name: "gadF"
source_database: "NCBI RefSeq"
source_id: "gene-b4718"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4718"
  - "gadF"
---

# gadF

`gene.b4718`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4718`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gadF (gene.b4718) is a gene entity. EcoCyc product frame: RNA0-392. Genomic coordinates: 3658992-3659082.

## Biological Role

Repressed by hns (protein.P0ACF8), crp (protein.P0ACJ8), fliZ (protein.P52627). Activated by rpoD (protein.P00579), arcA (protein.P0A9Q1), evgA (protein.P0ACZ4), rpoS (protein.P13445), gadX (protein.P37639), ydeO (protein.P76135).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=gadF; function=+
- `activates` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=gadF; function=+
- `activates` <-- [[protein.P0ACZ4|protein.P0ACZ4]] `RegulonDB` `S` - regulator=EvgA; target=gadF; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=gadF; function=+
- `activates` <-- [[protein.P37639|protein.P37639]] `RegulonDB` `S` - regulator=GadX; target=gadF; function=+
- `activates` <-- [[protein.P76135|protein.P76135]] `RegulonDB` `S` - regulator=YdeO; target=gadF; function=+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=gadF; function=-
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=gadF; function=-
- `represses` <-- [[protein.P52627|protein.P52627]] `RegulonDB` `C` - regulator=FliZ; target=gadF; function=-

## External IDs

- `Dbxref:ECOCYC:G0-16680,GeneID:38094974`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:3658992-3659082:+; feature_type=gene
