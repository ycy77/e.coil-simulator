---
entity_id: "gene.b1496"
entity_type: "gene"
name: "yddA"
source_database: "NCBI RefSeq"
source_id: "gene-b1496"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1496"
  - "yddA"
---

# yddA

`gene.b1496`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1496`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yddA (gene.b1496) is a gene entity. It encodes yddA (protein.P31826). Encoded protein function: Inner membrane ABC transporter ATP-binding protein YddA (CDS102) EcoCyc product frame: YDDA-MONOMER. Genomic coordinates: 1577657-1579342. EcoCyc protein note: yddA is located in a 3 gene cluster (yddA-yddB-ppqL) which may represent a 3-component iron-uptake system . Distant homologs (fusD, fusA and fusC respectively) encode a ferredoxin uptake system (Fus) in plant pathogenic Pectobacterium spp. . In the Transporter Classification Database, YddA is a member of the The Peroxysomal Fatty Acyl CoA Transporter (P-FAT) Family within the ATP-Binding Cassette (ABC) Superfamily . Overexpression of cloned yddA in the drug-supersensitive strain E. coli KAM3 did not alter its resistance phenotype against a large number of different drug and toxic compounds . YddA contains an ABC-TMD domain . Screening of a random transposon mutant library suggests that YddA is required for growth under optimum growth conditions (rich medium at 37°C), but not under cold conditions (15°C) or in minimal medium . yddA is one of 35 efflux-encoding genes that have been deleted or inactivated in 'Efflux KnockOut-35' (EKO-35) - a K-12 BW25133-derived strain that lacks 35 efflux pumps and can be used as a platform to study their function .

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31826|protein.P31826]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=yddA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004984,ECOCYC:EG11742,GeneID:945945`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1577657-1579342:-; feature_type=gene
