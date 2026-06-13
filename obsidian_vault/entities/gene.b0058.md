---
entity_id: "gene.b0058"
entity_type: "gene"
name: "rluA"
source_database: "NCBI RefSeq"
source_id: "gene-b0058"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0058"
  - "rluA"
---

# rluA

`gene.b0058`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0058`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rluA (gene.b0058) is a gene entity. It encodes rluA (protein.P0AA37). Encoded protein function: FUNCTION: Dual specificity enzyme that catalyzes the synthesis of pseudouridine from uracil-746 in 23S ribosomal RNA and from uracil-32 in the anticodon stem and loop of transfer RNAs. {ECO:0000269|PubMed:10383384, ECO:0000269|PubMed:7493321}. EcoCyc product frame: EG12609-MONOMER. EcoCyc synonyms: yabO. Genomic coordinates: 59687-60346. EcoCyc protein note: RluA is the pseudouridine synthase that catalyzes formation of pseudouridine at position 746 in 23S rRNA and at position 32 in tRNAPhe . In vitro, the enzyme acts on free 23S rRNA fragments (bases 1-847) and tRNAPhe . Synthetic anticodon stem-loop containing RNAs are substrates of the enzyme . RNA containing 5-fluorouridine forms a covalent complex with and inhibits RluA stoichiometrically . The chemical fate of the complex has been probed using kinetic and labelling studies . Pre-steady-state kinetic analysis showed that at low RluA concentrations, substrate binding is rate-limiting, while at higher enzyme concentrations, catalysis is the rate-limiting step . A crystal structure of RluA bound to substrate RNA has been solved at 2.05 Å resolution. The enzyme induces significant reorganization of the RNA stem-loop structure, which may contribute to sequence recognition...

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AA37|protein.P0AA37]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rluA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000196,ECOCYC:EG12609,GeneID:946262`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:59687-60346:-; feature_type=gene
