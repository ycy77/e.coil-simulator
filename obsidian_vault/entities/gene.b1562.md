---
entity_id: "gene.b1562"
entity_type: "gene"
name: "hokD"
source_database: "NCBI RefSeq"
source_id: "gene-b1562"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1562"
  - "hokD"
---

# hokD

`gene.b1562`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1562`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hokD (gene.b1562) is a gene entity. It encodes hokD (protein.P0ACG6). Encoded protein function: FUNCTION: Toxic component of a type I toxin-antitoxin (TA) system (Probable). When overexpressed kills cells within 2 minutes; causes collapse of the transmembrane potential and arrest of respiration (PubMed:3019679). {ECO:0000269|PubMed:3019679, ECO:0000305}. EcoCyc product frame: EG11130-MONOMER. EcoCyc synonyms: relF. Genomic coordinates: 1645119-1645274. EcoCyc protein note: Sequence analysis indicates that the hokD gene is a homologue of the hok (host killing) gene which is responsible for mediating plasmid stabilization by post-segregational killing (PSK) in plasmid R1. hok encodes a stable mRNA whose translation is inhibited by a less stable mRNA encoded by sok. The stable mRNA from hokD encodes a polypeptide that induction experiments have shown to be toxic to E. coli, resulting in loss of membrane potential, cell respiration arrest, morphological changes, and host cell death . The hokD gene is post-transcriptionally regulated in E. coli . Sequence analysis has also shown that the hokD locus has a fold-back inhibition element downstream of the hokD reading frame, but lacks the upstream regulatory elements of a hok-homologous gene system. The hokD system is therefore believed to have been inactivated by genetic rearrangement...

## Biological Role

Repressed by relB (protein.P0C079). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACG6|protein.P0ACG6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=hokD; function=+
- `represses` <-- [[protein.P0C079|protein.P0C079]] `RegulonDB` `C` - regulator=RelB; target=hokD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005219,ECOCYC:EG11130,GeneID:948616`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1645119-1645274:-; feature_type=gene
