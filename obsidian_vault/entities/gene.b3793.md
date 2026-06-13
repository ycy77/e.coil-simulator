---
entity_id: "gene.b3793"
entity_type: "gene"
name: "wzyE"
source_database: "NCBI RefSeq"
source_id: "gene-b3793"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3793"
  - "wzyE"
---

# wzyE

`gene.b3793`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3793`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

wzyE (gene.b3793) is a gene entity. It encodes wzyE (protein.P27835). Encoded protein function: FUNCTION: Probably involved in the polymerization of enterobacterial common antigen (ECA) trisaccharide repeat units. Required for the assembly of the phosphoglyceride-linked form of ECA (ECA(PG)) and the water-soluble cyclic form of ECA (ECA(CYC)). {ECO:0000269|PubMed:16199561}. EcoCyc product frame: FUC4NACTRANS-MONOMER. EcoCyc synonyms: rffT. Genomic coordinates: 3978601-3979953. EcoCyc protein note: The assembly of enterobacterial common antigen (ECA) occurs by a Wzx/Wzy-dependent pathway (see ). wzyE is located immediately downstream of wecF (encoding the 4-alpha-L-fucosyltransferase which catalyses the final step in biosythesis of an ECA trisaccharide) and is suggested to encode a polymerase involved in ECA polysaccharide chain elongation . WzyE is required for the assembly of glycerophosphatidyl-linked ECA (CPD-21605 ECAPG) and cyclic ECA (CPD0-2646 ECACYC) ; WzyE catalyses polymerization of repeat unit Und-P linked saccharides at the periplasmic face of the inner membrane via a 'block-transfer' mechanism with modulation of polysaccharide chain length dependent on EG11295-MONOMER WzzE. The lipid III flippase EG11486-MONOMER WzxE, ECA polymerase WzyE, and co-polymerase EG11295-MONOMER WzzE may function as a multiprotein complex...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P27835|protein.P27835]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012392,ECOCYC:EG11457,GeneID:948293`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3978601-3979953:+; feature_type=gene
