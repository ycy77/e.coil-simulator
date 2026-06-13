---
entity_id: "gene.b3957"
entity_type: "gene"
name: "argE"
source_database: "NCBI RefSeq"
source_id: "gene-b3957"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3957"
  - "argE"
---

# argE

`gene.b3957`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3957`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

argE (gene.b3957) is a gene entity. It encodes argE (protein.P23908). Encoded protein function: FUNCTION: Catalyzes the hydrolysis of the amide bond of N(2)-acetylated L-amino acids. Cleaves the acetyl group from N-acetyl-L-ornithine to form L-ornithine, an intermediate in L-arginine biosynthesis pathway, and a branchpoint in the synthesis of polyamines. {ECO:0000255|HAMAP-Rule:MF_01108, ECO:0000269|PubMed:10684608, ECO:0000269|PubMed:1551850}. EcoCyc product frame: ACETYLORNDEACET-MONOMER. Genomic coordinates: 4153696-4154847. EcoCyc protein note: E. coli acetylornithine deacetylase (ArgE) is a homodimer that catalyses the deacylation of N2-acetyl-L-ornithine to yield ornithine and acetate . Ornithine is an obligatory intermediate in the arginine biosynthetic pathway and a branch point in the synthesis of polyamines . It is a metalloenzyme that is activated by cobalt and inorganic phosphate . The enzyme contains two metal binding sites: a high-affinity site that shows a preference for Zn(II) and a second lower affinity site that shows a strong preference for Co(II) . ArgE can also be activated by Mn(II) ions . Two Mn(II) ions bind to ArgE to form a dinuclear site in ArgE .

## Biological Role

Repressed by argR (protein.P0A6D0). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P23908|protein.P23908]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=argE; function=+
- `represses` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `C` - regulator=ArgR; target=argE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012955,ECOCYC:EG11286,GeneID:948456`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4153696-4154847:-; feature_type=gene
