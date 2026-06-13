---
entity_id: "gene.b1435"
entity_type: "gene"
name: "rlhA"
source_database: "NCBI RefSeq"
source_id: "gene-b1435"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1435"
  - "rlhA"
---

# rlhA

`gene.b1435`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1435`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rlhA (gene.b1435) is a gene entity. It encodes rlhA (protein.P76104). Encoded protein function: FUNCTION: Responsible for the formation of the 5-hydroxycytidine modification at the C2501 position (ho5C2501) of 23S rRNA. May be a Fe-S protein that catalyzes ho5C2501 formation using prephenate as a hydroxyl group donor. {ECO:0000269|PubMed:29069499}. EcoCyc product frame: G6746-MONOMER. EcoCyc synonyms: ydcP. Genomic coordinates: 1506781-1508742. EcoCyc protein note: RlhA is the enzyme responsible for generating the 5-hydroxycytidine modification at the C2501 position (ho5C2501) of 23S rRNA. In addition to RlhA, prephenate biosynthesis and iron-sulfur cluster biogenesis proteins are required for generating the ho5C2501 modification . RlhA co-fractionates with the 30S subunit of the ribosome in a sucrose gradient, similar to other 23S rRNA-modifying enzymes . A ΔrlhA mutant strain completely lacks the ho5C2501 modification of 23S rRNA. Mutations in the conserved cysteine residues 169, 176, 580 and 611 abolish the activity of RlhA . RlhA: "large subunit ribosomal RNA hydroxylation A"

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76104|protein.P76104]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004786,ECOCYC:G6746,GeneID:945993`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1506781-1508742:+; feature_type=gene
