---
entity_id: "gene.b1713"
entity_type: "gene"
name: "pheT"
source_database: "NCBI RefSeq"
source_id: "gene-b1713"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1713"
  - "pheT"
---

# pheT

`gene.b1713`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1713`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pheT (gene.b1713) is a gene entity. It encodes pheT (protein.P07395). Encoded protein function: Phenylalanine--tRNA ligase beta subunit (EC 6.1.1.20) (Phenylalanyl-tRNA synthetase beta subunit) (PheRS) EcoCyc product frame: PHET-MONOMER. Genomic coordinates: 1795557-1797944. EcoCyc protein note: The β subunit of PheRS (also called PheST) contains the Phe-tRNAPhe binding site . The editing site of the enzyme localizes to the B3/B4 domain of the β subunit . Amino acid residues involved in the editing activity have been identified . The B2 OB-fold domain is not essential for catalytic activity, but may play a role as a secondary tRNA binding site in post-transfer editing . Isolated β subunits exist primarily as monomers . A Glu571Lys mutant (pheT36) is temperature-sensitive . The temperature-sensitive fitA76 and fit95 mutants related to pheS and pheT, respectively, have been genetically characterized . Reviews:

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P07395|protein.P07395]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005717,ECOCYC:EG10710,GeneID:945382`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1795557-1797944:-; feature_type=gene
