---
entity_id: "gene.b3447"
entity_type: "gene"
name: "ggt"
source_database: "NCBI RefSeq"
source_id: "gene-b3447"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3447"
  - "ggt"
---

# ggt

`gene.b3447`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3447`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ggt (gene.b3447) is a gene entity. It encodes ggt (protein.P18956). Encoded protein function: FUNCTION: Cleaves the gamma-glutamyl bond of periplasmic glutathione (gamma-Glu-Cys-Gly), glutathione conjugates, and other gamma-glutamyl compounds. The metabolism of glutathione releases free glutamate and the dipeptide cysteinyl-glycine, which is hydrolyzed to cysteine and glycine by dipeptidases; it may function in amino acid uptake/salvage, or possibly in peptidoglycan linkage. Catalyzes the hydrolysis and transpeptidation of many gamma-glutamyl compounds (including some D-gamma-glutamyl substrates), with a preference for basic and aromatic amino acids as acceptors (PubMed:2877974). The KM values for gamma-glutamyl acceptors are so high that it has been proposed transpeptidation is not the physiological role in E.coli (PubMed:2877974, PubMed:8104180). {ECO:0000269|PubMed:2877974, ECO:0000305|PubMed:8104180}. EcoCyc product frame: MONOMER0-4195. Genomic coordinates: 3585081-3586823. EcoCyc protein note: The glutathione hydrolase proenzyme undergoes autocatalytic processing to release a catalytic threonine (Thr391); processing generates a large (Ala26 → Gln390) and small (Thr391 → Tyr580) subunit which together form the active heterodimer...

## Enriched Pathways

- `eco00430` Taurine and hypotaurine metabolism (KEGG)
- `eco00460` Cyanoamino acid metabolism (KEGG)
- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P18956|protein.P18956]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011257,ECOCYC:EG10374,GeneID:947947`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3585081-3586823:-; feature_type=gene
