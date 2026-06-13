---
entity_id: "gene.b1280"
entity_type: "gene"
name: "lapB"
source_database: "NCBI RefSeq"
source_id: "gene-b1280"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1280"
  - "lapB"
---

# lapB

`gene.b1280`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1280`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lapB (gene.b1280) is a gene entity. It encodes lapB (protein.P0AB58). Encoded protein function: FUNCTION: Modulates cellular lipopolysaccharide (LPS) levels by regulating LpxC, which is involved in lipid A biosynthesis. Regulates the proteolytic activity of FtsH towards LpxC by acting as an adapter protein which interacts with FtsH via its transmembrane helices while its cytoplasmic domain recruits LpxC for degradation by FtsH. May also coordinate assembly of proteins involved in LPS synthesis at the plasma membrane. {ECO:0000255|HAMAP-Rule:MF_00994, ECO:0000269|PubMed:24266962, ECO:0000269|PubMed:24722986, ECO:0000269|PubMed:33260377, ECO:0000269|PubMed:35931690}. EcoCyc product frame: EG12691-MONOMER. EcoCyc synonyms: yciM. Genomic coordinates: 1340558-1341727.

## Biological Role

Activated by rpoD (protein.P00579), rpoH (protein.P0AGB3).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AB58|protein.P0AB58]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=lapB; function=+
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=lapB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0004300,ECOCYC:EG12691,GeneID:944858`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1340558-1341727:+; feature_type=gene
