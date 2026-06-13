---
entity_id: "gene.b3918"
entity_type: "gene"
name: "cdh"
source_database: "NCBI RefSeq"
source_id: "gene-b3918"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3918"
  - "cdh"
---

# cdh

`gene.b3918`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3918`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cdh (gene.b3918) is a gene entity. It encodes cdh (protein.P06282). Encoded protein function: CDP-diacylglycerol pyrophosphatase (EC 3.6.1.26) (CDP-diacylglycerol phosphatidylhydrolase) (CDP-diglyceride hydrolase) EcoCyc product frame: CDPDIGLYPYPHOSPHA-MONOMER. Genomic coordinates: 4109930-4110685. EcoCyc protein note: CDP-diacylglycerol pyrophosphatase (Cdh) catalyzes the hydrolysis of CDP-diacylglycerol . The enzyme can also catalyze the transfer of the CMP or dCMP moiety from (d)CDP-diacylglycerol to phosphate or a variety of phosphomonoesters . The true in vivo role of the enzyme is not known. Cdh is not required for lipid A biosynthesis in vivo. While the protein has UDP-2,3-diacylglucosamine pyrophosphatase activity in vitro and interferes with the assay of EG12666-MONOMER "LpxH" activity in crude cell extracts, the active site of the protein may be localized in the periplasm, explaining why it plays no role in the cytoplasmic steps of lipid A biosynthetic . were unable to detect Cdh protein and suggested that the protein is rapidly degraded in the cell. Cdh is predicted to be a bitopic inner membrane protein . cdh mutants contain elevated levels of CDP-diacylglycerol compared to wild type, but have no obvious growth defect . Cdh: CDP-diacylglycerol hydrolase

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P06282|protein.P06282]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012797,ECOCYC:EG10138,GeneID:948410`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4109930-4110685:+; feature_type=gene
