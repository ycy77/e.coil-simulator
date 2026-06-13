---
entity_id: "gene.b0796"
entity_type: "gene"
name: "cecR"
source_database: "NCBI RefSeq"
source_id: "gene-b0796"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0796"
  - "cecR"
---

# cecR

`gene.b0796`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0796`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cecR (gene.b0796) is a gene entity. It encodes cecR (protein.P0ACU0). Encoded protein function: FUNCTION: Regulates transcription of the cecR-ybhGFSR operon and the rhlE gene, which altogether are involved in the control of sensitivity to cefoperazone and chloramphenicol. Represses the cecR-ybhGFSR operon and activates the rhlE operon. Acts by binding to a palindromic sequence within the intergenic spacer located between these two divergently transcribed operons. {ECO:0000269|PubMed:27112147}. EcoCyc product frame: EG12406-MONOMER. EcoCyc synonyms: ybiH. Genomic coordinates: 829972-830643. EcoCyc protein note: CecR (also known as YbiH) is a TetR-family (subfamily D) transcription factor originally described as a "Cefoperazone and chloramphenicol Regulator" [Yamanaka16] and confirmed as a TF through an integrated workflow comprised of computational prediction, knowledge-based classification, and experimental validation of candidate TFs at the genome scale . CecR controls genes involved in sensitivity to cefoperazone and chloramphenicol . CecR functions as an all-helical TetR-like homodimer, and each protomer contains an N-terminal DNA-binding domain with a helix-turn-helix (HTH) motif and a C-terminal ligand-recognition domain . The CecR crystal structure (1...

## Biological Role

Repressed by cecR (protein.P0ACU0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACU0|protein.P0ACU0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACU0|protein.P0ACU0]] `RegulonDB` `C` - regulator=CecR; target=cecR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002711,ECOCYC:EG12406,GeneID:945421`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:829972-830643:-; feature_type=gene
