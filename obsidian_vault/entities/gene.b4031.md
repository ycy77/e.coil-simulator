---
entity_id: "gene.b4031"
entity_type: "gene"
name: "xylE"
source_database: "NCBI RefSeq"
source_id: "gene-b4031"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4031"
  - "xylE"
---

# xylE

`gene.b4031`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4031`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

xylE (gene.b4031) is a gene entity. It encodes xylE (protein.P0AGF4). Encoded protein function: FUNCTION: Uptake of D-xylose across the boundary membrane with the concomitant transport of protons into the cell (symport system). Glucose is not transported, but can compete for xylose binding sites and can inhibit xylose transport (in vitro). {ECO:0000269|PubMed:23075985}. EcoCyc product frame: XYLE-MONOMER. Genomic coordinates: 4240779-4242254. EcoCyc protein note: XylE is a D-xylose/proton symporter, one of two systems in E. coli K-12 responsible for the uptake of D-xylose - the other being the ATP-dependent ABC transporter XylFGH. The cloned xylE gene has been shown to complement xylE mutants in vivo . XylE-mediated transport in whole cells is inhibited by protonophores and elicits an alkaline pH change . Experiments using xylE and xylF mutants have established that XylE has a Km of 63-169 μM for D-xylose . Crystal structures of XylE bound to the ligands D-xylose, D-glucose and the chemically synthesized glucose derivative, 6-bromo-6-deoxy-D-glucose have been obtained at 2.6 - 2.9 Å. Structures were captured in an outward facing conformation. XylE contains 12 transmembrane (TM) helices organised into two distinct domains with amino and carboxy termini located on the cytosolic side of the membrane...

## Biological Role

Repressed by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748). Activated by xylR (protein.P0ACI3), crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AGF4|protein.P0AGF4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACI3|protein.P0ACI3]] `RegulonDB` `C` - regulator=XylR; target=xylE; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=xylE; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013189,ECOCYC:EG11076,GeneID:948529`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4240779-4242254:-; feature_type=gene
