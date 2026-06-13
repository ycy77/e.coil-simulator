---
entity_id: "gene.b3459"
entity_type: "gene"
name: "panZ"
source_database: "NCBI RefSeq"
source_id: "gene-b3459"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3459"
  - "panZ"
---

# panZ

`gene.b3459`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3459`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

panZ (gene.b3459) is a gene entity. It encodes panZ (protein.P37613). Encoded protein function: FUNCTION: Controls both the activation and catalytic activity of PanD in a coenzyme A (CoA)-dependent fashion. Binding of CoA or a derivative to PanZ leads to interaction with PanD, which promotes the processing and activation of pro-PanD, and subsequent substrate-mediated inhibition of the active form of PanD (PubMed:23170229, PubMed:25910242). Inhibition of PanD activity is probably the primary metabolic role of PanZ, allowing negative feedback regulation of pantothenate biosynthesis by CoA (PubMed:25910242). {ECO:0000269|PubMed:23170229, ECO:0000269|PubMed:25910242}. EcoCyc product frame: MONOMER0-4437. EcoCyc synonyms: livL, panM, yhhK. Genomic coordinates: 3597984-3598367. EcoCyc protein note: Coenzyme A-bound PanZ promotes activation of the ASPDECARBOX-MONOMER "PanD" proenzyme and negatively regulates the aspartate α-decarboxylase activity of activated PanD . PanZ is not an enzyme but a stoichiometric facilitator of PanD activation. Formation of a PanD-PanZ complex stabilizes a conformation of PanD in which the serine-25 hydroxyl group moves to a close proximity to the adjacent carbonyl group, thus facilitating an attack on the G24-S25 peptide bond . Addition of PanZ to an assay of β-alanine synthesis by PanD enhances activity 24-fold...

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37613|protein.P37613]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011296,ECOCYC:EG12211,GeneID:947963`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3597984-3598367:+; feature_type=gene
