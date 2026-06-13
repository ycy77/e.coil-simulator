---
entity_id: "gene.b2960"
entity_type: "gene"
name: "trmB"
source_database: "NCBI RefSeq"
source_id: "gene-b2960"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2960"
  - "trmB"
---

# trmB

`gene.b2960`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2960`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

trmB (gene.b2960) is a gene entity. It encodes trmB (protein.P0A8I5). Encoded protein function: FUNCTION: Catalyzes the formation of N(7)-methylguanine at position 46 (m7G46) in tRNA. {ECO:0000255|HAMAP-Rule:MF_01057, ECO:0000269|PubMed:12730187}. EcoCyc product frame: EG11779-MONOMER. EcoCyc synonyms: trmI, yggH. Genomic coordinates: 3102133-3102852. EcoCyc protein note: tRNA m7G46 methyltransferase (TrmB) catalyzes methylation of N(7) of the G46 nucleotide in the variable loop of tRNAs . tRNAs carry multiple modifications, often in nearby nucleotide residues. TrmB methyltransferase and tRNA binding activity is not influenced by prior tRNA modification in the T loop . Depending on the specific tRNA, lack of prior m7G modification at position 46 reduces 3-(3-amino-3-carboxypropyl)uridine (acp3U) modification at position 47 by G7349-MONOMER TapT . Based on a homology model of TrmB, potential catalytic residues have been mutagenized; kinetic analysis of the mutant enzymes showed a significant reduction in methyltransferase activity for most mutants . Crystal structures of TrmB alone and in complexes with SAM and SAH have been solved, showing that the enzyme adopts a modified Rossmann fold . TrmB has a relatively low affinity for tRNA, with a KD of about 6 μM in the absence of its cofactor SAM , but the affinity is significantly increased in the presence of SAM ( (KD of ~2 μM)...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8I5|protein.P0A8I5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009714,ECOCYC:EG11779,GeneID:947448`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3102133-3102852:-; feature_type=gene
