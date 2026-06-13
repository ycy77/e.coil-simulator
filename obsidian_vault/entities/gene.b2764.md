---
entity_id: "gene.b2764"
entity_type: "gene"
name: "cysJ"
source_database: "NCBI RefSeq"
source_id: "gene-b2764"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2764"
  - "cysJ"
---

# cysJ

`gene.b2764`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2764`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cysJ (gene.b2764) is a gene entity. It encodes cysJ (protein.P38038). Encoded protein function: FUNCTION: Component of the sulfite reductase complex that catalyzes the 6-electron reduction of sulfite to sulfide. This is one of several activities required for the biosynthesis of L-cysteine from sulfate. The flavoprotein component catalyzes the electron flow from NADPH -> FAD -> FMN to the hemoprotein component. {ECO:0000255|HAMAP-Rule:MF_01541}.; FUNCTION: In addition to its role in the sulfite reductase complex, it functions as a specific partner of the YcbX molybdoenzyme in the detoxification of N-hydroxylated base analogs (PubMed:20118259). CysJ mediates the N-reductive reaction through its NADPH:flavin oxidoreductase activity (PubMed:20118259). It may provide reducing equivalents to its partner YcbX, which ultimately performs the reduction of 6-N-hydroxylaminopurine (HAP) to non-toxic adenine (PubMed:20118259). The role of CysJ in base analog detoxification is independent of CysI and sulfite reductase (PubMed:20118259). {ECO:0000269|PubMed:20118259}. EcoCyc product frame: ALPHACOMP-MONOMER. Genomic coordinates: 2890099-2891898.

## Biological Role

Repressed by yeiE (protein.P0ACR4), nac (protein.Q47005). Activated by rpoD (protein.P00579), yafC (protein.P30864).

## Enriched Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01320` Sulfur cycle (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P38038|protein.P38038]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=cysJ; function=+
- `activates` <-- [[protein.P30864|protein.P30864]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACR4|protein.P0ACR4]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=cysJ; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0009063,ECOCYC:EG10191,GeneID:947239`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2890099-2891898:-; feature_type=gene
