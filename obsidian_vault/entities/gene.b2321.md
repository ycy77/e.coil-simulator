---
entity_id: "gene.b2321"
entity_type: "gene"
name: "flk"
source_database: "NCBI RefSeq"
source_id: "gene-b2321"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2321"
  - "flk"
---

# flk

`gene.b2321`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2321`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

flk (gene.b2321) is a gene entity. It encodes flk (protein.P15286). Encoded protein function: FUNCTION: Acts as a regulator of flagellar gene expression by modulating the protein level of the anti-sigma-28 factor FlgM upon sensing the point of assembly of the flagellar P- and L-rings, just prior to completion of the hook-basal body (HBB). Flk could inhibit FlgM secretion by acting as a braking system for the flagellar-associated type III secretion system (T3SS). Plays a role in preventing the premature switch of the flagellar T3SS specificity from rod/hook-type substrates to filament-type substrates prior to completion of the HBB, possibly by preventing the interaction of FliK with FlhB. {ECO:0000250|UniProtKB:Q7CQ37}. EcoCyc product frame: EG10229-MONOMER. EcoCyc synonyms: div. Genomic coordinates: 2437950-2438945. EcoCyc protein note: Flk belongs to the heterogeneous group of C-tail-anchored membrane proteins (TAMPs) . The C-terminal transmembrane domain is able to target a soluble reporter protein to the inner membrane where it is inserted in the expected C-out N-in orientation; mislocalization of the reporter protein occurs in strains that are lacking or depleted in SRP, FtsY, DnaK or YidC but not in strains lacking trigger factor or YajC; the transmembrane domain of the reporter protein cross-links to Ffh, trigger factor, YidC and YajC in vivo .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P15286|protein.P15286]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007667,ECOCYC:EG10229,GeneID:946776`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2437950-2438945:+; feature_type=gene
