---
entity_id: "gene.b4169"
entity_type: "gene"
name: "amiB"
source_database: "NCBI RefSeq"
source_id: "gene-b4169"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4169"
  - "amiB"
---

# amiB

`gene.b4169`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4169`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

amiB (gene.b4169) is a gene entity. It encodes amiB (protein.P26365). Encoded protein function: FUNCTION: Cell-wall hydrolase involved in septum cleavage during cell division. Can also act as powerful autolysin in the presence of murein synthesis inhibitors. {ECO:0000269|PubMed:11454209, ECO:0000269|PubMed:18390656}. EcoCyc product frame: NACMURLALAAMI2-MONOMER. EcoCyc synonyms: yjeD. Genomic coordinates: 4396065-4397402. EcoCyc protein note: amiB encodes a protein with N-acetylmuramoyl-L-alanine amidase activity. Murein sacculi isolated from a strain overexpressing amiB shows a significant decrease in the amount of high molecular weight murein; expression of amiB from a plasmid complements the chaining phenotype associated with deletion of the three N-acetylmuramoyl-L-alanine amidases NACMURLALAAMI1-MONOMER "AmiA", AmiB and G7458-MONOMER "AmiC" . Murein amidase activity produces stemless or a-denuded-peptidoglycan denuded glycans. Cells containing double amidase gene deletions (ΔamiAB, ΔamiAC and ΔamiBC) form septal peptidoglycan rings - thick dark bands of peptidoglycan between adjacent cells seen in the purified sacculi from chained cells . The murein amidases are necessary for the continued incorporation of peptidoglycan into the developing septum in E. coli...

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P26365|protein.P26365]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=amiB; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=amiB; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013653,ECOCYC:EG11363,GeneID:948683`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4396065-4397402:+; feature_type=gene
