---
entity_id: "gene.b4438"
entity_type: "gene"
name: "cyaR"
source_database: "NCBI RefSeq"
source_id: "gene-b4438"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4438"
  - "cyaR"
---

# cyaR

`gene.b4438`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4438`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cyaR (gene.b4438) is a gene entity. EcoCyc product frame: RYEE-RNA. EcoCyc synonyms: ryeE. Genomic coordinates: 2167114-2167200.

## Biological Role

Repressed by cpxR (protein.P0AE88). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8), rpoE (protein.P0AGB6), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (6)

- `represses` --> [[gene.b1740|gene.b1740]] `RegulonDB` `S` - regulator=CyaR; target=nadE; function=-
- `represses` --> [[gene.b1824|gene.b1824]] `RegulonDB` `S` - regulator=CyaR; target=yobF; function=-
- `represses` --> [[gene.b2666|gene.b2666]] `RegulonDB` `S` - regulator=CyaR; target=yqaE; function=-
- `represses` --> [[gene.b2687|gene.b2687]] `RegulonDB` `S` - regulator=CyaR; target=luxS; function=-
- `represses` --> [[gene.b2741|gene.b2741]] `RegulonDB` `S` - regulator=CyaR; target=rpoS; function=-
- `represses` --> [[gene.b3511|gene.b3511]] `RegulonDB` `S` - regulator=CyaR; target=hdeD; function=-

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=cyaR; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=cyaR; function=+
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `C` - sigma=sigma24; target=cyaR; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `C` - sigma=sigma38; target=cyaR; function=+
- `represses` <-- [[protein.P0AE88|protein.P0AE88]] `RegulonDB` `S` - regulator=CpxR; target=cyaR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0047258,ECOCYC:G0-8878,GeneID:2847769`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:2167114-2167200:+; feature_type=gene
