---
entity_id: "gene.b0995"
entity_type: "gene"
name: "torR"
source_database: "NCBI RefSeq"
source_id: "gene-b0995"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0995"
  - "torR"
---

# torR

`gene.b0995`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0995`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

torR (gene.b0995) is a gene entity. It encodes torR (protein.P38684). Encoded protein function: FUNCTION: Member of the two-component regulatory system TorS/TorR involved in the anaerobic utilization of trimethylamine-N-oxide (TMAO). Phosphorylated TorR activates the transcription of the torCAD operon by binding to four decameric boxes located in the torCAD promoter. Box1, 2 and 4 contain the DNA sequence 5'-CTGTTCATAT-3' and box3 contains the DNA sequence 5'-CCGTTCATCC-3'. Phosphorylated as well as unphosphorylated TorR negatively regulates its own expression by binding to box1 and 2. EcoCyc product frame: TORR-MONOMER. Genomic coordinates: 1057262-1057954. EcoCyc protein note: A knockout mutant of this gene was sensitive to boric acid exposure compared to most other gene knockouts; a complementation assay restored its intrinsic boric acid resistance .

## Biological Role

Repressed by torR (protein.P38684). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P38684|protein.P38684]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=torR; function=+
- `represses` <-- [[protein.P38684|protein.P38684]] `RegulonDB` `C` - regulator=TorR; target=torR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003362,ECOCYC:EG12615,GeneID:946182`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1057262-1057954:-; feature_type=gene
