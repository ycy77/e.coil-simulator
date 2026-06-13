---
entity_id: "gene.b2392"
entity_type: "gene"
name: "mntH"
source_database: "NCBI RefSeq"
source_id: "gene-b2392"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2392"
  - "mntH"
---

# mntH

`gene.b2392`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2392`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mntH (gene.b2392) is a gene entity. It encodes mntH (protein.P0A769). Encoded protein function: FUNCTION: H(+)-stimulated, divalent metal cation uptake system. Involved in manganese and iron uptake. Can also transport cadmium, cobalt, zinc and to a lesser extent nickel and copper. Involved in response to reactive oxygen. {ECO:0000255|HAMAP-Rule:MF_00221, ECO:0000269|PubMed:10712688, ECO:0000269|PubMed:10844693}. EcoCyc product frame: YFEP-MONOMER. EcoCyc synonyms: mntA, yfeP. Genomic coordinates: 2511468-2512706. EcoCyc protein note: Early studies indicated that E. coli is able to accumulate manganese by means of a highly-specific active transport system . mntH encodes a proton-dependent divalent metal ion transporter with a marked preference for Mn2+; MntH does transport ferrous iron but this is not expected to be physiologically relevant; Cd2+ is an alternative, non-physiological substrate . ΔmntH cells grow normally, but their manganese content is minimal and activity of the manganese-dependent superoxide dismutase SUPEROX-DISMUTMN-CPLX SodA is virtually absent; manganese import is essential in H2O2-stressed cells; manganese is not an efficient scavenger of reactive oxygen species; manganese may substitute for iron in some metalloenzymes making them less vulnerable to to oxidative damage...

## Biological Role

Repressed by fur (protein.P0A9A9), mntR (protein.P0A9F1), nac (protein.Q47005). Activated by rpoD (protein.P00579), oxyR (protein.P0ACQ4).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A769|protein.P0A769]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=mntH; function=+
- `activates` <-- [[protein.P0ACQ4|protein.P0ACQ4]] `RegulonDB` `C` - regulator=OxyR; target=mntH; function=+
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=mntH; function=-
- `represses` <-- [[protein.P0A9F1|protein.P0A9F1]] `RegulonDB` `S` - regulator=MntR; target=mntH; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=mntH; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007889,ECOCYC:G7254,GeneID:946899`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2511468-2512706:-; feature_type=gene
