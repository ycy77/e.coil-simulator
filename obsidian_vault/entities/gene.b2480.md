---
entity_id: "gene.b2480"
entity_type: "gene"
name: "bcp"
source_database: "NCBI RefSeq"
source_id: "gene-b2480"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2480"
  - "bcp"
---

# bcp

`gene.b2480`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2480`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

bcp (gene.b2480) is a gene entity. It encodes bcp (protein.P0AE52). Encoded protein function: FUNCTION: Thiol-specific peroxidase that catalyzes the reduction of hydrogen peroxide and organic hydroperoxides to water and alcohols, respectively. Plays a role in cell protection against oxidative stress by detoxifying peroxides and as sensor of hydrogen peroxide-mediated signaling events. {ECO:0000269|PubMed:21910476}. EcoCyc product frame: EG10108-MONOMER. Genomic coordinates: 2600478-2600948. EcoCyc protein note: Bcp is a RED-THIOREDOXIN-MONOMER-dependent thiol peroxidase that belongs to the family of atypical 2-Cys peroxidases . The enzyme can utilize a variety of peroxides and reducing substrates, including Trx1, Trx2, Grx1, and Grx3. The redox potential of Bcp is very high, at -145.9 mV . The reaction mechanism has been investigated. Utilizing an atypical two-cysteine peroxiredoxin pathway, a sulfenic acid is transiently formed on Cys45, followed by formation of an intramolecular disulfide bond between Cys45 and Cys50. This oxidized form of Bcp is a substrate for reduction by thioredoxin. In a C50S mutant, the sulfenic acid intermediate is resolved by formation of an intermolecular disulfide bond . Both the oxidized and the reduced form of the Bcp protein is monomeric in solution . A Cys45 mutant loses all catalytic activity...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AE52|protein.P0AE52]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008171,ECOCYC:EG10108,GeneID:946949`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2600478-2600948:+; feature_type=gene
