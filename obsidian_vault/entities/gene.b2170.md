---
entity_id: "gene.b2170"
entity_type: "gene"
name: "setB"
source_database: "NCBI RefSeq"
source_id: "gene-b2170"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2170"
  - "setB"
---

# setB

`gene.b2170`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2170`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

setB (gene.b2170) is a gene entity. It encodes setB (protein.P33026). Encoded protein function: FUNCTION: Involved in the efflux of sugars. The physiological role may be the detoxification of non-metabolizable sugar analogs. Can transport lactose and glucose. EcoCyc product frame: B2170-MONOMER. EcoCyc synonyms: yeiO. Genomic coordinates: 2263863-2265044. EcoCyc protein note: Early work characterized SetB as a sugar transporter; a later study implicated SetB in chromosome segregation. Inside-out membrane vesicles prepared from cells overexpressing setB accumulate significant amounts of lactose in a manner that is sensitive to the proton ionophore, carbonyl cyanide m-chlorophenylhydrazone (CCCP) . SetB can transport lactose and glucose but does not export the sugar analogs isopropyl β-D-thiogalactoside (IPTG) and 2-nitrophenyl-beta-D-thiogalactopyranoside (ONPTG); SetB has a narrower substrate specificity than B0070-MONOMER "SetA" . SetB has been implicated in chromosome segregation...

## Biological Role

Activated by FlhDC DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-3930).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33026|protein.P33026]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[complex.ecocyc.CPLX0-3930|complex.ecocyc.CPLX0-3930]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007184,ECOCYC:EG12034,GeneID:946673`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2263863-2265044:+; feature_type=gene
