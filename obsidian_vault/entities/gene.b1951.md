---
entity_id: "gene.b1951"
entity_type: "gene"
name: "rcsA"
source_database: "NCBI RefSeq"
source_id: "gene-b1951"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1951"
  - "rcsA"
---

# rcsA

`gene.b1951`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1951`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rcsA (gene.b1951) is a gene entity. It encodes rcsA (protein.P0DMC9). Encoded protein function: FUNCTION: Component of the Rcs signaling system, which controls transcription of numerous genes. Binds, with RcsB, to the RcsAB box to regulate expression of genes involved in colanic acid capsule synthesis. {ECO:0000255|HAMAP-Rule:MF_00982, ECO:0000269|PubMed:10702265, ECO:0000269|PubMed:1999391}. EcoCyc product frame: PD02233. EcoCyc synonyms: cpsR. Genomic coordinates: 2023968-2024591. EcoCyc protein note: The binding site length of rcsA comes from a single reference . RcsA was proteolyzed by ATP-stimulated HslVU protease in vivo and in vitro at 41°C, and this affected the activation of expression of a cpsB::lacZ gene fusion. This effect on cpsB::lacZ fusion gene expression was similar to that produced by Lon protease under the same temperature conditions . The amount of RcsA protein is limited both by its rapid degradation by Lon, an ATP-dependent protease, and by its low level of synthesis. RcsA is degraded in a Lon-dependent fashion. The rcsA transcription level is decreased in rpoB mutants . RcsA belongs to the LuxR/UhpA protein family. The rcsA gene is upregulated in response to ampicillin treatment .

## Biological Role

Repressed by nac (protein.Q47005). Activated by gadE (protein.P63204), ydaT (protein.P76064).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02024` Quorum sensing (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0DMC9|protein.P0DMC9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P63204|protein.P63204]] `RegulonDB` `S` - regulator=GadE; target=rcsA; function=+
- `activates` <-- [[protein.P76064|protein.P76064]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=rcsA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006482,ECOCYC:EG10820,GeneID:946467`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2023968-2024591:+; feature_type=gene
