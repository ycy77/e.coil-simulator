---
entity_id: "gene.b0593"
entity_type: "gene"
name: "entC"
source_database: "NCBI RefSeq"
source_id: "gene-b0593"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0593"
  - "entC"
---

# entC

`gene.b0593`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0593`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

entC (gene.b0593) is a gene entity. It encodes entC (protein.P0AEJ2). Encoded protein function: FUNCTION: Involved in the biosynthesis of the siderophore enterobactin (macrocyclic trimeric lactone of N-(2,3-dihydroxybenzoyl)-serine). Catalyzes the reversible conversion of chorismate to isochorismate. {ECO:0000269|PubMed:17243787, ECO:0000269|PubMed:20079748, ECO:0000269|PubMed:2139795, ECO:0000269|PubMed:2536681, ECO:0000269|PubMed:8655506, ECO:0000269|PubMed:9795253}. EcoCyc product frame: ENTC-MONOMER. EcoCyc synonyms: fepF. Genomic coordinates: 624885-626060. EcoCyc protein note: There are two isochorismate synthase enzymes present in E. coli, encoded by entC and menF. EntC is specific to the enterobactin biosynthetic pathway, while MenF is specific to the menaquinone biosynthetic pathway . Macromolecular crowding appears to increase the intrinsic activity of the enzyme by inducing structural changes . The crystal structure of EntC in complex with isochorismate and Mg2+ has been determined at 2.3 Å resolution. Also in this report, activity analysis of the wild-type enzyme and EntC mutants produced by site-directed mutagenesis provided insights into the catalytic mechanism . EntB has been shown to form a specific, intracellular pairwise interaction with EntC, and computational analysis indicates the EntB-EntC complex may provide a substrate channeling surface...

## Biological Role

Repressed by fur (protein.P0A9A9).

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01053` Biosynthesis of siderophore group nonribosomal peptides (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEJ2|protein.P0AEJ2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `C` - regulator=Fur; target=entC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002047,ECOCYC:EG10261,GeneID:945511`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:624885-626060:+; feature_type=gene
