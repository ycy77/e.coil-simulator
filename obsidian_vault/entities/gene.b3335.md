---
entity_id: "gene.b3335"
entity_type: "gene"
name: "gspO"
source_database: "NCBI RefSeq"
source_id: "gene-b3335"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3335"
  - "gspO"
---

# gspO

`gene.b3335`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3335`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gspO (gene.b3335) is a gene entity. It encodes gspO (protein.P25960). Encoded protein function: FUNCTION: Plays a role in type II pseudopili formation by proteolytically removing the leader sequence from substrate proteins and subsequently monomethylating the alpha-amino group of the newly exposed N-terminal phenylalanine. Substrates include proteins required for biogenesis of the type II general secretory apparatus. {ECO:0000305|PubMed:8655552}. EcoCyc product frame: EG11359-MONOMER. EcoCyc synonyms: hofD, hopD, hopO, yheC. Genomic coordinates: 3465543-3466220. EcoCyc protein note: In Escherichia coli, gspO is a member of an operon of genes (gspC-O) which are not normally expressed but are homologous to those encoding the secreton, or type II secretion machinery in Klebsiella oxytoca and Aeromonase hydrophila, among others . Although Escherichia coli K-12 does not secrete endogenous proteins, the gsp genes of E. coli are orthologs of those in other secretons , including those of the pullulanase (pul) secretion pathway of Klebsiella oxytoca. GspO encodes a protein similar to type IV prepilin peptidases, like pulO gene in K. oxytoca...

## Biological Role

Repressed by fur (protein.P0A9A9), hns (protein.P0ACF8). Activated by rpoD (protein.P00579), slyA (protein.P0A8W2), nac (protein.Q47005).

## Enriched Pathways

- `eco03070` Bacterial secretion system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P25960|protein.P25960]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=gspO; function=+
- `activates` <-- [[protein.P0A8W2|protein.P0A8W2]] `RegulonDB` `S` - regulator=SlyA; target=gspO; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=gspO; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=gspO; function=-
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=gspO; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010901,ECOCYC:EG11359,GeneID:947840`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3465543-3466220:+; feature_type=gene
