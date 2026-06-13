---
entity_id: "gene.b1690"
entity_type: "gene"
name: "ydiM"
source_database: "NCBI RefSeq"
source_id: "gene-b1690"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1690"
  - "ydiM"
---

# ydiM

`gene.b1690`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1690`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydiM (gene.b1690) is a gene entity. It encodes ydiM (protein.P76197). Encoded protein function: Inner membrane transport protein YdiM EcoCyc product frame: B1690-MONOMER. Genomic coordinates: 1771071-1772285. EcoCyc protein note: Deletion of ydiM results in reduced tolerance to isoprenol (12 hr exposure to 0.5% isoprenol) compared to wild-type and over-expression of ydiM improves resistance to isoprenol; isoprenol exposure induces up-regulation of ydiM . ydiM is one of 35 efflux-encoding genes that have been deleted or inactivated in 'Efflux KnockOut-35' (EKO-35) - a K-12 BW25133-derived strain that lacks 35 efflux pumps and can be used as a platform to study their function . Deletion of ydiM in a strain (ΔcydB::KmS/ΔappB::KmR) that is dependent solely on CYT-O-UBIOX-CPLX for respiratory growth, results in an aerobic growth defect; cytochrome bo3 oxidase activity is significantly reduced and its b- and o-type hemes cannot be detected . Deletion of ydiM in an otherwise wild-type background perturbs copper (but not iron) homeostasis . In the Transporter Classification Database, YdiM is a member of the Aromatic Acid:H+ Symporter (AAHS) family within the Major Facilitator Superfamily (MFS) .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76197|protein.P76197]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ydiM; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005645,ECOCYC:G6916,GeneID:946196`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1771071-1772285:+; feature_type=gene
