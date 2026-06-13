---
entity_id: "gene.b4389"
entity_type: "gene"
name: "radA"
source_database: "NCBI RefSeq"
source_id: "gene-b4389"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4389"
  - "radA"
---

# radA

`gene.b4389`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4389`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

radA (gene.b4389) is a gene entity. It encodes radA (protein.P24554). Encoded protein function: FUNCTION: DNA-dependent ATPase involved in processing of recombination intermediates, plays a role in repairing DNA breaks. Stimulates the branch migration of RecA-mediated strand transfer reactions, allowing the 3' invading strand to extend heteroduplex DNA faster. Binds ssDNA in the presence of ADP but not other nucleotides, has ATPase activity that is stimulated by ssDNA and various branched DNA structures, but inhibited by SSB. Does not have RecA's homology-searching function (PubMed:26845522). Genetic experiments involving combination of radA mutations with mutations in recA, recB, recG, recJ, recQ, ruvA and ruvC show it plays a role in recombination and recombinational repair, probably involving stabilizing or processing branched DNA or blocked replication forks. Is genetically synergistic to RecG and RuvABC (PubMed:12446634, PubMed:25484163). May be involved in recovery of genetic rearrangements during replication fork breakdown (PubMed:16904387). In combination with RadD is important in recovery from double-strand DNA breaks (DSB) (PubMed:25425430). {ECO:0000269|PubMed:12446634, ECO:0000269|PubMed:16904387, ECO:0000269|PubMed:25425430, ECO:0000269|PubMed:25484163, ECO:0000269|PubMed:26845522}. EcoCyc product frame: EG11296-MONOMER. EcoCyc synonyms: sms...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P24554|protein.P24554]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0014395,ECOCYC:EG11296,GeneID:948912`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4625912-4627294:+; feature_type=gene
