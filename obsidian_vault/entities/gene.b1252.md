---
entity_id: "gene.b1252"
entity_type: "gene"
name: "tonB"
source_database: "NCBI RefSeq"
source_id: "gene-b1252"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1252"
  - "tonB"
---

# tonB

`gene.b1252`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1252`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tonB (gene.b1252) is a gene entity. It encodes tonB (protein.P02929). Encoded protein function: FUNCTION: Interacts with outer membrane receptor proteins that carry out high-affinity binding and energy dependent uptake into the periplasmic space of specific substrates such as cobalamin, and various iron compounds (such as iron dicitrate, enterochelin, aerobactin, etc.). In the absence of TonB these receptors bind their substrates but do not carry out active transport. TonB also interacts with some colicins and is involved in the energy-dependent, irreversible steps of bacteriophages phi 80 and T1 infection. It could act to transduce energy from the cytoplasmic membrane to specific energy-requiring processes in the outer membrane, resulting in the release into the periplasm of ligands bound by these outer membrane proteins. Implicated in hydroxy radical-mediated cell death induced by hydroxyurea treatment (PubMed:20005847). {ECO:0000269|PubMed:20005847}. EcoCyc product frame: EG11012-MONOMER. EcoCyc synonyms: T1rec, exbA. Genomic coordinates: 1311089-1311808. EcoCyc protein note: TonB is a component of the energy transducing Ton system which functions to harness the energy of the proton motive force (pmf) at the cytoplasmic membrane to support active transport of iron-siderophore complexes and vitamin B12 across the outer membrane...

## Biological Role

Repressed by fur (protein.P0A9A9). Activated by rpoD (protein.P00579), fur (protein.P0A9A9).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P02929|protein.P02929]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=tonB; function=+
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=tonB; function=-+
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=tonB; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0004196,ECOCYC:EG11012,GeneID:945843`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1311089-1311808:+; feature_type=gene
