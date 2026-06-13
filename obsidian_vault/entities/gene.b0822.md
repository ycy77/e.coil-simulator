---
entity_id: "gene.b0822"
entity_type: "gene"
name: "ybiV"
source_database: "NCBI RefSeq"
source_id: "gene-b0822"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0822"
  - "ybiV"
---

# ybiV

`gene.b0822`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0822`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybiV (gene.b0822) is a gene entity. It encodes ybiV (protein.P75792). Encoded protein function: FUNCTION: Catalyzes the hydrolysis of sugar phosphate to sugar and inorganic phosphate. Has a wide substrate specificity catalyzing the hydrolysis of ribose-5-phosphate, glucose-6-phosphate, fructose-1-phosphate, acetyl-phosphate, glycerol-1-phosphate, glycerol-2-phosphate, 2-deoxy-glucose-6-phosphate, mannose-6-phosphate and fructose-6-phosphate. Appears to have a low level of phosphotransferase activity using monophosphates as the phosphate donor. {ECO:0000269|PubMed:15657928, ECO:0000269|PubMed:15808744, ECO:0000269|PubMed:16990279}. EcoCyc product frame: G6425-MONOMER. Genomic coordinates: 859213-860028. EcoCyc protein note: YbiV is a sugar phosphatase belonging to the family of type II haloacid dehalogenase (HAD)-like hydrolases . It shows a low level of discrimination between its preferred substrates . In addition, YbiV appears to have a low level of phosphotransferase activity using monophosphates as the phosphate donor . The phosphatase activity of YbiV was also discovered in a high-throughput screen of purified proteins . Crystal structures of YbiV have been solved, and a catalytic mechanism was suggested . YbiV may exist as a homodimer in solution . Overexpression of YbiV in an engineered strain that converts pentoses to glucose increases the glucose yield .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75792|protein.P75792]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002807,ECOCYC:G6425,GeneID:945432`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:859213-860028:-; feature_type=gene
