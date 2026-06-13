---
entity_id: "gene.b1059"
entity_type: "gene"
name: "solA"
source_database: "NCBI RefSeq"
source_id: "gene-b1059"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1059"
  - "solA"
---

# solA

`gene.b1059`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1059`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

solA (gene.b1059) is a gene entity. It encodes solA (protein.P40874). Encoded protein function: FUNCTION: Catalyzes the oxidative demethylation of N-methyl-L-tryptophan. Can also use other N-methyl amino acids, including sarcosine, which, however, is a poor substrate. EcoCyc product frame: SARCOX-MONOMER. Genomic coordinates: 1119468-1120586. EcoCyc protein note: The solA gene product has N-methyltryptophan oxidase (MTOX) activity. Despite significant similarity to the Bacillus sp. sarcosine oxidase, the enzyme has comparatively little sarcosine oxidase activity . MTOX can catalyze the demethylation of various N-methyl amino acids, but has a preference for N-methyltryptophan . The metabolic role and physiological substrate for the enzyme are unknown. Cys308 is the covalent attachment site for FAD . Studies of the reaction mechanism are consistent with a modified ping pong mechanism and exclude the formation of a covalent adduct intermediate . Lys259 is the site of oxygen activation and also plays a role in holoenzyme biosynthesis and N-methyltryptophan oxidation. The enzyme contains separate active sites for N-methyltryptophan oxidation and oxygen reduction on opposite faces of the flavin ring . A crystal structure of SolA has been solved at 3.2 Å resolution, identifying Thr239 as a key residue for substrate side chain recognition...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P40874|protein.P40874]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003590,ECOCYC:G6556,GeneID:944983`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1119468-1120586:-; feature_type=gene
