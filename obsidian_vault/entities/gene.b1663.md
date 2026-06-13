---
entity_id: "gene.b1663"
entity_type: "gene"
name: "mdtK"
source_database: "NCBI RefSeq"
source_id: "gene-b1663"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1663"
  - "mdtK"
---

# mdtK

`gene.b1663`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1663`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mdtK (gene.b1663) is a gene entity. It encodes mdtK (protein.P37340). Encoded protein function: FUNCTION: Multidrug efflux pump that probably functions as a Na(+)/drug antiporter. Confers resistance to many drugs such as fluoroquinolones (norfloxacin, ciprofloxacin, enoxacin) and tetraphenylphosphonium ion (TPP) (PubMed:11566977, PubMed:9661020). Also to deoxycholate, doxorubicin, trimethoprim, chloramphenicol, fosfomycin, ethidium bromide and benzalkonium (PubMed:11566977). Also able to export peptides; when overexpressed, allows cells deleted for multiple peptidases (pepA, pepB, pepD and pepN) to grow in the presence of dipeptides Ala-Gln or Gly-Tyr which otherwise inhibit growth (PubMed:20067529). Cells overexpressing this protein have decreased intracellular levels of Ala-Gln dipeptide, and in a system that produces the Ala-Gln dipeptide overproduction of this protein increases export of the dipeptide (PubMed:20067529). {ECO:0000269|PubMed:11566977, ECO:0000269|PubMed:12615854, ECO:0000269|PubMed:20067529, ECO:0000269|PubMed:9661020}. EcoCyc product frame: YDHE-MONOMER. EcoCyc synonyms: norE, norM, ydhE. Genomic coordinates: 1743457-1744830...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37340|protein.P37340]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005561,ECOCYC:EG12400,GeneID:945883`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1743457-1744830:+; feature_type=gene
