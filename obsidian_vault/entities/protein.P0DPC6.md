---
entity_id: "protein.P0DPC6"
entity_type: "protein"
name: "idlP"
source_database: "UniProt"
source_id: "P0DPC6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "idlP orf27 b4722"
---

# idlP

`protein.P0DPC6`

## Static

- Type: `protein`
- Source: `UniProt:P0DPC6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: A short protein whose stop codon overlaps with the start codon of downstream iraD; its mRNA secondary structure is predicted to fold and sequester the Shine-Dalgarno sequence of iraD. When this protein is expressed the downstream iraD is also expressed due to ribosomal coupling (PubMed:28851853). {ECO:0000269|PubMed:28851853}. The iraD leader peptide is encoded upstream of G7923-MONOMER; its translation is negatively regulated by the EG11447-MONOMER CsrA. The stop codon of the leader peptide overlaps the IraD start codon, and IraD translation is coupled to that of the leader peptide. CsrA thus also negatively regulates IraD translation . IdlP: "iraD leader peptide"

## Annotation

FUNCTION: A short protein whose stop codon overlaps with the start codon of downstream iraD; its mRNA secondary structure is predicted to fold and sequester the Shine-Dalgarno sequence of iraD. When this protein is expressed the downstream iraD is also expressed due to ribosomal coupling (PubMed:28851853). {ECO:0000269|PubMed:28851853}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b4722|gene.b4722]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0DPC6`
- `GeneID:75169818;`
- `GO:GO:0006417`

## Notes

iraD leader peptide
