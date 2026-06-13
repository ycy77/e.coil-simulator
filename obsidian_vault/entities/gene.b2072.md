---
entity_id: "gene.b2072"
entity_type: "gene"
name: "pphC"
source_database: "NCBI RefSeq"
source_id: "gene-b2072"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2072"
  - "pphC"
---

# pphC

`gene.b2072`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2072`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pphC (gene.b2072) is a gene entity. It encodes pphC (protein.P76395). Encoded protein function: FUNCTION: PP2C-like phosphatase that can dephosphorylate YegI. In vitro, can hydrolyze p-nitrophenyl phosphate (pNPP) to p-nitrophenol. {ECO:0000269|PubMed:29967116}. EcoCyc product frame: G7111-MONOMER. EcoCyc synonyms: yegK. Genomic coordinates: 2151711-2152472. EcoCyc protein note: PphC is a Mn2+-dependent protein phosphatase 2C (PP2C)-like protein-serine/threonine phosphatase . Both the protein sequence and the genome context differs between the otherwise closely related K-12 and B strains of E. coli. The PphC protein sequences are 93% identical. While the E. coli B REL606 genome encodes the YegI protein kinase immediatedly downstream of PphC, the two ORFs are separated by the divergently transcribed yegJ in E. coli K-12. It is notable that in long-term evolution experiments performed with E. coli B REL606, mutations in yegI have been found repeatedly. The E. coli B REL606 PphC was shown to dephosphorylate autophosphorylated YegI. The physiological role of the YegI/PphC kinase/phosphatase pair is so far unknown . PphC: "protein phosphatase C"

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76395|protein.P76395]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006865,ECOCYC:G7111,GeneID:947269`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2151711-2152472:-; feature_type=gene
