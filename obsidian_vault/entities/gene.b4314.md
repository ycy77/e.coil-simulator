---
entity_id: "gene.b4314"
entity_type: "gene"
name: "fimA"
source_database: "NCBI RefSeq"
source_id: "gene-b4314"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4314"
  - "fimA"
---

# fimA

`gene.b4314`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4314`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fimA (gene.b4314) is a gene entity. It encodes fimA (protein.P04128). Encoded protein function: FUNCTION: Fimbriae (also called pili), polar filaments radiating from the surface of the bacterium to a length of 0.5-1.5 micrometers and numbering 100-300 per cell, enable bacteria to colonize the epithelium of specific host organs. EcoCyc product frame: EG10308-MONOMER. EcoCyc synonyms: fimD, pilA. Genomic coordinates: 4543115-4543663. EcoCyc protein note: FimA, the major subunit of the Escherichia coli type 1 fimbriae (pili), has been identified and its gene sequence determined . A typical pilus is composed of around 1,000 subunits of FimA which form a right-handed helical rod connected to a short tip fibrillum composed of the adaptor proteins FimG and FimF, and the adhesin FimH attached at its distal end . The fimA promoter is contained within fimS, the fim switch, which controls transcription of fimA and the genes for the other fimbrial structural proteins by undergoing a site-specific inversion . Monomeric FimA is the dominant protein in K-12 MG1655 outer membrane vesicles (OMVs); disruption of fimbrial assembly alters OMV cargo . Deletion of fimA impairs pili-dependent surface motility (PDSM) in E. coli strain W3110 . E...

## Biological Role

Activated by rpoD (protein.P00579), fis (protein.P0A6R3), hns (protein.P0ACF8), lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P04128|protein.P04128]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=fimA; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=fimA; function=+
- `activates` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=fimA; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `C` - regulator=Lrp; target=fimA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0014145,ECOCYC:EG10308,GeneID:948838`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4543115-4543663:+; feature_type=gene
