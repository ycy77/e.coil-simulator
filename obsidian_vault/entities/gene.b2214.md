---
entity_id: "gene.b2214"
entity_type: "gene"
name: "ftp"
source_database: "NCBI RefSeq"
source_id: "gene-b2214"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2214"
  - "ftp"
---

# ftp

`gene.b2214`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2214`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ftp (gene.b2214) is a gene entity. It encodes apbE (protein.P0AB85). Encoded protein function: FUNCTION: Flavin transferase that catalyzes the transfer of the FMN moiety of FAD and its covalent binding to the hydroxyl group of a threonine residue in a target flavoprotein such as NqrB and NqrC, two subunits of the NQR complex. {ECO:0000250|UniProtKB:A5F5Y3}. EcoCyc product frame: EG12073-MONOMER. EcoCyc synonyms: yojK, yojL, apbE. Genomic coordinates: 2310479-2311534. EcoCyc protein note: ftp encodes a periplasmic flavin transferase which catalyses the transfer of flavin mononucleotide from FAD to target protein(s). Recombinant, purified Ftp appears to be a flavin-containing protein and is a dimer in solution . Purified Ftp flavinylates G6875-MONOMER "RsxG" in an Mg2+ dependent reaction . Ftp contains a bimetal (possibly Ca2+/Mg2+) centre . Ftp is a predicted lipoprotein . Ftp (formerly ApbE) is a component of the SoxR-reducing system; RsxABCDGE, RseC and ApbE likely form a complex that uses NAD(P)H to reduce the [2Fe-2S] center of PD04132 SoxR; a ΔabpE mutant exhibits increased expression of a EG10958 soxS promoter-linked LacZ reporter . ApbE is a periplasmic lipoprotein anchored to the inner membrane in Salmonella typhimurium; it was initially implicated in thiamine biosynthesis and iron-sulfur cluster metabolism and later shown to be a flavin transferase in Vibrio harveyii...

## Biological Role

Repressed by yeiE (protein.P0ACR4).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AB85|protein.P0AB85]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACR4|protein.P0ACR4]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007317,ECOCYC:EG12073,GeneID:946711`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2310479-2311534:-; feature_type=gene
