---
entity_id: "gene.b0844"
entity_type: "gene"
name: "ybjI"
source_database: "NCBI RefSeq"
source_id: "gene-b0844"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0844"
  - "ybjI"
---

# ybjI

`gene.b0844`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0844`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybjI (gene.b0844) is a gene entity. It encodes ybjI (protein.P75809). Encoded protein function: FUNCTION: Catalyzes the dephosphorylation of 5-amino-6-(5-phospho-D-ribitylamino)uracil, and thus could be involved in the riboflavin biosynthesis pathway (PubMed:24123841). Is also able to dephosphorylate flavin mononucleotide (FMN), erythrose 4-phosphate and other phosphoric acid esters (PubMed:15808744, PubMed:16990279, PubMed:24123841). {ECO:0000269|PubMed:15808744, ECO:0000269|PubMed:16990279, ECO:0000269|PubMed:24123841}. EcoCyc product frame: G6442-MONOMER. Genomic coordinates: 885316-886131. EcoCyc protein note: The identity of the enzyme(s) catalyzing the dephosphorylation of CPD-1086 in the riboflavin biosynthesis pathway was long unknown . have now shown that at least two enzymes, YbjI and YigB, can catalyze this reaction. YbjI was initially identified as an FMN phosphatase belonging to the superfamily of haloacid dehalogenase (HAD)-like hydrolases. In addition, YbjI has some phosphatase activity against pyridoxal phosphate . The phosphatase activity of YbjI was first discovered in a high-throughput screen of purified proteins . Deletion of ybjI alone does not result in riboflavin auxotrophy .

## Biological Role

Repressed by rcdA (protein.P75811).

## Enriched Pathways

- `eco00740` Riboflavin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75809|protein.P75809]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P75811|protein.P75811]] `RegulonDB` `C` - regulator=RcdA; target=ybjI; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002877,ECOCYC:G6442,GeneID:945470`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:885316-886131:-; feature_type=gene
