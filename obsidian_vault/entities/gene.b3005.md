---
entity_id: "gene.b3005"
entity_type: "gene"
name: "exbD"
source_database: "NCBI RefSeq"
source_id: "gene-b3005"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3005"
  - "exbD"
---

# exbD

`gene.b3005`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3005`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

exbD (gene.b3005) is a gene entity. It encodes exbD (protein.P0ABV2). Encoded protein function: FUNCTION: Involved in the TonB-dependent energy-dependent transport of various receptor-bound substrates. EcoCyc product frame: EG10272-MONOMER. Genomic coordinates: 3150818-3151243. EcoCyc protein note: ExbD is a component of the energy transducing Ton system which functions to harness the energy of the proton motive force (pmf) at the cytoplasmic membrane to support active transport of iron-siderophore complexes and certain cofactors across the outer membrane. ExbD is an inner membrane protein ; topology analysis suggests that it contains a single transmembrane region with the N-terminus located in the cytoplasm and a larger C-terminal domain located in the periplasm . ExbD interacts with TonB and with ExbB and forms homodimers in vivo; ExbD and TonB interact through their periplasmic domains; ExbD-TonB interaction requires PMF . ExbD binds to the TonB "D-box" motif and this interaction is suggested to be critical for force transduction between the membranes . Over-expressed ExbBD purifies in multiple stoichiometries; the principle complex, ExbB4ExbD2, contains a TM region expected to consist of 14 TM helices (12 from ExbB and two from ExbD), a periplasmic domain comprised of the ExbD C-terminus and a cytoplasmic domain...

## Biological Role

Repressed by fur (protein.P0A9A9).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABV2|protein.P0ABV2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=exbD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0009866,ECOCYC:EG10272,GeneID:946345`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3150818-3151243:-; feature_type=gene
