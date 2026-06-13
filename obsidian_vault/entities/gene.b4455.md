---
entity_id: "gene.b4455"
entity_type: "gene"
name: "hokA"
source_database: "NCBI RefSeq"
source_id: "gene-b4455"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4455"
  - "hokA"
---

# hokA

`gene.b4455`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4455`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hokA (gene.b4455) is a gene entity. It encodes hokA (protein.P37305). Encoded protein function: FUNCTION: Toxic component of a type I toxin-antitoxin (TA) system (Probable). When overexpressed kills cells within minutes; causes collapse of the transmembrane potential and arrest of respiration (PubMed:10361310, PubMed:20105222). Its toxic effect is probably neutralized by antisense antitoxin RNA SokA (PubMed:10361310). {ECO:0000269|PubMed:10361310, ECO:0000269|PubMed:20105222, ECO:0000305|PubMed:10361310}. EcoCyc product frame: MONOMER0-1605. EcoCyc synonyms: yiaZ. Genomic coordinates: 3720448-3720600. EcoCyc protein note: Sequence analysis indicates that the hokA gene is a homologue of the hok (host killing) gene which is responsible for plasmid stabilization in plasmid R1. hok encodes a stable mRNA whose translation is inhibited by a less stable mRNA encoded by sok. The stable mRNA from hokA encodes a polypeptide that induction experiments have shown to be toxic to Escherichia coli host cells, resulting in cell growth arrest, morphological changes, and rapid cell killing. The hokA system is inactive due to insertion of the insertion element IS150 32 bp upstream of the start codon of the gene...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37305|protein.P37305]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0047285,ECOCYC:G0-9613,GeneID:2847732`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3720448-3720600:-; feature_type=gene
