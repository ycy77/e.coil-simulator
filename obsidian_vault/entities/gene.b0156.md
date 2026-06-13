---
entity_id: "gene.b0156"
entity_type: "gene"
name: "erpA"
source_database: "NCBI RefSeq"
source_id: "gene-b0156"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0156"
  - "erpA"
---

# erpA

`gene.b0156`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0156`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

erpA (gene.b0156) is a gene entity. It encodes erpA (protein.P0ACC3). Encoded protein function: FUNCTION: Probably involved in the insertion of Fe-S clusters into apoproteins in vivo including IspG and/or IspH. Essential for growth under aerobic conditions and for anaerobic respiration but not for fermentation. In vitro it binds Fe-S clusters and transfers them to apo-IspG, which is involved in quinone biosynthesis among many other cell components. Experiments indicate that it is probably also involved in the insertion of other Fe-S clusters than IspG/IspH. EcoCyc product frame: EG12332-MONOMER. EcoCyc synonyms: yadR. Genomic coordinates: 176610-176954. EcoCyc protein note: ErpA is an A-type iron-sulfur carrier protein; it can bind both [2Fe-2S] and [4Fe-4S] clusters. In vitro, ErpA can transfer a [4Fe-4S] cluster to EG10370-MONOMER "apo-IspG" . Functional redundancy between the three A-type carriers (ATCs) in E. coli, ErpA (an ATC-I) and IscA and SufA (both belonging to the ATC-II family), has been investigated . ErpA is required for maturation of EG11212-MONOMER NsrR, but not G7326-MONOMER IscR . IscA and ErpA appear to have independent roles in the delivery of iron-sulfur clusters to individual subunits of the FHLMULTI-CPLX FHL complex . ErpA and G7748-MONOMER NfuA directly interact with each other...

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), ryhB (gene.b4451), fur (protein.P0A9A9), iscR (protein.P0AGK8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACC3|protein.P0ACC3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[gene.b4451|gene.b4451]] `RegulonDB` `S` - regulator=RyhB; target=erpA; function=-
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=erpA; function=-
- `represses` <-- [[protein.P0AGK8|protein.P0AGK8]] `RegulonDB` `S` - regulator=IscR; target=erpA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0000538,ECOCYC:EG12332,GeneID:944857`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:176610-176954:+; feature_type=gene
