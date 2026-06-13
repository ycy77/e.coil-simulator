---
entity_id: "gene.b1662"
entity_type: "gene"
name: "ribC"
source_database: "NCBI RefSeq"
source_id: "gene-b1662"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1662"
  - "ribC"
---

# ribC

`gene.b1662`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1662`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ribC (gene.b1662) is a gene entity. It encodes ribC (protein.P0AFU8). Encoded protein function: FUNCTION: Catalyzes the dismutation of two molecules of 6,7-dimethyl-8-ribityllumazine, resulting in the formation of riboflavin and 5-amino-6-(D-ribitylamino)uracil. {ECO:0000269|PubMed:9022701}. EcoCyc product frame: RIBOFLAVIN-SYN-MONOMER. EcoCyc synonyms: ribE. Genomic coordinates: 1742601-1743242. EcoCyc protein note: Riboflavin synthase catalyzes the final step in riboflavin biosynthesis, the formation of the carbocyclic ring of riboflavin by dismutation of 6,7-dimethyl-8-ribityllumazine. No homolog of this enzyme exists in humans, and it is therefore an attractive target for antimicrobial agents against microbes that are dependent on endogenous synthesis of riboflavin. Inhibitors of riboflavin synthase with antibiotic activity have been developed, e.g. . A recombinant N-terminal domain fragment dimerizes and is able to bind riboflavin . Catalytically relevant amino acid residues have been identified by mutagenesis . A kinetically competent reaction intermediate has been identified , and the enzyme kinetics have been studied under single turnover conditions . A new, simpler mechanism for formation of the pentacyclic reaction intermediate via hydryde transfer has been proposed . Riboflavin synthase is a homotrimer in solution...

## Enriched Pathways

- `eco00740` Riboflavin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFU8|protein.P0AFU8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005557,ECOCYC:EG11406,GeneID:945848`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1742601-1743242:-; feature_type=gene
