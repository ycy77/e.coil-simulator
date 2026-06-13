---
entity_id: "gene.b2011"
entity_type: "gene"
name: "sbcB"
source_database: "NCBI RefSeq"
source_id: "gene-b2011"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2011"
  - "sbcB"
---

# sbcB

`gene.b2011`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2011`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sbcB (gene.b2011) is a gene entity. It encodes sbcB (protein.P04995). Encoded protein function: FUNCTION: Degrades single-stranded DNA (ssDNA) in a highly processive manner (PubMed:23609540). Also functions as a DNA deoxyribophosphodiesterase that releases deoxyribose-phosphate moieties following the cleavage of DNA at an apurinic/apyrimidinic (AP) site by either an AP endonuclease or AP lyase (PubMed:1329027). {ECO:0000269|PubMed:1329027, ECO:0000269|PubMed:23609540}. EcoCyc product frame: EG10926-MONOMER. EcoCyc synonyms: exoI, rmuA, cpeA, xonA. Genomic coordinates: 2082756-2084183. EcoCyc protein note: Exonuclease I (ExoI) hydrolyzes DNA through its 3'-5' exonuclease acitivity. ExoI is specific for single-stranded DNA requiring a 3'-hydroxyl group. ExoI removes 5'-mononucleotides one at a time leaving the 5' dinucleotide intact . ExoI exhibits DNA deoxyribophosphodiesterase activity . ExoI releases deoxyribose-5-phosphate from DNA after endonuclease IV incision at apurinic/apyrimidinic (AP) sites, and 4-hydroxy-2-pentenal-5-phosphate after incision by endonuclease III at AP sites . ExoI activity has been shown to suppress illegitimate recombination by RecE . Exonuclease I activity is stimulated by EG10976-MONOMER. SSB binds to mutliple sites on exonuclease I, recruiting the enzyme to substrate and thus enhancing its activity...

## Enriched Pathways

- `eco03430` Mismatch repair (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P04995|protein.P04995]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006686,ECOCYC:EG10926,GeneID:946529`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2082756-2084183:+; feature_type=gene
