---
entity_id: "gene.b4428"
entity_type: "gene"
name: "hokB"
source_database: "NCBI RefSeq"
source_id: "gene-b4428"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4428"
  - "hokB"
---

# hokB

`gene.b4428`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4428`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hokB (gene.b4428) is a gene entity. It encodes hokB (protein.P77494). Encoded protein function: FUNCTION: Toxic component of a type I toxin-antitoxin (TA) system (Probable). When overexpressed kills cells within minutes; causes collapse of the transmembrane potential and arrest of respiration (PubMed:10361310). Expression leads to membrane depolarization; when protein levels are high enough depolarization probably leads to lowered metabolic activity which in turn induces some cells to enter the persistent state in which they transiently survive antibiotic exposure. Its toxic effect is probably neutralized by antisense antitoxin RNA SokB, which is encoded in trans on the opposite DNA strand (PubMed:10361310). {ECO:0000269|PubMed:10361310, ECO:0000269|PubMed:26051177, ECO:0000305|PubMed:10361310}. EcoCyc product frame: MONOMER0-1604. EcoCyc synonyms: ydcB. Genomic coordinates: 1491922-1492071. EcoCyc protein note: HokB is the toxin of the HokB-SokB type I toxin-antitoxin system. Increased expression of HokB mediates the effect of G7656-MONOMER ObgE on persister cell formation. Moderately increased expression of HokB leads to a decrease in the membrane potential. It may thus lower metabolic activity, inducing some cells to enter the persistent state that enables survival of exposure to antibiotics . A regulatory mechanism has been proposed...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77494|protein.P77494]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0047283,ECOCYC:G0-9610,GeneID:2847727`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1491922-1492071:-; feature_type=gene
