---
entity_id: "gene.b1857"
entity_type: "gene"
name: "znuA"
source_database: "NCBI RefSeq"
source_id: "gene-b1857"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1857"
  - "znuA"
---

# znuA

`gene.b1857`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1857`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

znuA (gene.b1857) is a gene entity. It encodes znuA (protein.P39172). Encoded protein function: FUNCTION: Part of the ATP-binding cassette (ABC) transport system ZnuABC involved in zinc import (PubMed:9680209). Binds zinc with high affinity and specificity and delivers it to the membrane permease for translocation into the cytoplasm (PubMed:18027003). {ECO:0000269|PubMed:18027003, ECO:0000269|PubMed:9680209}. EcoCyc product frame: ZNUA-MONOMER. EcoCyc synonyms: yzzP, yebL. Genomic coordinates: 1941651-1942583. EcoCyc protein note: ZnuA is the periplasmic binding protein of an ATP-dependent Zn2+ uptake system. High resolution crystal structures of ZnuA with bound Zn2+ consist of two structually similar domains (the N and C domains) connected by a long α-helix; a single Zn2+ binds at the interface between the two domains . Purified ZnuA interacts with Co2+, Ni2+, Cd 2+, Cu2+ and Cu+; purified ZnuA binds Zn2+ with high affinity (Kd znuA belongs to a network of genes which facilitate stress-induced mutagenesis (SIM) in E. coli K-12 . znu: Zn2+ uptake

## Biological Role

Repressed by zur (protein.P0AC51), nac (protein.Q47005). Activated by DNA-binding transcriptional dual regulator OmpR-phosphorylated (complex.ecocyc.PHOSPHO-OMPR), ompR (protein.P0AA16), oxyR (protein.P0ACQ4).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39172|protein.P39172]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[complex.ecocyc.PHOSPHO-OMPR|complex.ecocyc.PHOSPHO-OMPR]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `S` - regulator=OmpR; target=znuA; function=+
- `activates` <-- [[protein.P0ACQ4|protein.P0ACQ4]] `RegulonDB` `S` - regulator=OxyR; target=znuA; function=+
- `represses` <-- [[protein.P0AC51|protein.P0AC51]] `RegulonDB` `S` - regulator=Zur; target=znuA; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=znuA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006191,ECOCYC:G7017,GeneID:946375`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1941651-1942583:-; feature_type=gene
