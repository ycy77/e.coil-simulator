---
entity_id: "gene.b0172"
entity_type: "gene"
name: "frr"
source_database: "NCBI RefSeq"
source_id: "gene-b0172"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0172"
  - "frr"
---

# frr

`gene.b0172`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0172`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

frr (gene.b0172) is a gene entity. It encodes frr (protein.P0A805). Encoded protein function: FUNCTION: Responsible for the release of ribosomes from messenger RNA at the termination of protein biosynthesis. May increase the efficiency of translation by recycling ribosomes from one round of translation to another. EcoCyc product frame: EG10335-MONOMER. EcoCyc synonyms: rrf. Genomic coordinates: 192872-193429. EcoCyc protein note: Ribosome recycling factor (RRF) recycles the ribosome upon translation termination . RRF, release factor RF3, and elongation factor EF-G are involved in this recycling process . At termination, RRF and EF-G catalyze release of the 50S ribosomal subunit from the 70S complex, a GTPase-dependent process ; EF-G acts to release RRF from the ribosome . Release factor RF1 inhibits RRF activity . RRF with EF-2 and RF3 increase dissociation of peptidyl-tRNA from the ribosome . RRF stimulates translation , inhibits amber readthrough , and enables correct translation initiation of a translationally coupled open reading frame . Upon inactivation of a temperature-sensitive allele of rrf in vivo, the ribosome re-initiates translation downstream of the stop codon . E. coli growing exponentially in rich media contain approximately 16,500 molecules of RRF per cell . RRF has been structurally characterized . Crystal structures and NMR studies are presented...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A805|protein.P0A805]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000588,ECOCYC:EG10335,GeneID:946122`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:192872-193429:+; feature_type=gene
