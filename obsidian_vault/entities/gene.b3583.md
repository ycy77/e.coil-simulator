---
entity_id: "gene.b3583"
entity_type: "gene"
name: "sgbE"
source_database: "NCBI RefSeq"
source_id: "gene-b3583"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3583"
  - "sgbE"
---

# sgbE

`gene.b3583`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3583`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sgbE (gene.b3583) is a gene entity. It encodes sgbE (protein.P37680). Encoded protein function: FUNCTION: Catalyzes the interconversion of L-ribulose 5-phosphate (LRu5P) and D-xylulose 5-phosphate (D-Xu5P) via a retroaldol/aldol mechanism (carbon-carbon bond cleavage analogous to a class II aldolase reaction). May be involved in the utilization of 2,3-diketo-L-gulonate. {ECO:0000269|PubMed:10913097, ECO:0000269|PubMed:11741871}. EcoCyc product frame: EG12287-MONOMER. EcoCyc synonyms: yiaS. Genomic coordinates: 3750086-3750781. EcoCyc protein note: The sgbE gene encodes a second L-ribulose-5-phosphate 4-epimerase that functions in metabolism of L-lyxose and L-xylulose . The operon encoding SgbE is not required for fermentation of L-ascorbate . Review:

## Biological Role

Repressed by plaR (protein.P37671). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8), rpoE (protein.P0AGB6).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37680|protein.P37680]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=sgbE; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=sgbE; function=+
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=sgbE; function=+
- `represses` <-- [[protein.P37671|protein.P37671]] `RegulonDB` `C` - regulator=PlaR; target=sgbE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011702,ECOCYC:EG12287,GeneID:948099`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3750086-3750781:+; feature_type=gene
