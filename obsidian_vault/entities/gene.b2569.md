---
entity_id: "gene.b2569"
entity_type: "gene"
name: "lepA"
source_database: "NCBI RefSeq"
source_id: "gene-b2569"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2569"
  - "lepA"
---

# lepA

`gene.b2569`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2569`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lepA (gene.b2569) is a gene entity. It encodes lepA (protein.P60785). Encoded protein function: FUNCTION: Required for accurate and efficient protein synthesis under certain stress conditions. May act as a fidelity factor of the translation reaction, by catalyzing a one-codon backward translocation of tRNAs on improperly translocated ribosomes. Back-translocation proceeds from a post-translocation (POST) complex to a pre-translocation (PRE) complex, thus giving elongation factor G a second chance to translocate the tRNAs correctly. Binds to ribosomes in a GTP-dependent manner. {ECO:0000255|HAMAP-Rule:MF_00071, ECO:0000269|PubMed:17110332, ECO:0000269|PubMed:20045415}. EcoCyc product frame: EG10529-MONOMER. Genomic coordinates: 2705325-2707124. EcoCyc protein note: EF4 (LepA) is a highly conserved protein whose function in translation is still controversial. The most recent results indicate that LepA functions in 30S ribosomal subunit biogenesis . Various experimental results that suggested functions in translation initiation or elongation are summarized below. EF4 competes with EF-G for binding to the ribosome and forms a complex that is an intermediate between the PRE and POST complexes, thus sequestering a catalytically active ribosome...

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P60785|protein.P60785]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=lepA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0008452,ECOCYC:EG10529,GeneID:947051`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2705325-2707124:-; feature_type=gene
