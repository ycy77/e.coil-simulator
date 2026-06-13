---
entity_id: "gene.b2508"
entity_type: "gene"
name: "guaB"
source_database: "NCBI RefSeq"
source_id: "gene-b2508"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2508"
  - "guaB"
---

# guaB

`gene.b2508`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2508`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

guaB (gene.b2508) is a gene entity. It encodes guaB (protein.P0ADG7). Encoded protein function: FUNCTION: Catalyzes the conversion of inosine 5'-phosphate (IMP) to xanthosine 5'-phosphate (XMP), the first committed and rate-limiting step in the de novo synthesis of guanine nucleotides, and therefore plays an important role in the regulation of cell growth. {ECO:0000255|HAMAP-Rule:MF_01964, ECO:0000269|PubMed:9341229}. EcoCyc product frame: IMP-DEHYDROG-MONOMER. EcoCyc synonyms: guaR. Genomic coordinates: 2632604-2634070.

## Biological Role

Repressed by dnaA (protein.P03004), fis (protein.P0A6R3), purR (protein.P0ACP7). Activated by crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADG7|protein.P0ADG7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=guaB; function=+
- `represses` <-- [[protein.P03004|protein.P03004]] `RegulonDB` `S` - regulator=DnaA; target=guaB; function=-
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `C` - regulator=Fis; target=guaB; function=-
- `represses` <-- [[protein.P0ACP7|protein.P0ACP7]] `RegulonDB` `S` - regulator=PurR; target=guaB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008257,ECOCYC:EG10421,GeneID:946985`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2632604-2634070:-; feature_type=gene
