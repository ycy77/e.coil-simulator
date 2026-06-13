---
entity_id: "gene.b1615"
entity_type: "gene"
name: "uidC"
source_database: "NCBI RefSeq"
source_id: "gene-b1615"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1615"
  - "uidC"
---

# uidC

`gene.b1615`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1615`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

uidC (gene.b1615) is a gene entity. It encodes uidC (protein.Q47706). Encoded protein function: FUNCTION: Enhances the activity of the UidB (GusB) glucuronide transporter, on its own however it has no transport activity. Glucuronide transport does not occur in strain K12 due to a variant at position 100 of the UidB (GusB, AC P0CE44, AC P0CE45) protein. {ECO:0000269|PubMed:15774881}. EcoCyc product frame: G6866-MONOMER. EcoCyc synonyms: gusC. Genomic coordinates: 1691586-1692851. EcoCyc protein note: The uidC gene is part of the uidABC operon. The gene products of uidB and uidC have been shown through expression studies and transport assays in a natural isolate of Escherichia coli, strain CE1, to be involved in secondary active transport of beta-glucuronides into the cell energized by the respiration-generated proton motive force. Further metabolism of the beta-glucuronides is performed by UidA. Membrane separation experiments find the UidC protein associated with the outer membrane. Expression of UidC alone from strain CE1 in strain KW1 (uid operon deletion) does not confer transport activity, but improves efficiency of transport by UidB by an unknown mechanism when the two are expressed simultaneously . In the Transporter Classification Database UidC (GusC) is a member of the Outer Membrane Porin (Opr) Family .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q47706|protein.Q47706]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005405,ECOCYC:G6866,GeneID:944820`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1691586-1692851:-; feature_type=gene
