---
entity_id: "gene.b0994"
entity_type: "gene"
name: "torT"
source_database: "NCBI RefSeq"
source_id: "gene-b0994"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0994"
  - "torT"
---

# torT

`gene.b0994`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0994`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

torT (gene.b0994) is a gene entity. It encodes torT (protein.P38683). Encoded protein function: FUNCTION: Upon binding a putative inducer it probably interacts with TorS and allows it to play a role in the induction of the torCAD operon for trimethylamine N-oxide reductase. EcoCyc product frame: BOUND-TORT. EcoCyc synonyms: yccH. Genomic coordinates: 1056261-1057289. EcoCyc protein note: TorT is a periplasmic trimethylamine-N-oxide (TMAO) binding protein that forms part of the PWY0-1506 "TorTS-TorR signaling system" which regulates expression of the torCAD operon for TMAO-based respiration. torT encodes a periplasmic protein which is required for expression of the torCAD operon; disruption of torT results in significantly reduced expression of a torA'-'lacZ fusion and loss of inducible TMAO reductase activity; overproduction of the TorR response regulator can partially bypass the requirement for TorT . TorT is dispensable in a torS constitutive mutant . TorT binds TMAO with µM affinity (KD = 150 µM); TorT becomes resistant to proteolytic digestion in the presence of TMAO; both TorT alone and TorT-TMAO interact with the periplasmic domain of the two-component sensor protein TORS-CPLX "TorS"; TMAO binding may induce a cascade of conformational change from TorT to TorS...

## Biological Role

Repressed by iscR (protein.P0AGK8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P38683|protein.P38683]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0AGK8|protein.P0AGK8]] `RegulonDB` `C` - regulator=IscR; target=torT; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003360,ECOCYC:G6515,GeneID:946289`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1056261-1057289:+; feature_type=gene
