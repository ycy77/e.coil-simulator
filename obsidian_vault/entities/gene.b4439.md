---
entity_id: "gene.b4439"
entity_type: "gene"
name: "micF"
source_database: "NCBI RefSeq"
source_id: "gene-b4439"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4439"
  - "micF"
---

# micF

`gene.b4439`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4439`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

micF (gene.b4439) is a gene entity. EcoCyc product frame: MICF-RNA. EcoCyc synonyms: stc. Genomic coordinates: 2313084-2313176.

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by rpoD (protein.P00579), soxS (protein.P0A9E2), arcA (protein.P0A9Q1), ompR (protein.P0AA16), marA (protein.P0ACH5), rob (protein.P0ACI0), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `represses` --> [[gene.b0889|gene.b0889]] `RegulonDB` `S` - regulator=MicF; target=lrp; function=-

## Incoming Edges (8)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=micF; function=+
- `activates` <-- [[protein.P0A9E2|protein.P0A9E2]] `RegulonDB` `C` - regulator=SoxS; target=micF; function=+
- `activates` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=micF; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `C` - regulator=OmpR; target=micF; function=+
- `activates` <-- [[protein.P0ACH5|protein.P0ACH5]] `RegulonDB` `S` - regulator=MarA; target=micF; function=+
- `activates` <-- [[protein.P0ACI0|protein.P0ACI0]] `RegulonDB` `S` - regulator=Rob; target=micF; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=micF; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `S` - regulator=Lrp; target=micF; function=-

## External IDs

- `Dbxref:ASAP:ABE-0047259,ECOCYC:EG30063,GeneID:2847742`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:2313084-2313176:+; feature_type=gene
