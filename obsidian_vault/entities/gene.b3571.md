---
entity_id: "gene.b3571"
entity_type: "gene"
name: "malS"
source_database: "NCBI RefSeq"
source_id: "gene-b3571"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3571"
  - "malS"
---

# malS

`gene.b3571`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3571`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

malS (gene.b3571) is a gene entity. It encodes malS (protein.P25718). Encoded protein function: FUNCTION: Since only maltooligosaccharides up to a chain length of 6 glucose units are actively transported through the cytoplasmic membrane via the membrane-bound complex of three proteins, MalF, MalG, and MalK, longer maltooligosaccharides must first be degraded by the periplasmic alpha-amylase, the MalS protein. EcoCyc product frame: ALPHA-AMYL-PERI-MONOMER. Genomic coordinates: 3737497-3739527. EcoCyc protein note: MalS is a periplasmic enzyme that degrades linear Dextrins dextrins of at least three glucose residues. CPD-3781 and CPD-3783 serve as substrates, leading to classification of the enzyme as an α-amylase hydrolyzing internal 1,4-glucosidic linkages . MalS is one of two α-amylases present in E. coli. The second enzyme, ALPHA-AMYL-CYTO-MONOMER "AmyA", is cytoplasmic. MalS is an endo hydrolase that recognizes its substrates from their non-reducing end and preferentially liberates MALTOHEXAOSE , which can then be transported through the cytoplasmic membrane via the ABC-16-CPLX. MalS is thought to provide a growth advantage by degrading periplasmic maltodextrins between 7 and 15 glucose units in length . MalS is a monomer in solution; two intramolecular disulfide bonds have been mapped . A crystal structure was reported at a resolution of 2...

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P25718|protein.P25718]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011668,ECOCYC:EG11316,GeneID:948088`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3737497-3739527:+; feature_type=gene
