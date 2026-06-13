---
entity_id: "gene.b4398"
entity_type: "gene"
name: "creB"
source_database: "NCBI RefSeq"
source_id: "gene-b4398"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4398"
  - "creB"
---

# creB

`gene.b4398`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4398`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

creB (gene.b4398) is a gene entity. It encodes creB (protein.P08368). Encoded protein function: FUNCTION: Member of the two-component regulatory system CreC/CreB involved in catabolic regulation. EcoCyc product frame: PHOSPHO-CREB. EcoCyc synonyms: yjjE, ORF2. Genomic coordinates: 4636007-4636696. EcoCyc protein note: CreB "Carbon source responsive response regulator," is a DNA-binding transcriptional dual regulator and belongs to the CreBC two-component system (TCS) , which controls genes involved in acetate and ribose metabolism, in the maltose regulon , in the pentose phosphate pathway , and genes which repair DNA damage associated with the replication fork . CreBC regulates the expression of cre regulon genes in response to a switch from complex to minimal medium . It is active when cells are fermenting glycolytic carbon sources. Induction of the cre regulon during pyruvate growth is entirely CreC dependent . CreBC is considered a global regulator that is positioned at the heart of metabolic control . CreB and CreC are part of the creABCD operon . CreB binds in vitro to a TTCACnnnnnnTTCAC sequence called the cre tag direct repeat, which stimulates the cre regulon . CreBC (TCS) is homologous (60-70%) with BrlAB of Aeromonas spp. at the amino acid level...

## Biological Role

Activated by rpoH (protein.P0AGB3).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P08368|protein.P08368]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=creB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0014428,ECOCYC:EG11218,GeneID:948922`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4636007-4636696:+; feature_type=gene
