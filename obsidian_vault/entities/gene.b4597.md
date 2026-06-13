---
entity_id: "gene.b4597"
entity_type: "gene"
name: "rydC"
source_database: "NCBI RefSeq"
source_id: "gene-b4597"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4597"
  - "rydC"
---

# rydC

`gene.b4597`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4597`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rydC (gene.b4597) is a gene entity. EcoCyc product frame: RNA0-328. Genomic coordinates: 1491442-1491506.

## Biological Role

Repressed by yieP (protein.P31475). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (8)

- `activates` --> [[gene.b1260|gene.b1260]] `RegulonDB` `S` - regulator=RydC; target=trpA; function=+
- `activates` --> [[gene.b1261|gene.b1261]] `RegulonDB` `S` - regulator=RydC; target=trpB; function=+
- `activates` --> [[gene.b1262|gene.b1262]] `RegulonDB` `S` - regulator=RydC; target=trpC; function=+
- `activates` --> [[gene.b1263|gene.b1263]] `RegulonDB` `S` - regulator=RydC; target=trpD; function=+
- `activates` --> [[gene.b1264|gene.b1264]] `RegulonDB` `S` - regulator=RydC; target=trpE; function=+
- `activates` --> [[gene.b1265|gene.b1265]] `RegulonDB` `S` - regulator=RydC; target=trpL; function=+
- `activates` --> [[gene.b1661|gene.b1661]] `RegulonDB` `S` - regulator=RydC; target=cfa; function=+
- `represses` --> [[gene.b2599|gene.b2599]] `RegulonDB` `S` - regulator=RydC; target=pheA; function=-

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rydC; function=+
- `represses` <-- [[protein.P31475|protein.P31475]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ECOCYC:G0-10592,GeneID:5061508`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:1491442-1491506:-; feature_type=gene
