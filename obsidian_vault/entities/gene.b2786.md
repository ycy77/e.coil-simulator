---
entity_id: "gene.b2786"
entity_type: "gene"
name: "barA"
source_database: "NCBI RefSeq"
source_id: "gene-b2786"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2786"
  - "barA"
---

# barA

`gene.b2786`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2786`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

barA (gene.b2786) is a gene entity. It encodes barA (protein.P0AEC5). Encoded protein function: FUNCTION: Member of the two-component regulatory system UvrY/BarA involved in the regulation of carbon metabolism via the CsrA/CsrB regulatory system (PubMed:12193630, PubMed:12533459). Phosphorylates UvrY, probably via a four-step phosphorelay (PubMed:11022030). {ECO:0000269|PubMed:11022030, ECO:0000269|PubMed:12193630, ECO:0000269|PubMed:12533459}. EcoCyc product frame: MONOMER0-4299. EcoCyc synonyms: airS. Genomic coordinates: 2915057-2917813. EcoCyc protein note: Represents the Asp-718 phosphorylated form of BARA-MONOMER "BarA" - the sensor histidine kinase of the BarA/UvrY two-component signal transduction system. EcoCyc protein note: Represents the His-302 phosphorylated form of BARA-MONOMER "BarA" - the sensor histidine kinase of the BarA/UvrY two-component signal transduction system. EcoCyc protein note: Represents the His-861 phosphorylated form of BARA-MONOMER "BarA" - the sensor histidine kinase of the BarA/UvrY two-component signal transduction system.

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEC5|protein.P0AEC5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009131,ECOCYC:EG11367,GeneID:947255`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2915057-2917813:+; feature_type=gene
