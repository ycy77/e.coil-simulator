---
entity_id: "gene.b3042"
entity_type: "gene"
name: "ubiK"
source_database: "NCBI RefSeq"
source_id: "gene-b3042"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3042"
  - "ubiK"
---

# ubiK

`gene.b3042`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3042`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ubiK (gene.b3042) is a gene entity. It encodes ubiK (protein.Q46868). Encoded protein function: FUNCTION: Required for efficient ubiquinone (coenzyme Q) biosynthesis under aerobic conditions (PubMed:28559279, PubMed:30686758). UbiK is probably an accessory factor of Ubi enzymes and facilitates ubiquinone biosynthesis by acting as an assembly factor, a targeting factor, or both (PubMed:28559279). Dispensable for ubiquinone biosynthesis under anaerobiosis (PubMed:28559279). {ECO:0000269|PubMed:28559279, ECO:0000269|PubMed:30686758}. EcoCyc product frame: G7582-MONOMER. EcoCyc synonyms: yqiC. Genomic coordinates: 3184840-3185130. EcoCyc protein note: UbiK is an accessory factor in ubiquinone biosynthesis that is part of the Ubi complex metabolon . UbiK interacts directly with the C terminus of UbiJ; the isolated proteins appear to form a 2:1 UbiK:UbiJ heterotrimer that is able to bind palmitoleate , ubiquinone-8, 2-octaprenylphenol, and C6-demethoxy-ubiquinone-8 . Purified UbiK homotrimerizes . UbiK predominantly localizes to the membrane fraction, but can also be found in the cytosol. The seven ubiquinone biosynthesis proteins UbiE, UbiF, UbiG, UbiH, UbiI, UbiJ, and UbiK form a 1 MDa complex in the cytosol . A ubiK mutant contains 18% of the wild type level of ubiquinone and accumulates octaprenylphenol...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46868|protein.Q46868]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009987,ECOCYC:G7582,GeneID:947524`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3184840-3185130:+; feature_type=gene
