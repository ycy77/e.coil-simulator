---
entity_id: "gene.b0408"
entity_type: "gene"
name: "secD"
source_database: "NCBI RefSeq"
source_id: "gene-b0408"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0408"
  - "secD"
---

# secD

`gene.b0408`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0408`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

secD (gene.b0408) is a gene entity. It encodes secD (protein.P0AG90). Encoded protein function: FUNCTION: Part of the Sec protein translocase complex. Interacts with the SecYEG preprotein conducting channel. SecDF uses the proton motive force (PMF) to complete protein translocation after the ATP-dependent function of SecA. The large periplasmic domain is thought to have a base and head domain joined by a hinge; movement of the hinge may be coupled to both proton transport and protein export, with the head domain capturing substrate, and a conformational change preventing backward movement and driving forward movement. Expression of V.alginolyticus SecD and SecF in E.coli confers Na(+)-dependent protein export, strongly suggesting SecDF functions via cation-coupled protein translocation. {ECO:0000269|PubMed:21562494}. EcoCyc product frame: SECD. Genomic coordinates: 427647-429494. EcoCyc protein note: SecD is an inner membrane protein that is part of the heterotrimeric Sec translocon accessory complex. Early studies characterized the secD locus, composed of yajC-secD-secF, and implicated the products of secD and secF in protein export...

## Enriched Pathways

- `eco03060` Protein export (KEGG)
- `eco03070` Bacterial secretion system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AG90|protein.P0AG90]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001417,ECOCYC:EG10938,GeneID:949133`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:427647-429494:+; feature_type=gene
