---
entity_id: "gene.b1582"
entity_type: "gene"
name: "ynfA"
source_database: "NCBI RefSeq"
source_id: "gene-b1582"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1582"
  - "ynfA"
---

# ynfA

`gene.b1582`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1582`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ynfA (gene.b1582) is a gene entity. It encodes ynfA (protein.P76169). Encoded protein function: UPF0060 membrane protein YnfA EcoCyc product frame: G6840-MONOMER. Genomic coordinates: 1655347-1655673. EcoCyc protein note: YnfA is predicted to be an inner membrane protein with four transmembrane domains; experimental data suggests the C-terminus is located in the periplasm . YnfA may be a dual-topology protein which forms an antiparallel homodimer or higher order oligomer within the membrane; the protein has very weak topology bias and the C-terminal orientation of the protein is highly sensitive to charge mutations . A ynfA knockout mutant (ΔynfA::kan) exhibits a 'glycogen-excess' phenotype, that is, knockout cells accumulate significantly more glycogen than willd type upon entering stationary phase when an excess of carbon source is available . In the Transporter Classification Database YnfA is a member of the Drug/Metabolite Transporter (DMT) superfamily.

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76169|protein.P76169]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=ynfA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005279,ECOCYC:G6840,GeneID:946125`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1655347-1655673:-; feature_type=gene
