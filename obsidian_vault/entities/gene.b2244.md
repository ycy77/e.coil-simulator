---
entity_id: "gene.b2244"
entity_type: "gene"
name: "rpnE"
source_database: "NCBI RefSeq"
source_id: "gene-b2244"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2244"
  - "rpnE"
---

# rpnE

`gene.b2244`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2244`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rpnE (gene.b2244) is a gene entity. It encodes yfaD (protein.P37014). Encoded protein function: FUNCTION: Upon expression has no effect on RecA-independent DNA recombination, cell viability or DNA damage (PubMed:28096446). {ECO:0000269|PubMed:28096446}. EcoCyc product frame: EG12323-MONOMER. EcoCyc synonyms: yfaD. Genomic coordinates: 2356904-2357803. EcoCyc protein note: RpnE is one of five proteins in E. coli that belong to the "transposase_31" family , which is distantly related to the PD-(D/E)XK nuclease superfamily . Unlike the other E. coli members of the family, overexpression of rpnE does not increase RecA-independent recombination, reduce cell viability, or induce expression of the DNA damage-inducible gene dinD . RpnE: "inactive recombination-promoting nuclease-like protein E"

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37014|protein.P37014]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007429,ECOCYC:EG12323,GeneID:946737`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2356904-2357803:+; feature_type=gene
