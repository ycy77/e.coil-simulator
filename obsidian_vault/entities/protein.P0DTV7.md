---
entity_id: "protein.P0DTV7"
entity_type: "protein"
name: "speFL"
source_database: "UniProt"
source_id: "P0DTV7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "speFL b4803"
---

# speFL

`protein.P0DTV7`

## Static

- Type: `protein`
- Source: `UniProt:P0DTV7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: A small protein (arrest peptide) encoded upstream of inducible ornithine carboxylase gene (speF) that controls expression of downstream genes (speF and patE) by nascent chain-translational arrest and transcriptional attenuation. In the presence of ornithine a toeprint due to ribosomal arrest can be seen on the speFL transcript. Only L-ornithine (not other tested amino acids) has this effect (PubMed:32094585). It is thought that in the presence of ornithine, ribosomal stalling on speFL prevents binding of Rho transcription termination factor to a downstream rut site allowing transcription of the operon. In the absence of ornithine, ribosomes terminate translation and are recycled, exposing the rut site allowing Rho to bind and prematurely terminate transcription. The presence of a pair of rare Arg codons could slow down translation to prevent polysome accumulation and to expose the rut site to Rho (Probable). {ECO:0000255|HAMAP-Rule:MF_00851, ECO:0000269|PubMed:32094585, ECO:0000305|PubMed:32094585}. The SpeFL leader peptide enables regulation of translation of the ORNDECARBOXDEG-MONOMER (SpeF) by transcriptional attenuation . The authors of propose a model for regulation: in the presence of ornithine, the substrate for SpeF, the leading ribosome translating the speFL ORF stalls when codon 34 is located in the ribosomal P-site...

## Annotation

FUNCTION: A small protein (arrest peptide) encoded upstream of inducible ornithine carboxylase gene (speF) that controls expression of downstream genes (speF and patE) by nascent chain-translational arrest and transcriptional attenuation. In the presence of ornithine a toeprint due to ribosomal arrest can be seen on the speFL transcript. Only L-ornithine (not other tested amino acids) has this effect (PubMed:32094585). It is thought that in the presence of ornithine, ribosomal stalling on speFL prevents binding of Rho transcription termination factor to a downstream rut site allowing transcription of the operon. In the absence of ornithine, ribosomes terminate translation and are recycled, exposing the rut site allowing Rho to bind and prematurely terminate transcription. The presence of a pair of rare Arg codons could slow down translation to prevent polysome accumulation and to expose the rut site to Rho (Probable). {ECO:0000255|HAMAP-Rule:MF_00851, ECO:0000269|PubMed:32094585, ECO:0000305|PubMed:32094585}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b4803|gene.b4803]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0DTV7`
- `GeneID:75056550;`
- `GO:GO:0006448; GO:0019843; GO:0031556`

## Notes

Leader peptide SpeFL (Arrest peptide SpeFL)
