---
entity_id: "gene.b3864"
entity_type: "gene"
name: "spf"
source_database: "NCBI RefSeq"
source_id: "gene-b3864"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3864"
  - "spf"
---

# spf

`gene.b3864`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3864`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

spf (gene.b3864) is a gene entity. EcoCyc product frame: SPF-RNA. Genomic coordinates: 4049899-4050009.

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (9)

- `represses` --> [[gene.b1302|gene.b1302]] `RegulonDB` `S` - regulator=Spf; target=puuE; function=-
- `represses` --> [[gene.b1761|gene.b1761]] `RegulonDB` `S` - regulator=Spf; target=gdhA; function=-
- `represses` --> [[gene.b1901|gene.b1901]] `RegulonDB` `S` - regulator=Spf; target=araF; function=-
- `represses` --> [[gene.b2702|gene.b2702]] `RegulonDB` `S` - regulator=Spf; target=srlA; function=-
- `represses` --> [[gene.b2715|gene.b2715]] `RegulonDB` `S` - regulator=Spf; target=ascF; function=-
- `represses` --> [[gene.b2801|gene.b2801]] `RegulonDB` `S` - regulator=Spf; target=fucP; function=-
- `represses` --> [[gene.b3224|gene.b3224]] `RegulonDB` `S` - regulator=Spf; target=nanT; function=-
- `represses` --> [[gene.b3962|gene.b3962]] `RegulonDB` `S` - regulator=Spf; target=sthA; function=-
- `represses` --> [[gene.b4311|gene.b4311]] `RegulonDB` `S` - regulator=Spf; target=nanC; function=-

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=spf; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012621,ECOCYC:EG30098,GeneID:948354`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:4049899-4050009:+; feature_type=gene
