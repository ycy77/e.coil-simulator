---
entity_id: "gene.b2048"
entity_type: "gene"
name: "cpsG"
source_database: "NCBI RefSeq"
source_id: "gene-b2048"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2048"
  - "cpsG"
---

# cpsG

`gene.b2048`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2048`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cpsG (gene.b2048) is a gene entity. It encodes manB (protein.P24175). Encoded protein function: FUNCTION: Involved in the biosynthesis of the capsular polysaccharide colanic acid. EcoCyc product frame: PHOSMANMUT-MONOMER. EcoCyc synonyms: rfbK, manB. Genomic coordinates: 2121609-2122979. EcoCyc protein note: Colanic acid is an atypical type I capsule that is present in E. coli K-12. It is a high molecular weight polymer composed of six-residue repeat units made up of glucose, galactose, glucuronic acid and fucose. Phosphomannomutase is part of the GDP-mannose biosynthetic pathway, which is a precursor for colanic acid production. In E. coli K-12 phosphomannomutase is coded for by the cpsG gene, but in other E. coli strains it is the rfbK gene that codes for the enzyme (see pathways PWY-5659 and COLANSYN-PWY). In a metabolic engineering study, an E. coli mutant was constructed that included a deletion of manA and the cps gene cluster, and carried a plasmid harboring cpsG and cpsB from E. coli as well as another plasmid harboring msg from Rhodothermus marinus. This strain was used in the production of the osmolyte mannosylglycerate . In another study TDP-2-deoxy-glucose was produced in a one-pot enzymatic synthesis from TMP and 2-deoxy glucose-6-phosphate using the purified recombinant E. coli K-12 enzymes phsophomannomutase, TDP-glucose synthase, TMP kinase, and acetate kinase...

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P24175|protein.P24175]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006788,ECOCYC:EG10162,GeneID:946574`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2121609-2122979:-; feature_type=gene
