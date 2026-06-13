---
entity_id: "gene.b4030"
entity_type: "gene"
name: "psiE"
source_database: "NCBI RefSeq"
source_id: "gene-b4030"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4030"
  - "psiE"
---

# psiE

`gene.b4030`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4030`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

psiE (gene.b4030) is a gene entity. It encodes psiE (protein.P0A7C8). Encoded protein function: Protein PsiE EcoCyc product frame: EG11209-MONOMER. EcoCyc synonyms: yjbA. Genomic coordinates: 4240325-4240735. EcoCyc protein note: A large-scale phenotypic study of a psiE mutant is presented . Regulation has been described . Transcription of the psiE gene is activated upon starvation for phosphate, carbon, or nitrogen ; regulation shows some response to PhoB and PhoR, but not PhoM , and also involves PhoT and cAMP-CRP . Membrane topology predictions using experimentally determined C terminus locations indicate that PsiE has three transmembrane helices and the C-terminus is located in the cytoplasm . PsiE: "phosphate starvation-inducible"

## Biological Role

Repressed by crp (protein.P0ACJ8). Activated by rpoD (protein.P00579), phoB (protein.P0AFJ5).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7C8|protein.P0A7C8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=psiE; function=+
- `activates` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB` `S` - regulator=PhoB; target=psiE; function=+
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=psiE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013187,ECOCYC:EG11209,GeneID:948528`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4240325-4240735:+; feature_type=gene
