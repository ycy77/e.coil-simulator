---
entity_id: "gene.b1830"
entity_type: "gene"
name: "prc"
source_database: "NCBI RefSeq"
source_id: "gene-b1830"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1830"
  - "prc"
---

# prc

`gene.b1830`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1830`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

prc (gene.b1830) is a gene entity. It encodes prc (protein.P23865). Encoded protein function: FUNCTION: Involved in the cleavage of a C-terminal peptide of 11 residues from the precursor form of penicillin-binding protein 3 (PBP3). May be involved in protection of the bacterium from thermal and osmotic stresses. EcoCyc product frame: EG10760-MONOMER. EcoCyc synonyms: tsp. Genomic coordinates: 1912768-1914816. EcoCyc protein note: Early studies in E. coli K-12 identified various soluble serine proteases, including protease Re , later suggested to be identical with the periplasmic protease known as tail-specific protease (Tsp) encoded by prc (see ). Prc cleaves the C-terminal 11 residue peptide of EG10341-MONOMER "penicillin binding protein 3" to generate the mature protein . Prc binds to and degrades proteins that have been tagged with the quality control peptide sequence coded for by EG30100 "ssrA", indicative of a role in removing improperly translated proteins . Prc together with its adaptor protein CPLX0-8198 "NlpI", forms a proteolytic system that regulates peptidoglycan synthesis by degrading G7147-MONOMER "MepS", a murein endopeptidase that participates in expansion of the peptidoglycan sacculus during bacterial growth and morphogenesis (and further ). NlpI-Prc degrades EG10246-MONOMER . Prc binds NlpI with high affinity...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P23865|protein.P23865]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006090,ECOCYC:EG10760,GeneID:946096`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1912768-1914816:-; feature_type=gene
