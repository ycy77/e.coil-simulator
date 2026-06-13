---
entity_id: "gene.b4291"
entity_type: "gene"
name: "fecA"
source_database: "NCBI RefSeq"
source_id: "gene-b4291"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4291"
  - "fecA"
---

# fecA

`gene.b4291`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4291`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fecA (gene.b4291) is a gene entity. It encodes fecA (protein.P13036). Encoded protein function: FUNCTION: FecA is the outer membrane receptor protein in the Fe(3+) dicitrate transport system. EcoCyc product frame: EG10286-MONOMER. Genomic coordinates: 4514353-4516677. EcoCyc protein note: FecA is an outer membrane (OM) protein which mediates the citrate dependent import of ferric iron; FecA mediated transport across the OM is energized by the inner membrane proton gradient; energy transduction is facilitated by the CPLX0-1923 (reviewed in ). FecA also signals the extracellular presence of iron to the FecR/FecI anti-sigma factor/sigma factor pair in the Fec signaling pathway. The outer membrane protein, FecA, is expressed under iron-limiting growth conditions in the presence of citrate . fecA forms an operon with fecBCDE encoding a ferric dicitrate ABC transporter; the operon responds to ferric citrate induction and Fur-Fe2+ repression...

## Biological Role

Repressed by fur (protein.P0A9A9). Activated by fecI (protein.P23484).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P13036|protein.P13036]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P23484|protein.P23484]] `RegulonDB` `C` - sigma=sigma19; target=fecA; function=+
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `C` - regulator=Fur; target=fecA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0014067,ECOCYC:EG10286,GeneID:946427`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4514353-4516677:-; feature_type=gene
