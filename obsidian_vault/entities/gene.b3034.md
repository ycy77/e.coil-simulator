---
entity_id: "gene.b3034"
entity_type: "gene"
name: "nudF"
source_database: "NCBI RefSeq"
source_id: "gene-b3034"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3034"
  - "nudF"
---

# nudF

`gene.b3034`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3034`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nudF (gene.b3034) is a gene entity. It encodes nudF (protein.Q93K97). Encoded protein function: FUNCTION: Acts on ADP-mannose and ADP-glucose as well as ADP-ribose. Prevents glycogen biosynthesis. The reaction catalyzed by this enzyme is a limiting step of the gluconeogenic process. {ECO:0000269|PubMed:11416161}. EcoCyc product frame: EG12633-MONOMER. EcoCyc synonyms: trgB, aspP, yqiE. Genomic coordinates: 3177281-3177910. EcoCyc protein note: NudF is a member of the family of Nudix hydrolases and has ADP-sugar pyrophosphatase activity . ADP-glucose is a precursor molecule for glycogen biosynthesis; thus, it appears that the activity of NudF needs to be regulated. NudF is thought to control the flow of carbon toward glycogen, interconnecting gluconeogenesis with other metabolic pathways . NudF also contributes to the production of dimethylallyl phosphate, which is the substrate for UBIX-MONOMER UbiX-catalyzed generation of the prFMN cofactor in ubiquinone biosynthesis . Gel filtration experiments indicate that the enzyme is a dimer in solution . Crystal structures of NudF in various forms have been solved, showing a domain-swapped dimer where the Nudix motif residues compose a catalytic center . Binding of the substrate and Mg2+ results in a conformational change from an open to a closed complex...

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00740` Riboflavin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q93K97|protein.Q93K97]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009961,ECOCYC:EG12633,GeneID:947519`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3177281-3177910:-; feature_type=gene
