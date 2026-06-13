---
entity_id: "gene.b3917"
entity_type: "gene"
name: "sbp"
source_database: "NCBI RefSeq"
source_id: "gene-b3917"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3917"
  - "sbp"
---

# sbp

`gene.b3917`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3917`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sbp (gene.b3917) is a gene entity. It encodes sbp (protein.P0AG78). Encoded protein function: FUNCTION: This protein specifically binds sulfate and is involved in its transmembrane transport. EcoCyc product frame: SBP-MONOMER. Genomic coordinates: 4108834-4109823. EcoCyc protein note: Sbp is a periplasmic sulfate/thiosulfate binding protein; Sbp is one of two periplasmic binding proteins that separately interact with an ABC transporter permease (CysAUW) to mediate high affinity uptake of sulfate and thiosulfate. The predicted amino acid sequence of Sbp from E. coli is 95% identical to the (well characterized) protein from Salmonella typhimurium . Sbp binds sulfate with high affinity (Kd = 0.16 µM) . Double cysP sbp mutants (cysP::Cat sbp::Kan) are cysteine auxotrophs; growth on sulfate (and thiosulfate) as sole sulfur source can be restored in the double mutant by multicopy expression of either cysP or sbp however growth is impaired compared to the wild type strain; CysP and Sbp have overlapping specificity and both are required for wild-type levels of sulfate/thiosulfate transport . Sbp was identified in a set of 'sulfate starvation induced' (SSI) proteins which were induced when cells were grown with sulfur sources (eg.methionine, glutathione, ethanesulfonate) other than sulfate and cysteine...

## Enriched Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AG78|protein.P0AG78]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012794,ECOCYC:EG10929,GeneID:948411`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4108834-4109823:+; feature_type=gene
