---
entity_id: "gene.b2890"
entity_type: "gene"
name: "lysS"
source_database: "NCBI RefSeq"
source_id: "gene-b2890"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2890"
  - "lysS"
---

# lysS

`gene.b2890`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2890`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lysS (gene.b2890) is a gene entity. It encodes lysS (protein.P0A8N3). Encoded protein function: Lysine--tRNA ligase (EC 6.1.1.6) (Lysyl-tRNA synthetase) (LysRS) EcoCyc product frame: LYSS-MONOMER. EcoCyc synonyms: asuD, herC. Genomic coordinates: 3033657-3035174. EcoCyc protein note: The lysine-tRNA ligase LysS is a member of the family of aminoacyl-tRNA synthetases, which interpret the genetic code by covalently linking amino acids to their specific tRNA molecules. The reaction is driven by ATP hydrolysis. LysS belongs to the subclass IIB of aminoacyl-tRNA synthetases . E. coli contains both a constitutive and an inducible lysyl-tRNA synthetase ; lysS encodes the constitutively expressed enzyme and lysU encodes the inducible . The LYSU-MONOMER LysU enzyme appears to be more error-prone than LysS . The ATP binding site was investigated by affinity labeling . Key residues for recognition of the cognate amino acid and catalytic activity have been identified , providing insight into differences between the class I and class II tRNA synthetases. A model for the recognition specificity of the cognate anticodon is presented . A solution structure of the N-terminal anticodon binding domain has been solved...

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8N3|protein.P0A8N3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009486,ECOCYC:EG10552,GeneID:947372`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3033657-3035174:-; feature_type=gene
