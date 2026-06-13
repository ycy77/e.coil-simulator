---
entity_id: "gene.b1310"
entity_type: "gene"
name: "ycjN"
source_database: "NCBI RefSeq"
source_id: "gene-b1310"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1310"
  - "ycjN"
---

# ycjN

`gene.b1310`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1310`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ycjN (gene.b1310) is a gene entity. It encodes ycjN (protein.P76042). Encoded protein function: FUNCTION: Part of the ABC transporter complex YcjNOPV primarily involved in maltose uptake (PubMed:40721696). The transporter may also be involved in the uptake of glucosides (PubMed:40721696). In vitro, it actively transports ethidium bromide (EB) (PubMed:40721696). This subunit is the solute binding protein of the YcjNOPV transporter (Probable). {ECO:0000269|PubMed:40721696, ECO:0000305}. EcoCyc product frame: YCJN-MONOMER. Genomic coordinates: 1371909-1373201. EcoCyc protein note: YcjN is the predicted periplasmic binding protein of a putative ATP-binding cassette transporter (YcjNOPV) . YcjN is a verified lipoprotein according to unpublished data by S. Matsuyama et al. (cited in ). Over-expressed, purified YcjN is a lipoprotein that is predominantly diacylated at Cys-21; structural analysis indicates that the YcjN resembles sugar-binding proteins .

## Biological Role

Repressed by ycjW (protein.P77615).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76042|protein.P76042]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P77615|protein.P77615]] `RegulonDB` `S` - regulator=YcjW; target=ycjN; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004402,ECOCYC:G6648,GeneID:945696`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1371909-1373201:+; feature_type=gene
