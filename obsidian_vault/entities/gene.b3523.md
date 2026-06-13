---
entity_id: "gene.b3523"
entity_type: "gene"
name: "yhjE"
source_database: "NCBI RefSeq"
source_id: "gene-b3523"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3523"
  - "yhjE"
---

# yhjE

`gene.b3523`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3523`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yhjE (gene.b3523) is a gene entity. It encodes yhjE (protein.P37643). Encoded protein function: Inner membrane metabolite transport protein YhjE EcoCyc product frame: YHJE-MONOMER. Genomic coordinates: 3674786-3676108. EcoCyc protein note: In the Transporter Classification Database , YhjE is an uncharacterised member of the Metabolite:H+ Symporter (MHS) Family within the Major Facilitator Superfamily (MFS). Deletion of yhjE in a strain (ΔcydB::KmS/ΔappB::KmR) that is dependent solely on CYT-O-UBIOX-CPLX for respiratory growth, results in an aerobic growth defect; cytochrome bo3 oxidase activity is significantly reduced and its b- and o-type hemes cannot be detected . . Deletion of yhjE in an otherwise wild-type background perturbs iron (but not copper) homeostasis . ArcA appears to activate yhjE expression under anaerobiosis. A putative ArcA binding site is located 202 bp upstream of this gene

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), arcA (protein.P0A9Q1). Activated by lrp (protein.P0ACJ0), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37643|protein.P37643]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `S` - regulator=Lrp; target=yhjE; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yhjE; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=yhjE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011509,ECOCYC:EG12249,GeneID:948032`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3674786-3676108:+; feature_type=gene
