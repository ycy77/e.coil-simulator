---
entity_id: "gene.b2318"
entity_type: "gene"
name: "truA"
source_database: "NCBI RefSeq"
source_id: "gene-b2318"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2318"
  - "truA"
---

# truA

`gene.b2318`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2318`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

truA (gene.b2318) is a gene entity. It encodes truA (protein.P07649). Encoded protein function: FUNCTION: Formation of pseudouridine at positions 38, 39 and 40 in the anticodon stem and loop of transfer RNAs. {ECO:0000269|PubMed:17466622}. EcoCyc product frame: EG10454-MONOMER. EcoCyc synonyms: asuC, hisT, leuK. Genomic coordinates: 2434824-2435636. EcoCyc protein note: TruA is the tRNA pseudouridine synthase responsible for catalyzing pseudouridine formation in the anticodon loop of a subset of tRNAs . TruA-mediated pseudouridylation contributes to structural stability of this region of the tRNA and to reading frame maintenance by tRNALeu . Results from site-directed mutagenesis indicate that the reaction mechanism likely does not involve a covalent cysteine intermediate . Instead, the D60 residue is essential for catalytic activity , forming a covalent adduct that can undergo O-acyl hydrolytic cleavage to form the pseudouridine product . The Arg58 residue facilitates flipping of the substrate base into the active site . Pre-steady-state kinetic analysis showed that catalysis, but not substrate binding, is the rate-limiting step . Crystal structures of the enzyme have been solved . TruA is a dimer in the crystal as well as in solution . Modeling of the substrate recognition pathway indicates that the enzyme utilizes the intrinsic flexibility of the tRNA anticodon loop...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P07649|protein.P07649]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007657,ECOCYC:EG10454,GeneID:946793`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2434824-2435636:-; feature_type=gene
