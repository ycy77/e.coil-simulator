---
entity_id: "gene.b1069"
entity_type: "gene"
name: "murJ"
source_database: "NCBI RefSeq"
source_id: "gene-b1069"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1069"
  - "murJ"
---

# murJ

`gene.b1069`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1069`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

murJ (gene.b1069) is a gene entity. It encodes murJ (protein.P0AF16). Encoded protein function: FUNCTION: Involved in peptidoglycan biosynthesis. Transports lipid-linked peptidoglycan precursors from the inner to the outer leaflet of the cytoplasmic membrane. {ECO:0000255|HAMAP-Rule:MF_02078, ECO:0000269|PubMed:18708495, ECO:0000269|PubMed:18832143, ECO:0000269|PubMed:25013077}. EcoCyc product frame: G6561-MONOMER. EcoCyc synonyms: mviN, yceN. Genomic coordinates: 1127839-1129374. EcoCyc protein note: MurJ is the inner membrane protein responsible for flipping lipid II from the inner face of the inner membrane to the outer face prior to peptidoglycan (PG) polymerization; MurJ is essential for PG synthesis . There are conflicting reports on MurJ binding to lipid II: MurJ does not interact directly with lipid II in vitro and does not affect MrcB mediated lipid II polymerization in vitro ; purified MurJ binds lipid II with high affinity (Kd of 2.9 µM for binding of the first lipid II) . MurJ has 14 transmembrane (TM) domains with the N and C-termini located in the cytoplasm . MurJ contains a solvent exposed central cavity located within the membrane region which is consistent with a role in transport; the central cavity is lined by TM domains 1, 2, 7 and 8 and charged residues within the cavity are critical for function...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AF16|protein.P0AF16]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003630,ECOCYC:G6561,GeneID:945487`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1127839-1129374:+; feature_type=gene
