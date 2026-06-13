---
entity_id: "gene.b2631"
entity_type: "gene"
name: "rnlB"
source_database: "NCBI RefSeq"
source_id: "gene-b2631"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2631"
  - "rnlB"
---

# rnlB

`gene.b2631`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2631`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rnlB (gene.b2631) is a gene entity. It encodes rnlB (protein.P52130). Encoded protein function: FUNCTION: Antitoxin component of a type II toxin-antitoxin (TA) system. A labile antitoxin (half-life of 2.1 minutes) that inhibits the endonuclease activity of cognate toxin RnlA but not that of non-cognate toxin LsoA. {ECO:0000269|PubMed:20980243, ECO:0000269|PubMed:22403819}. EcoCyc product frame: G7366-MONOMER. EcoCyc synonyms: yfjO. Genomic coordinates: 2766984-2767355. EcoCyc protein note: RnlB is the antitoxin of the RnlA-RnlB toxin-antitoxin system. Overexpression of RnlA in ΔrnlAB cells inhibits cell growth and causes mRNA degradation, while overexpression of RnlB in wild-type cells suppresses the growth defect of the T4 dmd mutant . The RnlB protein is extremely unstable and is stabilized in clpX or lon mutants . RnlB interacts with the DBD domain of RnlA and suppresses its RNase LS activity . Reviews: , Comments:

## Biological Role

Repressed by iscR (protein.P0AGK8), nac (protein.Q47005). Activated by rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P52130|protein.P52130]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=rnlB; function=+
- `represses` <-- [[protein.P0AGK8|protein.P0AGK8]] `RegulonDB` `S` - regulator=IscR; target=rnlB; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=rnlB; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0008665,ECOCYC:G7366,GeneID:947113`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2766984-2767355:+; feature_type=gene
