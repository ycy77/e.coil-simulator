---
entity_id: "gene.b0048"
entity_type: "gene"
name: "folA"
source_database: "NCBI RefSeq"
source_id: "gene-b0048"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0048"
  - "folA"
---

# folA

`gene.b0048`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0048`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

folA (gene.b0048) is a gene entity. It encodes folA (protein.P0ABQ4). Encoded protein function: FUNCTION: Key enzyme in folate metabolism. Catalyzes an essential reaction for de novo glycine and purine synthesis, and for DNA precursor synthesis. EcoCyc product frame: DIHYDROFOLATEREDUCT-MONOMER. EcoCyc synonyms: tmr, tmrA. Genomic coordinates: 49823-50302. EcoCyc protein note: The enzyme encoded by folA, dihydrofolate reductase (DHFR) provides the major dihydrofolate reductase activity in the tetrahydrofolate biosynthetic pathway. It catalyzes the reduction of dihydrofolate to tetrahydrofolate via hydride transfer from NADPH to C6 of the pteridine ring. Tetrahydrofolate is an important intermediate in the biosynthesis of proteins and nucleic acids (see pathway PWY-6614). Because dihydrofolate reductase is essential for cell division and growth, it is a target for drug development. It is susceptible to inhibition by several agents which have antitumor, antibacterial and antimalarial properties including the well known drugs methotrexate and trimethoprim . The folA gene has been characterized and the enzyme has been purified and characterized . E. coli dihydrofolate reductase has been used as a model enzyme for research on the relationship between enzyme structure, dynamics and function...

## Biological Role

Activated by tyrR (protein.P07604).

## Enriched Pathways

- `eco00670` One carbon pool by folate (KEGG)
- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco04981` Folate transport and metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABQ4|protein.P0ABQ4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P07604|protein.P07604]] `RegulonDB` `C` - regulator=TyrR; target=folA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000164,ECOCYC:EG10326,GeneID:944790`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:49823-50302:+; feature_type=gene
