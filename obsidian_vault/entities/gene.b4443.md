---
entity_id: "gene.b4443"
entity_type: "gene"
name: "gcvB"
source_database: "NCBI RefSeq"
source_id: "gene-b4443"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4443"
  - "gcvB"
---

# gcvB

`gene.b4443`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4443`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gcvB (gene.b4443) is a gene entity. EcoCyc product frame: GCVB-RNA. EcoCyc synonyms: psrA11, IS145. Genomic coordinates: 2942696-2942901.

## Biological Role

Activated by rpoD (protein.P00579), gcvA (protein.P0A9F6), arcA (protein.P0A9Q1).

## Enriched Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (7)

- `represses` --> [[gene.b0168|gene.b0168]] `RegulonDB` `S` - regulator=GcvB; target=map; function=-
- `represses` --> [[gene.b0598|gene.b0598]] `RegulonDB` `S` - regulator=GcvB; target=cstA; function=-
- `represses` --> [[gene.b0889|gene.b0889]] `RegulonDB` `S` - regulator=GcvB; target=lrp; function=-
- `represses` --> [[gene.b1129|gene.b1129]] `RegulonDB` `S` - regulator=GcvB; target=phoQ; function=-
- `represses` --> [[gene.b1130|gene.b1130]] `RegulonDB` `S` - regulator=GcvB; target=phoP; function=-
- `represses` --> [[gene.b1534|gene.b1534]] `RegulonDB` `S` - regulator=GcvB; target=ydeE; function=-
- `represses` --> [[gene.b3771|gene.b3771]] `RegulonDB` `S` - regulator=GcvB; target=ilvD; function=-

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=gcvB; function=+
- `activates` <-- [[protein.P0A9F6|protein.P0A9F6]] `RegulonDB` `C` - regulator=GcvA; target=gcvB; function=+
- `activates` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=gcvB; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0047263,ECOCYC:G0-8867,GeneID:2847720`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:2942696-2942901:+; feature_type=gene
