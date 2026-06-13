---
entity_id: "gene.b0404"
entity_type: "gene"
name: "acpH"
source_database: "NCBI RefSeq"
source_id: "gene-b0404"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0404"
  - "acpH"
---

# acpH

`gene.b0404`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0404`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

acpH (gene.b0404) is a gene entity. It encodes acpH (protein.P21515). Encoded protein function: FUNCTION: Converts holo-ACP to apo-ACP by hydrolytic cleavage of the phosphopantetheine prosthetic group from ACP. {ECO:0000255|HAMAP-Rule:MF_01950, ECO:0000269|PubMed:16107329}. EcoCyc product frame: EG11095-MONOMER. EcoCyc synonyms: yajB. Genomic coordinates: 424337-424918. EcoCyc protein note: Acyl carrier protein (ACP) phosphodiesterase is responsible for the cleavage of PANTETHEINE-P (4'-PP) from ACP by hydrolysis of the phosphodiester linkage between 4'-PP and the hydroxyl group of a serine residue of the ACP apoprotein . This reaction requires divalent cations . Monomeric and trimeric forms of the purified protein are present in solution . AcpH is responsible for turnover of the ACP prosthetic group in vivo, but is not essential for growth. The physiological role of AcpH is unknown . Review:

## Enriched Pathways

- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P21515|protein.P21515]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001404,ECOCYC:EG11095,GeneID:949132`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:424337-424918:-; feature_type=gene
