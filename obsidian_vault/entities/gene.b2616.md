---
entity_id: "gene.b2616"
entity_type: "gene"
name: "recN"
source_database: "NCBI RefSeq"
source_id: "gene-b2616"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2616"
  - "recN"
---

# recN

`gene.b2616`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2616`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

recN (gene.b2616) is a gene entity. It encodes recN (protein.P05824). Encoded protein function: FUNCTION: May be involved in recombinational repair of damaged DNA. EcoCyc product frame: EG10831-MONOMER. EcoCyc synonyms: radB. Genomic coordinates: 2751795-2753456. EcoCyc protein note: RecN functions in the recombinational repair of DNA double-strand breaks recN mutations reduce conjugational recombination proficiency (in a recBC sbcC background) and confer sensitivity to mitomycin C (MMC) and ionizing radiation ; the recN product is involved in the repair of DNA double-strand breaks (DSBs) (see also ). recN expression is regulated by the LexA repressor; RecN is induced in the presence MMC . Multicopy expression of cloned recN increases resistance of recN mutants to ionizing radiation but decreases survival of wild-type cells . recN is induced by the SOS response in MMC treated cells and in UV-irradiated cells . RecN shows sequence similarity to proteins from the structural maintenance of chromosomes (SMC) family (see ). RecN is degraded by the ClpXP protease ; DNA damage promotes the formation of nucleoid-associated RecN foci; ClpXP promotes the degradation of RecN when cells are released from DNA damage . RecA is required for the assembly of RecN foci at MMC-induced DSBs; ATPase-defective RecN (RecNK35A) is recruited to sites of DNA damage, but may not be properly released...

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), lexA (protein.P0A7C2), fur (protein.P0A9A9).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P05824|protein.P05824]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A7C2|protein.P0A7C2]] `RegulonDB` `S` - regulator=LexA; target=recN; function=-
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=recN; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008611,ECOCYC:EG10831,GeneID:947105`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2751795-2753456:+; feature_type=gene
