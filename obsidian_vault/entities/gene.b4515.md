---
entity_id: "gene.b4515"
entity_type: "gene"
name: "cydX"
source_database: "NCBI RefSeq"
source_id: "gene-b4515"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4515"
  - "cydX"
---

# cydX

`gene.b4515`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4515`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cydX (gene.b4515) is a gene entity. It encodes cydX (protein.P56100). Encoded protein function: FUNCTION: Required for correct functioning of cytochrome bd-I oxidase. This protein and AppX may have some functional overlap. EcoCyc product frame: MONOMER0-2663. EcoCyc synonyms: ybgT. Genomic coordinates: 774196-774309. EcoCyc protein note: CydX is small, noncatalytic, single transmembrane, accessory subunit of CYT-D-UBIOX-CPLX . A strain lacking cydX is slow growing in aerobic liquid culture and on plates and has increased sensitivity to β-mercaptoethanol; a wild-type phenotype can be restored when cydX is expressed from a plasmid . Membrane extracts from a strain lacking cydX display reduced levels of N N N' N'-tetramethyl-p-phenylenediamine (TMPD) oxidation . Preparations of CydAB lacking CydX do not contain the di-heme centre (hemes b595 and d) suggesting that CydX may be involved in the assembly or stabilisation of the di-heme active centre (further ). The cydX open reading frame contains a predicted transmembrane segment, and the protein can be found in the membrane fraction . Using a sucrose fractionation protocol CydX partitions into both the inner membrane and outer membrane fractions . Topology assays using GFP and PhoA fusion proteins suggest that CydX is oriented with the C-terminus in the cytoplasm...

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P56100|protein.P56100]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0285036,ECOCYC:G0-10441,GeneID:1450246`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:774196-774309:+; feature_type=gene
