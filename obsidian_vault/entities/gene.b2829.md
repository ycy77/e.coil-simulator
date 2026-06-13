---
entity_id: "gene.b2829"
entity_type: "gene"
name: "ptsP"
source_database: "NCBI RefSeq"
source_id: "gene-b2829"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2829"
  - "ptsP"
---

# ptsP

`gene.b2829`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2829`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ptsP (gene.b2829) is a gene entity. It encodes ptsP (protein.P37177). Encoded protein function: FUNCTION: Component of the phosphoenolpyruvate-dependent nitrogen-metabolic phosphotransferase system (nitrogen-metabolic PTS), that seems to be involved in regulating nitrogen metabolism. Enzyme I-Ntr transfers the phosphoryl group from phosphoenolpyruvate (PEP) to the phosphoryl carrier protein (NPr) (PubMed:10473571). Could function in the transcriptional regulation of sigma-54 dependent operons in conjunction with the NPr (PtsO) and EIIA-Ntr (PtsN) proteins (PubMed:8973315). Enzyme I-Ntr is specific for NPr (PubMed:10473571). {ECO:0000269|PubMed:10473571, ECO:0000269|PubMed:8973315}. EcoCyc product frame: MONOMER0-4291. EcoCyc synonyms: ygdO, ygdF. Genomic coordinates: 2966188-2968434. EcoCyc protein note: PtsP, also known as EINtr, is the first enzyme of the nitrogen phosphotransferase system (PTS Ntr). The PTS Ntr system, consisting of the three cytoplasmic proteins PtsP, EG12147-MONOMER "NPr" and EG11682-MONOMER "PtsN", is believed to respond to nitrogen availability and is paralogous to the well-characterised PTSsugar. PtsP contains an N-terminal 127 amino acid GAF domain attached to a larger C-terminal Enzyme I domain . Autophosphorylation of PtsP by phosphoenolpyruvate (PEP) in vitro is inhibited by glutamine and stimulated by α-ketoglutarate...

## Enriched Pathways

- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37177|protein.P37177]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009274,ECOCYC:EG12188,GeneID:947301`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2966188-2968434:-; feature_type=gene
