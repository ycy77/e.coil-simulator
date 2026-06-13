---
entity_id: "gene.b3697"
entity_type: "gene"
name: "yidA"
source_database: "NCBI RefSeq"
source_id: "gene-b3697"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3697"
  - "yidA"
---

# yidA

`gene.b3697`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3697`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yidA (gene.b3697) is a gene entity. It encodes yidA (protein.P0A8Y5). Encoded protein function: FUNCTION: Catalyzes the dephosphorylation of different sugar phosphates including erythrose-4-phosphate (Ery4P), ribose-5-phosphate (Ribu5P), fructose-1-phosphate (Fru1P), fructose-6-phosphate (Fru6P), glucose-6-P (Glu6P), and also imidodiphosphate (Imido-di-P) and acetyl phosphate (Acetyl-P). Selectively hydrolyzes alpha-D-glucose-1-phosphate (Glu1P) and has no activity with the beta form. {ECO:0000269|PubMed:15808744, ECO:0000269|PubMed:16990279}. EcoCyc product frame: EG11195-MONOMER. Genomic coordinates: 3876140-3876952. EcoCyc protein note: YidA is a promiscuous sugar phosphatase belonging to the superfamily of haloacid dehalogenase (HAD)-like hydrolases. Its preferred substrate is erythrose-4-phosphate . YidA selectively hydrolyzes α-D-glucose-1-phosphate and has no activity with the β form . The reaction proceeds via the canonical phosphomonoester hydrolase mechanism, which involves breakage of the P-O bond, not the C1-O bond . The phosphatase activity of YidA was first discovered in a high-throughput screen of purified proteins . Mutagenesis of the predicted catalytic Asp residue in YidA results in loss of phosphatase activity . YidA does not catalyze phosphoryl transfer to a sugar acceptor .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8Y5|protein.P0A8Y5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012086,ECOCYC:EG11195,GeneID:948204`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3876140-3876952:-; feature_type=gene
