---
entity_id: "gene.b0838"
entity_type: "gene"
name: "gstB"
source_database: "NCBI RefSeq"
source_id: "gene-b0838"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0838"
  - "gstB"
---

# gstB

`gene.b0838`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0838`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gstB (gene.b0838) is a gene entity. It encodes gstB (protein.P0ACA7). Encoded protein function: FUNCTION: Conjugation of reduced glutathione to a wide number of exogenous and endogenous hydrophobic electrophiles. Catalyzes the glutathione-dependent dehalogenation of bromoacetate. {ECO:0000269|PubMed:20921376}. EcoCyc product frame: G6438-MONOMER. EcoCyc synonyms: yliJ. Genomic coordinates: 879854-880480. EcoCyc protein note: The GstB protein is a glutathione S-transferase that is able to dehalogenate the non-natural toxic chemicals bromoacetate and iodoacetate. GstB does not catalyze the dehalogenation of chloroacetate, bromoacetamide, 2-bromopropionate or 3-bromopropionate. Its physiological substrate may be a small molecule containing a carboxylate moiety . Arsenate resistance conferred by GstB is not dependent on glutaredoxins or on the C134/C137 residues within GstB, but requires two arginine residues, R111 and R119 within its substrate binding domain. The proposed mechanism for the glutathione-dependent reduction of arsenate by GstB includes enzymatic formation of an arsenate-glutathione intermediate, which is subsequently reduced by a second glutathione molecule in solution . A gstB mutant is hypersensitive to bromoacetate. Overexpression of gstB does not result in resistance to bromoacetate; instead, it decreases its minimum inhibitory concentration...

## Enriched Pathways

- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACA7|protein.P0ACA7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002855,ECOCYC:G6438,GeneID:945469`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:879854-880480:-; feature_type=gene
