---
entity_id: "gene.b3785"
entity_type: "gene"
name: "wzzE"
source_database: "NCBI RefSeq"
source_id: "gene-b3785"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3785"
  - "wzzE"
---

# wzzE

`gene.b3785`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3785`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

wzzE (gene.b3785) is a gene entity. It encodes wzzE (protein.P0AG00). Encoded protein function: FUNCTION: Modulates the polysaccharide chain length of enterobacterial common antigen (ECA). Required for the assembly of the phosphoglyceride-linked form of ECA (ECA(PG)) and the water-soluble cyclic form of ECA (ECA(CYC)). {ECO:0000269|PubMed:10515954, ECO:0000269|PubMed:16199561}. EcoCyc product frame: EG11295-MONOMER. EcoCyc synonyms: wzz, yifC. Genomic coordinates: 3969031-3970077. EcoCyc protein note: The assembly of enterobacterial common antigen (ECA) occurs by a Wzx/Wzy-dependent pathway (see ). wzzE is located within a gene cluster that encodes the enzymes required for ECA synthesis and assembly; WzzE functions to modulate the length of CPD-21605 ECAPG polysaccharide chains . Typically, ECAPG chain lengths are 1 to 14 repeats long with a modal value of 6 or 7; wzzE mutants display a random, non-modal distribution of ECAPG polysaccharide chain lengths . wzzE is also required for the synthesis of cyclic ECA (CPD0-2646 ECACYC) . The lipid III flippase EG11486-MONOMER WzxE, ECA polymerase FUC4NACTRANS-MONOMER WzyE, and WzzE may function as a multiprotein complex . WzyE and WzzE were shown in TAX-29471 to form a complex in vivo with stoichiometry of approximately eight WzzE to one WzyE...

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AG00|protein.P0AG00]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=wzzE; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012370,ECOCYC:EG11295,GeneID:944815`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3969031-3970077:+; feature_type=gene
