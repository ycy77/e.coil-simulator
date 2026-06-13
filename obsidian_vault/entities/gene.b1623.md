---
entity_id: "gene.b1623"
entity_type: "gene"
name: "add"
source_database: "NCBI RefSeq"
source_id: "gene-b1623"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1623"
  - "add"
---

# add

`gene.b1623`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1623`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

add (gene.b1623) is a gene entity. It encodes add (protein.P22333). Encoded protein function: FUNCTION: Catalyzes the hydrolytic deamination of adenosine and 2-deoxyadenosine. {ECO:0000255|HAMAP-Rule:MF_00540, ECO:0000269|PubMed:357905}. EcoCyc product frame: ADENODEAMIN-MONOMER. Genomic coordinates: 1702233-1703234. EcoCyc protein note: Adenosine deaminase participates in pathways for the degradation and salvage of purine ribonucleotides and deoxyribonucleotides. The salvage pathways can convert adenine, adenosine and deoxyadenosine to guanine nucleotides (see pathways PWY0-1296, PWY0-1297, PWY-6605, PWY-6609 and PWY-6611). This enzyme is one of two adenosine deaminases in E. coli, the other is TadA, CPLX0-901. The enzyme was shown to be induced in E. coli B by the presence of adenine or hypoxanthine in the culture medium . The native apparent molecular mass of the enzyme from E. coli K-12 was determined to be 29 kDa by gel filtration chromatography, using either purified enzyme, or enzyme from crude extracts . E. coli adenosine deaminase shares approximately 33% amino acid sequence identity and 50% overall homology with mammalian adenosine deaminases, suggesting structural and functional similarity . Murine adenosine deaminase is a monomeric enzyme that requires Zn2+ as a cofactor. Its crystal structure has been determined .

## Biological Role

Activated by rbsR (protein.P0ACQ0).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P22333|protein.P22333]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACQ0|protein.P0ACQ0]] `RegulonDB` `C` - regulator=RbsR; target=add; function=+

## External IDs

- `Dbxref:ASAP:ABE-0005435,ECOCYC:EG10030,GeneID:945851`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1702233-1703234:+; feature_type=gene
