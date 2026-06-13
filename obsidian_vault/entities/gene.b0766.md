---
entity_id: "gene.b0766"
entity_type: "gene"
name: "ybhA"
source_database: "NCBI RefSeq"
source_id: "gene-b0766"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0766"
  - "ybhA"
---

# ybhA

`gene.b0766`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0766`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybhA (gene.b0766) is a gene entity. It encodes ybhA (protein.P21829). Encoded protein function: FUNCTION: Catalyzes the dephosphorylation of pyridoxal-phosphate (PLP) (PubMed:15808744, PubMed:16990279, PubMed:39133002). Shows a broad substrate specificity in vitro, as it can hydrolyze a wide range of phosphorylated metabolites, including PLP, erythrose-4-phosphate (Ery4P), fructose-1,6-bis-phosphate (Fru1,6bisP), FMN, acetyl-phosphate, carbamoyl-phosphate, imido-di-phosphate and the artificial chromogenic susbtrate, p-nitrophenyl phosphate (pNPP) (PubMed:15808744, PubMed:16990279). Shows also weak activity with pyridoxine phosphate (PNP), but it plays only a minor role in PNP homeostasis (PubMed:39133002). {ECO:0000269|PubMed:15808744, ECO:0000269|PubMed:16990279, ECO:0000269|PubMed:39133002}. EcoCyc product frame: EG11239-MONOMER. Genomic coordinates: 797613-798431. EcoCyc protein note: YbhA is a pyridoxal phosphate phosphatase that contributes to PLP homeostasis within the cell. Addition of pyridoxal to a wild-type strain grown in minimal medium leads to an extended lag phase, and cells accumulate PLP. Overexpression of YbhA alleviates this phenotype. Conversely, overexpression of YbhA in cells grown in minimal medium leads to a reduced growth rate and decreased levels of intracellular PLP; the growth defect can be rescued by addition of pyridoxal to the growth medium...

## Enriched Pathways

- `eco00750` Vitamin B6 metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P21829|protein.P21829]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002607,ECOCYC:EG11239,GeneID:945372`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:797613-798431:-; feature_type=gene
