---
entity_id: "gene.b1025"
entity_type: "gene"
name: "dgcT"
source_database: "NCBI RefSeq"
source_id: "gene-b1025"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1025"
  - "dgcT"
---

# dgcT

`gene.b1025`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1025`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dgcT (gene.b1025) is a gene entity. It encodes dgcT (protein.P75908). Encoded protein function: FUNCTION: Probably catalyzes the synthesis of cyclic-di-GMP (c-di-GMP) via the condensation of 2 GTP molecules. Overexpression leads to a strong repression of swimming; swimming returns to normal when residues 359-360 are both mutated to Ala. Overexpression also leads to a 20-fold increase in c-di-GMP levels in vivo. Cyclic-di-GMP is a second messenger which controls cell surface-associated traits in bacteria. {ECO:0000269|PubMed:18713317}. EcoCyc product frame: G6532-MONOMER. EcoCyc synonyms: ycdT. Genomic coordinates: 1092876-1094234. EcoCyc protein note: DgcT is a diguanylate cyclase that regulates motility; the effect on motility is probably mediated by the second messenger molecule c-di-GMP . DgcT has an N-terminal MASE4 (Membrane-Associated SEnsor) domain, which includes eight transmembrane segments . The MASE4 domain is followed by the diguanylate cyclase (GGDEF) domain . Overexpression of DgcT represses swimming behavior . Expression of DgcT is repressed by CsrA, which interacts directly with the 5' leader sequence of the dgcT mRNA and modulates the stability of the message . DgcT: diguanylate cyclase T . Related review:

## Biological Role

Repressed by hns (protein.P0ACF8), nac (protein.Q47005). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75908|protein.P75908]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=dgcT; function=+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=dgcT; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0003472,ECOCYC:G6532,GeneID:945593`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1092876-1094234:+; feature_type=gene
