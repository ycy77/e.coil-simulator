---
entity_id: "gene.b2252"
entity_type: "gene"
name: "ais"
source_database: "NCBI RefSeq"
source_id: "gene-b2252"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2252"
  - "ais"
---

# ais

`gene.b2252`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2252`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ais (gene.b2252) is a gene entity. It encodes ais (protein.P45565). Encoded protein function: FUNCTION: Catalyzes the dephosphorylation of heptose(II) of the outer membrane lipopolysaccharide core. {ECO:0000250}. EcoCyc product frame: G7165-MONOMER. EcoCyc synonyms: pagH, pmrG. Genomic coordinates: 2365018-2365620. EcoCyc protein note: Expression of ais is significantly induced by addition of 0.2 mM ZnSO4 to the medium . The orthologous gene product of Salmonella enterica, PmrG, has been characterized as a periplasmic phosphatase that hydrolyzes the phosphate group at Hep(II) in the lipopolysaccharide core region and plays a role in resistance to Fe3+ and Al3+ . Ais: "aluminum inducible protein"

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P45565|protein.P45565]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007451,ECOCYC:G7165,GeneID:944945`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2365018-2365620:-; feature_type=gene
