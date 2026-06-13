---
entity_id: "gene.b4385"
entity_type: "gene"
name: "hipH"
source_database: "NCBI RefSeq"
source_id: "gene-b4385"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4385"
  - "hipH"
---

# hipH

`gene.b4385`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4385`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hipH (gene.b4385) is a gene entity. It encodes yjjJ (protein.P39410). Encoded protein function: FUNCTION: Toxic when overexpressed in E.coli, leading to long filamentous cells. The toxic effect is neutralized by non-cognate antitoxin HipB (PubMed:28430938). Does not seem to inhibit DNA, RNA or protein synthesis, and unlike paralogous toxin HipA its toxic activity is not counteracted by overexpression of GltX (PubMed:28430938). Binds DNA (PubMed:28430938). Might be a protein kinase (By similarity). {ECO:0000250|UniProtKB:P23874, ECO:0000269|PubMed:28430938}. EcoCyc product frame: MONOMER0-4564. EcoCyc synonyms: yjjJ. Genomic coordinates: 4621769-4623100. EcoCyc protein note: HipH is a serine/threonine kinase similar to the toxin EG10443-MONOMER HipA and is toxic upon overexpression, which leads to formation of elongated cells and a reduced number of colony-forming units after plating . Consequences of HipH induction include arrest of cell division and DNA segregation, increased glycogen synthesis, and altered ribosome assembly. Unlike HipA, HipH has no direct impact on antibiotic tolerance . The primary protein substrates of HipH are the EG10889-MONOMER (RpmE), which is phosphorylated at Ser69, and the CPLX0-7956 (CsrA), which is phosphorylated at Ser56. HipH also has autophosphorylase activity (phosphorylating Ser200, Ser201 and Ser217)...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39410|protein.P39410]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0014383,ECOCYC:EG12342,GeneID:944883`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4621769-4623100:+; feature_type=gene
