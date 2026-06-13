---
entity_id: "gene.b0627"
entity_type: "gene"
name: "tatE"
source_database: "NCBI RefSeq"
source_id: "gene-b0627"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0627"
  - "tatE"
---

# tatE

`gene.b0627`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0627`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tatE (gene.b0627) is a gene entity. It encodes tatE (protein.P0A843). Encoded protein function: FUNCTION: Part of the twin-arginine translocation (Tat) system that transports large folded proteins containing a characteristic twin-arginine motif in their signal peptide across membranes. TatE shares overlapping functions with TatA. {ECO:0000255|HAMAP-Rule:MF_00903, ECO:0000269|PubMed:9649434}. EcoCyc product frame: EG11305-MONOMER. EcoCyc synonyms: ybeC. Genomic coordinates: 658947-659150. EcoCyc protein note: TatE is an inner membrane component of the twin arginine translocation (Tat) complex for the export of folded proteins. TatE is predicted to contain an N-terminal transmembrane domain followed by an amphipathic helix and a cytoplasmic domain; TatE has 53% amino acid identity to TatA . ΔtatA ΔtatE knockout mutants are unable to export a number of redox cofactor containing proteins; a ΔtatA strain is significantly more compromised for export than a ΔtatE strain . tatE forms a monocistronic unit which is transcribed consititutively; TatE is synthesized at a much lower level than TatA . TatE supports a lower level of Tat mediated transport than TatA . TatE: twin arginine translocation

## Enriched Pathways

- `eco03060` Protein export (KEGG)
- `eco03070` Bacterial secretion system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A843|protein.P0A843]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002153,ECOCYC:EG11305,GeneID:945228`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:658947-659150:+; feature_type=gene
