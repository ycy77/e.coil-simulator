---
entity_id: "gene.b1833"
entity_type: "gene"
name: "letA"
source_database: "NCBI RefSeq"
source_id: "gene-b1833"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1833"
  - "letA"
---

# letA

`gene.b1833`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1833`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

letA (gene.b1833) is a gene entity. It encodes letA (protein.P0AD03). Encoded protein function: FUNCTION: Could be part, together with LetB, of a system that transports lipids between the inner membrane and the outer membrane (Probable). Contributes to membrane integrity (PubMed:27795327). {ECO:0000269|PubMed:27795327, ECO:0000305|PubMed:32359438}. EcoCyc product frame: G7006-MONOMER. EcoCyc synonyms: yebS. Genomic coordinates: 1916258-1917541. EcoCyc protein note: LetA is an inner membrane protein with six transmembrane regions . letAB, pqiABC and ABC-45-CPLX "mlaFEDCB" are related loci; letAB (and pqiABC) are predicted to encode inter-membrane transport pathways that contribute to membrane integrity; simultaneous deletion of letAB and pqiABC in a ΔmlaD background increases sensitivity to EDTA and SDS; the substrate for transport is not known (see also ). letA shows differential codon adaptation, resulting in differential translation efficiency signatures, in thermophilic microbes. It was therefore predicted to play a role in the heat shock response. A letA deletion mutant was shown to be more sensitive than wild-type specifically to heat shock, but not other stresses . A letA'-'lacZ fusion is induced in cells that produce truncated lipopolysaccharide or have other membrane defects . letA: lipophilic envelope-spanning tunnel

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AD03|protein.P0AD03]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006098,ECOCYC:G7006,GeneID:946353`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1916258-1917541:+; feature_type=gene
