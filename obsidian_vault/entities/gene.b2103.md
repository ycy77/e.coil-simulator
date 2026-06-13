---
entity_id: "gene.b2103"
entity_type: "gene"
name: "thiD"
source_database: "NCBI RefSeq"
source_id: "gene-b2103"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2103"
  - "thiD"
---

# thiD

`gene.b2103`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2103`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

thiD (gene.b2103) is a gene entity. It encodes thiD (protein.P76422). Encoded protein function: FUNCTION: Catalyzes the phosphorylation of hydroxymethylpyrimidine phosphate (HMP-P) to HMP-PP, and of HMP to HMP-P. Shows no activity with pyridoxal, pyridoxamine or pyridoxine. {ECO:0000269|PubMed:10075431}. EcoCyc product frame: HMP-P-KIN-MONOMER. EcoCyc synonyms: thiA, thiJ. Genomic coordinates: 2183716-2184516. EcoCyc protein note: The bifunctional hydroxymethylpyrimidine (HMP) kinase/phosphomethylpyrimidine (HMP-P) kinase (ThiD) is involved in the biosynthesis of the essential cofactor thiamine pyrophosphate. The two phosphorylation reactions appear to be successive, with transient formation of HMP-P . Modeling of the phosphorylation reactions based on the crystal structure of the Salmonella Typhimurium enzyme suggest an inline replacement mechanism . While reported that ThiD is a monomer (31 kDa) in solution, suggested that ThiD as well as PdxK (which is in fact a homodimer) are homotetramers. The Salmonella homolog is 91% identical to E. coli ThiD and forms a homodimer. A thiD mutant requires thiamine supplementation . E. coli encodes two enzymes with HMP kinase activity: ThiD (described here) and PDXK-CPLX PdxK. A thiD pdxK double mutant lacks all HMP kinase activity...

## Enriched Pathways

- `eco00730` Thiamine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76422|protein.P76422]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006958,ECOCYC:G7135,GeneID:946459`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2183716-2184516:-; feature_type=gene
