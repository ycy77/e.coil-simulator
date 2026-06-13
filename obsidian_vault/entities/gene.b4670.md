---
entity_id: "gene.b4670"
entity_type: "gene"
name: "yjeV"
source_database: "NCBI RefSeq"
source_id: "gene-b4670"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4670"
  - "yjeV"
---

# yjeV

`gene.b4670`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4670`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yjeV (gene.b4670) is a gene entity. It encodes yjeV (protein.C1P621). Encoded protein function: Uncharacterized protein YjeV EcoCyc product frame: MONOMER0-2869. Genomic coordinates: 4392892-4392945. EcoCyc protein note: The YjeV open reading frame was first annotated by as ORF2.1, and expression of a LacZ fusion was detected. Later, expression of the small protein was detected during exponential phase .

## Biological Role

Repressed by dnaA (protein.P03004). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.C1P621|protein.C1P621]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=yjeV; function=+
- `represses` <-- [[protein.P03004|protein.P03004]] `RegulonDB` `S` - regulator=DnaA; target=yjeV; function=-

## External IDs

- `Dbxref:ECOCYC:G0-10642,GeneID:7751630`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4392892-4392945:+; feature_type=gene
