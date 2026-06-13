---
entity_id: "gene.b3710"
entity_type: "gene"
name: "mdtL"
source_database: "NCBI RefSeq"
source_id: "gene-b3710"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3710"
  - "mdtL"
---

# mdtL

`gene.b3710`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3710`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mdtL (gene.b3710) is a gene entity. It encodes mdtL (protein.P31462). Encoded protein function: FUNCTION: Confers resistance to chloramphenicol. {ECO:0000269|PubMed:11566977}. EcoCyc product frame: YIDY-MONOMER. EcoCyc synonyms: yidY. Genomic coordinates: 3891615-3892790. EcoCyc protein note: MdtL (formerly YidY) is a member of the Drug:H+ Antiporter-1 (12 Spanner) (DHA1) family within the Major Facilitator Superfamily (MFS) . Overexpression of mdtL in a K-12 strain which lacks the major efflux pump permease AcrB (E. coli KAM3; see ) results in a two-fold increase in resistance to chloramphenicol but does not impact the resistance to a range of other antibiotics and toxic compounds . mdtL is one of 35 efflux-encoding genes that have been deleted or inactivated in 'Efflux KnockOut-35' (EKO-35) - a K-12 BW25133-derived strain that lacks 35 efflux pumps and can be used as a platform to study their function .

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9). Activated by zraR (protein.P14375).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31462|protein.P31462]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P14375|protein.P14375]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=mdtL; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012139,ECOCYC:EG11720,GeneID:948219`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3891615-3892790:+; feature_type=gene
