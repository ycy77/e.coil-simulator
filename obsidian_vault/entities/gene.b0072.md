---
entity_id: "gene.b0072"
entity_type: "gene"
name: "leuC"
source_database: "NCBI RefSeq"
source_id: "gene-b0072"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0072"
  - "leuC"
---

# leuC

`gene.b0072`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0072`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

leuC (gene.b0072) is a gene entity. It encodes leuC (protein.P0A6A6). Encoded protein function: FUNCTION: Catalyzes the isomerization between 2-isopropylmalate and 3-isopropylmalate, via the formation of 2-isopropylmaleate. EcoCyc product frame: LEUC-MONOMER. Genomic coordinates: 79464-80864. EcoCyc protein note: Isopropylmalate (IPM) isomerase catalyzes the second step in leucine biosynthesis, converting 2-isopropylmalate to 3-isopropylmalate. LeuC and LeuD are both required for the activity of IPM isomerase . Based on the IPM isomerase in Salmonella typhimurium and cross-species complementation studies with the Salmonella and S. cerevisiae enzymes, E. coli IPM isomerase is likely to be a protein complex consisting of a 1:1 pairing of the of leuC and leuD gene products . LeuC protein levels are increased in a threonine-overproducing mutant ; LeuC leves are decreased after 30 minutes of excess zinc stress . leuC insertion mutants, which cause leucine auxotrophy, lead to increased antibiotic tolerance in biofilms under leucine starvation conditions .

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco00660` C5-Branched dibasic acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6A6|protein.P0A6A6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=leuC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000261,ECOCYC:EG11576,GeneID:945076`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:79464-80864:-; feature_type=gene
