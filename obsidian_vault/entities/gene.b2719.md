---
entity_id: "gene.b2719"
entity_type: "gene"
name: "hycG"
source_database: "NCBI RefSeq"
source_id: "gene-b2719"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2719"
  - "hycG"
---

# hycG

`gene.b2719`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2719`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hycG (gene.b2719) is a gene entity. It encodes hycG (protein.P16433). Encoded protein function: Formate hydrogenlyase subunit 7 (FHL subunit 7) (Hydrogenase-3 component G) EcoCyc product frame: HYCG-MONOMER. EcoCyc synonyms: hevG. Genomic coordinates: 2843443-2844210. EcoCyc protein note: The hycBCDEFG genes in E. coli K-12 encode the hydrogenase component (hydrogenase 3) of the formate hydrogenlyase complex. HycG has similarity to small subunits of hydrogenases . HycG is absent in extracts of a slyD mutant strain grown anaerobically in the absence of nickel; however, this phenotype was restored upon addition of nickel to the growth medium . The HycG protein was undetectable in a hypA mutant and a hypA slyD double mutant .

## Biological Role

Activated by modE (protein.P0A9G8), fhlA (protein.P19323), rpoN (protein.P24255).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P16433|protein.P16433]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0A9G8|protein.P0A9G8]] `RegulonDB` `S` - regulator=ModE; target=hycG; function=+
- `activates` <-- [[protein.P19323|protein.P19323]] `RegulonDB` `S` - regulator=FhlA; target=hycG; function=+
- `activates` <-- [[protein.P24255|protein.P24255]] `RegulonDB` `S` - sigma=sigma54; target=hycG; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008936,ECOCYC:EG10480,GeneID:947191`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2843443-2844210:-; feature_type=gene
