---
entity_id: "gene.b1269"
entity_type: "gene"
name: "rluB"
source_database: "NCBI RefSeq"
source_id: "gene-b1269"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1269"
  - "rluB"
---

# rluB

`gene.b1269`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1269`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rluB (gene.b1269) is a gene entity. It encodes rluB (protein.P37765). Encoded protein function: FUNCTION: Responsible for synthesis of pseudouridine from uracil-2605 in 23S ribosomal RNA. {ECO:0000269|PubMed:11720289}. EcoCyc product frame: EG12433-MONOMER. EcoCyc synonyms: yciL. Genomic coordinates: 1326852-1327727. EcoCyc protein note: RluB is the pseudouridine synthase that catalyzes formation of pseudouridine at position 2605 in 23S rRNA. RluB belongs to the RsuA family of RNA pseudouridine synthases . RluB is associated with a particle the migrates slightly slower than the 50S ribosomal subunit, suggesting that it acts during 50S subunit maturation . Pseudouridine residues outside of helix-loop 69, including Ψ2605, appear to be made during the early steps of large ribosome subunit assembly . Crystal structures of the catalytic domain alone and in a complex with the substrate stem-loop have been solved, revealing a covalent bond between the hydroxyl group of the active site Tyr140 and the C6 of the U2605 substrate with the base flipped into the active site. The authors propose a Michael addition reaction mechanism for pseudouridine synthesis . The conserved active site residue Asp110 is essential for activity , while a Tyr140Phe mutant retains 3% of wild-type enzymatic activity . An rluB null mutant or an rluB rluF double null mutant exhibits no obvious growth defect...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37765|protein.P37765]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004259,ECOCYC:EG12433,GeneID:945840`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1326852-1327727:+; feature_type=gene
