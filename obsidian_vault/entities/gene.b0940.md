---
entity_id: "gene.b0940"
entity_type: "gene"
name: "elfC"
source_database: "NCBI RefSeq"
source_id: "gene-b0940"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0940"
  - "elfC"
---

# elfC

`gene.b0940`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0940`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

elfC (gene.b0940) is a gene entity. It encodes elfC (protein.P75857). Encoded protein function: FUNCTION: Part of the elfADCG-ycbUVF fimbrial operon, which promotes adhesion of bacteria to different abiotic surfaces. Could be involved in the export and assembly of the ElfA fimbrial subunits across the outer membrane. {ECO:0000269|PubMed:20345943}. EcoCyc product frame: G6482-MONOMER. EcoCyc synonyms: ycbS. Genomic coordinates: 999216-1001816. EcoCyc protein note: ycbQRSTUVF is a putative chaperone-usher fimbrial operon in E.coli K-12 . The operon is cryptic under normal laboratory conditions but when constitutive expression is induced in a strain that lacks the type 1 fimbrial complex the ycb operon promotes biofilm formation in minimal media on a variety of abiotic surfaces and produces numerous surface fimbrial structures that can be observed microscopically . Expression of the ycb operon is regulated by the global regulators PD00288 "H-NS" and CPLX0-226 "CRP cAMP" . YcbS is implicated in bacterial infection; a ΔycbS strain (in a K-12 BW25113 background) shows a significant decrease in invasion into a human ileocecal epithelial cell line compared to wild type and this phenotype is complemented by expression of ycbS from a plasmid; overexpression of ycbS from a plasmid increases invasion into the cell line...

## Biological Role

Repressed by glaR (protein.P37338).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75857|protein.P75857]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=elfC; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0003189,ECOCYC:G6482,GeneID:946934`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:999216-1001816:+; feature_type=gene
