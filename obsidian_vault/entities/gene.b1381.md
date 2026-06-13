---
entity_id: "gene.b1381"
entity_type: "gene"
name: "ydbH"
source_database: "NCBI RefSeq"
source_id: "gene-b1381"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1381"
  - "ydbH"
---

# ydbH

`gene.b1381`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1381`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydbH (gene.b1381) is a gene entity. It encodes ydbH (protein.P52645). Encoded protein function: FUNCTION: Involved in outer membrane lipid homeostasis (PubMed:34781743, PubMed:35226662, PubMed:38748582). Interacts with the outer membrane lipoprotein YnbE to form a functional protein bridge connecting the inner and outer membranes of the cell (PubMed:38748582). Likely transports phospholipids between the inner membrane and the outer membrane (PubMed:34781743, PubMed:35226662, PubMed:38748582). It would provide a bridge-like structure that protects phospholipids as they travel across the periplasm (PubMed:34781743). {ECO:0000269|PubMed:34781743, ECO:0000269|PubMed:35226662, ECO:0000269|PubMed:38748582}.; FUNCTION: TamB, YdbH and YhdP are redundant, but not equivalent, in performing an essential function for growth and maintaining lipid homeostasis in the outer membrane (PubMed:34781743). Any of these three proteins is sufficient for growth (PubMed:34781743). {ECO:0000269|PubMed:34781743}. EcoCyc product frame: G6703-MONOMER. Genomic coordinates: 1443051-1445690...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P52645|protein.P52645]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004623,ECOCYC:G6703,GeneID:945949`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1443051-1445690:+; feature_type=gene
