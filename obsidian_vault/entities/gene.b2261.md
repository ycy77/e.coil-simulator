---
entity_id: "gene.b2261"
entity_type: "gene"
name: "menC"
source_database: "NCBI RefSeq"
source_id: "gene-b2261"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2261"
  - "menC"
---

# menC

`gene.b2261`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2261`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

menC (gene.b2261) is a gene entity. It encodes menC (protein.P29208). Encoded protein function: FUNCTION: Converts 2-succinyl-6-hydroxy-2,4-cyclohexadiene-1-carboxylate (SHCHC) to 2-succinylbenzoate (OSB) (PubMed:10194342, PubMed:8335646). Does not show detectable N-acylamino acid racemase (NAAAR) activity with N-acetyl-S-methionine as substrate (PubMed:10194342). {ECO:0000269|PubMed:10194342, ECO:0000269|PubMed:8335646}. EcoCyc product frame: O-SUCCINYLBENZOATE-COA-SYN-MONOMER. Genomic coordinates: 2375000-2375962. EcoCyc protein note: O-succinylbenzoate synthase catalyzes the formation of the first aromatic intermediate of the menaquinone biosynthetic pathway by dehydration of 2-succinyl-6-hydroxy-2,4-cyclohexadiene-1-carboxylate . MenC belongs to the MLE subfamily of the enolase family of enzymes . Crystal structures of the ligand-free, mutant enzyme-substrate, and enzyme-product complexes have been solved, and a reaction mechanism has been proposed . Site-directed mutagenesis of two proposed active-site lysines, Lys133 and Lys235, yielded catalytically inactive enzymes . Review:

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P29208|protein.P29208]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007473,ECOCYC:EG11532,GeneID:946734`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2375000-2375962:-; feature_type=gene
