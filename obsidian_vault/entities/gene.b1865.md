---
entity_id: "gene.b1865"
entity_type: "gene"
name: "nudB"
source_database: "NCBI RefSeq"
source_id: "gene-b1865"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1865"
  - "nudB"
---

# nudB

`gene.b1865`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1865`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nudB (gene.b1865) is a gene entity. It encodes nudB (protein.P0AFC0). Encoded protein function: FUNCTION: Catalyzes the hydrolysis of dihydroneopterin triphosphate to dihydroneopterin monophosphate and pyrophosphate. Required for efficient folate biosynthesis. Can also hydrolyze nucleoside triphosphates with a preference for dATP. {ECO:0000269|PubMed:17698004, ECO:0000269|PubMed:8798731}. EcoCyc product frame: H2NEOPTERINP3PYROPHOSPHOHYDRO-MONOMER. EcoCyc synonyms: yebD, ntpA. Genomic coordinates: 1948180-1948632. EcoCyc protein note: Dihydroneopterin triphosphate diphosphatase (DHNTPase) catalyzes the hydrolytic removal of pyrophosphate from dihydroneopterin triphosphate (DHNTP) to yield dihydroneopterin phosphate. This is the committed step in the biosynthesis of folate . DHNTPase was also shown to have nucleotide pyrophosphohydrolase activity with various substrates , but the catalytic efficiency of the enzyme for DHNTP is over 7 times that for dATP. The severe reduction of folate levels in a nudB null mutant similarly argues that DHNTP is the physiological substrate of the enzyme . Crystal structures of NudB have been solved . The amino acid residues involved in coordinating four metal ions were identified, substrate binding was modeled , and a catalytic mechanism was proposed...

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFC0|protein.P0AFC0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006223,ECOCYC:EG11138,GeneID:946383`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1948180-1948632:-; feature_type=gene
