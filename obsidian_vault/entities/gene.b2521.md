---
entity_id: "gene.b2521"
entity_type: "gene"
name: "sseA"
source_database: "NCBI RefSeq"
source_id: "gene-b2521"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2521"
  - "sseA"
---

# sseA

`gene.b2521`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2521`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sseA (gene.b2521) is a gene entity. It encodes sseA (protein.P31142). Encoded protein function: FUNCTION: Catalyzes the transfer of sulfur from 3-mercaptopyruvate to a thiol-containing acceptor to form an intramolecular disulfide releasing hydrogen sulfide and pyruvate (Probable). May be involved in the enhancement of bacterial growth inhibition by serine (PubMed:7982894). {ECO:0000269|PubMed:7982894, ECO:0000305|PubMed:11445076}. EcoCyc product frame: EG11600-MONOMER. EcoCyc synonyms: mstA. Genomic coordinates: 2652494-2653339. EcoCyc protein note: 3-Mercaptopyruvate sulfurtransferase (3MST) is a rhodanese-like enzyme that, in contrast to rhodanese, uses 3-mercaptopyruvate as the preferred sulfur donor; thiosulfate can be used as a less efficient donor . 3MST is the major source of hydrogen sulfide production in E. coli grown in LB medium ; H2S in turn protects the cell against DNA damage by sequestering free Fe2+, which otherwise drives hydroxyl radical generation via the Fenton reaction . A crystal structure of 3MST has been solved at 2.8 Å resolution; the structure shows differences with the structure of rhodanese enzymes, including a variation in the active site loop. The structure provides insight into the catalytic mechanism of 3MST . The Ser240 residue is important for catalytic activity...

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco04122` Sulfur relay system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31142|protein.P31142]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008299,ECOCYC:EG11600,GeneID:946993`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2652494-2653339:+; feature_type=gene
