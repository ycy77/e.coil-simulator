---
entity_id: "gene.b2105"
entity_type: "gene"
name: "rcnR"
source_database: "NCBI RefSeq"
source_id: "gene-b2105"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2105"
  - "rcnR"
---

# rcnR

`gene.b2105`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2105`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rcnR (gene.b2105) is a gene entity. It encodes rcnR (protein.P64530). Encoded protein function: FUNCTION: Repressor of rcnA expression. Acts by binding specifically to the rcnA promoter in the absence of nickel and cobalt. In the presence of one of these metals, it has a weaker affinity for rcnA promoter. {ECO:0000269|PubMed:16956381, ECO:0000269|PubMed:17120142}. EcoCyc product frame: G7137-MONOMER. EcoCyc synonyms: yohL. Genomic coordinates: 2185524-2185796. EcoCyc protein note: The RcnR, resistance to cobalt and nickel regulator protein is an addition to the set of transcriptional metallo-regulator proteins of E. coli (some of the main ones are Fur, CueR, CusR, MntR, Zur, ZntR, and NikR) , that regulate the transcriptional expression of a recently described efflux protein, RcnA , to maintain nickel and cobalt homeostasis . The homeostasis of different metals in the cell is constantly monitored, and adequate pathways are activated or repressed to keep the metals within normal levels. Specifically, when nickel and cobalt exceed the normal levels, cell growth stops . Ni(II) and Co(II) binding results in the transcription of RcnAB in vivo, although it has been shown that RcnR binds a variety of metal ions in vitro . Binding of Co(II) and Ni(II) to RcnR affects its flexibility at the N terminus, and this effect modulates its DNA-binding affinity...

## Biological Role

Repressed by rcnR (protein.P64530).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64530|protein.P64530]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P64530|protein.P64530]] `RegulonDB` `S` - regulator=RcnR; target=rcnR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0006964,ECOCYC:G7137,GeneID:947114`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2185524-2185796:-; feature_type=gene
