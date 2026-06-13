---
entity_id: "gene.b1956"
entity_type: "gene"
name: "dgcQ"
source_database: "NCBI RefSeq"
source_id: "gene-b1956"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1956"
  - "dgcQ"
---

# dgcQ

`gene.b1956`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1956`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dgcQ (gene.b1956) is a gene entity. It encodes dgcQ (protein.P76330). Encoded protein function: FUNCTION: Catalyzes the synthesis of cyclic-di-GMP (c-di-GMP) via the condensation of 2 GTP molecules (By similarity). Cyclic-di-GMP is a second messenger which controls cell surface-associated traits in bacteria. Involved in the regulation of cellulose production (PubMed:20303158). {ECO:0000250|UniProtKB:P31129, ECO:0000269|PubMed:20303158}. EcoCyc product frame: G7049-MONOMER. EcoCyc synonyms: yedQ. Genomic coordinates: 2026323-2028017. EcoCyc protein note: DgcQ is a probable inner membrane protein with two predicted transmembrane domains and a C-terminal GGDEF domain with diguanylate cyclase activity . The N-terminal CHASE (Cyclases/Histidine kinases Associated Sensory) domain is predicted to be periplasmic . The C terminus is predicted to localize to the cytoplasm . DgcQ is implicated in phage N4 infection . The diguanylate cyclase domain of DgcQ physically interacts with PyrB, the catalytic subunit of ASPCARBTRANS-CPLX (PyrBI), an enzyme involved in de novoUMP biosynthesis. The diguanylate cyclase activity of this domain is activated by UTP and inhibited by CARBAMYUL-L-ASPARTATE, the product of PyrBI . In the commensal E. coli strain 1094, DgcQ is a regulator that constitutively activates cellulose production under all tested environmental conditions...

## Biological Role

Repressed by lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76330|protein.P76330]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006495,ECOCYC:G7049,GeneID:946471`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2026323-2028017:-; feature_type=gene
