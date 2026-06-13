---
entity_id: "gene.b1045"
entity_type: "gene"
name: "ymdB"
source_database: "NCBI RefSeq"
source_id: "gene-b1045"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1045"
  - "ymdB"
---

# ymdB

`gene.b1045`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1045`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ymdB (gene.b1045) is a gene entity. It encodes ymdB (protein.P0A8D6). Encoded protein function: FUNCTION: Deacetylates O-acetyl-ADP ribose to yield ADP-ribose and free acetate (PubMed:21257746, PubMed:26481419). Down-regulates ribonuclease 3 (RNase III) activity. Acts by interacting directly with the region of the ribonuclease that is required for dimerization/activation (PubMed:19141481). Overexpression inhibits biofilm formation via an RNase III-independent pathway. This inhibition is RpoS-dependent (PubMed:24267348, PubMed:28582517). Overexpression also results in increased susceptibility to apramycin (PubMed:28034758, PubMed:28582517). {ECO:0000269|PubMed:19141481, ECO:0000269|PubMed:21257746, ECO:0000269|PubMed:24267348, ECO:0000269|PubMed:26481419, ECO:0000269|PubMed:28034758, ECO:0000269|PubMed:28582517}. EcoCyc product frame: G6550-MONOMER. Genomic coordinates: 1105820-1106353. EcoCyc protein note: YmdB is a macrodomain family protein with O-acetyl-ADP-ribose deacetylase activity . O-acetyl-ADP-ribose is produced by NAD+-dependent protein deacetylation. The YmdB protein inhibits the activity of CPLX0-3281 by interacting directly with the enzyme. Amino acids 120-140 in the catalytic region of RNase III are necessary for YmdB binding...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8D6|protein.P0A8D6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003549,ECOCYC:G6550,GeneID:946987`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1105820-1106353:+; feature_type=gene
