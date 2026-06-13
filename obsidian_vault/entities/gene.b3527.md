---
entity_id: "gene.b3527"
entity_type: "gene"
name: "yhjJ"
source_database: "NCBI RefSeq"
source_id: "gene-b3527"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3527"
  - "yhjJ"
---

# yhjJ

`gene.b3527`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3527`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yhjJ (gene.b3527) is a gene entity. It encodes yhjJ (protein.P37648). Encoded protein function: Protein YhjJ EcoCyc product frame: EG12254-MONOMER. EcoCyc synonyms: yhjJ. Genomic coordinates: 3680444-3681940. EcoCyc protein note: bipP encodes a periplasmic protein that regulates the EG10760-MONOMER Prc-EG12371-MONOMER Nlp proteolytic system; BipP controls the level of peptidoglycan-cleaving enzymes G7147-MONOMER MepS, G6892-MONOMER MepH and EG10246-MONOMER MltD, by negatively regulating the NlpI-Prc system in response to peptidoglycan hydrolase activity; BipP controls the NlpI-Prc system through its interaction with NlpI; BipP binds to NlpI and inhibits substrate recognition through steric hindrance . BipP contains a metallopeptidase M16 domain but lacks critical metal-binding residues . Overexpression of yhjJ from an ASKA plasmid leads to a more than 3-fold increase in the MIC of hydrogen peroxide . bipP: brake on NlpI-Prc-promoted proteolysis .

## Biological Role

Activated by lrp (protein.P0ACJ0), rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37648|protein.P37648]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=bipP; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011524,ECOCYC:EG12254,GeneID:948040`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3680444-3681940:-; feature_type=gene
