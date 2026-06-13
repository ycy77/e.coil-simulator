---
entity_id: "gene.b0245"
entity_type: "gene"
name: "ykfI"
source_database: "NCBI RefSeq"
source_id: "gene-b0245"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0245"
  - "ykfI"
---

# ykfI

`gene.b0245`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0245`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ykfI (gene.b0245) is a gene entity. It encodes ykfI (protein.P77692). Encoded protein function: FUNCTION: Toxic component of a type IV toxin-antitoxin (TA) system (PubMed:14594833, PubMed:28257056, PubMed:28931012). Acts as a toxin inhibitor that blocks cell division and cell elongation via FtsZ and possibly also MreB (although no interaction with MreB has been proven) (PubMed:28931012). Overexpression results in inhibition of growth in liquid cultures and a decrease in colony formation (PubMed:14594833, PubMed:28257056, PubMed:28931012). These effects are overcome by concomitant expression of cognate antitoxin YafW, which leads to toxin loss by an unknown mechanism (PubMed:14594833, PubMed:28257056). Overexpression leads to formation of lemon-shaped cells and cell lysis; inactivated by overexpression of cognate antitoxin YafW but not when the 2 genes are coexpressed from the same plasmid (PubMed:28257056). Also neutralized by overexpression of non-cognate antitoxins YfjZ and CbeA (PubMed:28257056). Co-overexpression of toxin YkfI and antitoxin YafW leads to formation of elongated cells (PubMed:28257056). {ECO:0000269|PubMed:14594833, ECO:0000269|PubMed:28257056, ECO:0000269|PubMed:28931012}. EcoCyc product frame: G6120-MONOMER. Genomic coordinates: 263328-263669. EcoCyc protein note: YkfI is the toxin of the YkfI-YafW toxin-antitoxin system...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77692|protein.P77692]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000836,ECOCYC:G6120,GeneID:946726`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:263328-263669:-; feature_type=gene
