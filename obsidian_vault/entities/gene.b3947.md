---
entity_id: "gene.b3947"
entity_type: "gene"
name: "ptsA"
source_database: "NCBI RefSeq"
source_id: "gene-b3947"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3947"
  - "ptsA"
---

# ptsA

`gene.b3947`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3947`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ptsA (gene.b3947) is a gene entity. It encodes ptsA (protein.P32670). Encoded protein function: FUNCTION: Multifunctional protein that includes general (non sugar-specific) and sugar-specific components of the phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS). This major carbohydrate active transport system catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II FrwABC PTS system is involved in fructose transport. {ECO:0000305|PubMed:7773398}. EcoCyc product frame: EG11906-MONOMER. EcoCyc synonyms: yijH, frwA, pt1A. Genomic coordinates: 4139720-4142221. EcoCyc protein note: Sequence analysis indicates that ptsA encodes a protein with similarity to sugar phosphotransferase system (PTS) components. The 560 residue N-terminal domain is similar to Enzymes I of the PTS and is more similar to Enzyme I's from gram positive bacteria than to Enzyme I's from gram negative bacteria. This domain contains a conserved histidine residue (his301) predicted to be the site of phosphorylation. The C-terminal domain of PtsA has similarity to the IIA domains of the PTS Enzymes II specific for fructose . ptsA is predicted to encode a triphosphoryl transfer protein with the domain order H-I-IIA...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32670|protein.P32670]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012920,ECOCYC:EG11906,GeneID:948437`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4139720-4142221:-; feature_type=gene
