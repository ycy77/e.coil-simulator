---
entity_id: "gene.b1787"
entity_type: "gene"
name: "yeaK"
source_database: "NCBI RefSeq"
source_id: "gene-b1787"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1787"
  - "yeaK"
---

# yeaK

`gene.b1787`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1787`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yeaK (gene.b1787) is a gene entity. It encodes proXp-y (protein.P64483). Encoded protein function: FUNCTION: An aminoacyl-tRNA editing enzyme that deacylates Ser-tRNA and/or Thr-tRNA mischarged by lysyl-tRNA synthetase (LysRS), threonyl-tRNA synthetase (ThrRS), seryl-tRNA synthetase (SerRS), alanyl-tRNA synthetase (AlaRS), valyl-tRNA synthetase (ValRS) and isoleucyl-tRNA synthetase (IleRS) in vitro. Also deacylates mischarged Hse-tRNA(Lys) and Hse-tRNA(Ser), and cognate Ser-tRNA(Ser) and Thr-tRNA(Thr) in vitro. The presence of cognate ThrRS abolishes the Thr-tRNA(Thr) deacylase activity, hence this activity is not applicable physiologically. Not able to remove the amino acid moiety from cognate Val-tRNA(Val), Ile-tRNA(Ile), Lys-tRNA(Lys), Ala-tRNA(Ala) or Pro-tRNA(Pro), or from incorrectly charged Ala-tRNA(Pro), Cys-tRNA(Pro) or Leu-tRNA(Pro) in vitro. May be required in vivo to prevent mistranslation and to maintain growth when the error prone stress-inducible lysyl-tRNA synthetase (LysU) is expressed under environmental pressure. {ECO:0000269|PubMed:25918376}. EcoCyc product frame: G6973-MONOMER. Genomic coordinates: 1873574-1874077. EcoCyc protein note: The YeaK protein ("ProXp-ST1") has aminoacyl-tRNA editing activity...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64483|protein.P64483]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005945,ECOCYC:G6973,GeneID:946303`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1873574-1874077:+; feature_type=gene
