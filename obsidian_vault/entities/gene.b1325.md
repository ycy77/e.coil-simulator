---
entity_id: "gene.b1325"
entity_type: "gene"
name: "ycjG"
source_database: "NCBI RefSeq"
source_id: "gene-b1325"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1325"
  - "ycjG"
---

# ycjG

`gene.b1325`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1325`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ycjG (gene.b1325) is a gene entity. It encodes ycjG (protein.P51981). Encoded protein function: FUNCTION: Catalyzes the epimerization of L-Ala-D-Glu to L-Ala-L-Glu and has a role in the recycling of the murein peptide, of which L-Ala-D-Glu is a component. Is also able to catalyze the reverse reaction and the epimerization of all the L-Ala-X dipeptides, except L-Ala-L-Arg, L-Ala-L-Lys and L-Ala-L-Pro. Is also active with L-Gly-L-Glu, L-Phe-L-Glu, and L-Ser-L-Glu, but not with L-Glu-L-Glu, L-Lys-L-Glu, L-Pro-L-Glu, L-Lys-L-Ala, or D-Ala-D-Ala. {ECO:0000269|PubMed:11747447, ECO:0000269|PubMed:18535144}. EcoCyc product frame: G6661-MONOMER. EcoCyc synonyms: ycjH. Genomic coordinates: 1388930-1389895. EcoCyc protein note: YcjG is an L-Ala-D/L-Glu epimerase that may play a role in the metabolism of murein peptide. The substrate specificity of the enzyme is not strict. YcjG belongs to the MLE subfamily of the enolase family of enzymes . The crystal structure of YcjG has been solved at 2.6 Å resolution. Although YcjG behaves like a monomer in solution, the crystal structure shows extensive surface contacts between two monomers . A D297G mutant can catalyze both the wild-type reaction as well as the o-succinylbenzoate synthase reaction; thus this substitution relaxes the substrate specificity of the enzyme...

## Biological Role

Repressed by pgrR (protein.P77333).

## Enriched Pathways

- `eco00470` D-Amino acid metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P51981|protein.P51981]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P77333|protein.P77333]] `RegulonDB` `S` - regulator=PgrR; target=ycjG; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004448,ECOCYC:G6661,GeneID:946013`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1388930-1389895:+; feature_type=gene
