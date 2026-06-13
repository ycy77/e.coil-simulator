---
entity_id: "gene.b0224"
entity_type: "gene"
name: "dpaA"
source_database: "NCBI RefSeq"
source_id: "gene-b0224"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0224"
  - "dpaA"
---

# dpaA

`gene.b0224`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0224`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dpaA (gene.b0224) is a gene entity. It encodes dpaA (protein.P0AA99). Encoded protein function: FUNCTION: Hydrolase that plays a role in the regulation of peptidoglycan-outer membrane linkages (PubMed:33941679, PubMed:33947763). It has two distinctive enzymatic functions, an L,D-endopeptidase activity and a carboxypeptidase activity (PubMed:33941679, PubMed:33947763). Acts as a murein L,D-endopeptidase that catalyzes the cleavage of the cross-link between the outer membrane-anchored Braun's lipoprotein (Lpp) and peptidoglycan, detaching Lpp from the peptidoglycan layer (PubMed:33941679, PubMed:33947763, PubMed:37830798). It also exhibits glycine-specific carboxypeptidase activity on muropeptides containing a terminal glycine residue (PubMed:33941679, PubMed:33947763). DpaA hydrolyzes the amide bond between the L-center of meso-diaminopimelate in peptidoglycan stem peptides and the C-terminal L-lysine of Lpp, and between the L-center of meso-diaminopimelate and a terminal glycine residue in tetrapeptides (PubMed:33941679, PubMed:33947763). The detachment of Lpp from peptidoglycan is beneficial for the cell under certain stress conditions, suggesting that DpaA may help the cell to cope with these stress conditions (PubMed:33947763). DpaA may also cleave Lpp bound to the inner membrane (PubMed:33941679)...

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AA99|protein.P0AA99]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=dpaA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000757,ECOCYC:G6108,GeneID:944910`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:245065-245805:-; feature_type=gene
