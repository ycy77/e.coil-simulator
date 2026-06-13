---
entity_id: "gene.b3721"
entity_type: "gene"
name: "bglB"
source_database: "NCBI RefSeq"
source_id: "gene-b3721"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3721"
  - "bglB"
---

# bglB

`gene.b3721`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3721`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

bglB (gene.b3721) is a gene entity. It encodes bglB (protein.P11988). Encoded protein function: FUNCTION: Catalyzes the hydrolysis of phosphorylated beta-glucosides into glucose-6-phosphate (G-6-P) and aglycone. It has a high affinity for phosphorylated aromatic beta-glucosides (p-nitrophenyl-beta-glucoside, phenyl beta-glucoside, arbutin and phosphorylated salicin), and a low affinity for phosphorylated beta-methyl-glucoside. {ECO:0000269|PubMed:4576407}. EcoCyc product frame: EG10114-MONOMER. EcoCyc synonyms: blgA. Genomic coordinates: 3902289-3903701. EcoCyc protein note: BglB is a phospho-β-glucosidase encoded within the cryptic bgl operon .

## Biological Role

Repressed by fis (protein.P0A6R3), hns (protein.P0ACF8), nac (protein.Q47005). Activated by crp (protein.P0ACJ8), leuO (protein.P10151).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P11988|protein.P11988]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=bglB; function=+
- `activates` <-- [[protein.P10151|protein.P10151]] `RegulonDB` `S` - regulator=LeuO; target=bglB; function=+
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=bglB; function=-
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=bglB; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=bglB; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012169,ECOCYC:EG10114,GeneID:948234`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3902289-3903701:-; feature_type=gene
