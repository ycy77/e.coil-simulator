---
entity_id: "gene.b3071"
entity_type: "gene"
name: "nfeR"
source_database: "NCBI RefSeq"
source_id: "gene-b3071"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3071"
  - "nfeR"
---

# nfeR

`gene.b3071`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3071`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nfeR (gene.b3071) is a gene entity. It encodes yqjI (protein.P64588). Encoded protein function: FUNCTION: Represses the expression of YqjH which is involved in iron homeostasis under excess nickel conditions. Also represses its own expression. {ECO:0000269|PubMed:21097627}. EcoCyc product frame: G7594-MONOMER. EcoCyc synonyms: yqjI. Genomic coordinates: 3216779-3217402. EcoCyc protein note: NfeR, "Ni-responsive Fe uptake regulator" (previously known as YqjI), is a local transcription regulator that represses expression of the divergent operon, yqjH-yqjI, related to its autorepression and the synthesis of an NADPH-dependent ferric reductase . This regulator forms a complex with DNA in the absence of nickel, binding to a 20-bp-long sequence with an imperfect palindromic sequence. YqjI is inactivated under conditions of elevated nickel levels, and the presence of this divalent metal prevents its binding to the target gene. Thus, this regulator maintains the iron homeostasis during high levels of nickel . However, in vitro studies have shown that YqjI can be affected by other divalent metals. The YqjI regulator is structurally related to the PadR family, which is characterized by a winged helix-turn-helix (WHTH) motif. The amino-terminal region of this protein is similar to the C-terminal SlyD protein and to the N-terminal RcnA protein...

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9), yqjI (protein.P64588).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64588|protein.P64588]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=nfeR; function=-
- `represses` <-- [[protein.P64588|protein.P64588]] `RegulonDB` `C` - regulator=NfeR; target=nfeR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010084,ECOCYC:G7594,GeneID:947584`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3216779-3217402:+; feature_type=gene
