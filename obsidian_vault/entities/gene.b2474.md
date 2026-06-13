---
entity_id: "gene.b2474"
entity_type: "gene"
name: "tmcA"
source_database: "NCBI RefSeq"
source_id: "gene-b2474"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2474"
  - "tmcA"
---

# tmcA

`gene.b2474`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2474`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tmcA (gene.b2474) is a gene entity. It encodes tmcA (protein.P76562). Encoded protein function: FUNCTION: Catalyzes the formation of N(4)-acetylcytidine (ac(4)C) at the wobble position of tRNA(Met), by using acetyl-CoA as an acetyl donor and ATP (or GTP). It recognizes the wobble base of tRNA(Met), thus distinguishing between tRNA(Met) and the structurally similar tRNA(Ile2) (PubMed:18668122, PubMed:19322199). Could use an RNA helicase motor driven by ATP hydrolysis to deliver the wobble base of tRNA(Met) to the acetyltransferase domain of TmcA (Probable). {ECO:0000269|PubMed:18668122, ECO:0000269|PubMed:19322199, ECO:0000305|PubMed:19322199}.; FUNCTION: Also functions as a lysine 2-hydroxyisobutyryltransferase to regulate transcription. Can specifically catalyze the 2-hydroxyisobutyrylation (Khib) of the DNA-binding protein H-NS. Hydroxyisobutyrylation of H-NS decreases its DNA-binding activity, promotes the expression of acid-resistance genes and enhances bacterial survival under extreme acid stress. {ECO:0000269|PubMed:34903851}. EcoCyc product frame: G7297-MONOMER. EcoCyc synonyms: ypfI. Genomic coordinates: 2593844-2595859. EcoCyc protein note: tRNAMet cytidine acetyltransferase acetylates the wobble base C34 of the Elongation-tRNAMet...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76562|protein.P76562]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008150,ECOCYC:G7297,GeneID:946053`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2593844-2595859:-; feature_type=gene
